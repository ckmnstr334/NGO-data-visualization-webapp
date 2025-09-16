from flask import Flask, render_template, request, session
from flask_session import Session
import pandas as pd
from os.path import exists
import csv

file = open('numbers.csv')
table = pd.read_csv(file)
donors = table["donors"]
income = table["income"]
beneficiaries = table["beneficiaries"].sum()
projects = table["projects"].sum()
teachers = table["teachers"].sum()
avg_don = round((income.sum() / donors.sum()), 0)
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    return render_template("index.html", slider_min=5, slider_max=avg_don*2, slider_default=avg_don, projects=projects, teachers=teachers, beneficiaries=beneficiaries)


@app.route("/donate", methods=["GET", "POST"])
def donate():
    if request.method == "POST":
        donation = request.form.get("amount")  # Get slider value
        session["donation"] = donation
    else:
        donation = session.get("donation", 0)

    return render_template("donate.html", donation=donation)


@app.route("/impress")
def impress():
    return render_template("impress.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


@app.route("/thanks", methods=["GET", "POST"])
def thanks():
    if request.method == "POST":
        name = request.form.get("first-name")
        last_name = request.form.get("last-name")
        email = request.form.get("email")
        amount = request.form.get("donation")

        donations = [["First Name", "Last Name", "Email", "Amount"],]
        donation = [name, last_name, email, amount]

        if not exists("donations.csv"):
            donations.append(donation)
            with open("donations.csv", "w") as file:
                writer = csv.writer(file)
                writer.writerows(donations)
        else:
            with open("donations.csv", "a") as file:
                writer = csv.writer(file)
                new = []
                new.append(donation)
                writer.writerows(new)

    return render_template("thanks.html", name=name)


@app.route("/donations")
def donations():
    if not exists("donations.csv"):
        uploaded_df_html = "No donations yet :("
    else:
        uploaded_df = pd.read_csv("donations.csv",
                                  encoding='unicode_escape')
        uploaded_df_html = uploaded_df.to_html()
    return render_template('donations.html',
                           donations=uploaded_df_html)
