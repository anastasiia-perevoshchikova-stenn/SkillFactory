sequence = list(map(int, input("Insert a sequence of numbers: ").split()))
random_number = int(input("Insert random number: "))

while random_number:
    if random_number <= min(sequence):
        print("the number does not match the search criteria, the number is less or equal to the minimum")
        random_number = int(input("Insert random number: "))
    elif random_number > max(sequence):
        print("the number does not match the search criteria, the number is greater than the maximum")
        random_number = int(input("Insert random number: "))
    else:
        break


def bubble(sequence):
    for i in range(len(sequence)):
        for j in range(len(sequence) - i - 1):
            if sequence[j] > sequence[j + 1]:
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
    return sequence


sequence_sorted = bubble(sequence)
print(sequence_sorted)


def binary_search(sequence_sorted, random_number, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if sequence_sorted[middle] < random_number and sequence_sorted[middle + 1] >= random_number:
        return middle
    elif random_number < sequence_sorted[middle]:
        return binary_search(sequence_sorted, random_number, left, middle - 1)
    else:
        return binary_search(sequence_sorted, random_number, middle + 1, right)


print(binary_search(sequence_sorted, random_number, 0, len(sequence_sorted) - 1))