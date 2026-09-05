import sys

def main():
    print("--- Basic Python Addition Application ---")
    
    # Allows for non-interactive execution during CI testing
    if len(sys.argv) == 3:
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
        except ValueError:
            print("Error: Please provide valid numbers as arguments.")
            sys.exit(1)
    else:
        # Fallback to interactive mode if no arguments are provided
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Error: Invalid input. Please enter numerical values.")
            sys.exit(1)
            
    total = num1 + num2
    print(f"The sum of {num1} and {num2} is: {total}")

if __name__ == "__main__":
    main()
