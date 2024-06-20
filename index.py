import numpy as nu
import torch 
import torchvision 
from torchvision.datasets import MNIST
x = nu.array([[1,2],[3,4.]])
y= torch.from_numpy(x);
print(y)
print(x.dtype)
print(y.dtype);