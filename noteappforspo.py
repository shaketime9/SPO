from tkinter import * 
import shelve
db= shelve.open('noteapp')
app = Tk()

def add(self):
    name = name_entry.get()
    number = number_entry.get()
    db[str(name)] = number
def show(self):
    list_info = Listbox(app)
    for key in db.keys():
        s = key+ "-"+ db[key]
        list_info.insert(0, s)
    list_info.grid(row=6,column=0,sticky=W)

def delete(self):
    name = name_entry.get()
    if name in db: del db[name]
   
app.title('Your contacts')
app.geometry('700x350')
#name
name_label=Label(app, text='Имя:')
name_label.grid(row=0,column=0, sticky=W)
name_entry= Entry(app)
name_entry.grid(row=0,column=1, sticky=W)
#add
name_button=Button(app, text='Добавить')
name_button.bind("<Button-1>", add)
name_button.grid(row=3,column=0,sticky=W)
#number
number_label=Label(app, text='Номер:')
number_label.grid(row=1,column=0, sticky=W)
number_entry= Entry(app)
number_entry.grid(row=1,column=1, sticky=W)
#show
show_button=Button(app, text='Показать Записи')
show_button.bind("<Button-1>", show)
show_button.grid(row=4,column=0,sticky=W)
#delete
del_button=Button(app, text='Удалить')
del_button.bind("<Button-1>", delete)
del_button.grid(row=5,column=0,sticky=W)
app.mainloop()
db.close()