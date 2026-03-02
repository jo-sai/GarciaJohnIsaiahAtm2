def garcia_simple_atm():
    garciabal = 1000.0

    print("=" * 50)
    print("           WELCOME TO THE ATM ")
    print("=" * 50)
    print(f"Initial Balance: ₱{garciabal:.2f}")
    print("-" * 50)

    while True:
        print("\n|____________________________________|")
        print("|         ATM MAIN MENU              |")
        print("|------------------------------------|")
        print("|  1. Check Balance                  |")
        print("|  2. Deposit Money                  |")
        print("|  3. Withdraw Money                 |")
        print("|  4. Transaction History            |")
        print("|  5. Exit                           |")
        print("|____________________________________|")

        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            print(f"\n Your current balance: ₱{garciabal:.2f}")

        elif choice == '2':
            garciaamount_str = input("Enter amount to deposit: ₱")
            if garciaamount_str.replace('.', '', 1).isdigit(): # Check if input is a valid number
                garciaamount = float(garciaamount_str)
                if garciaamount > 0:
                    garciabal += garciaamount
                    print(f"\n Successfully deposited ₱{garciaamount:.2f}")
                    print(f" New balance: ₱{garciabal:.2f}")
                else:
                    print("\n Invalid amount! Please enter a positive number.")
            else:
                print("\n Invalid input! Please enter a number.")

        elif choice == '3':
            while True: 
                garciaamount_str = input("Enter amount to withdraw (whole numbers only): ₱")
                if garciaamount_str.isdigit(): 
                    garciaamount = int(garciaamount_str) 
                    if garciaamount > 0:
                        if garciaamount <= garciabal:
                            garciabal -= garciaamount
                            print(f"\n Successfully withdrew ₱{garciaamount:.0f}")
                            print(f" Remaining balance: ₱{garciabal:.2f}")
                            break 
                        else:
                            print(f"\n Insufficient funds!")
                            print(f" Available balance: ₱{garciabal:.2f}")
                    else:
                        print("\n Invalid amount! Please enter a positive whole number.")
                else:
                    print("\n Invalid input! Please enter a whole number.")

        elif choice == '4':
            print("\n Transaction History:")
            print("-" * 30)
            print(f"Initial Balance: ₱1000.00")
            print(f"Current Balance: ₱{garciabal:.2f}")
            garcia_net_change = garciabal - 1000.0
            if garcia_net_change >= 0:
                print(f"Net Change: +₱{garcia_net_change:.2f} (Deposit)")
            else:
                print(f"Net Change: -₱{abs(garcia_net_change):.2f} (Withdrawal)")

        elif choice == '5':
            print("\n" + "=" * 50)
            print("     Thank you for using ATM!")
            print("           Have a nice day! ")
            print("=" * 50)
            break

        else:
            print("\n Invalid choice! Please enter 1-5.")


        input("\nPress Enter to continue...")


garcia_simple_atm()