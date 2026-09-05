import sys

def main():
    print("--- Basic Python Application ---")
    
    # Check if arguments are provided (useful for automated CI testing)
    if len(sys.argv) == 3:
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
        except ValueError:
            print("Error: Please provide valid numbers.")
            sys.exit(1)
    else:
        # Fallback to interactive input if run manually
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Error: Invalid input. Please enter numbers only.")
            sys.exit(1)
            
    total_sum = num1 + num2
    print(f"The sum of {num1} and {num2} is: {total_sum}")

if __name__ == "__main__":
    main()
