# ---------------
# Type comments to whats going on  (done)
# ------------------------------
# I want you to write the name and phone number from the user (done)
# ------------------------------
# * Make a delete opinion (Will work on it later)
# ------------------------------
# I want you to record the data into a json file (done)
# ------------------------------
# load data from the json file into contacts  (done)
import json

contacts = []

# the function to add the inputed data into the json


def write_json(new_data, filename='x.json'):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["emp_details"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)
# function that adds new contacts to the data base


def add_new_contact():
    # objects to be appended are the user_name=input
    user_name = input("Your name: ")
    user_tel = input("Your tell: ")
    # contact = {}the new data to add to the json
    contact = {"name": user_name, "tel": user_tel}
    contacts.append(contact)
    print("Contact has been added to json!")
    write_json(contact)
# prints contacts


def print_all_contacts():
    with open('x.json', 'r') as print_contacts:
        contacts = json.load(print_contacts)
    print(contacts)
# just prints an output


def del_contact():
    print("function that kill a contact")
# just prints an output


def search_contact():
    print("function that searches for a contact")
# main function acts as a BLACK BOX


def main():
    user_selection = ""
    while user_selection != "x":
        # menu
        print("a - add new contact")
        print("d - delete a contact")
        print("s - search a  contact")
        print("p - print all  contacts")
        print("x - exit")
        # get the user selection
        user_selection = input("select an option: ")
        print("The user select: "+user_selection)
        # implement the user selection
        if user_selection == "a":
            add_new_contact()
            break
        if user_selection == "p":
            print_all_contacts()
            break
        if user_selection == "d":
            del_contact()
            break
        if user_selection == "s":
            search_contact()
            break

        # if user_selection == "x": print("make a function that exit from the program")
if __name__ == "__main__":
    main()
