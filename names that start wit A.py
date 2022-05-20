def search_name():
    my_file = open("names.txt", "r")
    for s in my_file:
        if s.startswith("A"):
            print(s)
search_name() 
