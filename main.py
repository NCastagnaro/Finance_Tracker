# File that handles the main flow of the project
import pandas as pd     # pandas allows us to load in the csv file and work with it more easily
import csv
from datetime import datetime  # provides classes for working with dates and times, allowing you to manipulate date and time values
from data_entry import get_amount, get_category, get_date, get_description  #Imports the functions from our data_entry.py file so we can access them
import matplotlib.pyplot as plt


#define class called "CSV"
class CSV:
    CSV_FILE = "finance_data.csv"   # The variable "CSV_FILE" holds the string "finance_data.csv", which represents the name of a CSV file that will be used in the methods of this class.
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%m-%d-%Y"
    
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
            
            
    @classmethod
    #This gives us all the transactions within a date range
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        #Convert all of the dates inside of the date column to a datetime object to use them to filter by different transactions
        df["date"] = pd.to_datetime(df["date"], format = CSV.FORMAT)  #Ability to access all the different values in the date column
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)
        
        #Creating a mask, which is something that we can apply to different rows inside of dataframe to see if we should select that row or not
        #This applies to every single row inside dataframe and it's going to filter the different elements
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)    #checks if the date in the current row in the column "date" is greater than the start date and less than or equal to the end_date 
        filtered_df = df.loc[mask]  #Returms a new filtered dataframe
            
        if filtered_df.empty:
            print("No transactions found in the given data range")
        else:
            print(
                f"Transcations from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}"
            )
            
            print(
                filtered_df.to_string(
                    index=False, formatters={"date": lambda x:x.strftime(CSV.FORMAT)}
                )
            )   #We specify that we want to format the date column. We put the column name aka "date" in this case, as the key and we put a function we want to apply to every single element inside the colummn if we want to format it differently
            
            #We are getting all the rows in the dataframe where the category is equal to "Income" and "Expense". Then, from all of those rows, we are looking at the values in the "amount" column and then we are summing them.
            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum() #We want to get all the rows where the category is equl to income. Thenonce we have those rows, we want to get all of the values in the "amount" column and sum them up. 
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
            print("\nSummary:")
            print(f"Total Income: ${total_income:.2f}")     #".2f" is a format specifier that rounds it to 2 decimnal places
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings: ${(total_income - total_expense):.2f}")
            
        return filtered_df
            
#Function that will call the functions we imported in the order that we want in order to collect our data            
def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (mm-dd-yyyy) or enter for today's data:", allow_default = True)
    amount = get_amount()  
    category = get_category()
    description = get_description()
    CSV.add_entry(date,amount, category, description)   #Passes the values into the CSV file
    
#When plotting our data, we use a dataframe as a parameter,. The dataframe is going to contain all the transactions that we want to plot
#We want income to be one line and expenses be another line
def plot_transactions(df):
    df = df.sort_values(by="date")  # Ensure dates are sorted
    df.set_index('date', inplace = True)    #The index is the way in which we locate and manipulate different rows. We use the "date" column because that is how we want to find the information
    #The reindex portion is making sure the index is correct after we applied the resample operation and after we aggregate the rows that have the same date and add their ammounts together with the sum() function
    income_df = (
        df[df["category"] == "Income"]
        .resample("D")
        .sum()
        .reindex(df.index,fill_value = 0)    #The resample("D") portion: "D" stands for "daily frequency". So, we are taking the filtered dataframe with the transcations that we want. And we make sure we have a row for every single day. It also allows us to aggregate different values on the same day. It basically falls in all the missing days with "0" for the range we pick. e.g.: we pick a range and we have 3 expenses over a 200 day span. We want to fill in those empty days to help showcase our data better
    )
    
    expense_df = (
        df[df["category"] == "Expense"]
        .resample("D")
        .sum()
        .reindex(df.index,fill_value = 0)   
    )
    
    
    plt.figure(figsize=(10,5))            #figure() sets up the screen/canvas where we are going to put the graph
    plt.plot(income_df.index,income_df["amount"], label="Income", color="g")   #x axis is the index aka all the different dates. Y axis is using the amounts. And we gave it a label and picked "g" for color which is green
    plt.plot(expense_df.index,expense_df["amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses Over Time")
    plt.legend()        #Enables the legend
    plt.grid(True)      #Enables the grid lines
    plt.show()          #This takes the plot and shows it on the screen
    
    
  
  
def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transcations and a summary within a date range")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date {mm-dd-yyyy}: ")
            end_date = get_date("Enter the end date {mm-dd-yyyy}: ")
            df = CSV.get_transactions(start_date, end_date)     #assign it to df for when we plot on graph
            if input("Do you want to see a plot? (y/n)").lower() =="y":
                plot_transactions(df)           #If user selects "y", we will pass that filtered dataframe, and show the graph on screen.
        elif choice == "3":
            print("Exiting...")
            break                           #Break out of the while loop 
        
        else:
            print("Invalid choice. Enter 1, 2 or 3. ")  
            
#If we run this file directly, this if condition will fire, and then execute the main() function
#Whereas if we import this file, the main() function won't execute because the "__name__" !== "__main__"
#This protects the code from executing the main() function unless we directly execute the file
#If we removed the if statement, and even if we imported something, the main() function would execute. So, we have the conditional statement to make it so 
#we only execute this file when we run this file directly. 
if __name__ ==   "__main__":
    main()   
            



  
# CSV.get_transactions("01-01-2023", "30-04-2025")  
        
# # add()
