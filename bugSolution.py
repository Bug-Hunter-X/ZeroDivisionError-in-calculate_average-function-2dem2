def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# This will now correctly return 0
my_list = []
average = calculate_average(my_list)
print(average)  # Output: 0

my_list = [10, 20, 30]
average = calculate_average(my_list)
print(average) # Output: 20.0