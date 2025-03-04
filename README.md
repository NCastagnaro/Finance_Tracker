Personal Finance Tracker

Overview

The Personal Finance Tracker is a Python-based command-line application designed to help users track their income and expenses efficiently. Users can log financial transactions, retrieve transactions within a specified date range, and visualize their financial data using matplotlib.

Features

Add new financial transactions (income or expenses)

View transactions within a specified date range

Get a summary of total income, total expenses, and net savings

Visualize income and expenses over time using a line chart

Files and Their Purpose

1. main.py

This is the primary script that manages the overall workflow of the application. It provides a menu-driven interface that allows users to:

Add new transactions

Retrieve and summarize transactions within a date range

Generate a plot for income and expense trends

Key functionalities:

CSV.initialize_csv(): Ensures the CSV file exists before adding data

CSV.add_entry(): Appends transaction data to finance_data.csv

CSV.get_transactions(): Retrieves transactions within a specified date range and summarizes them

plot_transactions(): Plots a time series of income and expenses using matplotlib

2. data_entry.py

Handles user input for transaction details, ensuring validity and ease of data entry.

Key functions:

get_date(prompt, allow_default=False): Ensures the entered date is valid

get_amount(): Validates that the entered amount is a positive number

get_category(): Ensures the category is either Income (I) or Expense (E)

get_description(): Captures an optional transaction description

3. finance_data.csv

A CSV file that stores financial transactions. It includes:

date: The transaction date (formatted as mm-dd-yyyy)

amount: The transaction amount

category: Either "Income" or "Expense"

description: An optional field for transaction details

Installation & Usage

Prerequisites

Ensure you have Python installed on your system. The application requires the following Python libraries:

pandas

matplotlib

You can install dependencies using pip:

pip install pandas matplotlib

Running the Application

To start tracking your finances, run:

python main.py

Example Usage

Add a new transaction:

Enter transaction details when prompted (date, amount, category, and description)

View transactions and summary within a date range:

Enter a start and end date to filter transactions

View a summary of total income, total expenses, and net savings

Visualize financial data:

Choose to generate a line chart displaying income and expenses over time

Future Enhancements

Implement a GUI for better user experience

Support for additional financial categories

Export summary reports in different formats (PDF, Excel)

License

This project is open-source and available under the MIT License.
