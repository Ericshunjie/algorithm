# 手动实现Bachnormalization
import numpy as np

def batchNorm(x, mode, params):
    mode = mode
    running_mean = params.get('running_mean')
    running_std = params.get('running_std')
    beta = params.get('beta')
    gamma = params.get('gamma')
    eps = params.get('eps', 1e-5)
    if mode == "train":
        samples_mean = np.mean(x, axis=0)
        samples_std = np.std(x, axis=0)
        outs = (x - samples_mean) / (samples_std + eps)
        out = gamma * outs + beta
        momentum = params.get('momentum')
        running_mean = momentum * running_mean + (1-momentum) * samples_mean
        running_std = momentum * running_std + (1 - momentum) * samples_std
        params['running_mean'] = running_mean
        params['running_std'] = running_std
    elif mode == 'test':
        out = (x - running_mean) / (running_std + eps)
    return out