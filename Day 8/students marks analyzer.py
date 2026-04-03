#Students marks analyzer#
# Student Marks File Analyzer

total_marks = 0
count = 0

try:
    with open("marks.txt", "r") as file:
        print("Student Records:\n")
        
        for line in file:
            # Split each line into name and marks
            name, marks = line.split()
            marks = int(marks)
            
            print(f"Name: {name}, Marks: {marks}")
            
            total_marks += marks
            count += 1

    # Calculate average
    if count > 0:
        average = total_marks / count
        print("\nAverage Marks of the Class:", average)
    else:
        print("\nNo records found.")

except FileNotFoundError:
    print("Error: marks.txt file not found.")