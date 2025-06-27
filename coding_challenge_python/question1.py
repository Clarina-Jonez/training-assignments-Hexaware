movie_list = ["Inception", "Interstellar", "The Matrix", "Avengers: Endgame", "The Lion King"]

movie_prices = {"Inception": 100, "Interstellar": 120, "The Matrix": 130, "Avengers: Endgame": 110, "The Lion King": 100}


def show_movies():
    print("Available Movies:")
    for i in range(len(movie_list)):
        print(str(i + 1) + ". " + movie_list[i] + " - " + str(movie_prices[movie_list[i]]))


def calculate_total(price, tickets):
    return price * tickets


def book_movie():
    show_movies()
    choice = int(input("Enter the number of the movie you want to book: "))
    
    if choice < 1 or choice > len(movie_list):
        print("Invalid movie choice.")
        return
    
    selected_movie = movie_list[choice - 1]
    tickets = int(input(f"How many tickets do you want for {selected_movie}? "))
    
    if tickets < 1:
        print("You must book at least 1 ticket.")
        return
    

    price = movie_prices[selected_movie]
    total = calculate_total(price, tickets)
    

    
    print(f"You booked {tickets} ticket(s) for {selected_movie}.")
    print(f"Total amount: {total}")

if __name__ == "__main__":
    book_movie()
