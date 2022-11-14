# 手动实现Bachnormalization
import numpy as np
from torch import nn
import torch

class BatchNorm(nn.Module):
    def __init__(self, num_features, num_dims=4):
        if num_dims == 2:
            shape = (1, num_features)
        elif num_dims == 4:
            shape = (1, num_features, 1,1)
        self.running_mean = torch.zeros(shape)
        self.running_std = torch.ones(shape)
        # 这是可以训练的
        self.gamma = nn.Parameter(torch.ones(shape))
        self.beta = nn.Parameter(torch.zeros(shape))
        self.eps = 10e-5

        self.momentum = 0.9
    def forward(self, x, mode):
        return self.batchNorm(x, mode)

    def batchNorm(self, x, mode):
        if mode == "train":
            if len(x.shape) == 2:
                x_mean = x.mean(dim=0, keepdim=True)
                x_std = x.std(dim=0, keepdim=True)
            else:
                x_mean = x.mean(dim=(0,2,3), keepdim=True)
                x_std = x.std(dim=(0,2,3), keepdim=True)

            self.running_mean = self.momentum * self.running_mean + (1-self.momentum) * x_mean
            self.running_std = self.momentum * self.running_std + (1 - self.momentum) * x_std
            x_hat = (x - x_mean) / (x_std + self.eps)
        else:
            x_hat = (x - self.running_mean) / (self.running_std + self.eps)
        y = self.gamma * x_hat + self.beta
        return y