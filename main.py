from flask import Flask, render_template
import csv

file = open("oskarid.csv")
data = csv.reader(file)

app = Flask(__name__)
@app.route('/')
def gen_table():
    return render_template('index.html', data=data)

