#Cree un diccionario que guarde la siguiente información sobre un hotel
# Crear un diccionario para almacenar la información del usuario
user_data = {}

user_name = input('Please add your name: ')
star_rating = int(input('Please add a rating of your room: '))

rooms = []

num_rooms = int(input("How many rooms do you want to add? "))

for i in range(num_rooms):
    print(f"\nRoom {i + 1}:")
    room_number = input("Enter room number: ")
    floor = input("Enter floor number: ")
    price_per_night = int(input("Enter price per night: $ "))


    rooms.append({
        "number": room_number,
        "floor": floor,
        "price_per_night": price_per_night
    })


user_data["user_name"] = user_name
user_data["star_rating"] = star_rating
user_data["rooms"] = rooms 


print("\nInformation gathered from the user:", user_data)


