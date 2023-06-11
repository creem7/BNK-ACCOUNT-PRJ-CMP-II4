from tkinter import *
import os
from PIL import ImageTk, Image
from tkinter import messagebox

# Account classes
class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: +{amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -{amount}")
        else:
            print("Insufficient funds")
            self.transaction_history.append(f"Withdrawal attempted: -{amount} (Insufficient funds)")

#GUI for account interface
def deposit_amount():
    amount = float(deposit_entry.get())
    if amount > 0:
        current_account.deposit(amount)
        update_balance()
        update_transaction_history()
    else:
        print("Invalid amount")

current_account = Account(account_number="CUR001", balance=500)

def withdraw_amount():
    amount = float(withdraw_entry.get())
    if amount > 0:
        current_account.withdraw(amount)
        update_balance()
        update_transaction_history()
    else:
        print("Invalid amount")

def update_balance():
    balance_label["text"] = f"Balance: {current_account.balance}"

def update_transaction_history():
    history_text.delete("1.0", END)
    for transaction in current_account.transaction_history:
        history_text.insert(END, transaction + "\n")

def navigate_home():
    home_frame.pack()
    account_frame.pack_forget()

def navigate_account():
    home_frame.pack_forget()
    account_frame.pack()

# GUI interface for the first window(first screen)
window = Tk()
window.title("GMC ELECTRONIC BANKING SYSTEM")
window.geometry("410x430")
window.configure(bg="cyan")


home_frame = Frame(window)
frame = Frame(window, bg="#2432f2", width=410, height=430)
frame.place(x=0, y=0)
img = Image.open('logo.png')
img = img.resize({400,300})
img = ImageTk.PhotoImage(img)

Label(window, image=img, border=0).place(x=3, y=50)
welcome_label = Label(window, text="Welcome to GMC Banking App!", bg="#2432f2", fg="white",  font=("Arial", 16, "bold"))
welcome_label.place(x=45, y=15)
# Account GUI interface
def navigate_account():
   home_frame = Toplevel(window)
   home_frame.title("Account page")
   home_frame.geometry("410x430")
   home_frame.configure(bg="#2432f2")

   Label(home_frame, text="Which is your preference?", bg="#2432f2", font=('Arial', 15, 'bold')).place(x=75, y=40)
   savings_button = Button(home_frame, text="Savings", bg="cyan",border=4, pady=7, font=('Arial',12), command=navigate_savings).place(x=75, y=150)
   current_button = Button(home_frame, text="Current", bg='cyan', border=4, pady=7, font=('Arial',12), command=navigate_current).place(x=240, y=150)
   home_frame.mainloop()


account_button = Button(window, text="Account", bg="cyan", fg="white", border=2, font=("Arial", 14), command=navigate_account)
account_button.place(x=220, y=360)

# Savings account interface

account_frame = Frame(window)
def navigate_savings():
    account_frame = Toplevel(home_frame)
    account_frame.title("Savings Account")
    account_frame.geometry("410x430")
    account_frame.configure(bg="cyan")

    class Account:
        def __init__(self, account_number, balance=0):
            self.account_number = account_number
            self.balance = balance
            self.transaction_history = []

        def deposit(self, amount):
            self.balance += amount
            self.transaction_history.append(f"Deposit: +{amount}")

        def withdraw(self, amount):
            if self.balance >= amount:
                self.balance -= amount
                self.transaction_history.append(f"Withdrawal: -{amount}")
            else:
                print("Insufficient funds")
                self.transaction_history.append(f"Withdrawal attempted: -{amount} (Insufficient funds)")

    # GUI  savings account functions
    def deposit_amount():
        amount = float(deposit_entry.get())
        if amount > 0:
            current_account.deposit(amount)
            update_balance()
            update_transaction_history()
        else:
            print("invalid amount")

    current_account = Account(account_number="CUR001", balance=0)

