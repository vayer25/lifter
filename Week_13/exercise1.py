class Guest:
    def __init__(self, role: str):
        self.role = role

def guest_only(func):
    def wrapper(user, *args, **kwargs):
        if user.role != "Guest":
            raise ValueError("Access denied: only guests can open this room.")
        return func(user, *args, **kwargs)
    return wrapper

@guest_only
def open_room(user, room_number):
    print(f"Welcome! You have opened room {room_number}.")


owner = Guest("Owner")
guest = Guest("Guest")

print("one: Guest tries to open the room:")
open_room(guest, 1421)

print("\ntwo: Owner tries to open the room:")
open_room(owner, 1421)