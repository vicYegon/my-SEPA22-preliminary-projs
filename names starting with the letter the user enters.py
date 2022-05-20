user_input = input(">>").title()

my_file = open("names.txt" , "r")

def searchname():
    for s in my_file:
        if s.startswith(user_input):
            print(s)
searchname()
