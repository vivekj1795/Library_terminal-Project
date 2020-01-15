import Student_Database
import sqlite3
from datetime import datetime

def check_student_username(username,password):
    conn=sqlite3.connect("library1.db")
    c=conn.cursor()
    c.execute("select [USERID],[USERNAME],[PASSWORD] FROM usersDB where [USERNAME]=(:uname) AND [PASSWORD]=(:pass)",{'uname':username,'pass':password})
    mylist = c.fetchall()
    conn.close()
    if mylist==[]:
        return 'fail',None
    else:
        return "success",mylist[0][0]

def check_librarian_username(username,contact_informaton):
    con=sqlite3.connect("library1.db")
    c=con.cursor()
    c.execute("select [USERID],[NAME],[CONTACT_INFORMATION] From librarian where [NAME]=(:uname) AND [CONTACT_INFORMATION]=(:cname)",{'uname':username,'cname':contact_informaton})
    mylist = c.fetchall()
    con.close()
    if mylist==[]:
        return 'fail',None
    else:
        return "success",mylist[0][0]


def Add_new_user_student(username,password,access,fees):
    conn=sqlite3.connect("library1.db")
    c=conn.cursor()
    c.execute("select [USERID],[USERNAME],[PASSWORD] From usersDB where [USERNAME]=(:uname) AND [PASSWORD]=(:pass)",{'uname':username,'pass':password})
    mylist = c.fetchall()
    if mylist == []:
        c.execute("insert into usersDB([USERNAME],[PASSWORD],[access],[fees]) VALUES(:uname,:pass,:acc,:fee)",{'uname':username ,'pass':password,'acc':access,'fee':fees})
        conn.commit()
        conn.close()
        return 'success',username 
    else:
        return 'fail',username 

def Add_new_user_librarian(username,contact_name):
    conn=sqlite3.connect("library1.db")
    c=conn.cursor()
    c.execute("select [USERID],[NAME],[CONTACT_INFORMATION] From librarian where [NAME]=(:uname) AND [CONTACT_INFORMATION]=(:cname)",{'uname':username,'cname':contact_name})
    mylist = c.fetchall()
    if mylist == []:
        c.execute("insert into librarian([NAME],[CONTACT_INFORMATION]) VALUES(:name,:cont)",{'name':username,'cont':contact_name})
        conn.commit()
        conn.close()
        return 'success',username 
    else:
        return 'fail',username

def get_password(username):
    conn=sqlite3.connect("library1.db")
    c=conn.cursor()
    c.execute("select [USERNAME],[PASSWORD] FROM usersDB where [USERNAME]=(:uname)",{'uname':username})
    mylist = c.fetchall()
    conn.close()
    if mylist == []:     
        return "fail"
    else:
        return mylist[0][1]
    

def update_student(username,username1,password):
    conn=sqlite3.connect("library1.db")
    c=conn.cursor()
    c.execute("select [USERNAME],[PASSWORD] FROM usersDB where [USERNAME]=(:uname)",{'uname':username})
    mylist = c.fetchall()
    if mylist != []:
        c.execute("UPDATE usersDB SET [USERNAME] = (:uname1),[PASSWORD]=(:pass1) WHERE [USERNAME]=(:uname) ",{'uname1':username1,'uname':username,'pass1':password})
        conn.commit()
        conn.close()
        return "update_successfull"
    return "username Does not exist"

def update_librarian(username,username1,password):
    conn=sqlite3.connect("library1.db")
    c=conn.cursor()
    c.execute("select [NAME],[CONTACT_INFORMATION] FROM librarian where [NAME]=(:uname)",{'uname':username})
    mylist = c.fetchall()
    if mylist != []:
        c.execute("UPDATE librarian SET [NAME] = (:uname1),[CONTAcT_INFORMATION]=(:pass1) WHERE [NAME]=(:uname) ",{'uname1':username1,'uname':username,'pass1':password})
        conn.commit()
        conn.close()
        return "update_successfull"
    return "username Does not exist"


def Delete_Account(username):
    conn=sqlite3.connect("library1.db")
    c=conn.cursor()
    c.execute("select [USERNAME] FROM usersDB where [USERNAME]=(:uname)",{'uname':username})
    mylist = c.fetchall()
    if mylist != []:
        c.execute("DELETE FROM usersDB where [USERNAME]=(:uname)",{'uname':username})    
        conn.commit()
        conn.close()
        return "deleted successfully"
    return "username does not exists"

def Add_Books(Name,author,publicaton,date,user):
    conn=sqlite3.connect("library1.db")
    c=conn.cursor()
    c.execute("select [index],[author],[name],[PUBLICATION_COMPANY],[RENTED_DATE],[RENTED_USER] FROM books where [NAME]=(:bname)",{'bname':Name})
    mylist=c.fetchall()
    print(mylist)
    if mylist == []:
        c.execute("insert into books([author],[name],[PUBLICATION_COMPANY],[RENTED_DATE],[RENTED_USER]) VALUES(:uname,:aut,:pub,:dat,:use)",{'uname':Name,'aut':author,'pub':publicaton,'dat':date,'use':user})
        conn.commit()
        conn.close()
        return "Added successfully"
    return "book already exists"

def Delete_books(Name,author):
    conn=sqlite3.connect("library1.db")
    c=conn.cursor()
    c.execute("select [name],[author] from books where [name]=(:bname) and [author]=(:bauthor)",{"bname":Name,"bauthor":author})
    mylist=c.fetchall()
    if mylist != []:
        c.execute("delete from books where [name]=(:bname) and [author]=(:bauthor)",{"bname":Name,"bauthor":author})
        conn.commit()
        conn.close()
        return "Deleted successfully"
    return "book does not exist"

def books_list():
    conn=sqlite3.connect("library1.db")
    c=conn.cursor()
    c.execute("select [name]from books")
    rows = c.fetchall()
    for i in rows: 
        print(i)
    conn.commit()
    conn.close()
