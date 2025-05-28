def list_sum(list1, list2) -> list:
    """This function takes two list as arguments and returns a list
       with the sums of the items in the two original lists at each index"""
    total = []
    list1_len = len(list1)
    list2_len = len(list2)
    index = 0
    while index < (list1_len):
        if index < list1_len:
            total.append(list1[index] + list2[index])
        index += 1
    return total


if __name__ == "__main__":
    print(list_sum(list1=[1, 2, 10], list2=[7, 8, 9]))