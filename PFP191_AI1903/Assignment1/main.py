def menu():
    print(
        "Menu: "
        "\n1.Report"
        "\n2.Admin"
        "\n3.Exit"
    )

menu()
option = int(input("Enter option: "))


while option !=3:
    if option == 1:
        pass
    elif option == 2:
        pass
    
    else:
        print("Invalid choice.")
    print()
    menu()
    option = int(input("Enter option: "))
print("Exiting.")