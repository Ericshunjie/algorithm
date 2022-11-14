# 非极大值抑制 目标检测中常用
import numpy as np

def nms(dets, nms_threshold=0.5,score_threshold=0.5):
    """
    :param dets:  [[x1,y1,x2,y2,score],...]
    :param nms_threshold:
    :param score_threshold:
    :return:
    """
    # 首先过滤掉得分低的
    conf = dets[:, -1]
    conf_bool_idx = (conf > score_threshold)
    dets = dets[conf_bool_idx]

    x1 = dets[:,0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    scores = dets[:, -1]

    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    # 按照得分降序排列
    order = scores.argsort()[::-1]
    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)

        #计算得分最高的矩形框 与剩下所有矩形框的相交区域
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])

        # 计算相交的面积
        w = np.maximum(0, xx2-xx1+1)
        h = np.maximum(0, yy2-yy1+1)
        inter = w * h
        # 计算IoU
        iou = inter / (areas[i] + areas[order[1:]] - inter)
        # 保留iou小于阈值的box
        inds = np.where(iou < nms_threshold)[0]
        order = order[inds + 1]# 加一是因为iou数组少一个
    return np.where(conf_bool_idx)[0][keep]


dets = np.array([
    [100,120,170,220, 0.98],
    [20,40,80,90, 0.99],
    [20,38,82,88, 0.96],
    [200,300,282,488, 0.4],
    [19,38,75,91, 0.8],
    ])
print(nms(dets, 0.5,0.5))





