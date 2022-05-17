inline = open("names.txt", "r")
user_input=str(input("Enter a number: "))
def searchAge():
    for s in inline:
        if user_input in s:
            print(s)

searchAge()