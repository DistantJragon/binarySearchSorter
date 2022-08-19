import time
from random import randint


def swap_indices(alist, a, b):
    temp = alist[a]
    alist[a] = alist[b]
    alist[b] = temp


def binary_search_sort(unsorted_list):
    alist = unsorted_list.copy()
    for i in range(1, len(alist)):
        if alist[i] > alist[i - 1]:
            continue
        else:
            # Find the index of the first element that is smaller than alist[i]
            search_index0 = 0
            search_index1 = i - 1
            while search_index0 < search_index1:
                mid = (search_index0 + search_index1) // 2
                if alist[i] > alist[mid]:
                    search_index0 = mid + 1
                else:
                    search_index1 = mid
            # Put alist[i] into the sorted part of the list via swapping
            for j in range(i, search_index0, -1):
                swap_indices(alist, j, j - 1)

    return alist


def double_binary_search_sort(alist):
    index_sorted1 = 0
    index_sorted2 = len(alist) - 1


def bubble_sort(unsorted_list):
    alist = unsorted_list.copy()
    for i in range(len(alist)):
        for j in range(len(alist) - 1):
            if alist[j] > alist[j + 1]:
                swap_indices(alist, j, j + 1)

    return alist


def insertion_sort(unsorted_list):
    alist = unsorted_list.copy()
    for i in range(1, len(alist)):
        j = i
        while j > 0 and alist[j] < alist[j - 1]:
            swap_indices(alist, j, j - 1)
            j -= 1

    return alist


def selection_sort(unsorted_list):
    alist = unsorted_list.copy()
    for i in range(len(alist)):
        min_index = i
        for j in range(i, len(alist)):
            if alist[j] < alist[min_index]:
                min_index = j
        swap_indices(alist, i, min_index)

    return alist


if __name__ == '__main__':
    listOfUnsortedLists = []
    myList = []
    for _ in range(2 ** 1):
        listOfUnsortedLists.append([randint(0, 2 ** 30) for _ in range(2 ** 15)])

    # t = time.time()
    # for _list in listOfUnsortedLists:
    #     binary_search_sort(_list)
    # print("Binary Search Sort:", time.time() - t)
    #
    # t = time.time()
    # for _list in listOfUnsortedLists:
    #     bubble_sort(_list)
    # print("Bubble Sort:", time.time() - t)
    #
    # t = time.time()
    # for _list in listOfUnsortedLists:
    #     insertion_sort(_list)
    # print("Insertion Sort:", time.time() - t)
    #
    # t = time.time()
    # for _list in listOfUnsortedLists:
    #     selection_sort(_list)
    # print("Selection Sort:", time.time() - t)

    t = time.time()
    for mlist in listOfUnsortedLists:
        myList = mlist.sort()
        print(mlist)
    print("Python Sort:", time.time() - t)
