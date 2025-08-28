# Project Architecture

## Overview
LinAnomalyDetect is modularized for maintainability:
- **Data Collection**: Uses psutil to read Linux metrics.
- **Preprocessing**: Normalizes data for ML input.
- **Model**: PyTorch autoencoder learns normal patterns.
- **Detection**: Computes reconstruction errors to flag anomalies.
- **Visualization**: Matplotlib plots for insights.
- **CLI**: Argparse for user interaction.

## Data Flow
1. Collect raw metrics -> CSV.
2. Preprocess -> Normalized numpy array.
3. Train model -> Saved PTH file.
4. Detect -> Anomaly CSV.
5. Visualize -> PNG plots.

## Security Considerations
- Anomaly detection can flag potential intrusions (e.g., sudden CPU spikes).
- Code avoids root privileges; runs as user.

## Future Enhancements
- Integrate eBPF for kernel-level metrics.
- Add support for containerized environments (Docker/Kubernetes).
- Upstream contributions to open-source monitoring tools.