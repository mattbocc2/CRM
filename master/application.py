from flask import Flask, render_template, request
from markupsafe import escape
import requests
import json
from create_db import crea_database
import sqlite3

app = Flask(__name__)

crea_database()
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/accounts")
def view_accounts():
    conn = sqlite3.connect("crm.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT company_name, vat_code, street_name, phone,email, ateco, FROM account")
    account = cursor.fetchall()

    cursor.close()
    conn.close()

    if account is None:
        return "Account non trovato"

    return render_template("accounts.html", accounts=account)


@app.route("/view_account/<string:vat_code>")
def view_account_by_vat_code(vat_code):

    conn = sqlite3.connect("crm.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM account WHERE PIVA = ?", (vat_code,))
    account = cursor.fetchone()

    conn.close()

    if account is None:
        return "Account non trovato"

    return render_template("view_account_by_vat_code.html", account=account)



@app.route("/create_account")
def create_account():
    return render_template("create_account.html")

@app.route("/handle_creating_account", methods=['POST'])
def handle_creating_account():

    with open("credentials.json") as file:
        credentials = json.load(file)

    vat_code = request.form["vat_code"]
    
    url = f"https://test.company.openapi.com/IT-full/vat_code"
    headers = {
        "Authorization": f"Bearer {credentials["token"]}",
        "Accept": "application/json"
    }
    response = requests.get(
        url = url,
        headers = headers
    )
    return response.content

@app.route("/check_tax_code")
def check_tax_code():
    print("Hello")


# @app.route("/handle_creating_contact", methods=['POST'])
# def handle_creating_account():
#     vat_code = request.form["vat_code"]
    
#     url = f"https://test.company.openapi.com/IT-full/vat_code"
#     headers = {
#         "Authorization": "Bearer ",
#         "Accept": "application/json"
#     }
#     response = requests.get(
#         url = url,
#         headers = headers
#     )
#     return response.content

@app.route("/contacts")
def view_contacts():
    return render_template("contacts.html")





@app.route("/create_contact/<string:vat_code>")
def create_contact(vat_code):
    return render_template("create_contact.html", vat_code=vat_code)

@app.route("/contacts/<string:vat_code>")
def view_contacts_by_vat_code(vat_code):
    return escape(vat_code)



if __name__ == "__main__":
    app.run(debug = True)

