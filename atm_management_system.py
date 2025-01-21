# -*- coding: utf-8 -*-
"""ATM Management system.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1plELQt-Hq4P2z4TIiPyHqc-qQ2chCfOw

**ATM Management System**

The ATM Management System is a Python project that simulates real-world ATM functionalities. Designed with a focus on simplicity, security, and user-friendliness, the system provides core ATM features, such as secure user authentication, account management, and transaction processing.

***Steps followed:***

**Define Project**: Identified features like authentication, transactions, and account management.

**Design Architecture:** Plan core functionalities and a modular structure.

**Implement Authentication:** Develop PIN-based login using hashed PINs (Python library).

**Account Management:** Add account creation, PIN change, and balance updates.

**Perform Transactions:** Implement deposit, withdrawal, and balance inquiry features.

**Integrate Security:** Hash PINs and include session timeout functionality.

**Implement loop for menu-dirven interface:** Create a menu-driven interface for smooth navigation.

***Future Scope:***

The future scope includes integrating a real database for secure storage and transaction history like importing sqlite3, implementing advanced security features like multi-factor authentication and encryption like otp, and enabling fund transfers and scheduled payments. The system can evolve with a graphical user interface (GUI) or web-based access, providing cross-platform usability. Incorporating AI and machine learning could enhance fraud detection and personalized financial insights. Additionally, scalability through cloud deployment and compliance with financial regulations would make the system suitable for real-world applications.

***References:***

**Hashlib Module:** For implementing PIN hashing and secure data storage.
URL: https://docs.python.org/3/library/hashlib.html

**Python for everybody** certification - Coursera- https://www.coursera.org/specializations/python
"""

import hashlib
import time

def hash_pin(pin):
    return hashlib.sha256(pin.encode()).hexdigest()

class ATMSystem:
    def __init__(self):
        self.accounts = {}
        self.logged_in_user = None
        self.is_running = True  # Flag to control the main loop

    def create_account(self):
        print("Creating a new account...")
        username = input("Enter username: ")
        if username in self.accounts:
            print("Username already exists. Please choose a different username.")
            return
        pin = input("Enter PIN (4 digits): ")
        hashed_pin = hash_pin(pin)

        self.accounts[username] = {"pin": hashed_pin, "balance": 0.0}
        print("Account created successfully!")

    def authenticate(self):
        username = input("Enter username: ")
        if username not in self.accounts:
            print("Username not found.")
            return False
        pin = input("Enter PIN: ")
        hashed_pin = hash_pin(pin)

        if self.accounts[username]["pin"] == hashed_pin:
            self.logged_in_user = username
            print(f"Welcome, {username}!")
            return True
        else:
            print("Incorrect PIN.")
            return False

    def withdraw(self):
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Amount must be greater than 0.")
        elif amount > self.accounts[self.logged_in_user]["balance"]:
            print("Insufficient funds.")
        else:
            self.accounts[self.logged_in_user]["balance"] -= amount
            print(f"Withdrawal successful. New balance: ${self.accounts[self.logged_in_user]['balance']:.2f}")

    def deposit(self):
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("Amount must be greater than 0.")
        else:
            self.accounts[self.logged_in_user]["balance"] += amount
            print(f"Deposit successful. New balance: ${self.accounts[self.logged_in_user]['balance']:.2f}")

    def check_balance(self):
        print(f"Your balance is: ${self.accounts[self.logged_in_user]['balance']:.2f}")

    def change_pin(self):
        new_pin = input("Enter new PIN (4 digits): ")
        self.accounts[self.logged_in_user]["pin"] = hash_pin(new_pin)
        print("PIN updated successfully.")

    def menu(self):
        while True:
            print("\n--- ATM Menu ---")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Check Balance")
            print("4. Change PIN")
            print("5. Logout")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.withdraw()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.check_balance()
            elif choice == "4":
                self.change_pin()
            elif choice == "5":
                print("Logging out...")
                self.logged_in_user = None
                break
            else:
                print("Invalid choice. Please try again.")

    def run(self):
        while self.is_running:
            if not self.logged_in_user:
                print("\n--- Welcome to the ATM ---")
                print("1. Login")
                print("2. Create a New Account")
                print("3. Exit")
                choice = input("Enter your choice: ")
                if choice == "1":
                    if self.authenticate():
                        self.menu()
                elif choice == "2":
                    self.create_account()
                elif choice == "3":
                    print("Exiting... Goodbye!")
                    self.is_running = False
                else:
                    print("Invalid choice. Please try again.")

if __name__ == "__main__":
    atm_system = ATMSystem()
    atm_system.run()