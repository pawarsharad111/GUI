import sqlite3

def create():
    conn = sqlite3.connect('data.db')
    cur=conn.cursor()
    CREATE_QUERY="CREATE TABLE  IF NOT EXISTS books(title TEXT, author TEXT,isbn int, year Int)"
    cur.execute(CREATE_QUERY)
    conn.commit()
    conn.close()

def insert(title,author,isbn,year):
    conn=sqlite3.connect('data.db')
    cur=conn.cursor()
    insert_query="insert into books VALUES(?,?,?,?)"
    cur.execute(insert_query,(title,author,isbn,year))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    select_query = "SELECT * FROM books"
    cur.execute(select_query)
    result=cur.fetchall()
    conn.close()
    return result
def delete(title):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    delete_query="delete from books where Title=?"
    cur.execute(delete_query,(title,))  #when we used one element in tuple we used , after field
    conn.commit()
    conn.close()
def search(title="",author="",isbn="",year=""):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    search_query="SELECT * FROM books where Title=? or Author=? or ISBN=? or Year=?"
    cur.execute(search_query,(title,author,isbn,year))
    result=cur.fetchall()
    conn.close()
    return result
delete('python')