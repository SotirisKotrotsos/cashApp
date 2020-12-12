from tkinter import *
import tkinter.font as font  
from cashDB import Database
import datetime

db = Database('cash.db')

#ωρα και ημερ/νια συστηματος
date_time = datetime.datetime.today()
time = date_time.strftime("%X")
day = date_time.strftime("%d")
month = date_time.strftime("%m")
year = date_time.strftime("%Y")
date = day + "/" + month + "/" + year


def sum_no_pay():
    Price = []
    Sumnopay = []
    N = StringVar.get(no_pay)
    Price = N.split("+")         
    price_no_pay_len = len(Price)
    for y in range(0,price_no_pay_len):
        z = float(Price[y])
        Sumnopay.append(z)
    return sum(Sumnopay)
    

def sum_pay():
    Price1 = []
    Sumpay = []
    P = StringVar.get(pay)
    Price1 = P.split("+")         
    price_pay_len = len(Price1)
    for m in range(0,price_pay_len):
        n = float(Price1[m])
        Sumpay.append(n)
    return sum(Sumpay)

def total_cash():
    total_cash = 0.01 * IntVar.get(c001) + 0.02 * IntVar.get(c002)\
    + 0.05 * IntVar.get(c005) + 0.1 * IntVar.get(c01) + 0.2 * IntVar.get(c02)\
    + 0.5 * IntVar.get(c05) + 1 * IntVar.get(c1) + 2 * IntVar.get(c2)\
    + 5 * IntVar.get(p5) + 10 * IntVar.get(p10) + 20 * IntVar.get(p20) \
    + 50 * IntVar.get(p50) + 100 * IntVar.get(p100) + 200 * IntVar.get(p200)\
    + 500 * IntVar.get(p500)
    return total_cash

def Total():
    Total = Label(app,text=float(StringVar.get(programm_cash))\
    - float(StringVar.get(credit_card))-total_cash() + float(StringVar.get(start_cash))\
    - float(sum_no_pay())  + float(sum_pay()))
    Total['font'] = myfont
    Total.grid(row=6,column=5)
    return

def Save():
    difference = float(StringVar.get(programm_cash))\
    - float(StringVar.get(credit_card))-total_cash() + float(StringVar.get(start_cash))\
    - float(sum_no_pay())  + float(sum_pay())
    db.insert(date,str(time),name.get(),total_cash(),float(StringVar.get(start_cash)),
        float(StringVar.get(programm_cash)),float(StringVar.get(credit_card)),sum_no_pay(),sum_pay(),difference)
        
def Print():
    Print_list = Tk()
    print_font = font.Font(family='Calibri', size=8, weight='bold')
    scrollbar = Scrollbar(Print_list)
    scrollbar.pack(side = RIGHT, fill = Y )
    mylist = Listbox(Print_list, yscrollcommand = scrollbar.set )
    mylist['font'] = print_font
    row = db.fetch(date_search.get())
    len_row = len(row)#πληθος του row
    for x in range(0,len_row):
        mylist.insert(END, "'Ωρα: " + str(row[x][0]))
        mylist.insert(END, "Όνομα: " + str(row[x][1]))
        mylist.insert(END, "Τελικό ταμείο: " + str(row[x][2]))
        mylist.insert(END, "Αρχικό ταμείο: " + str(row[x][3]))
        mylist.insert(END, "Σύνολο προγράμματος: " + str(row[x][4]))
        mylist.insert(END, "Πιστωτική κάρτα: " + str(row[x][5]))
        mylist.insert(END, "Μη εισπραχθέντα: " + str(row[x][6]))
        mylist.insert(END, "Επιπλέον εισπραχθέντα: " + str(row[x][7]))
        mylist.insert(END, "Διαφορά: " + str(row[x][8]))
        mylist.insert(END, "----------------")
    mylist.pack( side = TOP, fill = BOTH ) 
    scrollbar.config( command = mylist.yview ) 
    Print_list.title('List')
    Print_list.geometry('240x200')
    Print_list.mainloop()

def Delete():
    db.delete(date_search.get())

app = Tk()
myfont = font.Font(family='Calibri', size=14, weight='bold')

c2 = IntVar()
c2_label = Label(app,bg='#66CCFF', text='Νομ/τα 2',  pady=20)
c2_label['font'] = myfont
c2_label.grid(row=0, column=0)
c2_entry = Entry(app, textvariable=c2)
c2_entry.grid(row=0, column=1)

c1 = IntVar()
c1_label = Label(app,bg='#66CCFF', text='Νομ/τα 1', pady=20)
c1_label['font'] = myfont
c1_label.grid(row=1, column=0)
c1_entry = Entry(app, textvariable=c1)
c1_entry.grid(row=1, column=1)

c05 = IntVar()
c05_label = Label(app,bg='#66CCFF', text='Νομ/τα 0,5', pady=20)
c05_label['font'] = myfont
c05_label.grid(row=2, column=0)
c05_entry = Entry(app, textvariable=c05)
c05_entry.grid(row=2, column=1)

c02 = IntVar()
c02_label = Label(app,bg='#66CCFF', text='Νομ/τα 0,2', pady=20)
c02_label['font'] = myfont
c02_label.grid(row=3, column=0)
c02_entry = Entry(app, textvariable=c02)
c02_entry.grid(row=3, column=1)

c01 = IntVar()
c01_label = Label(app,bg='#66CCFF', text='Νομ/τα 0,1', pady=20)
c01_label['font'] = myfont
c01_label.grid(row=4, column=0)
c01_entry = Entry(app, textvariable=c01)
c01_entry.grid(row=4, column=1)

