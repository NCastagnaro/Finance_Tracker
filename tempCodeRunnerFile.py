# File that handles the main flow of the project
import pandas as pd     # pandas allows us to load in the csv file and work with it more easily
import csv
from datetime import datetime  # provides classes for working with dates and times, allowing you to manipulate date and time values
from data_entry import get_amount, get_category, get_date, get_description  #Imports the functions from our data_entry.py file so we can access them



#define class called "CSV"
class CSV:
    CSV_FILE = "finance_data.csv"   # The variable "CSV_FILE" holds the string "finance_data.csv", which represents the name of a CSV file that will be used in the methods of this class.
    COLUMNS = ["date", "amount", "category", "description"]

    @classmethod # This decorator indicates that "initialize_csv" is a class method, not an instance method. Class methods take the class itself (cls) as their first argument, instead of "self" for instance methods
    #This function initializes the csv file
    def initialize_csv(cls):
        # This block tries to read the CSV file using pandas' read_csv function, which loads the contents of the file into a DataFrame. It uses cls.CSV_FILE to reference the class variable CSV_FILE, so the file name "finance_data.csv" is used here
        try:
            pd.read_csv(cls.CSV_FILE)
        # If the file "finance_data.csv" is not found (i.e., a FileNotFoundError is raised), the code inside the except block will execute. This block creates an empty DataFrame with the columns "date", "amount", "category", and "description"
        except FileNotFoundError:
            # dataframe is an object within pandas that allows us to access different rows and columns from a CSV file
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)    # Convert to a CSV file, which saves a local file with the name of "finance_data.csv" in the same directory as the Python file
    
    
    @classmethod
    # This function adds our entry to the csv file 
    def add_entry(cls, date, amount, category, description):
        # store in a python dictionary
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        # stores the open file in "csvfile" variable. Once we are done with the code inside, this line (33) handles automatically closing the file and dealing with memory leaks
        with open(cls.CSV_FILE, "a", newline="") as csvfile:  # using "a" to append to the file to write to the end of the file, rather than overwriting the file
            # This takes the data from our dictionary and associates it with the correct column
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            # we add this new entry
            writer.writerow(new_entry)
            print("Entry added successfully")
            
            
#Function that will call the functions we imported in the order that we want in order to collect our data            
def add():
    CSV.initialize_csv()
    data = get_date("Enter the date of the transaction (dd-mm-yyy) or enter for today's data:", allow_default = True)
    amount = get_amount()  
    category = get_category()
    description = get_description()
    CSV.add_entry(date,amount, category, description)
  
  
        
add()
