import mysql.connector
import flask as f
from simulation_functions import *




app = f.Flask(__name__, template_folder='', static_folder='')
app.config.update(TEMPLATES_AUTO_RELOAD=True)

prices = {'hdfc':1232,'uco':11,'zomato':61,'hindustan_uni':2500,'cipla':920,'tata':450}

@app.route('/', methods=['POST','GET'])
def home():
    if f.request.method=='POST':
        buybtn=f.request.form.get('buy')
        sellbtn=f.request.form.get('sell')
        admno= f.request.form["admno"]
        comp=f.request.form["company"].lower()
        shares=int(f.request.form["noshares"])
        if buybtn:
            insert(admno,comp,shares,prices)
        if sellbtn:
            delete(admno,comp,shares,prices)
    db=mysql.connector.connect(host='localhost', user='root', password='', database='workex')
    cur = db.cursor()
    cur.execute('select * from students;')
    data=cur.fetchall()
    db.close()
    cur.close()
    return f.render_template('index.html', data=data)




if __name__ == "__main__":
    app.run(debug=True)
