from mycode.functions import iniconfig


def configsubclifunction():
    menus = ["1", "9"]

    running = True
    while running:
        print("Configuration Menu")
        print("1) Set max remote variables")
        print("9) Back to main menu")
        print("Select an option :", end="")
        option = input().strip()
        if option == "":
            print("No input provided. Please enter a valid option.")
            continue
        if option not in menus:
            print("Invalid option. Please select a valid option from the menu.")
            continue
        
        match option:
            case "1":
                quantity = input("Enter the number of remote directories to set: ").strip()
                if not quantity.isdigit():
                    print("Please enter a valid number.")
                    continue
                
                iniconfig.addvariables(int(quantity))
                iniconfig.erasevariables(int(quantity))
                print(f"Remote directories set to {quantity}.")


            case "9":
                print("Returning to main menu.")
                running = False
            case default:
                print("Invalid option. Please select a valid option from the menu.")
                continue