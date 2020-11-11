import sys

#This is step 1 of the project 
"TODO:Take command-line arugments as input"
"TODO:Have a help command to describe command-line arugmemts"
"TODO: Export to file or output so we can use it on command-tool"
"TODO:STDOUT must be piped to file using linux pipe operators" #What are  linux pipe operators 
"TODO: Export all interal data in a file or some sort"

#Patient information:
#Name - Takes 1 agrumemt
#Surname - Gives one arugment
#username -Gives one arugment
#email  - Gives one arugment
#subject to be assited on?- Takes more the one agrument 
#Creates a patient ID with user name 

#Take a Patient info export to a file 
#With the headings

def test():
    input("Please Enter the following information: Name,Surname,Username,email: ")
    if len(sys.argv) == 6:
        name =  sys.argv[2]
        surname = sys.argv[3]
        username = sys.argv[4]
        email = sys.argv[5]
        name.capitalize
        surname.capitalize
        user_info = []
        user_info.append(name)
        user_info.append(surname)
        user_info.append(username)
        user_info.append(email)
        print(user_info)
        print(name)
    # with open("User_information.txt",'w') as user_information:
    #     info = user_information.write(name)

def user_info(name,surname,username,email):
    test()
    user_info = []
    print(name)
    user_info.append(name)
    user_info.append(surname)
    user_info.append(username)
    user_info.append(email)
    print(user_info)
    print(f"{name} + {surname}")
        

    # sub = input("Please enter the subjects you strugging with?")
  
    # print(user_info)
    # file_information = open("User_information.txt","w")
    # for i in user_info:
    #     file_information.writelines(i) 
    # file_information.close

# def importing_info():
#     test()
#     file_information = open("User_information.txt","a")
#     file_information.write(test())
#     file_information.close

if __name__ == "__main__":
    test()
    