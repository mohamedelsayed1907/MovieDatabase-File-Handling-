def display_menu():
    print("1. Add Movie")
    print("2. List Movies")
    print("3. Search Movie")
    print("4. Exit Program")
    choice = input("Choice:\t")
    return choice

def add_movie():
    name = input("Movie name:\t")
    year = input("Year:\t")
    author = input("Author:\t")
    return (name, year, author)

while True:
    choice = display_menu()
    if choice == "0":
        break
    elif choice == "1":
        name, year, author = add_movie()
        with open("MovieData.txt", "a") as movie_database:
            movie_database.write(name + "#" + year + "#" + author + "\n")
    elif choice == "2":
        with open("MovieData.txt", "r") as movie_database:
            for line in movie_database:
                print(line)
    elif choice == "3":
        name = input("Enter movie name:\t")
        with open("MovieData.txt", "r") as movie_database:
            for line in movie_database:
                if name.lower() in line.lower():
                    details = line.split("#")
                    print("Name = ", details[0])
                    print("Year = ", details[1])
                    print("Author = ", details[2])