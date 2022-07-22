# Create a file with the User class, including the __init__ with all the attributes, parameters, and default values:

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
# Add the display_info(self) method to the User class
# /n can also be used to separate the strings into separate lines

    def display_info(self):
        print("==========================")
        print(f"Name: {self.first_name}" + " " + f"{self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
        print("==========================")

# Add the enroll method to the User class
# Implement the logic for testing if already a member:

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print("Welcome new member!")
        else: 
            print(f"{self.first_name} is already a member")

# Implement the spend_points method

    def spend_points(self, amount):
        if self.gold_card_points - amount <= 0:
            print("You do not have enough points!")
        else:
            self.gold_card_points = self.gold_card_points - amount
            return self, amount

# In the outer scope, create a user instance and call the display_info method to test:

nathan = User("Nathan", "Ingersoll", "123@email.com", 26)

# Create two more instances of the User class

lyndsay = User("Lyndsay", "Matter", "321@superemail.com", 28)

dakota = User("Dakota", "Anderson", "213@supersuperemail.com", 26)

nathan.display_info()

# implement and test by calling the enroll method on the user in the outer scope.

nathan.enroll()

nathan.display_info()

# Re-enroll the 1st user

nathan.enroll()

# Have the first user spend 50 points

nathan.spend_points(50)

nathan.display_info()

# Have the second user enroll

lyndsay.enroll()

lyndsay.display_info()

# Have the second user spend 80 points

lyndsay.spend_points(80)

lyndsay.display_info()

# Call the display method on all users

nathan.display_info()
lyndsay.display_info()
dakota.display_info()

# Call the spend_points method with 40 points on the 3rd user:

dakota.spend_points(40)

dakota.display_info()