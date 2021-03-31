from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
import csv
from datetime import datetime
from time import sleep
import re
import os, sys

print(os.getcwd())

class ScreenMain(QDialog):
    def __init__(self):
        super(ScreenMain, self).__init__()
        loadUi("screen_main.ui", self)

        self.button_register.clicked.connect(self.goto_ScreenRegister)
        self.button_login_user.clicked.connect(self.goto_ScreenLoginUser)
        self.button_login_officer.clicked.connect(self.goto_ScreenLoginOfficer)

    def goto_ScreenRegister(self):
        screenRegister=ScreenRegister()
        widget.addWidget(screenRegister)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_ScreenLoginUser(self):
        screenLoginUser=ScreenLoginUser()
        widget.addWidget(screenLoginUser)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_ScreenLoginOfficer(self):
        screenLoginOfficer=ScreenLoginOfficer()
        widget.addWidget(screenLoginOfficer)
        widget.setCurrentIndex(widget.currentIndex()+1)

class ScreenRegister(QDialog):
    def __init__(self):
        super(ScreenRegister, self).__init__()
        loadUi("screen_register.ui", self)

        self.button_register.clicked.connect(self.register_control)
        self.button_return.clicked.connect(self.goto_ScreenMain)

    def register_control(self):
        self.name = self.line_register_name.text()
        self.idnumber = self.line_register_id.text()
        self.password = self.line_register_password.text()
        self.email = self.line_register_email.text()

        result=User().signup(self.name,self.idnumber,self.password,self.email)
        self.text_browser_display.setText(result)


    def goto_ScreenMain(self):
        screenMain = ScreenMain()
        widget.addWidget(screenMain)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class ScreenLoginUser(QDialog):
    def __init__(self):
        super(ScreenLoginUser, self).__init__()
        loadUi("screen_login_user.ui", self)

        self.button_login_user.clicked.connect(self.check_the_login)
        self.button_return.clicked.connect(self.goto_ScreenMain)

    def check_the_login(self):

        self.email = self.line_email.text()
        self.password = self.line_password.text()
        result = User().login(self.email,self.password)
        self.text_browser_display.setText(result)
        if User.isloggedIn:
            sleep(2)
            self.goto_ScreenOperations()


    def goto_ScreenOperations(self):
        screenOperations=ScreenOperations()
        widget.addWidget(screenOperations)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_ScreenMain(self):
        screenMain = ScreenMain()
        widget.addWidget(screenMain)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class ScreenLoginOfficer(QDialog):
    def __init__(self):
        super(ScreenLoginOfficer, self).__init__()
        loadUi("screen_login_officer.ui", self)

        self.button_login_officer.clicked.connect(self.check_the_login)
        self.button_return.clicked.connect(self.goto_ScreenMain)

    def check_the_login(self):

        self.email = self.line_email.text()
        self.password = self.line_password.text()
        result = User().login_officer(self.email,self.password)
        self.text_browser_display.setText(result)
        if User.isloggedIn:
            sleep(2)
            self.goto_ScreenOperationsBank()

    def goto_ScreenOperationsBank(self):
        screenOperationsBank=ScreenOperationsBank()
        widget.addWidget(screenOperationsBank)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_ScreenMain(self):
        screenMain = ScreenMain()
        widget.addWidget(screenMain)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class ScreenOperations(QDialog):
    def __init__(self):
        super(ScreenOperations, self).__init__()
        loadUi("screen_operations.ui", self)

        self.button_logout.clicked.connect(self.goto_Logout)
        self.button_insert.clicked.connect(self.goto_ScreenInsert)
        self.button_withdraw.clicked.connect(self.goto_ScreenWithdraw)
        self.button_edit_user.clicked.connect(self.goto_ScreenEditUser)
        self.button_transfer_int.clicked.connect(self.goto_ScreenTransferInt)
        self.button_transfer_ext.clicked.connect(self.goto_ScreenTransferExt)
        self.button_user_info.clicked.connect(self.check_user_info)
        self.button_extract.clicked.connect(self.extract_account)
        self.button_check_balance.clicked.connect(self.goto_check_balance)


    def goto_Logout(self):

        result = User().logout()
        self.text_browser_display.setText(result)
        if User.isloggedIn==False:
            sleep(2)
            self.goto_ScreenMain()


    def goto_ScreenMain(self):
        screenMain = ScreenMain()
        widget.addWidget(screenMain)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goto_ScreenInsert(self):
        screenInsert = ScreenInsert()
        widget.addWidget(screenInsert)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    def goto_ScreenWithdraw(self):
        screenWithdraw = ScreenWithdraw()
        widget.addWidget(screenWithdraw)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goto_ScreenEditUser(self):
        screenEditUser = ScreenEditUser()
        widget.addWidget(screenEditUser)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goto_ScreenTransferInt(self):
        screenTransferInt = ScreenTransferInt()
        widget.addWidget(screenTransferInt)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goto_ScreenTransferExt(self):
        screenTransferExt = ScreenTransferExt()
        widget.addWidget(screenTransferExt)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def check_user_info(self):
        result = User().usr_info()
        self.text_browser_display.setText(result)

    def extract_account(self):
        result = User().usr_extractOfAccount()
        self.text_browser_display.setText(result)

    def goto_check_balance(self):
        result = Bank().user_check_balance()
        self.text_browser_display.setText(result)

