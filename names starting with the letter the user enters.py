user_input = input(">>").title()
names_input = []
my_file = open("names.txt" , "r")
def searchname():
    for s in my_file:
        if s.startswith(user_input):
            names_input.append(s)
    print(names_input)
searchname()
