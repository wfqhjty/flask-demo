class BinarySearch:

    def __init__(self):
        self.num = 0

    """
    二分法求数组最小值
    """

    def minArray(self, array, start, end):
        self.num += 1
        if start == end:
            return array[start]
        mid = (start+end)//2
        left = self.minArray(array, 0, mid)
        right = self.minArray(array, mid+1, end)
        return min(left, right)


if __name__ == "__main__":
    binary_search = BinarySearch()
    # 二分法求数组最小值
    array = [3, 4, 6, 2, 11, 9, 12, 15, 10, 17]
    mini = binary_search.minArray(array, 0, len(array)-1)
    print(mini)
    print(binary_search.num)
