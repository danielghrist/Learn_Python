class User:
    # Initialize the attributes
    def __init__(self, user_id, username):
        print("New user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1



user_1 = User("001", "danny")
user_2 = User("002", "angela")

# print(f"Username: {user_1.username}, ID#: {user_1.id}")
# print(f"Username: {user_2.username}, ID#: {user_2.id}")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# class Car:
#     def __init__(self):
#         self.seats = 5
#
#     def enter_race_mode(self):
#         self.seats = 2




