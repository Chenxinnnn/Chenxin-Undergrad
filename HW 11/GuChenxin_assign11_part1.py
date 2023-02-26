import random

#Start to define the object
class Gumball_Machine:
    def __init__(self, num):
        self.num = num
        self.money = 0.0
        self.type = []
        self.blueball = 0
        self.redball = 0
        self.greenball = 0
        for i in range(num):
            random_num = random.randint(1,3)
            if random_num == 1:
                random_ball = "blue"
                self.type.append(random_ball)
                self.blueball += 1
            elif random_num == 2:
                random_ball = "red"
                self.type.append(random_ball)
                self.redball += 1
            elif random_num == 3:
                random_ball = "green"
                self.type.append(random_ball)
                self.greenball += 1
                
        print(f"Gumball Machine created with {self.num} random gumballs")
        print("")
        
    def report(self):
        print("Gumball Machine Report:")
        print(f"* Gumballs in machine: {len(self.type)}")
        print(f"* Money in machine: ${self.money:,.2f}")
        print("")

    #define the functions
    def count_gumballs_by_type(self, color):
        if color == "blue":
            print(f"There are {self.blueball} gumballs of type blue in the machine")
        elif color == "red":
            print(f"There are {self.redball} gumballs of type red in the machine")
        elif color == "green":
            print(f"There are {self.greenball} gumballs of type green in the machine")
        print("")

    def dispense(self, coin):
        if coin != 0.25:
            print("Invalid coin, no gumball will be dispensed")
            print("")
        else:
            if self.type == []:
                print("Machine is empty, no gumball will be dispensed")
                print("")
            else:
                self.money += 0.25
                while True:
                    random_number = random.randint(1,3)
                    if random_number == 1:
                        random_ball = "blue"
                        if self.blueball > 0:
                            self.blueball -= 1
                            break
                        else:
                            continue
                    elif random_number == 2:
                        random_ball = "red"
                        if self.redball > 0:
                            self.redball -= 1
                            break
                        else:
                            continue
                    elif random_number == 3:
                        random_ball = "green"
                        if self.greenball >0:
                            self.greenball -= 1
                            break
                        else:
                            continue
                self.type.remove(random_ball)
                print(f"Accepting 0.25; Dispensing a {random_ball} gumball")
                print("")


