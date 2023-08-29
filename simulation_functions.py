import mysql.connector
def insert(adno,company,amount,prices):
    db=mysql.connector.connect(host='localhost', user='root', password='', database='workex')
    mc= db.cursor()
    mc.execute(f'select cash_in_hand,{company} from students where admission_no={adno}')
    fetch= mc.fetchall()
    mc.execute(f'select cash_in_hand,{company} from students where admission_no={adno}')
    fetch= mc.fetchall()

    if fetch==[]:
        mc.execute(f"insert into students (admission_no,cash_in_hand,{company}) values ({adno},{5000-(prices[company]*amount)},{prices[company]*amount})")

    else:
        cash=fetch[0][0]
        comp=fetch[0][1]
        mc.execute(f"update students set cash_in_hand={cash-prices[company]*amount},{company}={comp+prices[company]*amount} where admission_no={adno}")
    db.commit()
    db.close()


def delete(adno,company,amount,prices):
    db=mysql.connector.connect(host='localhost', user='root', password='', database='workex')
    mc= db.cursor()
    mc.execute(f'select cash_in_hand,{company} from students where admission_no={adno}')
    fetch= mc.fetchall()

    if fetch==[]:
        print('bro does not exist')
    else:
        cash=fetch[0][0]
        comp = fetch[0][1]
        mc.execute(f"update students set cash_in_hand={cash+prices[company]*amount},{company}={comp-prices[company]*amount} where admission_no={adno}")
    db.commit()
    db.close()