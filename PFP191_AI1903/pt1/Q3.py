import datetime

def is_valid_date(day, month, year):
    try:
        datetime.datetime(year, month, day)
        return True
    except ValueError:
        return False

def print_ascii_codes(chars):
    for char in sorted(chars, reverse=True):
        print(f"{char}: {ord(char)}, {hex(ord(char))}")

while True:
    print("1- Processing date data")
    print("2- Character data")
    print("3- Quit")
    
    choice = input("Choose an operation: ")
    
    if choice == "1":
        day = int(input("Enter day: "))
        month = int(input("Enter month: "))
        year = int(input("Enter year: "))
        
        if is_valid_date(day, month, year):
            print("The date is valid.")
        else:
            print("The date is not valid.")
            
    elif choice == "2":
        chars = input("Enter two characters: ")
        
        if len(chars) != 2:
            print("Please enter exactly two characters.")
            continue
        
        print_ascii_codes(chars)
        
    elif choice == "3":
        break
    
    else:
         print ("Invalid option selected. Please try again.")