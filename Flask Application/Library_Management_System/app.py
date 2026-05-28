from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    f"mysql+pymysql://{MYSQL_USER}:Sbi%402001@{MYSQL_HOST}/{MYSQL_DB}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY

db = SQLAlchemy(app)
jwt = JWTManager(app)

# FRONTEND ROUTES

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/books")
def books():
    return render_template("books.html")

@app.route("/clients")
def clients():
    return render_template("clients.html")

@app.route("/issued-books")
def issued_books():
    return render_template("issued_books.html")

@app.route("/accounts")
def accounts():
    return render_template("accounts.html")


if __name__ == "__main__":
    app.run(debug=True)