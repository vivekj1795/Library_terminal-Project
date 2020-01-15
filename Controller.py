import view
import Model
import Controller
import time

class user():
    def __init__(self):
        self.student_username=None
        self.student_password=None
        self.userid=None
        self.books=None 
        self.librarian_username=None
        self.librarian_contactname=None
        self.books_list=None
        self.student_access=None
        self.access=None
        self.new_student_username=None
        self.new_student_password=None
        self.book_name=None
        self.Author_name=None
        self.publication_company=None
        self.Rented_date=None
        self.Rented_user=None 

    def login_student(self):
        self.student_username = input(view.Querystring("username")) 
        self.student_password = input(view.Querystring("password"))
        status,self.userid=Model.check_student_username(self.student_username,self.student_password)
        if status == 'fail':
           view.invalid_statement()
           return mainmenu()
        return login_student_menu()  

    def login_librarian(self):
        self.librarian_username = input(view.Querystring("username"))
        self.librarian_contactname = input(view.Querystring("password"))
        status,self.userid=Model.check_librarian_username(self.librarian_username,self.librarian_contactname)
        if status == 'fail':
            view.invalid_statement()
            return mainmenu()
        return login_librarian_menu()  

    def New_register_student(self,access,fees):
        self.student_username = input(view.Querystring("username"))
        self.student_password = input(view.Querystring("password"))
        self.access = access
        self.fees = fees
        status,self.userid=Model.Add_new_user_student(self.student_username,self.student_password,self.access,self.fees)
        if status == 'fail':
            print("username already exists")
            return mainmenu()
        else:
            print(self.student_username +" added")   
            return mainmenu()

    def New_register_librarian(self):
       self.librarian_username = input(view.Querystring("username"))
       self.librarian_contactname = input(view.Querystring("contact_name"))
       status,self.userid=Model.Add_new_user_librarian(self.librarian_username,self.librarian_contactname)
       if status == 'fail':
           print("username already exists")
           return mainmenu()
       else:
            print(self.librarian_username +" added")
            return mainmenu()

    def forgot_password(self):
        self.student_username =(input(view.Querystring("username")))
        status=Model.get_password(self.student_username)
        self.student_password = status
        print(status)
        try:
                print("your password is" +self.student_password)
        except:
            print("username does not exist")
       

    def update_credentials_student(self):
        self.student_username = (input(view.Querystring("existing username")))
        self.new_student_username = (input(view.Querystring("new username")))
        self.new_student_password = (input(view.Querystring("new password")))
        status=Model.update_student(self.student_username,self.new_student_username,self.new_student_password)
        print(status)

    def update_credentials_librarian(self):
        self.librarian_username = (input(view.Querystring("existing name")))
        self.new_librarian_username = (input(view.Querystring("new name")))
        self.new_librarian_contactname = (input(view.Querystring("new contact_information")))
        status=Model.update_librarian(self.librarian_username,self.new_librarian_username,self.new_librarian_contactname)
        print(status)
    
    def delete_student_Account(self):
        self.student_username = (input(view.Querystring("username")))
        status=Model.Delete_Account(self.student_username)
        print(status)

    def Add_Books_librarian(self):
        self.book_name = (input(view.Querystring("Book Name")))
        self.Author_name=(input(view.Querystring("Author Name")))
        self.publication_company = (input(view.Querystring("publication")))
        self.Rented_user=input(view.Querystring("username"))
        self.Rented_date=input(view.Querystring("date"))
        status=Model.Add_Books(self.book_name,self.Author_name,self.publication_company,self.Rented_date,self.Rented_user)
        print(status)

    def Delete_Books_librarian(self):
        self.book_name = (input(view.Querystring("Book Name")))
        self.Author_name=(input(view.Querystring("Author Name")))
        status=Model.Delete_books(self.book_name,self.Author_name)
        print(status)

    def View_book_list(self):
        status=Model.books_list()
        print(status)
         
def mainmenu():
    choice=input(view.welcome_terminal())
    if choice=='S' or choice=='s':
         tempuser.login_student()
    elif choice=='RS' or choice=='rs':
        tempuser.New_register_student('user',5)
    elif choice== 'L' or choice=='l':
        tempuser.username = tempuser.login_librarian()
    elif choice=='RL' or choice=='rl':
        tempuser.New_register_librarian()
    elif choice=='F' or choice == 'f':
        tempuser.forgot_password()
    

tempuser = user()

def update_menu():
    choice=input(view.Update_Account())
    if choice=='S' or choice == 's':
        tempuser.update_credentials_student()
    elif choice=='L' or choice == 'l':
        tempuser.update_credentials_librarian()

def login_student_menu():
    choice=input(view.Login_Student())
    if choice=='U' or choice == 'u':
        tempuser.update_credentials_student()
    elif choice == 'D' or choice == 'd':
        tempuser.delete_student_Account()
    elif choice == 'v' or choice == 'v':
        tempuser.View_book_list

def login_librarian_menu():
    choice=input(view.login_Librarian())
    if choice=='U' or choice == 'u':
        tempuser.update_credentials_librarian()
    elif choice == 'A' or choice == 'a'  :
        tempuser.Add_Books_librarian()
    elif choice == 'D' or choice == 'd':
        tempuser.Delete_Books_librarian()

mainmenu()



