# THIS MODULE IMPLEMENTS A HELP COMMAND WITH A LIST OF ALL POSSIBLE


# Defining of Global variables is done here

list_of_commands = {
"mbook" : "view and book availble time slots",
"vbook" : "view bookings",
"cbook" : "cancel booking",
"mtslot" : "create time slot",
"dtslot" : "displays time slots",
"ctslot" : "cancel time slot"
}

# End of global variables

def print_help():
    global list_of_commands
    print("Valid Commands:")
    for i in list_of_commands:
        print(f"{i} : {list_of_commands[i]}")

if __name__ == "__main__":
    print_help()
