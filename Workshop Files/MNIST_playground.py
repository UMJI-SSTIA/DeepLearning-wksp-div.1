# Reference: JI DeepLearning Tutorial
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import torch.nn.functional as F

transform = transforms.Compose(
    [transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))]
)

trainset = torchvision.datasets.MNIST(
    root="./data", train=True, download=True, transform=transform
)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=32, shuffle=True)
testset = torchvision.datasets.MNIST(
    root="./data", train=False, download=True, transform=transform
)
testloader = torch.utils.data.DataLoader(testset, batch_size=32, shuffle=False)


# useful methods:
# F.relu(x) or torch.relu(x)-> ReLU
# F.linear(a,b) or nn.Linear(a,b) -> Fully connected layer (a->input, b->output)
# F.max_pool2d(x,(a,b)) or nn.MaxPool2d(x,(a,b)) -> Max pooling layer, (a,b)->kernel size
# F.conv2d(a,b,k) or nn.Conv2d(a,b,k) -> Convolutional layer (a->input channels, b->output channels, k->kernel size)
# x.view(-1, size) -> Reshape the tensor to (auto, size)
# nn.CrossEntropyLoss() -> Cross Entropy Loss
# optim.SGD(model.parameters(), lr=a) -> Stochastic Gradient Descent optimizer, lr->learning rate


# Note: the size of one MNIST pic is 28*28


class MNISTNN(nn.Module):
    def __init__(self):
        super(MNISTNN, self).__init__()
        # code

    def forward(self, x):
        # code
        return x


model = MNISTNN()
# code

# Training Loop
for epoch in range(5):
    for i, data in enumerate(trainloader, 0):
        inputs, labels = data
        # code
        if i % 500 == 0:
            print(
                f"Epoch [{epoch + 1}/5], Step [{i + 1}/{len(trainloader)}], Loss: {loss.item()}"
            )

# Test
correct = 0
total = 0
with torch.no_grad():
    for data in testloader:
        images, labels = data
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f"Accuracy: {100 * correct / total}%")
