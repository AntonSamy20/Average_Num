# Function to calculate the average of three numbers
def average_of_three_numbers(num1, num2, num3):
    total = num1 + num2 + num3
    average = total / 3
    return average

# Example usage
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

avg = average_of_three_numbers(num1, num2, num3)
print(f"The average of the three numbers is: {avg}")
