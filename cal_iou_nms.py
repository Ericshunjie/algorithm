

def cal_iou(box1, box2):
    """
    :param box1: [x1,y1,x2,y2]
    :param box2:
    :return:
    """
    if box1[2] < box2[0] or box1[1] > box2[3]:
        return 0
    # computing area of each rectangles
    S1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
    S2 = (box2[2] - box2[0]) * (box2[3] - box2[1])

    # computing the sum_area
    s_sum = S1 + S2

    # find the each edge of intersect rectangle
    left_line = max(box1[0], box2[0])
    right_line = min(box1[2], box2[2])
    top_line = max(box1[1], box2[1])
    bottom_line = min(box1[2], box2[2])

    intersect = (right_line - left_line) * (bottom_line - top_line)
    return intersect / float(s_sum - intersect)

# box1 = [30, 40, 80, 90]
# box2 = [50,70, 90,100]
# iou = cal_iou(box1, box2)
# print(iou)

import numpy as np



def cal_NMS(boxes, thresh):
    """
    :param boxes: [x1,y1,x2,y2,score]
    :param thresh:
    :return:
    """
    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]
    scores = boxes[:, 4]
    areas = (y2 - y1 + 1) * (x2 - x1 + 1)

    keep = []
    # 取分数从大到小排序的索引
    index = scores.argsort()[::-1]
    while index.size > 0:
        # 取出第一个方框进行和其他方框比对，看有没有可以合并的
        i = index[0]
        keep.append(i)

        # 计算交集的左上角和右下角
        # 这里要注意，比如x1[i]这个方框的左上角x和所有其他的方框的左上角x的
        xx1 = np.maximum(x1[i], x1[index[1:]])
        xx2 = np.minimum(x2[i], x2[index[1:]])
        yy1 = np.maximum(y1[i], y1[index[1:]])
        yy2 = np.minimum(y2[i], y2[index[1:]])

        w = np.maximum(0, xx2 - xx1)
        h = np.maximum(0, yy2 - yy1)

        overlaps = w * h

        ious = overlaps / (areas[i] + areas[index[1:]] - overlaps)
        print(ious)
        # 找到iou大于阈值的框剔除,小于阈值的接着做NMS
        idx = np.where(ious <= thresh)[0]
        # 把留下来框在进行NMS操作
        # 这边留下的框是去除当前操作的框，和当前操作的框重叠度大于thresh的框
        # 每一次都会先去除当前操作框，所以索引的列表就会向前移动移位，要还原就+1，向后移动一位
        index = index[idx + 1]
    return keep

boxes = np.array([[100, 100, 210, 210, 0.72],
                  [250, 250, 420, 420, 0.8],
                  [220, 220, 320, 330, 0.92],
                  [100, 100, 210, 210, 0.72],
                  [230, 240, 325, 330, 0.81],
                  [220, 230, 315, 340, 0.9]])
import matplotlib.pyplot as plt


def plot_bbox(dets, c='k'):
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]

    plt.plot([x1, x2], [y1, y1], c)
    plt.plot([x1, x1], [y1, y2], c)
    plt.plot([x1, x2], [y2, y2], c)
    plt.plot([x2, x2], [y1, y2], c)
    plt.title(" nms")



plt.figure(1)
ax1 = plt.subplot(1, 2, 1)
ax2 = plt.subplot(1, 2, 2)

plt.sca(ax1)
plot_bbox(boxes, 'k')  # before nms

keep = cal_NMS(boxes, thresh=0.3)
plt.sca(ax2)
plot_bbox(boxes[keep], 'r') # after nms
plt.show()



