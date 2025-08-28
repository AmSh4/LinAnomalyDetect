import argparse
import yaml
from data_collector import collect_metrics
from preprocessor import preprocess_data
from model import train_autoencoder, save_model, load_model
from detector import detect_anomalies
from visualizer import plot_metrics, plot_anomalies
from utils import setup_logger
import os
import pandas as pd

logger = setup_logger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Linux Anomaly Detection Tool")
    parser.add_argument('--config', default='config.yaml', help='Path to config file')
    parser.add_argument('--collect', type=int, help='Collect data for X seconds')
    parser.add_argument('--train', action='store_true', help='Train the model')
    parser.add_argument('--detect', action='store_true', help='Detect anomalies')
    parser.add_argument('--visualize', action='store_true', help='Visualize results')
    args = parser.parse_args()

    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)

    data_file = 'metrics.csv'
    model_path = 'models/autoencoder.pth'
    os.makedirs('models', exist_ok=True)
    os.makedirs(config['visualization']['output_dir'], exist_ok=True)

    if args.collect:
        logger.info(f"Collecting data for {args.collect} seconds...")
        collect_metrics(duration=args.collect, interval=config['collection']['interval'], output_file=data_file)

    if args.train:
        logger.info("Training model...")
        df = pd.read_csv(data_file)
        data = preprocess_data(df)
        model = train_autoencoder(data, config['model'])
        save_model(model, model_path)

    if args.detect:
        logger.info("Detecting anomalies...")
        df = pd.read_csv(data_file)
        data = preprocess_data(df)
        model = load_model(model_path, config['model']['input_dim'], config['model']['hidden_dim'])
        anomalies = detect_anomalies(model, data, config['detection']['threshold'])
        anomalies.to_csv('anomalies.csv', index=False)
        logger.info("Anomalies saved to anomalies.csv")

    if args.visualize:
        logger.info("Generating visualizations...")
        df = pd.read_csv(data_file)
        plot_metrics(df, config['visualization']['output_dir'])
        if os.path.exists('anomalies.csv'):
            anomalies = pd.read_csv('anomalies.csv')
            plot_anomalies(df, anomalies, config['visualization']['output_dir'])

if __name__ == '__main__':
    main()