    def withdraw_amount():
        amount = float(withdraw_entry.get())
        if amount <= 5000:
            current_account.withdraw(amount)
            update_balance()
            update_transaction_history()
            messagebox.showinfo({current_account.balance}, "has been deducted")
        elif amount > 5000:
            messagebox.showerror("Invalid", "Invalid Amount")

    def update_balance():
        balance_label["text"] = f"Balance: {current_account.balance}"

    def update_transaction_history():
        history_text.delete("1.0", END)
        for transaction in current_account.transaction_history:
            history_text.insert(END, transaction + "\n")

    def navigate_home():
        home_frame.pack()
        account_frame.pack_forget()

    def navigate_account():
        home_frame.pack_forget()
        account_frame.pack()

    account_label = Label(account_frame, text="Account", font=("Arial", 16, "bold"))
    account_label.pack()

    deposit_label = Label(account_frame, text="Deposit Amount:", font=("Arial", 12))
    deposit_label.pack()
    deposit_entry = Entry(account_frame, font=("Arial", 12))
    deposit_entry.pack()
    deposit_button = Button(account_frame, text="Deposit", font=("Arial", 12), command=deposit_amount)
    deposit_button.pack()

    withdraw_label = Label(account_frame, text="Withdraw Amount:", font=("Arial", 12))
    withdraw_label.pack()
    withdraw_entry = Entry(account_frame, font=("Arial", 12))
    withdraw_entry.pack()
    withdraw_button = Button(account_frame, text="Withdraw", font=("Arial", 12), command=withdraw_amount)
    withdraw_button.pack()

    balance_label = Label(account_frame, text="Balance:", font=("Arial", 12))
    balance_label.pack()
    update_balance()

    history_label = Label(account_frame, text="Transaction History:", font=("Arial", 12))
    history_label.pack()
    history_text = Text(account_frame, width=30, height=10, font=("Arial", 12))
    history_text.pack()
    update_transaction_history()

# current account GUI interface

account_frame1 = Frame(window)
def navigate_current():
    account_frame1 = Toplevel(home_frame)
    account_frame1.title("Current account")
    account_frame1.geometry("410x430")
    account_frame1.configure(bg="cyan")

    class Account:
        def __init__(self, account_number, balance=0):
            self.account_number = account_number
            self.balance = balance
            self.transaction_history = []

        def deposit(self, amount):
            self.balance += amount
            self.transaction_history.append(f"Deposit: +{amount}")

        def withdraw(self, amount):
            if self.balance >= amount:
                self.balance -= amount
                self.transaction_history.append(f"Withdrawal: -{amount}")
            else:
                print("Insufficient funds")
                self.transaction_history.append(f"Withdrawal attempted: -{amount} (Insufficient funds)")

    # current account GUI functions
    def deposit_amount():
        amount = float(deposit_entry.get())
        if amount > 0:
            current_account.deposit(amount)
            update_balance()
            update_transaction_history()
        else:
            print("Invalid amount")

    current_account = Account(account_number="CUR001", balance=0)

    def withdraw_amount():
        amount = float(withdraw_entry.get())
        if amount > 0:
            current_account.withdraw(amount)
            update_balance()
            update_transaction_history()
            messagebox.showinfo({current_account.balance}, "has been deducted")
        elif amount < 0:
            messagebox.showerror("Invalid", "Invalid amount")

    def update_balance():
        balance_label["text"] = f"Balance: {current_account.balance}"

    def update_transaction_history():
        history_text.delete("1.0", END)
        for transaction in current_account.transaction_history:
            history_text.insert(END, transaction + "\n")

    def navigate_home():
        home_frame.pack()
        account_frame.pack_forget()

    def navigate_account():
        home_frame.pack_forget()
        account_frame.pack()

    account_label = Label(account_frame1, text="Account", font=("Arial", 16, "bold"))
    account_label.pack()