class ScreenInsert(QDialog):
    def __init__(self):
        super(ScreenInsert, self).__init__()
        loadUi("screen_insert.ui", self)
        self.text_browser_display.setText("Please enter amount of insert money")
        self.button_insert.clicked.connect(self.insert_control)
        self.button_return.clicked.connect(self.goto_ScreenOperations)

    def insert_control(self):
        self.amount_insert = self.line_insert.text()
        result=Bank().insert_money(self.amount_insert)
        self.text_browser_display.setText(result)

    def goto_ScreenOperations(self):
        screenOperations=ScreenOperations()
        widget.addWidget(screenOperations)
        widget.setCurrentIndex(widget.currentIndex()+1)

class ScreenWithdraw(QDialog):
    def __init__(self):
        super(ScreenWithdraw, self).__init__()
        loadUi("screen_withdraw.ui", self)
        self.text_browser_display.setText("Please enter amount of withdraw money")
        self.button_withdraw.clicked.connect(self.withdraw_control)
        self.button_return.clicked.connect(self.goto_ScreenOperations)

    def withdraw_control(self):
        self.amount_withdraw = self.line_withdraw.text()
        result=Bank().withdraw_money(self.amount_withdraw)
        self.text_browser_display.setText(result)

    def goto_ScreenOperations(self):
        screenOperations = ScreenOperations()
        widget.addWidget(screenOperations)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class ScreenEditUser(QDialog):
    def __init__(self):
        super(ScreenEditUser, self).__init__()
        loadUi("screen_edit_user.ui", self)
        self.button_save_edit.clicked.connect(self.control_save_edit)
        self.button_delete_user.clicked.connect(self.control_delete_user)
        self.button_return.clicked.connect(self.goto_ScreenOperations)

    def control_save_edit(self):
        self.name = self.line_edit_name.text()
        self.password = self.line_edit_password.text()
        self.id = self.line_edit_id.text()
        result=User().edit_usr_acnt(self.name,self.password,self.id)
        self.text_browser_display.setText(result)

    def control_delete_user(self):
        result = User().del_usr_acnt()
        self.text_browser_display.setText(result)
        result = User().logout()
        self.text_browser_display.setText(result)
        ScreenOperations().goto_ScreenMain()



    def goto_ScreenOperations(self):
        screenOperations = ScreenOperations()
        widget.addWidget(screenOperations)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class ScreenTransferInt(QDialog):
    def __init__(self):
        super(ScreenTransferInt, self).__init__()
        loadUi("screen_transfer_int.ui", self)
        self.text_browser_display.setText("Please enter internal email and amount of money")
        self.button_transfer_int.clicked.connect(self.transfer_int_control)
        self.button_return.clicked.connect(self.goto_ScreenOperations)

    def transfer_int_control(self):
        self.transfer_email = self.line_int_trans_email.text()
        self.transfer_amount = self.line_int_trans_money.text()
        result=Bank().transfer_money_internal(self.transfer_email,self.transfer_amount)
        self.text_browser_display.setText(result)

    def goto_ScreenOperations(self):
        screenOperations = ScreenOperations()
        widget.addWidget(screenOperations)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class ScreenTransferExt(QDialog):
    def __init__(self):
        super(ScreenTransferExt, self).__init__()
        loadUi("screen_transfer_ext.ui", self)
        self.text_browser_display.setText("Please enter external email and amount of money")
        self.button_transfer_ext.clicked.connect(self.transfer_ext_control)
        self.button_return.clicked.connect(self.goto_ScreenOperations)

    def transfer_ext_control(self):
        self.transfer_email = self.line_ext_trans_email.text()
        self.transfer_amount = self.line_ext_trans_money.text()
        result=Bank().transfer_money_external(self.transfer_email,self.transfer_amount)
        self.text_browser_display.setText(result)

    def goto_ScreenOperations(self):
        screenOperations = ScreenOperations()
        widget.addWidget(screenOperations)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class ScreenOperationsBank(QDialog):
    def __init__(self):
        super(ScreenOperationsBank, self).__init__()
        loadUi("screen_operations_bank.ui", self)

        self.button_logout.clicked.connect(self.goto_Logout)
        self.button_insert.clicked.connect(self.display_tot_insert)
        self.button_withdraw.clicked.connect(self.display_tot_withdraw)
        self.button_transfer_int.clicked.connect(self.display_tot_transfer_int)
        self.button_transfer_ext.clicked.connect(self.display_tot_transfer_ext)
        self.button_check_balance.clicked.connect(self.display_tot_balance)
        self.button_extract.clicked.connect(self.extract_account)

    def goto_Logout(self):
        result = User().logout()
        self.text_browser_display.setText(result)
        if User.isloggedIn==False:
            sleep(2)
            self.goto_ScreenMain()

    def display_tot_insert(self):
        result = Bank().bank_daily_tot_insert()
        self.text_browser_display.setText(result)

    def display_tot_withdraw(self):
        result = Bank().bank_daily_tot_withdraw()
        self.text_browser_display.setText(result)

    def display_tot_transfer_int(self):
        result = Bank().bank_daily_tot_transfer_int()
        self.text_browser_display.setText(result)

    def display_tot_transfer_ext(self):
        result = Bank().bank_daily_tot_transfer_ext()
        self.text_browser_display.setText(result)

    def display_tot_balance(self):
        result = Bank().user_check_balance()
        self.text_browser_display.setText(result)

    def extract_account(self):
        result = User().bank_extractOfAccount()
        self.text_browser_display.setText(result)

    def goto_ScreenMain(self):
        screenMain = ScreenMain()
        widget.addWidget(screenMain)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class User:
    isloggedIn=False
    currentUser= []

    def __init__(self, balance=0):
        self.balance = balance

    def signup(self,name,idnumber,password,email):
        signupp=0

        self.name = name
        if self.name != "":
            word_amount=(self.name).split(" ")
            all_alphabet = all(map(str.isalpha, word_amount))
            if len(word_amount)<2:
                print("Please enter a valid name and surname (It must minimum 2 words)")
                return "Please enter a valid name and surname (It must minimum 2 words)"
            elif all_alphabet!=True:
                print("Name and surname should only consist of letters.")
                return "Name and surname should only consist of letters."
        else:
            print("Please enter a name")
            return "Please enter a name"


        self.idnumber = idnumber
        if self.idnumber != "":
            all_digit = all(map(str.isdigit,self.idnumber))
            if all_digit!=True:
                print("ID Number should only consist of numbers.")
                return "ID Number should only consist of numbers."
        else:
            print("Please enter an id number")
            return "Please enter an id number"


        self.password = password
        if self.password != "":
            patern = r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=.,:;]).*$"
            pasword_test = re.findall(patern, self.password)
            if pasword_test:
                pass
            else:
                warn="""
                        Please enter a valid password\n
                        
                      * Must be at least 8 characters
                      * Must contain at least one uppercase letters: A-Z
                      * Must contain at least one lowercase letters: a-z
                      * Must contain at least one numbers: 0-9
                      * Must contain at least one special characters: @#$%^&+=.,:;
                      """
                print(warn)
                return warn
        else:
            print("Please enter a password")
            return "Please enter a password"

        self.email = email

        if self.email != "":

            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            text_found = re.search(regex, self.email)
            if text_found:
                pass
            else:
                print("Please enter a valid email")
                return "Please enter a valid email"
        else:

            print("Please enter an email")
            return "Please enter an email"

        if self.name and self.idnumber and self.password and self.email:

            with open("users.csv") as file:
                csvreader = csv.reader(file)
                users = list(csvreader)

            for user in users:

                if user[0] == self.email:
                    signupp = 1
                    print("This user already exists. Please use another e-mail address.")
                    return "This user already exists. Please use another e-mail address."


        if signupp!=1:
            now = datetime.now()
            timestamp = datetime.timestamp(now)
            dt_object = datetime.fromtimestamp(timestamp)

            with open("users.csv", "a", newline="") as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow([self.email, self.password, self.name, self.idnumber, self.balance])
            print(f"{self.name} is succesfully signup.")

            with open("user_operations.csv", "a", newline="") as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow([self.email, self.name,"Succesfully Signed Up", dt_object, "-"])

            return f"{self.name} is succesfully signed up."

    def login(self,email,password):

        self.email=email
        self.password=password

        if email != "" and password != "" and User.isloggedIn==False:
            with open("users.csv") as file:
                csvreader = csv.DictReader(file)

                for user in csvreader:
                    if email == user['email'] and password == user['password']:
                        User.currentUser = [user['email'], user['password'], user['name'], user['idnumber'],
                                            user['balance']]
                        User.isloggedIn = True
                        print(f"{User.currentUser[2]} is succesfully login")

                        if User.isloggedIn:
                            now = datetime.now()
                            timestamp = datetime.timestamp(now)
                            dt_object = datetime.fromtimestamp(timestamp)

                            with open("user_operations.csv", "a", newline="") as file:
                                csvwriter = csv.writer(file)
                                csvwriter.writerow(
                                    [User.currentUser[0], User.currentUser[2], "Succesfully Logged in", dt_object, "-"])

                        return f"{User.currentUser[2]} is succesfully login"

                if User.isloggedIn == False:
                    print("At least one of the email or password is incorrect. Please try again.")
                    return "At least one of the email or password is incorrect. Please try again."
        elif (email == "" or password == "") and User.isloggedIn==False:
            print("Please enter an email and password")
            return "Please enter an email and password"

    def login_officer(self,email,password):

        self.email=email
        self.password=password

        if email != "" and password != "" and User.isloggedIn==False:

            with open("users.csv") as file:
                csvreader = csv.reader(file)
                users = list(csvreader)

                if users[1][0] == self.email and users[1][1] == self.password:
                    User.isloggedIn = True
                    User.currentUser = [users[1][0], users[1][1], users[1][2], users[1][3],
                                        users[1][4]]
                    print(f"{User.currentUser[2]} is succesfully login")

                    if User.isloggedIn:
                        now = datetime.now()
                        timestamp = datetime.timestamp(now)
                        dt_object = datetime.fromtimestamp(timestamp)

                        with open("user_operations.csv", "a", newline="") as file:
                            csvwriter = csv.writer(file)
                            csvwriter.writerow([User.currentUser[0], User.currentUser[2], "Succesfully Logged in", dt_object, "-"])

                    return f"{User.currentUser[2]} is succesfully login"

                else:
                    print("At least one of the email or password is incorrect. Please try again.")
                    return "At least one of the email or password is incorrect. Please try again."
        elif (email == "" or password == "") and User.isloggedIn==False:
            print("Please enter an email and password")
            return "Please enter an email and password"

    def logout(self):

        if User.isloggedIn == True:

            now = datetime.now()
            timestamp = datetime.timestamp(now)
            dt_object = datetime.fromtimestamp(timestamp)

            with open("user_operations.csv", "a", newline="") as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow([User.currentUser[0], User.currentUser[2], "Succesfully Logged out", dt_object, "-"])
            print(f"{User.currentUser[2]} is succesfully logged out")
            User.isloggedIn = False
            temp=User.currentUser[2]
            User.currentUser = []
            return f"{temp} is succesfully logged out"

    def usr_info(self):

        print(f"Email: {User.currentUser[0]}, Name: {User.currentUser[2]}\n"
              f"ID Number: {User.currentUser[3]}, Current Balance: {User.currentUser[-1]}")

        now = datetime.now()
        timestamp = datetime.timestamp(now)
        dt_object = datetime.fromtimestamp(timestamp)

        with open("user_operations.csv", "a", newline="") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow([User.currentUser[0], User.currentUser[2],
                                "User information is displayed", dt_object, "-"])

        return f"Email: {User.currentUser[0]}, Name: {User.currentUser[2]}\n" \
               f"ID Number: {User.currentUser[3]}, Current Balance: {User.currentUser[-1]}"

    def edit_usr_acnt(self,name,password,id):
        name_change = 0
        password_change = 0
        id_change = 0

        if name != "" or password != "" or id != "":

            if name != User.currentUser[2]:
                tmp=name
                User.currentUser[2]=tmp
                print("Name is succesfully changed")

                now = datetime.now()
                timestamp = datetime.timestamp(now)
                dt_object = datetime.fromtimestamp(timestamp)

                with open("user_operations.csv", "a", newline="") as file:
                    csvwriter = csv.writer(file)
                    csvwriter.writerow(
                        [User.currentUser[0], User.currentUser[2], "Name is succesfully changed", dt_object, "-"])

                with open("users.csv") as file:
                    csvreader = csv.reader(file)
                    users = list(csvreader)

                with open("users.csv", 'w', newline="") as file:
                    csvwriter = csv.writer(file)

                    for user in users:

                        if user[0] == User.currentUser[0]:
                            csvwriter.writerow(User.currentUser)
                        else:
                            csvwriter.writerow(user)
                name_change=1

            if password != User.currentUser[1]:
                tmp=password
                User.currentUser[1] = tmp
                print("Password is succesfully changed")

                now = datetime.now()
                timestamp = datetime.timestamp(now)
                dt_object = datetime.fromtimestamp(timestamp)

                with open("user_operations.csv", "a", newline="") as file:
                    csvwriter = csv.writer(file)
                    csvwriter.writerow([User.currentUser[0], User.currentUser[2], "Password is succesfully changed", dt_object, "-"])

                with open("users.csv") as file:
                    csvreader = csv.reader(file)
                    users = list(csvreader)

                with open("users.csv", 'w', newline="") as file:
                    csvwriter = csv.writer(file)

                    for user in users:

                        if user[0] == User.currentUser[0]:
                            csvwriter.writerow(User.currentUser)
                        else:
                            csvwriter.writerow(user)

                password_change = 1
            if id != User.currentUser[3]:
                tmp=id
                User.currentUser[3] = tmp
                print("Id Number is succesfully changed")

                now = datetime.now()
                timestamp = datetime.timestamp(now)
                dt_object = datetime.fromtimestamp(timestamp)

                with open("user_operations.csv", "a", newline="") as file:
                    csvwriter = csv.writer(file)
                    csvwriter.writerow([User.currentUser[0], User.currentUser[2], "ID Number is succesfully changed", dt_object, "-"])

                with open("users.csv") as file:
                    csvreader = csv.reader(file)
                    users = list(csvreader)

                with open("users.csv", 'w', newline="") as file:
                    csvwriter = csv.writer(file)

                    for user in users:

                        if user[0] == User.currentUser[0]:
                            csvwriter.writerow(User.currentUser)
                        else:
                            csvwriter.writerow(user)

                id_change=1

        else:
            print("Please make a valid selection!!!")
            return "Please make a valid selection!!!"

        if name_change==1:
            return "Name is succesfully changed"
        elif password_change ==1:
            return "Password is succesfully changed"
        elif id_change == 1:
            return "Id Number is succesfully changed"

    def del_usr_acnt(self):

        with open("users.csv") as file:
            csvreader = csv.reader(file)
            users = list(csvreader)

        with open("users.csv", 'w', newline="") as file:
            csvwriter = csv.writer(file)

            for user in users:

                if user[0] == User.currentUser[0]:
                    print(f"{User.currentUser[2]} is succesfully Deleted")
                else:
                    csvwriter.writerow(user)

        now = datetime.now()
        timestamp = datetime.timestamp(now)
        dt_object = datetime.fromtimestamp(timestamp)

        with open("user_operations.csv", "a", newline="") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow([User.currentUser[0], User.currentUser[2],
                                "User account is succesfully deleted", dt_object, "-"])

        return f"{User.currentUser[2]} is succesfully Deleted"

    def usr_extractOfAccount(self):

        with open("user_operations.csv") as file:
            csvreader = csv.reader(file)
            users = list(csvreader)
            all=""
            for user in users:
                if user[0] == User.currentUser[0]:
                   all+=str(user)[1:-1]+"\n"
            print(all)
        return f"{all}"

    def bank_extractOfAccount(self):

        with open("user_operations.csv") as file:
            csvreader = csv.reader(file)
            users = list(csvreader)
            all=""
            for user in users:
                if user[-1] != "-" and user[-1] != "balance":
                    all += str(user)[1:-1] + "\n"

            print(all)
        return f"{all}"

