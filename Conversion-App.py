# A quick python program to convert measurements used for beer brewing.

# Declare conversion constants at the top level
GALLON_TO_CUPS = 16
POUND_TO_GRAMS = 453.592
OUNCE_TO_GRAMS = 28.3495

# Conversion functions
def gallons_to_cups(gallons: float):
    return gallons * GALLON_TO_CUPS

def pounds_to_grams(pounds: float):
    return pounds * POUND_TO_GRAMS

def ounces_to_grams(ounces: float):
    return ounces * OUNCE_TO_GRAMS

# Main program loop
def main():
    print("Welcome to the Unit Conversion APP!")

    while True:
        print("\nChoose a conversion:")
        print("1. Gallons to Cups")
        print("2. Pounds to Grams")
        print("3. Ounces to Grams")
        print("4. Quit")
    
        pick = input("Enter in your pick: 1-4 ")
      #Setting up the different options to pick from.
      #option 1:
        if pick == '1':
        try:
                gallons = float(input("Enter in gallons: "))
                cups = gallons_to_cups(gallons)
                print(f"{gallons} gallons is {cups} cups. ")
        except ValueError:
    print("Invalid input. Please enter a number.")

       #option 2:
        elif pick == '2':
        try: 
                pounds = float(input("Enter pounds: "))
                grams = pounds_to_grams(pounds)
                print(f"{pounds} pounds is {grams} grams.")
        except ValueError:
                print("Invalid input. Please enter a number.")


        #option 3
        elif pick == '3':
        try:
                ounces = float(input("Enter ounces: "))
                grams = ounces_to_grams(ounces)
                print(f"{ounces} ounces is {grams} grams.")
        except ValueError:
                print("Invalid input. Please enter a number.")

        #option 4
        elif pick == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    main()
