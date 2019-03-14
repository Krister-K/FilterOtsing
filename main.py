from flask import Flask, render_template, request
import csv

app = Flask(__name__)
@app.route('/')
def gen_table():
    file = open("oskarid.csv")
    data = csv.reader(file)
    return render_template('index.html', data=data)
@app.route('/search', methods=["GET","POST"])
def search():
    file = open("oskarid.csv")
    data = csv.reader(file)
    key = request.args.get('key')
    sieve = request.args.get('filter')
    return render_template('search.html', data=data, key=key, sieve=sieve)

