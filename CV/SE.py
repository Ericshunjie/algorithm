"通道域的attention模块"

import torch
from torch import nn
import torch.nn.functional as F

class SE(nn.Module):
    def __init__(self, in_channels, ratio):
        super(SE,self).__init__()
        self.squeeze = nn.AdaptiveAvgPool2d(output_size=(1,1))
        self.compress = nn.Conv2d(in_channels=in_channels,
                                  out_channels= in_channels// ratio,
                                  kernel_size=1,
                                  stride=1,
                                  padding=0)
        self.excitation = nn.Conv2d(in_channels=in_channels//ratio,
                                    out_channels=in_channels,
                                    kernel_size=1,
                                    stride=1,
                                    padding=0)
    def forward(self,x):
        out = self.squeeze(x)
        out = self.compress(out)
        out = F.relu(out)
        out = self.excitation(out)
        return x * F.softmax(out)