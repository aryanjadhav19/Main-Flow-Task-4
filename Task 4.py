# Function to find the missing number in the array
def find_missing_number(arr):
    n = len(arr) + 1  # Array size n+1, so the sum should be for numbers 1 to n+1
    total_sum = (n * (n + 1)) // 2  # Sum of first n+1 natural numbers
    arr_sum = sum(arr)  # Sum of elements in the given array
    return total_sum - arr_sum

# Function to check if parentheses are balanced
def check_balanced_parentheses(s):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in matching.values():
            stack.append(char)
        elif char in matching.keys():
            if not stack or stack.pop() != matching[char]:
                return False
    return not stack

# Function to find the longest word in a sentence
def longest_word_in_sentence(sentence):
    words = sentence.split()
    return max(words, key=len)

# Function to count words in a sentence
def count_words_in_sentence(sentence):
    return len(sentence.split())

# Function to check if three numbers form a Pythagorean triplet
def check_pythagorean_triplet(a, b, c):
    a, b, c = sorted([a, b, c])
    return a**2 + b**2 == c**2

# Bubble Sort function
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Binary Search function
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Function to find subarray with given sum
def find_subarray_with_given_sum(arr, target_sum):
    current_sum = 0
    start = 0
    for end in range(len(arr)):
        current_sum += arr[end]
        while current_sum > target_sum and start <= end:
            current_sum -= arr[start]
            start += 1
        if current_sum == target_sum:
            return start, end
    return -1

# Menu-driven program
def menu():
    while True:
        print("\nMenu:")
        print("1. Find Missing Number")
        print("2. Check Balanced Parentheses")
        print("3. Longest Word in a Sentence")
        print("4. Count Words in a Sentence")
        print("5. Check Pythagorean Triplet")
        print("6. Bubble Sort")
        print("7. Binary Search")
        print("8. Find Subarray with Given Sum")
        print("9. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            arr = list(map(int, input("Enter the array elements (space separated): ").split()))
            print("Missing Number:", find_missing_number(arr))

        elif choice == 2:
            s = input("Enter the string of parentheses: ")
            if check_balanced_parentheses(s):
                print("The parentheses are balanced.")
            else:
                print("The parentheses are not balanced.")

        elif choice == 3:
            sentence = input("Enter a sentence: ")
            print("Longest Word:", longest_word_in_sentence(sentence))

        elif choice == 4:
            sentence = input("Enter a sentence: ")
            print("Word Count:", count_words_in_sentence(sentence))

        elif choice == 5:
            a, b, c = map(int, input("Enter three numbers (space separated): ").split())
            if check_pythagorean_triplet(a, b, c):
                print(f"{a}, {b}, {c} form a Pythagorean triplet.")
            else:
                print(f"{a}, {b}, {c} do not form a Pythagorean triplet.")

        elif choice == 6:
            arr = list(map(int, input("Enter the list of numbers (space separated): ").split()))
            sorted_arr = bubble_sort(arr)
            print("Sorted List:", sorted_arr)

        elif choice == 7:
            arr = list(map(int, input("Enter a sorted list of numbers (space separated): ").split()))
            target = int(input("Enter the target number: "))
            result = binary_search(arr, target)
            if result != -1:
                print(f"Target found at index {result}.")
            else:
                print("Target not found.")

        elif choice == 8:
            arr = list(map(int, input("Enter the list of numbers (space separated): ").split()))
            target_sum = int(input("Enter the target sum: "))
            result = find_subarray_with_given_sum(arr, target_sum)
            if result != -1:
                print(f"Subarray with given sum found between indices {result[0]} and {result[1]}.")
            else:
                print("No subarray found with the given sum.")

        elif choice == 9:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()