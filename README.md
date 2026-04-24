# ATM Simulation System

*This project is a menu-driven ATM simulation system built using Python. It replicates the core functionalities of a real-world ATM, allowing users to perform basic banking operations such as checking balance, depositing money, withdrawing funds, and viewing transaction history.*

*The application follows a modular and object-oriented design, separating concerns into models, services, and a user interface layer for better maintainability and scalability.*

## Features
**Account management with a default test account
Deposit and withdrawal operations with validation
Real-time balance inquiry
Transaction history (mini statement) with timestamps
Interactive command-line interface
Error handling for invalid inputs and insufficient funds
Project Structure**

*The project is organized into multiple components:*

## Models
Account – Represents a bank account
Transaction – Stores transaction details with type and timestamp
Services
BankService – Handles core banking logic (deposit, withdraw, balance)
StatementService – Manages transaction records
## UI Layer
ATMMenu – Provides a menu-driven interface for user interaction
Entry Point
main.py – Starts the ATM application
## How It Works
The program initializes with a default account:
Account Number: 1234567890
Holder Name: John Doe
Balance: $1000.00
**Users interact through a menu with options to:**
Check balance
Withdraw money
Deposit money
View transaction statement
Exit the system
**Each transaction is recorded with:**
Type (Deposit/Withdrawal)
Amount
Updated balance
Timestamp
## Technologies Used
***Python 3
Object-Oriented Programming (OOP)
Built-in modules: datetime, enum***

## Purpose

*This project is designed to:

Demonstrate OOP principles in Python
Showcase clean architecture and separation of concerns
Provide a beginner-friendly banking system simulation
Serve as a base for more advanced systems (e.g., GUI, database integration)*

## Future Enhancements

Add multiple account support with authentication
Integrate a database (SQLite/MySQL)
Build a graphical user interface (GUI)
Add PIN-based security system