    deposit_label = Label(account_frame1, text="Deposit Amount:", font=("Arial", 12))
    deposit_label.pack()
    deposit_entry = Entry(account_frame1, font=("Arial", 12))
    deposit_entry.pack()
    deposit_button = Button(account_frame1, text="Deposit", font=("Arial", 12), command=deposit_amount)
    deposit_button.pack()

    withdraw_label = Label(account_frame1, text="Withdraw Amount:", font=("Arial", 12))
    withdraw_label.pack()
    withdraw_entry = Entry(account_frame1, font=("Arial", 12))
    withdraw_entry.pack()
    withdraw_button = Button(account_frame1, text="Withdraw", font=("Arial", 12), command=withdraw_amount)
    withdraw_button.pack()

    balance_label = Label(account_frame1, text="Balance:", font=("Arial", 12))
    balance_label.pack()
    update_balance()

    history_label = Label(account_frame1, text="Transaction History:", font=("Arial", 12))
    history_label.pack()
    history_text = Text(account_frame1, width=30, height=10, font=("Arial", 12))
    history_text.pack()
    update_transaction_history()

# Home window GUI interface

home_frame1 = Frame(window)
def navigate_home():
    home_frame1 = Toplevel(window)
    home_frame1.title("Login page")
    home_frame1.geometry("410x430")
    home_frame1.resizable(False, False)
    home_frame1.configure(bg="blue")

    img = PhotoImage(file="background.png")
    Label(home_frame1, image=img, bg="blue").place(x=0, y=0)



    Frame(home_frame1, width=340, height=380, bg="cyan").place(x=40, y=35)

    heading = Label(home_frame1, text="LOGIN", fg="#010203", bg="cyan", font=('Arial', 18, 'bold'))
    heading.place(x=160, y=15)
    heading_2 = Label(home_frame1, text="WELCOME!", fg="#010203", bg="cyan", font=('Arial', 16, 'italic'))
    heading_2.place(x=140, y=60)

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == '':
            user.insert(0, 'Username')

