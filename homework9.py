dict_users = {    # словник з номерами и именами людей
    "dima": "039902003",
    "elena": "9000299192",
    "arsen": "9292123222"
}   

def input_error(func):    #декоратор
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Something went wrong"
        except ValueError:
            return "Something went wrong"
    return inner

def say_bye():  
    return "Goob bye, see u soon"


def hello_answer(smt):
    return "Hello, glad to see u\nHow can I help you?"

@input_error
def show_all(smt):
    info = ""
    for name, number in dict_users.items():
        info += f"Name: {name.title()}  Number: {number}\n"
    return info

@input_error
def add_user(name, phone):
    dict_users[name]= phone
    return f"You added new user {name.title()} with phone {phone}"

@input_error
def change_user(user, phone):
    if user in dict_users:
        dict_users[user] = phone
        return f"Now {user.title()} has new number - {phone}"
    else:
        return f"{user.title()} not exist in dictionary"

@input_error
def show_phone(user):
    phone = dict_users.get(user)
    return f"{user.title()} has phone - {phone}"



                        


def main():
    while True:
        input_user = input("Enter your command: ").lower()
        list_input = input_user.split()
        
        if input_user in (".", "good bye", "exit", "close"):
            print(say_bye())
            break
        
        elif input_user == "hello":
            print(hello_answer("smt"))
            
        elif input_user == ("show all"):
            print(show_all("smt"))
            
        elif input_user.startswith("phone"):
            print(show_phone(list_input[-1]))
        
        elif input_user.startswith("change"):
            print(change_user(list_input[-2],list_input[-1]))
        
        elif input_user.startswith("add"):
            print(add_user(list_input[-2], list_input[-1]))
            
            
 
      
        
           
if __name__ == "__main__":
    main()
































































        
