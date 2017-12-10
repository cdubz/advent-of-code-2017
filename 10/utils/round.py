def run_round(lengths, sparse_hash, pos=0, skip=0):
    max_len = len(sparse_hash)
    for length in lengths:
        pos %= max_len
        subset = list(
            reversed((sparse_hash + sparse_hash)[pos:(pos + length)]))
        for d in subset:
            pos %= max_len
            sparse_hash[pos] = d
            pos += 1
        pos += skip
        skip += 1
    return sparse_hash, pos % max_len, skip % max_len
