def rotate(arr, k):
    k = k % len(arr)
    arr = arr[-k:] + arr[:-k]
    return arr

if __name__ == '__main__':
    rotate()