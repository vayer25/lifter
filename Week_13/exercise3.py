from datetime import date
class User:
    def __init__(self, name: str, date_of_birth: date):
        self.name = name
        self.date_of_birth = date_of_birth
    @property
    def age(self):
        today = date.today()
        years = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1
        return years
def adult_only(func):
    def wrapper(user: 'User', *args, **kwargs):
        if not isinstance(user, User):
            raise TypeError("First argument must be a User instance.")
        if user.age < 18:
            raise PermissionError(f"Access denied: {user.name} is underage ({user.age} years old).")
        return func(user, *args, **kwargs)
    return wrapper
@adult_only
def buy_alcohol(user, product_name):
    print(f"{user.name} bought {product_name} successfully!")



adult1 = User("Alice", date(1990, 6, 15))
adult2 = User("Carlos", date(1985, 12, 5))
adult3 = User("Diana", date(1998, 3, 10))
minor = User("Bob", date(2010, 8, 20))

buy_alcohol(adult1, "wine")     
buy_alcohol(adult2, "vodka")    
buy_alcohol(adult3, "beer")    






