# ===================
# my train seat finder

# topics:
# O(log n) | binary search | recursion
# recursive time complexity | space complexity and call stack
# complexity ladder

# sorted train seat numbers
seat_numbers = [101, 104, 108, 112, 115, 120, 125, 130, 135, 140, 145, 150]
target_seat = 130

print("====================")
print("MY TRAIN SEAT FINDER")
print("====================")
print("Available seats:", seat_numbers)
print("Seat to Find:", target_seat)

# PART 1 - BINARY SEARCH
# algorithm:
# check the middle seat
# if the target seat is smaller, search the left
# if the target seat is bigger, search the right half
# repeat until the seat is found or the search area becomnes empty
# time complexity: O(log n)
# space complextiy : O(1)

def binary_search(seats, target):
    low = 0
    high = len(seats) - 1
    mid = (low + high) // 2
    print("Checking middle seat:", seats[mid])

    if seats[mid] == target:
        return mid, steps # type: ignore
    elif target < seats[mid]:
        high = mid - 1
    else: low = mid + 1

    return -1, steps # type: ignore

index, steps = binary_search(seat_numbers, target_seat)
print("Binary Search Result:")
if index != -1:
    print("Seat found at index:", index)
else:
    print("Seat not found.")

print("Steps taken:", steps)
print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")

# part 2 - recursive binary search
# Recursion:
# A function class itself to solve a smaller versio. of the same problem.
# Recusive Time Complexity: O(log n)
# Space Complexity: O(log n), because each recursive call uses the call stack

def recursive_binary_search(seats, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    print("Recursiv check:", seats[mid])

    if seats[mid] == target:
        return mid
    elif  target < seats[mid]:
        return recursive_binary_search(seats, target, low, mid - 1)
    else:
        return recursive_binary_search(seats, target, mid + 1, high)

recursive_index = recursive_binary_search(
    seat_numbers,
    target_seat,
    0,
    len(seat_numbers) - 1

)
print("Recursive Binary Search Result:")
if recursive_index != -1:
    print("Seat found at index:", recursive_index)
else:
    print("Seat not found.")

print("Recursive Time comlexity: O(log n)")
print("Space Complexiy: O(log n) because of the call stack")

# the complextiy ladder
print("=================")
print("COMPLEXITY LADDER")
print("==================")
print("O(1): directly checking one fixed seat")
print("O(log n): Binary search by cutting the list in half")
print("O(n): checking every seat one by one")
print("O(n^2): Comparing very seat with every othr seat")
print("===============")
# final summary
print("SUMMARY")
print("binary search is faster then checking every steal one by one")
print("It works only when the seat list is sorted")
print("Recursive binary search aslo uses O(log n) time")\
 