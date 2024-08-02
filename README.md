# Personal Finance Tracker

A personal finance tracking application that allows you to log, visualize, and analyze your income and expenses over time. The project consists of a main Python application, a data entry module, and a Dash-based web dashboard.

## Features

- **Add Transactions**: Log new transactions with date, amount, category, and description.
- **View Transactions**: Filter and view transactions within a specific date range.
- **Income vs Expense Analysis**: Visualize the distribution of income and expenses using pie charts.
- **Monthly Summary**: Generate and view bar graphs showing monthly income and expenses.
- **Comparative Analysis**: Compare income and expenses over time with customizable periods (daily, weekly, monthly, yearly).

## Files

- `main.py`: Main script to add transactions, view transactions, and plot various graphs.
- `data_entry.py`: Contains functions to handle user input for date, amount, category, and description.
- `dashboard.py`: Dash application for interactive web-based visualization of income and expenses.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages:
  - `pandas`
  - `matplotlib`
  - `plotly`
  - `dash`

Install the required packages using pip:

```bash
pip install pandas matplotlib plotly dash
```

### Running the Application

#### Run the Main Application

To start the command-line interface, use:

```bash
python main.py
```

Follow the on-screen prompts to:

1. **Add a new transaction**:
   - Enter the date (or leave blank for today's date).
   - Enter the amount (must be a positive number).
   - Enter the category (`'I'` for Income or `'E'` for Expense).
   - Provide an optional description.

2. **View transactions**:
   - Filter transactions by date range.
   - View the filtered transactions in the console.
   - Optionally, visualize the data using a graph.

3. **Generate visualizations**:
   - (3) Income vs Expense pie chart.
   - (4) Monthly income vs expense bar graph.
   - (5) Comparative analysis over different periods (daily, weekly, monthly, yearly).

#### Run the Web Dashboard

To start the Dash-based web dashboard, use:

```bash
python dashboard.py
```

## Usage

### Adding a New Transaction

When prompted, enter:

- **Date** (or leave blank for today's date).
- **Amount** (must be a positive number).
- **Category** (`'I'` for Income or `'E'` for Expense).
- **Description** (optional).

### Viewing Transactions

To view transactions within a specific date range:

1. Enter the start date and end date.
2. Optionally, choose to visualize the data using a graph.

### Visualizing Data

- **Income vs Expense Pie Chart**: Displays the distribution of income and expenses.
- **Monthly Summary Bar Graph**: Shows income and expenses on a monthly basis.
- **Income vs Expense Comparison**: Provides a comparison over selected periods (daily, weekly, monthly, yearly).


## Code Overview

### `main.py`

Contains the core functionality for managing transactions and generating visualizations. Key components include:

- **`CSV` class**: Handles CSV file operations (initialization, adding entries, and retrieving transactions).
- **`add()` function**: Adds a new transaction.
- **Visualization functions**: `plot_transactions()`, `plot_income_vs_expense_pie()`, `plot_monthly_summary_bar()`, and `plot_income_vs_expense_comparison()`.

### `data_entry.py`

Provides functions to get user input for transaction details:

- **`get_date()`**
- **`get_amount()`**
- **`get_category()`**
- **`get_description()`**

### `dashboard.py`

Uses Dash to create a web-based dashboard for visualizing financial data:

- **Pie chart** for income vs. expense.
- **Bar graph** for daily income and expenses.

