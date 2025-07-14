#include "iostream"

int main()
{
    system("color 0A"); 
    bool running = true;
    while (running == true)
    {
        std::string input;
        int option;

        std::cout << std::endl;
        std::cout << std::endl;
        std::cout << " =========================" << std::endl;
        std::cout << " USB SYSTEM SINCRONITATION" << std::endl;
        std::cout << " =========================" << std::endl;
        std::cout << std::endl;
        std::cout << " 1) Synchronize Local to external" << std::endl;
        std::cout << " 2) Synchronize external to Local" << std::endl;
        std::cout << " 3) Exit" << std::endl;
        std::cout << std::endl;
        std::cout << " Select an option [1-3]:";

        std::getline(std::cin, input);

        if (input.empty())
        {
            std::cout << "No input provided. Please enter a valid option." << std::endl;
            continue;
        }

        try {
            option = std::stoi(input);
        } catch (...) {
            std::cout << "Invalid option. Please select a valid option.[1, 2, 3]" << std::endl;
            continue;
        }

        switch (option)
        {
        case 1:
        {
            std::cout << "[Synchronizing Local to external...]" << std::endl;
            system("python code\\pctoremote.py");
            continue;
        }
        case 2:
        {
            std::cout << "[Synchronizing external to Local...]" << std::endl;
            system("python code\\remotetopc.py");
            continue;
        }
        case 3:
        {
            std::cout << "Exiting the program. Goodbye!" << std::endl;
            running = false; // Set running to false to exit the loop
            continue;
        }
        default:
        {
            std::cout << "Invalid option. Please select a valid option.[1, 2, 3]" << std::endl;
            continue;
        }
        }
    }
}
