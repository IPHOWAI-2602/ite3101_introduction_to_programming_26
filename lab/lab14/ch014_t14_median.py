def median(numbers):
    seq = sorted(numbers)
    n = len(seq)
    mid = n // 2
    if n % 2 == 1:
        return seq[mid]
    else:
        return (seq[mid - 1] + seq[mid]) / 2.0
