# Program to print all even numbers from a given list

def print_even_numbers(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    print("Even numbers:", evens)

# Example usage
sample_list = [1, 2, 3, 4, 5, 6]
print_even_numbers(sample_list)
