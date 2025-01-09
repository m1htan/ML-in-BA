from flask import Flask, request, render_template, session, redirect, app
import numpy as np
import pandas as pd
from libs.utlis import find_and_sort_orders

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