import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS cash
                        (date varchar(20),
                        time varchar(20),
                        name varchar(20),
                        total_cash float,
                        start_cash float,
                        programm_cash float,
                        credit_card float,
                        total_nopay float,
                        total_pay float,
                        difference float)""")
        self.conn.commit()

    def insert(self,date,time,name,total_cash,start_cash,programm_cash,credit_card,total_nopay,total_pay,difference):
        self.cur.execute("""INSERT INTO cash VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                            (date,time,name,total_cash,start_cash,programm_cash,credit_card,total_nopay,total_pay,difference))
        self.conn.commit()                   

    def fetch(self, date):
        self.cur.execute("""SELECT time,name,total_cash,start_cash,programm_cash,
                        credit_card,total_nopay,total_pay,difference FROM cash WHERE (date=?)""",[date])
        rows = self.cur.fetchall()
        return rows 

    def delete(self, date):
        self.cur.execute("""DELETE FROM cash WHERE (date=?)""",[date])
        self.conn.commit()