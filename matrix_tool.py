import numpy as np

print("==== MATRIX OPERATIONS TOOL ====")

# Get matrix size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input Matrix 1
print("\nEnter values for Matrix 1:")

matrix1 = []

for i in range(rows):
    row = list(map(int, input(f"Enter values separated by spaces for Row {i+1}: ").split()))
    matrix1.append(row)

# Input Matrix 2
print("\nEnter values for Matrix 2:")

matrix2 = []

for i in range(rows):
    row = list(map(int, input(f"Enter values separated by spaces for Row {i+1}: ").split()))
    matrix2.append(row)

# Convert to NumPy arrays
matrix1 = np.array(matrix1)
matrix2 = np.array(matrix2)

# Loop for multiple operations
while True:

    print("\n===== OPERATIONS MENU =====")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Exit")

    choice = int(input("\nEnter your choice: "))

    # Addition
    if choice == 1:

        print("\n=== ADDITION ===")
        print(matrix1 + matrix2)

    # Subtraction
    elif choice == 2:

        print("\n=== SUBTRACTION ===")
        print(matrix1 - matrix2)

    # Multiplication
    # Multiplication
    elif choice == 3:

        if matrix1.shape[1] == matrix2.shape[0]:

            print("\n=== MULTIPLICATION ===")
            print(np.dot(matrix1, matrix2))

        else:
            print("\nMatrix multiplication is not possible.")
            print("Number of columns of Matrix 1 must be equal to number of rows of Matrix 2.")

    # Transpose
    elif choice == 4:

        print("\n=== TRANSPOSE OF MATRIX 1 ===")
        print(matrix1.T)

    # Determinant
    elif choice == 5:

        if rows == cols:

            print("\n=== DETERMINANT OF MATRIX 1 ===")
            print(np.linalg.det(matrix1))

        else:
            print("\nDeterminant can only be found for square matrices.")

    # Exit
    elif choice == 6:

        print("\nExiting Program...")
        break

    # Invalid Choice
    else:
        print("\nInvalid Choice!")

    # Continue option
    continue_choice = input("\nDo you want to perform another operation? (yes/no): ")

    if continue_choice.lower() != "yes":

        print("\nExiting Program...")
        break

print("\nProgram Completed Successfully!")
