from utils.transform import flip, list2str, rotate, str2list


def get_keys(pattern):
    keys = []
    if isinstance(pattern, str):
        pattern = str2list(pattern)
    keys.append(list2str(pattern))
    keys.append(list2str(flip(pattern)))
    for i in range(0, 3):
        pattern = rotate(pattern)
        keys.append(list2str(pattern))
        keys.append(list2str(flip(pattern)))
    return keys
