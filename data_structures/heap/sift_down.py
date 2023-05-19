"""Реализация алгоритма просеивания вниз для неубывающей кучи."""


def sift_down(heap, idx) -> int:
    left = idx * 2
    right = idx * 2 + 1

    if left >= len(heap):
        return idx

    if right < len(heap) and heap[left] < heap[right]:
        index_largest = right
    else:
        index_largest = left

    if heap[idx] < heap[index_largest]:
        heap[idx], heap[index_largest] = heap[index_largest], heap[idx]
        return sift_down(heap, index_largest)
    return idx


def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5


if __name__ == '__main__':
    test()
