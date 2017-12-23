import numpy as np

from math import sqrt

from utils.transform import list2str, str2list


def combine(parts):
    if len(parts) == 1:
        return parts[0]
    columns = []
    for i in range(0, int(sqrt(len(parts)))):
        columns.append([])
        key = len(columns) - 1
        for j in range(i, len(parts), int(sqrt(len(parts)))):
            for line in parts[j].split('/'):
                columns[key].append(line)
    new = np.column_stack(columns).tolist()
    return list2str(new)


def divide(pattern):
    """
    @url https://stackoverflow.com/questions/16856788/slice-2d-array-into-smaller-2d-arrays
    """
    if isinstance(pattern, str):
        pattern = str2list(pattern)
    arr = np.asarray(pattern)
    h, w = arr.shape
    if h % 2 == 0:
        by = 2
    else:
        by = 3
    return arr.reshape(h//by, by, -1, by).swapaxes(1, 2).reshape(-1, by, by)
