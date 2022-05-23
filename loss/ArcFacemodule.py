import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn import Parameter
import math

class ArcMarginModule(nn.Module):
    def __init__(self, args):
        super(ArcMarginModule, self).__init__()
        self.weight = Parameter(torch.FloatTensor(args.nums_class, args.emb_size))
        nn.init.xavier_uniform_(self.weight)

        self.easy_margin = args.easy_margin
        self.m = 0.5
        self.s = 64
        self.cos_m = math.cos(self.m)
        self.sin_m = math.sin(self.m)

        self.th = math.cos(math.pi - self.m)
        self.mm = math.sin(math.pi - self.m) * self.m

    def forward(self, input, label):
        x = F.normalize(input)
        W = F.normalize((self.weight))

        cosine = F.linear(x, W)
        # cos(\theta+m) = cos(\theta)cos(m) - sin(\theta)sin(m)
        sine = torch.sqrt(1.0 - torch.pow(cosine, 2))
        phi = cosine * self.cos_m - sine * self.sin_m
        if self.easy_margin:
            phi = torch.where(cosine > 0,phi,cosine)
        else:
            phi = torch.where(cosine > self.th,phi,cosine-self.m)
        onehot = torch.zeros_like(cosine)
        onehot.scatter(1,label.view(-1,1), 1)
        output = onehot * phi + (1.0 - onehot) * cosine
        output *= self.s
        return output