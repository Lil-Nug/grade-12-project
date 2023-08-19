import mysql.connector
import flask as f

db=mysql.connector.connect(host='localhost', user='root', password='', database='workex')


app = f.Flask(__name__, template_folder='', static_folder='')
app.config.update(TEMPLATES_AUTO_RELOAD=True)



@app.route('/', methods=['POST','GET'])
def home():
    cur = db.cursor()
    cur.execute('select * from students;')
    data=cur.fetchall()

    if f.request.method=='post':
        cur.execute('select * from students;')
        data=cur.fetchall()
        print(data)
    return f.render_template('index.html', data=data)




if __name__ == "__main__":
    app.run(debug=True)
