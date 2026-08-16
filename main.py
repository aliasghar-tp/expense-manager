import json
from datetime import datetime


with open("user.json", "r") as file:
    user_list = json.load(file)
    user = user_list[0]
    Username = user["username"]
    Password = user["password"]


def save_expenses(expenses):
    with open("expense.json", "w") as file:
        json.dump(expenses, file, indent=4)


try:
    with open("expense.json", "r") as file:
        list_expense = json.load(file)
except(FileNotFoundError, json.JSONDecodeError):
    list_expense = []


def edit_expense(list_expense):
    if not list_expense:
        print("Expense list is empty!")

    for index, item in enumerate(list_expense):
        print(f"{index + 1}. {item['title']}-->{item['amount']}")
    
    try:
        exp_num_str = input("Enter the expense number: ")
        
        if exp_num_str.lower() == 'exite':
            print("Exiting edit menu.")
        else:
            expense_number = int(exp_num_str)
        
        if expense_number < 1 or expense_number > len(list_expense):
            print(f"Invalid expense number! Must be between 1 to {len(list_expense)}.")

        selected_expense = list_expense[expense_number - 1]
        print(f"\nEditing item: {selected_expense['title']}")
        print("1. title")
        print("2. amount")
        print("3. category")
        print("4. all")
        print("5. Exite")

        edit_item_num = int(input("Enter the item to edit (1-5): "))
        
        if edit_item_num == 1:
            new_title = input("Enter the new title: ")
            selected_expense['title'] = new_title
            print("Changes have been successfully saved")
        
        elif edit_item_num == 2:
            new_amount = input("Enter the new amount: ")
            selected_expense['amount'] = new_amount
            print("Changes have been successfully saved")
        
        elif edit_item_num == 3:
            new_category = input("Enter the new category: ")
            selected_expense['category'] = new_category
            print("Changes have been successfully saved")
        
        elif edit_item_num == 4:
            new_title = input("Enter the new title: ")
            new_amount = input("Enter the new amount: ")
            new_category = input("Enter the new category: ")
            selected_expense['title'] = new_title
            selected_expense['amount'] = new_amount
            selected_expense['category'] = new_category
            print("Changes have been successfully saved")
        
        elif edit_item_num == 5:
            print("Exiting edit menu.")
        
        else:
            print("Invalid item number! Enter between 1 to 5.")

        edit_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        selected_expense['edit_time'] = edit_time_str
        
        save_expenses(list_expense)

    except ValueError:
        print("Invalid input. Please enter numbers where required.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def show_expense(list_expense):
    try:
        print("===list expense===")
        for i in list_expense:
            print("Title : ", i["title"])
            print("amount : ", i["amount"])
            print("category : ", i["category"])
            print("time :", i["time"])
            try:
                print("edit_time : ", i["edit_time"])
            except KeyError:
                pass 
            print("======")
    except Exception as e:
        print("There is no cost", e)


def Cost_Search():
    your_search = input("What are you looking for: ")
    print("")

    found= False
    for i in list_expense:
        if your_search.lower() in str(i["title"]).lower() or your_search.lower() in str(i["category"]).lower():
            print("Title : ", i["title"])
            print("amount : ", i["amount"])
            print("category : ", i["category"])
            print("time :", i["time"])
            try:
                print("edit_time : ", i["edit_time"])
            except KeyError:
                pass                

            print("======")
            found = True
    
    if not found:
        print("No expense found!")


def remove_cost():
    your_search = input("What are you looking for: ")
    print("")

    found= False
    for i in list_expense:
        if your_search.lower() in str(i["title"]).lower() or your_search.lower() in str(i["category"]).lower():
            print("======")
            print("Title : ", i["title"])
            print("amount : ", i["amount"])
            print("category : ", i["category"])
            print("time :", i["time"])
            try:
                print("edit_time : ", i["edit_time"])
            except KeyError:
                pass 
            print("")
            a = input("Are you sure you want to delete this? y/n : ")
            print("....")
            a = a.lower()
            if a == "y":
                list_expense.remove(i)
                with open("expense.json", "w") as file:
                    json.dump(list_expense, file, indent = 4)
                print("The item was successfully deleted")
                found = True
            elif a == "n":
                found = True
            else:
                print("The command entered is not valid!")


    if not found:
        print("No expense found!")


def add_expense(Title, Amount, Category, time):
    new_expense = {
        "title": Title,
        "amount": Amount,
        "category": Category,
        "time" : time
    }

    list_expense.append(new_expense)
    with open("expense.json", "w") as file:
        json.dump(list_expense, file, indent = 4)
    print("The expense was added successfully!")

print("====Welcom=====")
print("")

f = True
while f:
    username = input("USERNAME: ")
    password = input("PASSWORD: ")
    print("")

    if username == Username and password == Password:
        print("Hello", user["username"])
        f= False

        flag = True
        while flag:
            print("")
            print("==== Cost management: ====")
            print("1.Add new expense")
            print("2.Show expenses")
            print("3.Calculating the total costs")  
            print("4.Cost Search")
            print("5.Remove cost")
            print("6.Edit expense")
            print("7.Exite")
            print("")
            while True:
                try:
                    num = input("Please choose one: ")
                    num = int(num)
                    print("")
                    if 1<= num <= 7:
                        break
                    else:
                        print("Invalid input! Please enter a number between 1 and 6.")
                        print("")
                except ValueError:
                    print("Invalid input! Please enter an integer number.")
                    print("")

                    
            if num == 1:
                print("Add new expense: ")
                print("")
                Title = input("Title: ")
                while True:
                    try:
                        Amount = int(input("Amount: "))
                        break
                    except ValueError:
                        print("The entered value is invalid!")
                Category = input("Category: ")
                time = datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))
                print("")
                add_expense(Title, Amount, Category, time)


            elif num == 2:
                show_expense(list_expense)
        
            elif num == 3:
                total_Amount = 0
                for index, i in enumerate(list_expense):
                    print(f"{index + 1}.{i['title']}-->{i['amount']}")
                    total_Amount += float(i["amount"])

                print("+......")
                print(f"Total expense: {total_Amount}")


            elif num == 4:
                Cost_Search()


            elif num == 5:
                remove_cost()


            elif num == 6:
                edit_expense(list_expense)

            elif num == 7:
                f = True
                flag = False
        



    else:
        print("Invalid information")
        print("-------")
    






