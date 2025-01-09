from flask import Flask, request, render_template, session, redirect, app
import numpy as np
import pandas as pd

def find_and_sort_orders(df, min_value, max_value, sort_type=True):
    """
    Find and sort unique orders within a specified range of total values.

    Parameters:
        df (DataFrame): The input DataFrame containing sales transaction data.
        min_value (float): The minimum value of the order total range.
        max_value (float): The maximum value of the order total range.
        sort_type (bool): Sorting order, True for ascending, False for descending.

    Returns:
        DataFrame: A DataFrame containing OrderID and their total value, sorted based on sort_type.
    """
    # Calculate total value for each order
    order_totals = df.groupby('OrderID').apply(
        lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum()
    ).reset_index(name='Sum')  # Rename the aggregated column to 'Sum'

    # Filter orders within the specified range
    filtered_orders = order_totals[
        (order_totals['Sum'] >= min_value) & (order_totals['Sum'] <= max_value)
    ]

    # Sort the orders based on the sort_type
    sorted_orders = filtered_orders.sort_values(by='Sum', ascending=sort_type)

    return sorted_orders

app=Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        min_value = float(request.form["min_value"])
        max_value = float(request.form["max_value"])
        sort_order = request.form["sort_order"]  # Get sort order from the form
        sort_type = True if sort_order == "ascending" else False  # Determine sorting type

        df = pd.read_csv('../Dataset/SalesTransactions.csv')
        result = find_and_sort_orders(df, min_value, max_value, sort_type)

        return render_template(
            "orders_sort.html",
            tables=[result.to_html(classes='data')],
            titles=result.columns.values
        )
    else:
        return render_template("orders_sort.html")

if __name__ =="__main__":
    app.run(host="localhost",port=9000,debug=True)