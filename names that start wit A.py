names_starting_with_a = []
my_file = open("names.txt", "r")
def search_name():
    for s in my_file:
        if s.startswith("A"):
            words=s.split()
            names_starting_with_a.append(words)

    print(names_starting_with_a)
search_name() 