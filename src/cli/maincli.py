import os
from mycode import remotetopc
from mycode import pctoremote
from cli import configsubcli

os.system("color 0A")
menus = ["1", "2", "3", "4"]
running = True
while running:
    print()
    print(" =========================")
    print(" USB SYSTEM SINCRONITATION")
    print(" =========================")
    print()
    print(" 1) Synchronize Local to external")
    print(" 2) Synchronize external to Local")
    print(" 3) Configuration")
    print(" 4) Exit")
    print()
    print(" Select an option [1-4]:", end="")

    option = input().strip()

    if option == "":
        print("No input provided. Please enter a valid option.")
        continue

    if option not in menus:
        print("Invalid option. Please select a valid option from the menu.")
        continue

    match option:
        case "1":
            pctoremote.pctoremotefunction()
        case "2":
            remotetopc.remotetopcfunction()
        case "3":
            configsubcli.configsubclifunction()
        case "4":
            print("Exiting the program. Goodbye!")
            running = False
        case default:
            print("Invalid option. Please select a valid option.[1, 2, 3, 4]")