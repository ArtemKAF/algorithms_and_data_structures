def shakersort(seq):
    """Функция сортировки методом сортировки перемешиванием"""
    if len(seq) < 1:
        return seq
    left = 0
    right = len(seq) - 1
    while left <= right:
        for i in range(right):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
        right -= 1
        for i in range(right, left, -1):
            if seq[i] < seq[i-1]:
                seq[i], seq[i-1] = seq[i-1], seq[i]
        left += 1
    return seq