c005 = IntVar()
c005_label = Label(app,bg='#66CCFF', text='Νομ/τα 0,05', pady=20)
c005_label['font'] = myfont
c005_label.grid(row=5, column=0)
c005_entry = Entry(app, textvariable=c005)
c005_entry.grid(row=5, column=1)

c002 = IntVar()
c002_label = Label(app,bg='#66CCFF', text='Νομ/τα 0,02', pady=20)
c002_label['font'] = myfont
c002_label.grid(row=6, column=0)
c002_entry = Entry(app, textvariable=c002)
c002_entry.grid(row=6, column=1)

c001 = IntVar()
c001_label = Label(app,bg='#66CCFF', text='Νομ/τα 0,01', pady=20)
c001_label['font'] = myfont
c001_label.grid(row=7, column=0)
c001_entry = Entry(app, textvariable=c001)
c001_entry.grid(row=7, column=1)

p5 = IntVar()
p5_label = Label(app,bg='#66CCFF', text='Χαρ\τα των 5', pady=20)
p5_label['font'] = myfont
p5_label.grid(row=0, column=2)
p5_entry = Entry(app, textvariable=p5)
p5_entry.grid(row=0, column=3)

p10 = IntVar()
p10_label = Label(app,bg='#66CCFF', text='Χαρ\τα των 10', pady=20)
p10_label['font'] = myfont
p10_label.grid(row=1, column=2)
p10_entry = Entry(app, textvariable=p10)
p10_entry.grid(row=1, column=3)

p20 = IntVar()
p20_label = Label(app,bg='#66CCFF', text='Χαρ\τα των 20', pady=20)
p20_label['font'] = myfont
p20_label.grid(row=2, column=2)
p20_entry = Entry(app, textvariable=p20)
p20_entry.grid(row=2, column=3)

p50 = IntVar()
p50_label = Label(app,bg='#66CCFF', text='Χαρ\τα των 50', pady=20)
p50_label['font'] = myfont
p50_label.grid(row=3, column=2)
p50_entry = Entry(app, textvariable=p50)
p50_entry.grid(row=3, column=3)

p100 = IntVar()
p100_label = Label(app,bg='#66CCFF', text='Χαρ\τα των 100', pady=20)
p100_label['font'] = myfont
p100_label.grid(row=4, column=2)
p100_entry = Entry(app, textvariable=p100)
p100_entry.grid(row=4, column=3)

p200 = IntVar()
p200_label = Label(app,bg='#66CCFF', text='Χαρ\τα των 200', pady=20)
p200_label['font'] = myfont
p200_label.grid(row=5, column=2)
p200_entry = Entry(app, textvariable=p200)
p200_entry.grid(row=5, column=3)

p500 = IntVar() 
p500_label = Label(app,bg='#66CCFF', text='Χαρ\τα των 500', pady=20)
p500_label['font'] = myfont
p500_label.grid(row=6, column=2)
p500_entry = Entry(app, textvariable=p500)
p500_entry.grid(row=6, column=3)

start_cash = StringVar()
start_label = Label(app,bg='#66CCFF', text='Αρχικό ταμείο')
start_label['font'] = myfont
start_label.grid(row=0, column=4)
start_entry = Entry(app, text=start_cash)
start_entry.grid(row=0, column=5)

programm_cash = StringVar()
programmC_label = Label(app,bg='#66CCFF', text='Σύνολο προγράμματος')
programmC_label['font'] = myfont
programmC_label.grid(row=1, column=4)
programmC_entry = Entry(app, textvariable=programm_cash)
programmC_entry.grid(row=1, column=5)

credit_card = StringVar()
credit_label = Label(app,bg='#66CCFF', text='Πιστωτική κάρτα')
credit_label['font'] = myfont
credit_label.grid(row=2, column=4)
credit_entry = Entry(app, textvariable=credit_card)
credit_entry.grid(row=2, column=5)

no_pay = StringVar()
no_pay_label = Label(app,bg='#66CCFF', text='Μη εισπραχθεντα')
no_pay_label['font'] = myfont
no_pay_label.grid(row=3, column=4)
no_pay_entry = Entry(app, textvariable=no_pay)
no_pay_entry.grid(row=3, column=5)

pay = StringVar()
pay_label = Label(app,bg='#66CCFF' ,text='Επιπλεον εισπραχθεντα')
pay_label['font'] = myfont
pay_label.grid(row=4,column=4)
pay_entry = Entry(app, textvariable=pay)
pay_entry.grid(row=4,column=5)    

#Total button
total_btn = Button(app,bg='red', text='Τελικό', width=12, command=Total)
total_btn['font'] = myfont
total_btn.grid(row=5,column=4)
#date column
date_search = StringVar()
date_label = Label(app,bg='#66CCFF',text='Ημερ/νια')
date_label['font'] = myfont
date_label.grid(row=8,column=0)
date_entry = Entry(app, textvariable=date_search)
date_entry.grid(row=8,column=1)
#print button
print_btn=Button(app,bg='red',text = 'print',width=12, command=Print)
print_btn['font'] = myfont
print_btn.grid(row=8,column=2)
#name button
name = StringVar()
name_label = Label(app,bg='#66CCFF',text="Ονομ/νυμο")
name_label['font'] = myfont
name_label.grid(row=6, column=4)
name_entry = Entry(app, textvariable=name)
name_entry.grid(row=6,column=5)
#save button
save_btn=Button(app,bg='red',text ='save', width=12, command=Save)
save_btn['font'] = myfont
save_btn.grid(row=7,column=4)
#delete button
delete_btn = Button(app,bg='red',text='delete',width=12,command=Delete)
delete_btn['font']=myfont
delete_btn.grid(row=7,column=5)


app.configure(background='#66CCFF')    
app.title('Cash App')
app.geometry('950x600')

app.mainloop()

