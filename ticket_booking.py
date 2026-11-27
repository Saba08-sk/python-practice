import random

# Movie Collection
movies = {
    1: {
        "name": "Interstellar",
        "time": "10:00 AM",
        "price": 250,
        "seats": ["A1", "A2", "A3", "A4", "A5"]
    },
    2: {
        "name": "Inception",
        "time": "1:30 PM",
        "price": 200,
        "seats": ["B1", "B2", "B3", "B4", "B5"]
    },
    3: {
        "name": "The Dark Knight",
        "time": "6:00 PM",
        "price": 220,
        "seats": ["C1", "C2", "C3", "C4", "C5"]
    }
}

# Store booking details
bookings = {}


# Display available movies
def display_movies():
    print("\n AVAILABLE MOVIES")

    for movie_id, details in movies.items():
        print(f"\nMovie ID: {movie_id}")
        print(f"Movie: {details['name']}")
        print(f"Time: {details['time']}")
        print(f"Price: Rs.{details['price']}")


# Display available seats
def display_seats(movie_id):
    print("\nAvailable Seats:")

    for seat in movies[movie_id]["seats"]:
        print(seat, end="  ")

    print()


# Book movie tickets
def book_tickets():

    display_movies()

    try:
        movie_id = int(input("\nEnter Movie ID: "))

        if movie_id not in movies:
            print("Invalid Movie ID!")
            return

        display_seats(movie_id)

        selected_seats = input(
            "\nEnter seat numbers separated by commas: "
        ).upper().replace(" ", "").split(",")

        available_seats = movies[movie_id]["seats"]

        # Validate seats
        if not selected_seats or any(seat not in available_seats
                                     for seat in selected_seats):
            print("Invalid or unavailable seat!")
            return

        if len(selected_seats) != len(set(selected_seats)):
            print("You cannot select the same seat twice!")
            return

        # Calculate ticket price
        ticket_price = movies[movie_id]["price"]
        total = ticket_price * len(selected_seats)

        # Apply discount
        discount = 0

        if len(selected_seats) >= 3:
            discount = total * 0.10

        final_amount = total - discount

        # Generate booking ID
        booking_id = "BK" + str(random.randint(1000, 9999))

        # Save booking
        bookings[booking_id] = {
            "movie": movies[movie_id]["name"],
            "time": movies[movie_id]["time"],
            "seats": selected_seats,
            "total": final_amount
        }

        # Remove booked seats
        for seat in selected_seats:
            available_seats.remove(seat)

        # Display ticket
        print("\n BOOKING CONFIRMED ")
        print(f"Booking ID: {booking_id}")
        print(f"Movie: {movies[movie_id]['name']}")
        print(f"Show Time: {movies[movie_id]['time']}")
        print(f"Seats: {', '.join(selected_seats)}")
        print(f"Total Amount: Rs.{total}")
        print(f"Discount: Rs.{discount:.2f}")
        print(f"Final Amount: Rs.{final_amount:.2f}")
        print("=======================================")

    except ValueError:
        print("Please enter valid input!")


# View booking details
def view_booking():

    booking_id = input("\nEnter Booking ID: ").upper()

    if booking_id in bookings:
        details = bookings[booking_id]

        print("\nBOOKING DETAILS ")
        print(f"Booking ID: {booking_id}")
        print(f"Movie: {details['movie']}")
        print(f"Time: {details['time']}")
        print(f"Seats: {', '.join(details['seats'])}")
        print(f"Amount Paid: Rs.{details['total']:.2f}")
        print("=====================================")

    else:
        print("Booking not found!")


# Main Menu
def main():

    while True:
        print("\n MOVIE TICKET BOOKING ")
        print("1. View Movies")
        print("2. Book Tickets")
        print("3. View Booking")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            display_movies()

        elif choice == "2":
            book_tickets()

        elif choice == "3":
            view_booking()

        elif choice == "4":
            print("\nThank you for visiting our cinema!")
            break

        else:
            print("Invalid choice! Please try again.")


# Start Program
if __name__ == "__main__":
    main()