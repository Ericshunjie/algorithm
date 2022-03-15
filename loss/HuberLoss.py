import numpy as np


def huber(true, pred, delta):
    loss = np.where(np.abs(true - pred) < delta, 0.5*((true-pred)**2), delta*np.abs(true-pred)-0.5*(delta**2))
    return loss