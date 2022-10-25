from flask import Flask, render_template, request
app = Flask(__name__)




#import database
import sqlite3

@app.route('/')
def index():

    con = sqlite3.connect('activedata.db')
    con.row_factory = sqlite3.Row
    db = con.cursor()
    res = db.execute("SELECT Value from data WHERE ID = 739")
    return render_template('index.html', datas=res.fetchall())

    db.close()
    
    ########test
    
        from flask import Flask, render_template, request
app = Flask(__name__)


ACTIVEDATADB = 'activedata.db'

#import database
import sqlite3


def fetchactivedata(con):

    datas = []
    cur = con.execute('SELECT Value from data WHERE ID = 739')
    for row in cur:
        datas.append(list(row))

    return{'Value':datas}

@app.route('/')
def index():
    con = sqlite3.connect(ACTIVEDATADB)
    activedata = fetchactivedata(con)
    con.close()
    return render_template('index.html', datas=activedata['Value'])


     
