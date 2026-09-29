def get_grade(mark):
    """Return the letter grade based on the CAIE grading scale."""
    if 90 <= mark <= 100:
        return "A"
    elif 80 <= mark <= 89:
        return "B"
    elif 70 <= mark <= 79:
        return "C"
    elif 60 <= mark <= 69:
        return "D"
    elif 0 <= mark < 60:
        return "E"
    else:
        return None


def main():
    while True:
        user_input = input("Enter your mark (0-100) or type 'exit' to quit: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            mark = float(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        grade = get_grade(mark)

        if grade is None:
            print("Invalid mark. Please enter a number between 0 and 100.")
        else:
            print(f"Mark: {mark} -> Grade: {grade}")


if __name__ == "__main__":
    main()