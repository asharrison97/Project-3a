from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash

from .forms import StockForm
from .charts import *

@app.route("/", methods=['GET', 'POST'])
@app.route("/stocks", methods=['GET', 'POST'])
def stocks():

    form = StockForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            #Get the form data to query the api
            symbol = request.form['symbol']
            chart_type = request.form['chart_type']
            time_series = request.form['time_series']
            start_date = convert_date(request.form['start_date'])
            end_date = convert_date(request.form['end_date'])

            if end_date <= start_date:
                #Generate error messagte as pass to the page
                err = "ERROR: End date cannot be earlier than Start date."
                chart = None
            else:
                #query the api using the form data
                err = None

                #THIS IS WHERE YOU WILL CALL THE METHODS FOR THE CHARTS.PY FILE AND IMPLEMENT YOUR CODE


                chart = "ASSIGN CHART TO THIS VARIABLE"

            return render_template("stock.html", form=form, template="form-template", err = err, chart = chart)

    return render_template("stock.html", form=form, template="form-template")