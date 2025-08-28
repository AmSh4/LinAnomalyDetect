# LinAnomalyDetect

A Python-based tool for detecting anomalies in Linux system performance using machine learning. This project collects real-time system metrics from Linux sources (e.g., /proc), preprocesses the data, trains an autoencoder model with PyTorch to learn normal behavior, and detects deviations that could indicate performance issues, security threats, or hardware problems.

## Features
- **Data Collection**: Gathers CPU, memory, disk, and network metrics from Linux system files.
- **Preprocessing**: Cleans and normalizes data using Pandas and Numpy.
- **ML Model**: Uses a PyTorch autoencoder for unsupervised anomaly detection.
- **Detection**: Real-time anomaly scoring with reconstruction error thresholds.
- **Visualization**: Plots metrics and anomalies using Matplotlib.
- **CLI Interface**: Easy-to-use command-line interface with argparse.
- **Configurable**: YAML configuration for thresholds, intervals, etc.
- **Tests**: Unit tests for key modules.
- **Setup Script**: Bash script for environment setup.

This tool is designed for Linux enthusiasts, sysadmins, and developers interested in system monitoring and AI-driven security. It's extensible for integrating with open-source projects like Ubuntu tools or kernel monitoring.

## Installation
1. Clone the repository:
git clone https://github.com/yourusername/LinAnomalyDetect.git
cd LinAnomalyDetect

2. Install dependencies:
pip install -r requirements.txt

3. (Optional) Run setup script for any system-specific configs:

bash scripts/setup.sh

## Usage
Run the main script:

python src/main.py [options]

Options:
- `--collect`: Collect data for a specified duration (e.g., --collect 60 for 60 seconds).
- `--train`: Train the model on collected data.
- `--detect`: Detect anomalies on new data.
- `--visualize`: Generate plots of metrics and anomalies.
- `--config config.yaml`: Specify config file.
- `--help`: Show help.

Example:
python src/main.py --collect 300 --train --detect --visualize


## Project Structure

https://github.com/AmSh4/LinAnomalyDetect/blob/main/Structure.md



## Contributing
Contributions are welcome! Fork the repo, create a branch, and submit a PR. Focus on improving model accuracy, adding more metrics, or integrating with containers/Kubernetes.

## License
MIT License. See LICENSE for details. 

## Acknowledgments

Built with open-source libraries: PyTorch, Pandas, Matplotlib. Inspired by Linux kernel monitoring needs in enterprise environments.
