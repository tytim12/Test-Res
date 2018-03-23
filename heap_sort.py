from heapq import heappush, heappop


def heap_sort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]


def main():
    L = [10,1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    print (heap_sort(L))


if __name__ == "__main__":
    main()
