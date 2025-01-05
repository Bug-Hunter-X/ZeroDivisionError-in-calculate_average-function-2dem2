def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# This will raise ZeroDivisionError if the list is empty
my_list = []
average = calculate_average(my_list)