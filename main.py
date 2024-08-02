import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description
import matplotlib.pyplot as plt 

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date","amount", "category", "description"]
    FORMAT = "%m-%d-%Y"
   
    @classmethod # has access to the class itself but not to an instance of the class
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index =False)
    
    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS) # takes a dict and writes it into a csv file
            writer.writerow(new_entry)

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        
        #convert start and end dates to datetime objs bc they are strings
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)
        
        #used for filtering 
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask] #returns a new filtered df that only contains rows when mask is true

        if filtered_df.empty:
            print("No transactions found in given date range.")
        else:
            print(f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print(filtered_df.to_string(index=False, formatters={"date": lambda x:x.strftime(CSV.FORMAT)}))

            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
            print("\nSummary:")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings: ${(total_income - total_expense):.2f}")

        return filtered_df

def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (mm-dd-yyyy) or enter for todays date: ", allow_default=True)
    amount = get_amount()
    category = get_category()   
    description = get_description()
    CSV.add_entry(date, amount, category, description)
    print("\nEntry added successfully.")

def plot_transactions(df):
    df.set_index("date", inplace=True)
    income_df = df[df["category"] == "Income"].resample("D").sum().reindex(df.index, fill_value=0)
    expense_df = df[df["category"]== "Expense"].resample("D").sum().reindex(df.index, fill_value=0)

    plt.figure(figsize=(10,5))
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_income_vs_expense_pie(df):
    income = df[df["category"] == "Income"]["amount"].sum()
    expense = df[df["category"] == "Expense"]["amount"].sum()
    labels = ['Income', 'Expense']
    sizes = [income, expense]
    colors = ['#66b3ff','#ff6666']
    
    plt.figure(figsize=(7,7))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title("Income vs Expense Distribution")
    plt.axis('equal')
    plt.show()


def plot_monthly_summary_bar(df):
    df['month'] = df.index.to_period('M')
    monthly_summary = df.groupby(['month', 'category'])['amount'].sum().unstack()
    
    monthly_summary.plot(kind='bar', figsize=(10, 6), stacked=True)
    plt.title('Monthly Income and Expenses')
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.grid(True)
    plt.show()


def aggregate_income_expense(df, period='M'):
    # Resample the data based on the provided period
    aggregated_df = df.resample(period).sum()
    return aggregated_df


def plot_income_vs_expense_comparison(df, period='M'):
    aggregated_df = aggregate_income_expense(df, period)
    
    plt.figure(figsize=(10, 6))
    plt.plot(aggregated_df.index, aggregated_df["amount"], label="Net Savings", color="b")
    plt.fill_between(aggregated_df.index, aggregated_df["amount"], color="b", alpha=0.1)
    plt.title(f'Income vs Expense ({period}-wise)')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    while True:
        print("\n1. Add a new transaction.")
        print("2. View transaction and summary within a date range.")
        print("3. View Income vs Expense pie chart.")
        print("4. View Monthly Income vs Expense bar graph.")
        print("5. Compare Income vs Expense over time.")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (mm-dd-yyyy): ")
            end_date = get_date("Enter the end date (mm-dd-yyyy): ")
            df = CSV.get_transactions(start_date, end_date)
            if input("Do you want to see this on a graph (y/n)").lower() == "y":
                plot_transactions(df)
        elif choice == "3":
            df = pd.read_csv(CSV.CSV_FILE)
            df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
            plot_income_vs_expense_pie(df)
        elif choice == "4":
            df = pd.read_csv(CSV.CSV_FILE)
            df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
            df.set_index("date", inplace=True)
            plot_monthly_summary_bar(df)
        elif choice == "5":
            df = pd.read_csv(CSV.CSV_FILE)
            df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
            df.set_index("date", inplace=True)
            period = input("Enter the comparison period ('D' for daily, 'W' for weekly, 'M' for monthly, 'Y' for yearly): ").upper()
            plot_income_vs_expense_comparison(df, period)
        elif choice == "6":
            print("Exiting....")
            break
        else:
            print("Invalid choice. Enter 1, 2, 3, 4, 5, or 6.")


    
if __name__ == "__main__":
    main()