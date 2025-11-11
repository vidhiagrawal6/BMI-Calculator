def calculate_bmi(weight, height):
    """Calculates the BMI using the formula: BMI = weight / (height^2)."""
    return weight / (height ** 2)


def categorize_bmi(bmi):
    """Categorizes the BMI into health ranges."""
    if bmi < 18.5:
        return "Underweight "
    elif 18.5 <= bmi < 24.9:
        return "Normal weight "
    elif 25 <= bmi < 29.9:
        return "Overweight "
    else:
        return "Obese "


def main():
    print("=== BMI CALCULATOR ===")

    # Input validation for weight
    while True:
        try:
            weight = float(input("Enter your weight (in kilograms): "))
            if weight <= 0:
                print(" Weight must be greater than zero.")
                continue
            break
        except ValueError:
            print(" Please enter a valid number for weight.")

    # Input validation for height
    while True:
        try:
            height = float(input("Enter your height (in meters): "))
            if height <= 0:
                print(" Height must be greater than zero.")
                continue
            break
        except ValueError:
            print(" Please enter a valid number for height.")

    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    category = categorize_bmi(bmi)

    # Output result
    print("\n--- RESULTS ---")
    print(f"Your BMI: {bmi:.2f}")
    print(f"Category: {category}")
    print("----------------")


if __name__ == "__main__":
    main()
