import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

class Autoencoder(nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super(Autoencoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU()
        )
        self.decoder = nn.Sequential(
            nn.Linear(hidden_dim // 2, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, input_dim),
            nn.Sigmoid()
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded

def train_autoencoder(data, config):
    input_dim = data.shape[1]
    hidden_dim = config['hidden_dim']
    model = Autoencoder(input_dim, hidden_dim)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=config['learning_rate'])

    dataset = TensorDataset(torch.tensor(data, dtype=torch.float32))
    dataloader = DataLoader(dataset, batch_size=config['batch_size'], shuffle=True)

    for epoch in range(config['epochs']):
        for batch in dataloader:
            inputs = batch[0]
            outputs = model(inputs)
            loss = criterion(outputs, inputs)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch+1}/{config['epochs']}, Loss: {loss.item():.4f}")

    return model

def save_model(model, path):
    torch.save(model.state_dict(), path)

def load_model(path, input_dim, hidden_dim):
    model = Autoencoder(input_dim, hidden_dim)
    model.load_state_dict(torch.load(path))
    model.eval()
    return model