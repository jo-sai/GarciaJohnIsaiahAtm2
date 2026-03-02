# Simple Python ATM Simulator

A Python command-line ATM simulator demonstrating interactive menus, basic loops, conditionals, and string-based user input validation.

## Description

This repository features a Python script (`garciaSimpleAtmLoop.py`) that simulates a basic ATM interface. Users can interact with a text-based menu to check their balance, deposit funds, withdraw money, and view a summary of their net transactions in Philippine Peso (PHP). The project utilizes a continuous `while` loop for navigation and employs string methods like `isdigit()` to validate user inputs, ensuring the program handles invalid entries gracefully.

## Features

* **Interactive Menu:** Continuous loop for multiple transactions without restarting the script.
* **Core Banking Actions:** Options to deposit, withdraw (restricted to whole numbers), and check the current balance.
* **Transaction History:** Calculates and displays the net change from the initial ₱1000.00 balance.
* **Input Validation:** Uses string manipulation to verify that users enter valid numeric formats before processing transactions, preventing crashes.

## How to Run

1. Make sure you have Python installed on your computer.
2. Clone this repository or download the script.
3. Open your terminal or command prompt.
4. Navigate to the folder containing the script and run:
   ```bash
   python garciaSimpleAtmLoop.py
