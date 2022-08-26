# menu
# load
# add
# print
# delete
# search
import json

contacts=[]

# implemented
# display menu, get user selection
def menu():
    print("1 - load")
    print("2 - add")
    print("3 - print")
    print("4 - delete")
    print("5 - search")
    print("6 - exit")
    user_selection=input("your selection:")
    return int(user_selection)

# add a new contact to contacts list
def add(): contacts.append({"name":input("your name?"),"cell":input("cell? ")})
   
# print all contacts
def print_all(): print(contacts)

# load from file to list contacts
def load():
    global contacts
    with open('contacts.json', 'r') as f:
        contacts = json.load(f)
        
# save contacts list to a file
def save():
    with open('contacts.json', 'w') as f:
        json.dump(contacts, f)

# search by name...
def search():
    contact_2_search=input("su esmak?")
    for contact in contacts:
        if contact["name"] == contact_2_search:
            print (f"found, name: {contact['name']} cell: {contact['cell']}")
            return
    print(f"not found {contact_2_search}")

def delete():
    contact_2_search=input("What the name of the cunt you are willing to remove? ")
    for contact in contacts:
        if contact["name"] == contact_2_search:
            print (f"delete, name: {contact['name']} cell: {contact['cell']}")
            contacts.remove(contact)
            return
    print(f"not found {contact_2_search}")

def exit():
    return
    

def main():
    load() # load from file to contacts list
    user_selection= menu() # get user selection from menu 
    while  user_selection != 6:
        if user_selection == 2:add() # add new contact to contacts
        if user_selection == 3:print_all() #print all contacts
        if user_selection == 4:delete() # delete a contact2
        if user_selection == 5:search() # search a contact
        if user_selection == 6:exit()
        user_selection= menu()
    save() # save all contacts to JSON file

if __name__ == "__main__":
    main()
    