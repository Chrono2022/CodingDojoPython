# Assignment Task 1: Update the Constructor (init function)

    # We start off with a basic class (named Player) and a basic init function (constructor) 

class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

    # Our task with the above is to update the constructor to accept a dictionary with a single player's information (name, age, etc.) without typing the individual arguments

    # Arguments would be defining the individual variables in the constructor (name, age, etc.)

kevin = Player("Kevin", 26, "Front-Support", "New England Patriots")

    # Now that kevin has been named in the class Player with the arguments that define the name, age, etc. you can call upon the name to bring up the info

    # Since self.name = name, and since kevin has become the self in this case, we just say kevin.name, and it will bring up the name. Same as age, etc.
print(kevin.name)
print(kevin.age)

    # But the purpose of Assignment Task 1 is to condense the arguments (name, age, etc.) so we do not need to type them individually

    # We'll start by changing the constructor

class Player:
    def __init__(self, player):
        self.name = player['name']
        self.age = player['age']
        self.position = player['position']
        self.team = player['team']

    # We condensed name, age, etc. into one argument: player. So now the name is player['name'], because 'name' will be listed in the players dictionary, and this will 
        # allow it to be called using player.name, because rather than us defining the name individually, the dictionary we call does that for us.

    # With the above, if a player has the information written, we just simply need to call that dictionary into the class


# Assignment Task 2: Create instances using individual player dictionaries

    # So here we have a list of dictionaries that fortunately have the name, age, etc. listed for us:

kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
}

    # In order for us to call these using the class that we made, we must pass these as arguments, fortunately we don't have to pass the name, age, etc, we only need to pass
        # the player

player_kevin = Player(kevin)

player_jason = Player(jason)

    # We made a new variable called player_kevin, and made it equal to the class Player with the argument kevin to define the player. Since kevin already had all the info,
        # then we now can call the name, age, etc. from this 

print(player_kevin.name)
print(player_jason.age)


# Assignment Task 3: Make a list of Player instances from a list of dictionaries

    # So for this we'll need a list of dictionaries: 

players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
    }
]

    # For the above, players is the list [] with a few dictionaries {}

    # We want to make a for loop that will take all the dictionaries, and put them in a new list as object instances. 

    # A good example of an object instance is what we get when we use this:

print(player_kevin)

    # It will print <__main__.Player object at (insert bunch of numbers / letters here). This is what we want to put in the new list

    # First we will create an empty list:

new_team = []

    # Now we will make the for loop. We don't need to make it as a function, but for ease of use we will here: 

def add_players(team_list):
    for key in team_list:
        new_team.append(Player(key))
    print(new_team)
    return new_team

    # We use def to start the function, which we have named add_players. It requires one argument, which we had named team_list, in the (). We will use the giant list called
        # players to act as the team_list, but so long as any list has the name, age, etc, this function would work for any of them. 

    # The next part of the function is for key in team_list. A key, in the case of a dictionary, is like {key1:value1} or in players case, name(key)="Kevin Durant"(value)

    # We want the loop to cycle through each key in the list, gathering the names, ages, etc. of the people in the list and using our class Player to make them into objects to be
        # called upon later

    # So for key (name, age, etc.) in team_list (which we'll make players, the list above, define the argument team_list in this case)

    # new_team (the empty list) will .append, or add to itself, (Player(key)), which means the keys that are being found as the loop goes will go through the Player class
        # and condense the information per dictionary into an object to be called upon later

    # Once the loop is done, we can call the function and it will print and return the value of the now filled list new_team. Because we were just wanting the objects, 
        # the list now contains a bunch of <__main__.Player object at (insert bunch of numbers / letters here), one for each dictionary in the list. 

add_players(players)

    # We used the list above called players to replace the argument team_list, so when the function mentions team_list, it will look to the info in players


# Assignment Task 4: Add a class method that, given a list of dictionaries, returns a new list of player objects

    # This is basically the exact same thing we did before, but with minor differences

    # First we will put this within our class. We will use the Player class from earlier: 

class Player:
    def __init__(self, player):
        self.name = player['name']
        self.age = player['age']
        self.position = player['position']
        self.team = player['team']

    @classmethod 
    def get_team(cls, team_list):
        team = []
        for key in team_list:
            team.append(cls(key))
        print(team)
        return team

    # Here we wrote @classmethod and placed the function inside the class. Since it is inside the class, we don't need to specify the class Player in the function, we just have
        # to write cls (class). 
    
    # We also have to create the empty list (team in this case) inside the function, otherwise it won't know what team is. 

Player.get_team(players)

    # When the whole thing is written, now we just call the class, the function, and offer a list to replace the argument team_list, and the function will create player
        # objects in the new list called team. 