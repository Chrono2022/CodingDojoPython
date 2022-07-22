class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("==========================")
        print(f"Name: {self.first_name}" + " " + f"{self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
        print("==========================")
        return self

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print("Welcome new member!")
        else: 
            print(f"{self.first_name} is already a member")
        return self

    def spend_points(self, amount):
        if self.gold_card_points - amount <= 0:
            print("You do not have enough points!")
        else:
            self.gold_card_points = self.gold_card_points - amount
        return self

nathan = User("Nathan", "Ingersoll", "123@email.com", 26)

lyndsay = User("Lyndsay", "Matter", "321@superemail.com", 28)

dakota = User("Dakota", "Anderson", "213@supersuperemail.com", 26)

nathan.display_info().enroll().spend_points(50).display_info()

lyndsay.enroll().spend_points(199).display_info()