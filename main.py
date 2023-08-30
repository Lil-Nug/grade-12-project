import mysql.connector
import flask as f
from simulation_functions import *


host='localhost'
user='root'
password='5120'
database='school'


app = f.Flask(__name__, template_folder='', static_folder='')
app.config.update(TEMPLATES_AUTO_RELOAD=True)

@app.route('/')
def index():
    cn=mysql.connector.connect(host=host, user=user, password=password,database=database)
    cur=cn.cursor()
    cur.execute('show tables;')
    data=cur.fetchall()
    cn.close()
    cur.close()
    return f.render_template('index.html', data=data)
    
    
@app.route('/table', methods=['POST'])
def table():
    cn=mysql.connector.connect(host=host, user=user, password=password,database=database)
    cur=cn.cursor()
    cur.execute(f"select * from {f.request.form['table']}")
    data=cur.fetchall()
    return f.render_template('sim_page.html', data=data)

if __name__ == "__main__":
    
    app.run(debug=True)
