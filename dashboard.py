import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

df = pd.read_csv('finance_data.csv')
df['date'] = pd.to_datetime(df['date'], format="%m-%d-%Y")

income_expense_pie = px.pie(df, values='amount', names='category', title='Income vs Expense')
bar_fig = px.bar(df, x='date', y='amount', color='category', title='Daily Income and Expenses')

app.layout = html.Div(children=[
    html.H1(children='Personal Finance Dashboard'),
    
    dcc.Graph(
        id='income-expense-pie',
        figure=income_expense_pie
    ),
    
    dcc.Graph(
        id='daily-income-expense-bar',
        figure=bar_fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
