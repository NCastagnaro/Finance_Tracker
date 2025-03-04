#File to collect data from the user
from datetime import datetime
date_format = "%m-%d-%Y"        #Defines the expected format for date input and output in your program. The format string follows the datetime module's convention: %m → Month (01-12)   %d → Day (01-31)   %Y → Year (4-digit, e.g., 2025)
CATEGORIES = {"I": "Income", "E":"Expense"} #set up a dictionary

#Prompt is what we ask the user to input
#If user wants to use today's date, they can just hit "enter", otherwise they can enter a specific date

#Recursive function that we will keep calling until we eventually have a valid date entered 
def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        print(datetime.now())
        return datetime.today().strftime(date_format)
        
    
    #if date they entered in was invalid, this will handle that situation
    try:
        #We take what the user enters and converting it into a date-time object
        valid_date = datetime.strptime(date_str, date_format)   #date_str is the data input and date_format is the format string
        return valid_date.strftime(date_format)     #Cleans up the date that the user entered and returns it in the format that the user needs
    #If the try statement does not work because we have a ValueError, we will prompt the user to enter a valid date
    except ValueError:
        print("Invalid date format. Please enter the date in mm-dd-yyyy format")
        return get_date(prompt, allow_default)  #Recursive part of the function that will call the function again if we hit this part of the code
    
    

def get_amount():
    try:
        amount = float(input("Enter the amount:"))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative non-zero value.")
        return amount
    #If conversion to a float does not work, we will go here 
    except ValueError as e:
        print(e)
        return get_amount()
 
def get_category():
    category = input("Enter the category('I' for Income or 'E' for Expense):").upper()  #Converts user input to uppercase
    if category in CATEGORIES:
        return CATEGORIES[category]     #Rather than returning "I" or "E", we return "Income" or "Expense"
    
    #This serves as the else statement
    print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
    return get_category()   #Recursively runs till we get a category
    
        

def get_description():
    return input("Enter a description(optional): ")

    