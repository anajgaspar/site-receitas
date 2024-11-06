from flask import Flask, render_template, url_for
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

mysql = MySQL(app)

@app.route("/")
def inicio():
    return render_template('index.html')

@app.route("/pedido")
def pedido():
    return render_template('pedido.html')

@app.route("/recipe")
def recipe():
    return render_template('recipe.html')

@app.route("/recipelas")
def recipelas():
    return render_template('recipe-las.html')

@app.route("/recipechee")
def recipechee():
    return render_template('recipe-che.html')