    user = Entry(home_frame1, width=200, fg="black", border=2, bg="white", font=('Microsoft YaHei UI Light', 11))
    user.place(x=5, y=102)
    user.insert(0, 'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)
    Frame(home_frame1, width=295, height=2, bg="black").place(x=5, y=102)

    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        name = code.get()
        if name == '':
            code.insert(0, 'Password')

    code = Entry(home_frame1, width=200, fg="black", border=2, bg="white", font=('Microsoft YaHei UI Light', 11))
    code.place(x=5, y=210)
    code.insert(0, 'Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)
    Frame(home_frame1, width=295, height=2, bg='black').place(x=5, y=210)

    Button(home_frame1, width=39, pady=7, text='LOGIN', bg="#2432f2", fg='white', border=3, command=LOGIN).place(x=65, y=290)
    label = Label(home_frame1, text="Don't have an account?", fg="black", bg="white", border=1, font=('Arial', 9))
    label.place(x=90, y=340)

    sign_up = Button(home_frame1, text="Sign up", fg="white", bg="#2432f2", border=2, cursor='hand2', command=signup)
    sign_up.place(x=230, y=340)

# login page GUI interface

def LOGIN():
    username = user.get()
    password = code.get()

    if username == "user209" or username == "user402" or username == "user407" or username == "user806" and password == "Gmc40" or password == "Gmc25" or password == "Gmc75" or password == "Gmc60":
        messagebox.showinfo("successful", "Login successful")
    elif username != "user209" and username != "user407" and username != "user402" and username != "user806" and password != "Gmc40" and password != "Gmc25" and password != "Gmc60" and password != "Gmc75":
        messagebox.showerror("Invalid", "invalid username and password")
    elif username != "user209" and username != "user407" and username != "user402" and username != "user806":
        messagebox.showerror("Invalid", "invalid username")
    elif password != "Gmc40" and password != "Gmc25" and password != "Gmc60" and password != "Gmc75":
        messagebox.showerror("Invalid", "invalid password")




def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

user = Entry(home_frame1, width=200, fg="black", border=2, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=5, y=102)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(home_frame1, width=295, height=2, bg="black").place(x=5, y=102)

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')

code = Entry(home_frame1, width=200, fg="black", border=2, bg="white", font=('Microsoft YaHei UI Light', 11))
code.place(x=5, y=210)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame(home_frame1, width=295, height=2, bg='black').place(x=5, y=210)

# linkage between login and signup page

home_frame2 = Frame(window)
def signup():
    home_frame2 = Toplevel(home_frame1)
    home_frame2.title("SIGNUP PAGE")
    home_frame2.geometry("410x430")
    home_frame2.resizable(False, False)
    home_frame2.configure(bg="#18d9d2")

    img = PhotoImage(file="background.png")
    Label(home_frame2, image=img, bg="#18d9d2").place(x=0, y=0)

    heading = Label(home_frame2, text="SIGN UP", fg="#010203", bg="cyan", font=('Arial', 18, 'bold'))
    heading.place(x=150, y=10)
    heading_2 = Label(home_frame2, text="NEW HERE? REGISTER WITH US!", fg="#010203", bg="cyan", font=('Arial', 16, 'italic'))
    heading_2.place(x=40, y=60)

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == '':
            user.insert(0, 'Enter your name')

    user = Entry(home_frame2, width=200, fg="black", border=2, bg="white", font=('Microsoft YaHei UI Light', 11))
    user.place(x=5, y=142)
    user.insert(0, 'Enter your name')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    def on_enter(e):
        age.delete(0, 'end')

    def on_leave(e):
        name = age.get()
        if name == '':
            age.insert(0, 'Enter your age')

    age = Entry(home_frame2, width=200, fg="black", border=2, bg="white", font=('Microsoft YaHei UI Light', 11))
    age.place(x=5, y=184)
    age.insert(0, 'Enter your age')
    age.bind('<FocusIn>', on_enter)
    age.bind('FocusOut', on_leave)

    def on_enter(e):
        gender.delete(0, 'end')

    def on_leave(e):
        name = gender.get()
        if name == '':
            gender.insert(0, 'Enter your gender')

    gender = Entry(home_frame2, width=200, fg="black", border=2, bg="white", font=('Microsoft YaHei UI Light', 11))
    gender.place(x=5, y=226)
    gender.insert(0, 'Enter your gender')
    gender.bind('<FocusIn>', on_enter)
    gender.bind('<FocusOut>', on_leave)

    def on_enter(e):
        occupation.delete(0, 'end')

    def on_leave(e):
        name = occupation.get()
        if name == '':
            occupation.insert(0, 'Enter your occupation')

    occupation = Entry(home_frame2, width=200, fg="black", border=2, bg="white", font=('Microsoft YaHei UI Light', 11))
    occupation.place(x=5, y=268)
    occupation.insert(0, 'Enter your occupation')
    occupation.bind('<FocusIn>', on_enter)
    occupation.bind('<FocusOut>', on_leave)

    Button(home_frame2, width=39, pady=7, text='SIGN UP', bg="#2432f2", fg='white', border=0).place(x=50, y=320)
    Label(home_frame2, text="I have an account?", fg="black", bg="white", font=("Arial", 9)).place(x=100, y=360)

    click = Button(home_frame2, text="LOGIN", fg="white", bg="#2432f2", border=0, cursor="hand2", command=LOGIN)
    click.place(x=220, y=360)


home_button = Button(window, text="Home", bg="cyan", fg="white", border=2, font=("Arial", 14), command=navigate_home)
home_button.place(x=110, y=360)

# Set initial account
current_account = Account(account_number="CUR001", balance=500)

home_frame2.mainloop()

home_frame1.mainloop()

# Display home screen initially
navigate_home()


window.mainloop()
