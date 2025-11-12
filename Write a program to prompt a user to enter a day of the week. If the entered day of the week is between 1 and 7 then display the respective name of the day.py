
# Program to print the day of the week based on a number (1-7)

def get_day_name(day_number):
    """Return the day name for a given number between 1 and 7."""
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return days.get(day_number, None)  # Returns None if invalid

def main():
    try:
        # Take user input
        day_number = int(input("Enter a number between 1 and 7: "))
        
        # Validate and print result
        day_name = get_day_name(day_number)
        if day_name:
            print(f"Day {day_number} is {day_name}.")
        else:
            print("Error: Please enter a valid number between 1 and 7.")
    
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
