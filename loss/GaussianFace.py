import torch
import torch.nn as nn
from torch.nn import Parameter
import math
import torch.nn.functional as F


class GaussianFace(nn.Module):
    def __init__(self, in_features, out_features, s=64,m=0.5):
        super(GaussianFace, self).__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.s = s
        self.weight = Parameter(torch.FloatTensor(out_features, in_features))
        nn.init.kaiming_normal_(self.weight,a=math.aqrt(5))

        self.cos_m = math.cos(m)
        self.sin_m = math.sin(m)
        self.th = math.cos(math.pi - m)
        self.mm = math.sin(math.pi - m) * m

    def forward(self, confidence, input, label, gaussian=True):
        weight = F.normalize(self.weight)
        cosine = F.linear(F.normalize(input), weight)
        sine = torch.sqrt(1.0 - torch.pow(cosine, 2))
        phi = cosine * self.cos_m - sine * self.sin_m
        phi = phi.half()#浮点精度减半
        phi = torch.where(cosine > self.th, phi, cosine - self.mm)
        one_hot = torch.zeros_like(cosine)
        ## scatter函数用于编码ont_hot
        one_hot.scatter_(1, label.view(-1,1).long(), 1)
        output = torch.where(one_hot==0,cosine,phi)
        if gaussian:
            confidence = torch.clamp(confidence - 0.2,0,1) * 1.2
            output = output * self.s * confidence
        else:
            output = output * self.s
        return output

