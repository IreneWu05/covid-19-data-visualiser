from flask import Flask, render_template, request
app = Flask(__name__)




#import database
import sqlite3

@app.route('/')
def index():
    
    Value = []
    con = sqlite3.connect('activedata.db')
    cur = con.cursor()
    sql = "SELECT Value from data WHERE ID = 749 OR ID = 752 OR ID = 751 OR ID = 747"
    data1 = cur.execute(sql)
    for item in data1:
        Value.append(item)

    bar1 = []
    con = sqlite3.connect('activedata.db')
    cur = con.cursor()
    sql = 'SELECT Value from data WHERE ID = 752'
    data2 = cur.execute(sql)
    for item in data2:
        bar1.append(' '.join(str(i) for i in item))#remove the brackets

    cur.close()
    con.close()
    return render_template('index.html',Value=Value, bar1=bar1)