class Bank:
    destinationUser=[]

    def __init__(self):
        pass

    def user_check_balance(self):

        with open("users.csv") as file:
            csvreader = csv.DictReader(file)

            for user in csvreader:
                if User.currentUser[0] == user['email']:
                    print(f"The balance of {user['name']} is {user['balance']}€")

                    now = datetime.now()
                    timestamp = datetime.timestamp(now)
                    dt_object = datetime.fromtimestamp(timestamp)

                    with open("user_operations.csv", "a", newline="") as file:
                        csvwriter = csv.writer(file)
                        csvwriter.writerow([User.currentUser[0], User.currentUser[2], "Checked the Balance",
                                            dt_object, f"Current Balance:{User.currentUser[-1]} Euro"])

                    return f"The balance of {user['name']} is {user['balance']}€"

    def insert_money(self,insert_mny_raw):

        if insert_mny_raw != "":
            try:
                insert_mny=int(insert_mny_raw)
            except:

                print("Insert money should only consist of numbers! Please make a valid selection!")
                return "Insert money should only consist of numbers! Please make a valid selection!"
        else:
            print("Please enter amount of money")
            return "Please enter amount of money"


        User.currentUser[-1]=int(User.currentUser[-1])+insert_mny
        with open("users.csv") as file:
            csvreader = csv.reader(file)
            users = list(csvreader)

        with open("users.csv", 'w', newline="") as file:
            csvwriter = csv.writer(file)
            for user in users:
                if user[0] == User.currentUser[0]:
                    csvwriter.writerow(User.currentUser)
                elif user[0]=="admin@gmail.com":
                    user[4]=int(user[4])+insert_mny
                    csvwriter.writerow(user)
                else:
                    csvwriter.writerow(user)

        now = datetime.now()
        timestamp = datetime.timestamp(now)
        dt_object = datetime.fromtimestamp(timestamp)

        with open("user_operations.csv", "a", newline="") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(
                [User.currentUser[0], User.currentUser[2],
                 f"Inserted {insert_mny} Euro (Ex Balance: {int(User.currentUser[-1])-insert_mny})",
                 dt_object, f"New Balance: {User.currentUser[-1]} Euro"])

        print(f"The current balance of {User.currentUser[2]} is {User.currentUser[-1]}€")
        return f"The current balance of {User.currentUser[2]} is {User.currentUser[-1]}€"

    def withdraw_money(self,withdraw_mny_raw):

        if withdraw_mny_raw != "":
            try:
                withdraw_mny=int(withdraw_mny_raw)
            except:

                print("Withdraw money should only consist of numbers! Please make a valid selection!")
                return "Withdraw money should only consist of numbers! Please make a valid selection!"
        else:
            print("Please enter amount of money")
            return "Please enter amount of money"


        temp=int(User.currentUser[-1])-withdraw_mny
        if temp < 0:
            print("You do not have enough money in your account. "
                  "\nPlease try to withdraw a lower amount. ")

            return "You do not have enough money in your account."\
                   "\nPlease try to withdraw a lower amount. "
        else:
            User.currentUser[-1]=temp


        with open("users.csv") as file:
            csvreader = csv.reader(file)
            users = list(csvreader)

        with open("users.csv", 'w', newline="") as file:
            csvwriter = csv.writer(file)
            for user in users:
                if user[0] == User.currentUser[0]:
                    csvwriter.writerow(User.currentUser)

                elif user[0]=="admin@gmail.com":
                    user[4]=int(user[4])-withdraw_mny
                    csvwriter.writerow(user)
                else:
                    csvwriter.writerow(user)

        if temp > 0:

            now = datetime.now()
            timestamp = datetime.timestamp(now)
            dt_object = datetime.fromtimestamp(timestamp)

            with open("user_operations.csv", "a", newline="") as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow(
                    [User.currentUser[0], User.currentUser[2],
                     f"Withdrawed {withdraw_mny} Euro (Ex Balance: {int(User.currentUser[-1]) + withdraw_mny} Euro)",
                     dt_object, f"New Balance: {User.currentUser[-1]} Euro"])

        print(f"The current balance of {User.currentUser[2]} is {User.currentUser[-1]}€")
        return f"The current balance of {User.currentUser[2]} is {User.currentUser[-1]}€"

    def transfer_money_internal(self,dest_user,transfer_mny_int_raw):
        find_user = ""
        Bank.destinationUser=[]

        with open("users.csv") as file:
            csvreader = csv.DictReader(file)

            for user in csvreader:
                if dest_user == user['email']:
                    Bank.destinationUser = [user['email'], user['password'], user['name'], user['idnumber'],
                                        user['balance']]
                    find_user="user found"

        if find_user == "user found":

            try:
                transfer_mny_int = int(transfer_mny_int_raw)
            except:
                print("Transfer money should only consist of numbers! Please make a valid selection!")
                return "Transfer money should only consist of numbers! Please make a valid selection!"

        else:
            print("We couldn't find a user in database")
            return "We couldn't find a user in database"

        temp = int(User.currentUser[-1]) - transfer_mny_int
        if temp < 0:
            print("You do not have enough money in your account. "
                  "\nPlease try to withdraw a lower amount. ")

            return "You do not have enough money in your account. "\
                  "\nPlease try to withdraw a lower amount. "
        else:
            User.currentUser[-1] = temp

            Bank.destinationUser[-1] = int(Bank.destinationUser[-1]) + transfer_mny_int


        with open("users.csv") as file:
            csvreader = csv.reader(file)
            users = list(csvreader)

        with open("users.csv", 'w', newline="") as file:
            csvwriter = csv.writer(file)
            for user in users:
                if user[0] == User.currentUser[0]:
                    csvwriter.writerow(User.currentUser)
                elif user[0] == Bank.destinationUser[0]:
                    csvwriter.writerow(Bank.destinationUser)
                else:
                    csvwriter.writerow(user)

        if temp > 0:

            now = datetime.now()
            timestamp = datetime.timestamp(now)
            dt_object = datetime.fromtimestamp(timestamp)

            with open("user_operations.csv", "a", newline="") as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow(
                    [User.currentUser[0], User.currentUser[2],
                     f"Internal Transfered {transfer_mny_int} Euro (Ex Balance: {int(User.currentUser[-1]) + transfer_mny_int} Euro)",
                     dt_object, f"New Balance: {User.currentUser[-1]} Euro"])
        print("The transfer is successful.")
        print(f"The current balance of {User.currentUser[2]} is {User.currentUser[-1]}€")
        print(f"The current balance of {Bank.destinationUser[2]} is {Bank.destinationUser[-1]}€")

        return f"The transfer is successful.\n" \
               f"The current balance of {User.currentUser[2]} is {User.currentUser[-1]}€\n" \
               f"The current balance of {Bank.destinationUser[2]} is {Bank.destinationUser[-1]}€"

    def transfer_money_external(self,dest_user_raw,transfer_mny_ext_raw):

        if dest_user_raw != "" and transfer_mny_ext_raw != "":

            dest_user = dest_user_raw
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            email_check = re.search(regex, dest_user)
            if email_check:
                pass
            else:
                print("Please enter a valid email")
                return "Please enter a valid email"

            try:
                    transfer_mny_ext=int(transfer_mny_ext_raw)

            except:
                print("Transfer money should only consist of numbers! Please make a valid selection!")
                return "Transfer money should only consist of numbers! Please make a valid selection!"

        else:
            print("Please enter a valid email and amount")
            return "Please enter a valid email and amount"

        temp=int(User.currentUser[-1])-transfer_mny_ext

        if temp < 0:
            print("You do not have enough money in your account. "
                  "\nPlease try to transfer a lower amount. ")
            return "You do not have enough money in your account. "\
                  "\nPlease try to transfer a lower amount. "
        else:
            User.currentUser[-1]=temp


        with open("users.csv") as file:
            csvreader = csv.reader(file)
            users = list(csvreader)

        with open("users.csv", 'w', newline="") as file:
            csvwriter = csv.writer(file)
            for user in users:
                if user[0] == User.currentUser[0]:
                    csvwriter.writerow(User.currentUser)

                elif user[0]=="admin@gmail.com":
                    user[4]=int(user[4])-transfer_mny_ext
                    csvwriter.writerow(user)
                else:
                    csvwriter.writerow(user)

        if temp > 0:

            now = datetime.now()
            timestamp = datetime.timestamp(now)
            dt_object = datetime.fromtimestamp(timestamp)

            with open("user_operations.csv", "a", newline="") as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow(
                    [User.currentUser[0], User.currentUser[2],
                     f"External Transfered {transfer_mny_ext} Euro (Ex Balance: {int(User.currentUser[-1]) + transfer_mny_ext} Euro)",
                     dt_object, f"New Balance: {User.currentUser[-1]} Euro"])

        print("The transfer is successful.")
        print(f"The current balance of {User.currentUser[2]} is {User.currentUser[-1]}€")
        return f"The transfer is successful."\
               f"The current balance of {User.currentUser[2]} is {User.currentUser[-1]}€"

    def bank_daily_tot_insert(self):
        total_insert=0
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        dt_object = datetime.fromtimestamp(timestamp)

        with open("user_operations.csv") as file:
            csvreader = csv.reader(file)
            users = list(csvreader)

            for user in users:
                if str(dt_object.date())==(user[3])[0:10] and (user[2])[0:8]=="Inserted":
                    lst=(user[2]).split(" ")
                    total_insert+=int(lst[1])



        print(f"Daily totaly inserted money is {total_insert} Euro")
        return f"Daily totaly inserted money is {total_insert} Euro"

    def bank_daily_tot_withdraw(self):
        total_withdraw=0
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        dt_object = datetime.fromtimestamp(timestamp)

        with open("user_operations.csv") as file:
            csvreader = csv.reader(file)
            users = list(csvreader)

            for user in users:
                if str(dt_object.date())==(user[3])[0:10] and (user[2])[0:10]=="Withdrawed":
                    lst=(user[2]).split(" ")
                    total_withdraw+=int(lst[1])

        print(f"Daily totaly withdrawed money is {total_withdraw} Euro")
        return f"Daily totaly withdrawed money is {total_withdraw} Euro"

    def bank_daily_tot_transfer_int(self):
        total_transfer_int=0
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        dt_object = datetime.fromtimestamp(timestamp)

        with open("user_operations.csv") as file:
            csvreader = csv.reader(file)
            users = list(csvreader)

            for user in users:
                if str(dt_object.date())==(user[3])[0:10] and (user[2])[0:8]=="Internal":
                    lst=(user[2]).split(" ")
                    total_transfer_int+=int(lst[2])

        print(f"Daily totaly internal transfered money is {total_transfer_int} Euro")
        return f"Daily totaly internal transfered money is {total_transfer_int} Euro"

    def bank_daily_tot_transfer_ext(self):
        total_transfer_ext=0
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        dt_object = datetime.fromtimestamp(timestamp)

        with open("user_operations.csv") as file:
            csvreader = csv.reader(file)
            users = list(csvreader)

            for user in users:
                if str(dt_object.date())==(user[3])[0:10] and (user[2])[0:8]=="External":
                    lst=(user[2]).split(" ")
                    total_transfer_ext+=int(lst[2])

        print(f"Daily totaly externel transfered money is {total_transfer_ext} Euro")
        return f"Daily totaly external transfered money is {total_transfer_ext} Euro"

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = ScreenMain()
widget.addWidget(mainwindow)
widget.setWindowTitle("PAY BANK")
widget.setFixedHeight(450)
widget.setFixedWidth(550)
widget.show()
sys.exit(app.exec_())

