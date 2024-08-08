"""
This algorith is an algorithm to sort lists in ascending or descending order.
INPUT: Takes in "numbers" which is the array that gets sorted, use lists. "Order" wants to know the order
"""


def sorted_list(numbers, order):
    """
    Sorts arrays from any order you like
    """
    for i in range(0, len(numbers)):

        if order == True:
            for j in range(i + 1, len(numbers), 2):
                if numbers[i] < numbers[j]:
                    temp = numbers[i]
                    numbers[i] = numbers[j]
                    numbers[j] = temp
        else:
            for j in range(i + 1, len(numbers), 2):
                if numbers[i] > numbers[j]:
                    temp = numbers[i]
                    numbers[i] = numbers[j]
                    numbers[j] = temp
        return numbers