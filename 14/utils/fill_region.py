def fill_region(disk, row, col, region):
    disk[row][col] = region
    if col - 1 > -1 and disk[row][(col - 1)] == 1:
        fill_region(disk, row, col - 1, region)
    if col + 1 < len(disk[row]) and disk[row][(col + 1)] == 1:
        fill_region(disk, row, col + 1, region)
    if row - 1 > -1 and disk[(row - 1)][col] == 1:
        fill_region(disk, row - 1, col, region)
    if row + 1 < len(disk) and disk[(row + 1)][col] == 1:
        fill_region(disk, row + 1, col, region)
