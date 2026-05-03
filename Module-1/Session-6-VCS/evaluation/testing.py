students = [
    {'name': 'asha', 'scores': [72, 85, 90], 'active': True},
    {'name': 'ravi', 'scores': [55, 60, 58], 'active': True},
    {'name': 'meera', 'scores': [88, 92, 95], 'active': False},
    {'name': 'kabir', 'scores': [63, 70, 75], 'active': True}
]

def calculate_average(scores):
    return sum(scores) / len(scores)

def get_status(average):
    if average >= 80:
        return "Strong"
    elif average >= 60:
        return "Steady"
    else:
        return "Needs Practice"
    
summary = {"Strong":0, "Steady":0, "Needs Practice":0}

for student in students:
    if student['active']:
        avg = calculate_average(student['scores'])
        status = get_status(avg)

        print(f"Name: {student['name'].title()}")
        print(f"Average: {avg:.2f}")
        print(f"Status: {status}")
        print("-" * 30)

        summary[status] += 1

print("Final Summary:")
for key, value in summary.items():
    print(f"{key}: {value}")



# Write a Python program that does all of the following:

# Define a function calculate_average(scores) that returns the average of a list of scores.
# Define a function get_status(average) that returns:
# Strong if the average is 80 or above
# Steady if the average is 60 or above but below 80
# Needs Practice if the average is below 60
# Loop through the list and process only active students.
# For each active student, print the student's name in title case, average score rounded to 2 decimals, and status.
# Maintain a summary dictionary that counts how many active students fall under each status.
# Print the final summary in a readable format.

# Your output should clearly show:

# each active student's name
# each active student's average score
# each active student's status
# final count of students in each status category