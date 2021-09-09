import pickle
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch
from torchvision import transforms
import torch.utils.data
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, 5)
        self.conv2 = nn.Conv2d(32, 64, 5)
        self.conv3 = nn.Conv2d(64, 128, 5)
        self.pool1 = nn.MaxPool2d((2, 2))
        self.pool2 = nn.MaxPool2d((2, 2))
        self.pool3 = nn.MaxPool2d((2, 2))
        self.fc1 = nn.Linear(512, 512)
        # input of self.fc1 == x.shape[1]
        self.fc2 = nn.Linear(512, 2)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool1(x)
        x = F.relu(self.conv2(x))
        x = self.pool2(x)
        x = F.relu(self.conv3(x))
        x = self.pool3(x)
        x = x.flatten(start_dim=1)

        # print(x.shape[1])
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.softmax(x, dim=1)


with open("training_data", "rb") as f:
    training_data = pickle.load(open("training_data", "rb"))
    X = torch.Tensor([n[0] for n in training_data]).view(-1, 50, 50)
    X = X / torch.max(X)
    y = torch.Tensor([n[1] for n in training_data])
    train_size = 0.8
    X_train = X[:int(len(X) * 0.8)]
    X_test = X[int(len(X) * 0.8):]
    y_train = y[:int(len(X) * 0.8)]
    y_test = y[int(len(X) * 0.8):]
    print(len(X_train))
    print(len(X_test))
    print(len(y_train))
    print(len(y_test))

    model = Model()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    loss_func = nn.MSELoss()

    for epoch in range(3):
        for n in tqdm(range(0, len(X_train), 100)):
            batch_X_train = X_train[n:n + 100].view(-1, 1, 50, 50)
            batch_y_train = y_train[n:n + 100]
            model.zero_grad()
            outputs = model.forward(batch_X_train)
            loss = loss_func(outputs, batch_y_train)
            loss.backward()
            optimizer.step()
        print(f"{epoch}:{loss}")

    total = 0
    correct = 0
    with torch.no_grad():
        model.eval()
        for n in tqdm(range(len(X_test))):
            y_true = torch.argmax(y_test[n])
            y_pred = torch.argmax(model.forward(X_test[n].view(-1, 1, 50, 50))[0])
            if y_true == y_pred:
                correct += 1
            total += 1
    model.train()
    print(correct / total)
