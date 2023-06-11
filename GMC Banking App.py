import tkinter as tk

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

# GUI functions
def deposit_amount():
    amount = float(deposit_entry.get())
    if amount > 0:
        current_account.deposit(amount)
        update_balance()
        update_transaction_history()
    else:
        print("Invalid amount")

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
    history_text.delete("1.0", tk.END)
    for transaction in current_account.transaction_history:
        history_text.insert(tk.END, transaction + "\n")

def navigate_home():
    home_frame.pack()
    account_frame.pack_forget()

def navigate_account():
    home_frame.pack_forget()
    account_frame.pack()

# Create the main window
window = tk.Tk()
window.title("Banking App")

# Set initial account
current_account = Account(account_number="CUR001", balance=500)


# Set window icon (replace 'icon.png' with your own icon image file)
window.iconbitmap('logo.png')

# Home screen
home_frame = tk.Frame(window)

welcome_label = tk.Label(home_frame, text="Welcome to the Banking App!", font=("Arial", 16, "bold"))
welcome_label.pack()

account_button = tk.Button(home_frame, text="Account", font=("Arial", 14), command=navigate_account)
account_button.pack()

# Account screen
account_frame = tk.Frame(window)

account_label = tk.Label(account_frame, text="Account", font=("Arial", 16, "bold"))
account_label.pack()

deposit_label = tk.Label(account_frame, text="Deposit Amount:", font=("Arial", 12))
deposit_label.pack()
deposit_entry = tk.Entry(account_frame, font=("Arial", 12))
deposit_entry.pack()
deposit_button = tk.Button(account_frame, text="Deposit", font=("Arial", 12), command=deposit_amount)
deposit_button.pack()

withdraw_label = tk.Label(account_frame, text="Withdraw Amount:", font=("Arial", 12))
withdraw_label.pack()
withdraw_entry = tk.Entry(account_frame, font=("Arial", 12))
withdraw_entry.pack()
withdraw_button = tk.Button(account_frame, text="Withdraw", font=("Arial", 12), command=withdraw_amount)
withdraw_button.pack()

balance_label = tk.Label(account_frame, text="Balance:", font=("Arial", 12))
balance_label.pack()
update_balance()

history_label = tk.Label(account_frame, text="Transaction History:", font=("Arial", 12))
history_label.pack()
history_text = tk.Text(account_frame, width=30, height=10, font=("Arial", 12))
history_text.pack()
update_transaction_history()

home_button = tk.Button(account_frame, text="Home", font=("Arial", 12), command=navigate_home)
home_button.pack()

# Set initial account
current_account = Account(account_number="CUR001", balance=500)

# Display home screen initially
navigate_home()

window.mainloop()
