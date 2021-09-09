import torch
from torchvision import transforms, datasets
import matplotlib.pyplot as plt
import torch.utils.data
from collections import Counter
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

# x = torch.Tensor([4, 3])
# y = torch.Tensor([2, 5])
# print(x * y)
# x = torch.zeros([2, 5])
# print(x.shape)
# y = torch.rand([2, 5])
# print(y, y.shape)
# y = y.view([1, 10])
# print(y)
# print("Testing")
train = datasets.MNIST("", train=True, transform=transforms.Compose([transforms.ToTensor()]))
test = datasets.MNIST("", train=False, transform=transforms.Compose([transforms.ToTensor()]))
trainset = torch.utils.data.DataLoader(train, batch_size=10, shuffle=True)
testset = torch.utils.data.DataLoader(test, batch_size=10, shuffle=True)

# first batch of 10 images
images, labels = [], []
for n in trainset:
    b_images, b_labels = n
    images.extend(b_images)
    labels.extend(b_labels)
images = [image.view([28, 28]) for image in images]
labels = [int(label) for label in labels]
print(Counter(labels))


class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(28 * 28, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 64)
        self.fc4 = nn.Linear(64, 10)

    def ff(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = F.log_softmax(self.fc4(x), dim=1)

        return x


model = Model()
optimizer = optim.Adam(model.parameters(), lr=.001)
# X = torch.rand((28, 28))
# plt.imshow(X)
# X = X.view(-1, 28*28)
# output = net.ff(X)
# print(output)

for epoch in range(3):
    for data in trainset:
        X, y = data
        # plt.imshow(X[0].view(28, 28))
        # print(y[0])
        model.zero_grad()
        output = model.ff(X.view(-1, 28 * 28))
        loss = F.nll_loss(output, y)
        loss.backward()
        optimizer.step()
        # print(loss)

# correct = 0
# total = 0
# model.eval()
# with torch.no_grad():
#     for data in trainset:
#         X, y = data
#         output = model.ff(X.view(-1, 28 * 28))
#         for idx, i in enumerate(output):
#             if torch.argmax(i) == y[idx]:
#                 correct += 1
#             total += 1
# print(correct/total)

model.train()

for data in trainset:
    X, y = data
    plt.imshow(X[0].view(28, 28))
    print(y[0])
    print(torch.argmax(model.ff(X[0].view(-1, 28*28))))
    plt.show()
