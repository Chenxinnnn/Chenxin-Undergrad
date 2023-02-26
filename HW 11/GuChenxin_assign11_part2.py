#First define your object
class Smartphone:
    #define the initial
    def __init__(self, capacity, name):
        print("Smartphone created!")
        self.name = name
        self.capacity = capacity
        self.apps = {}
        self.applist = self.apps.keys()
        self.appsizes = self.apps.values()
        self.used = 0
        self.available = self.capacity - self.used
        print(f"Name: {self.name}")
        print(f"Capacity: {self.used} out of {capacity} GB")
        print(f"Available space: {self.available}")
        print(f"Apps installed: {len(self.applist)}")
        for ii in self.apps:
            print(f"* {ii} is using {self.apps[ii]} GB")
        print("")

    #define the functions    
    def add_app(self, appname, appsize):
        if appname not in self.applist:
            if appsize <= self.available:
                self.apps[appname] = appsize
                self.used += appsize
                self.available = self.capacity - self.used
            else:
                print("Cannot install app, no available space")
        else:
            print("Has already installed this app")
                
    def remove_app(self, appname):
        if appname in self.applist:
            self.used -= self.apps[appname]
            self.apps.pop(appname)
            self.available = self.capacity - self.used
            print(f"App removed: {appname}")
	
    def reset(self):
        self.name = "Untitled"
        self.apps = {}
        self.used = 0
        self.applist = self.apps.keys()
        self.appsizes = self.apps.values()

    def rename(self, new_name):
        self.name = new_name

    def has_app(self, appname):
        if new_name in self.applist:
            return True
        else:
            return False

    def get_available_space(self):
        self.available = self.capacity - self.used
        return int(self.available)

    def report(self):
        print(f"Name: {self.name}")
        print(f"Capacity: {self.used} out of {capacity} GB")
        print(f"Available space: {self.get_available_space()}")
        print(f"Apps installed: {len(self.applist)}")
        for i in sorted(self.apps):
            print(f"* {i} is using {self.apps[i]} GB")


#First let the users input a valid machine
while True:
    capacities = input("Size of your new smartphone (32, 64 or 128 GB): ")
    if capacities.isdigit() == True:
        capacity = int(capacities)
        break
    else:
        print("Invalid input, try again")
        print("")

name = input("Smartphone name: ")
machine = Smartphone(capacity, name)

#Start the program
while True:
    signal = input("(r)eport, (a)dd app, r(e)move app, re(s)et, re(n)ame or (q)uit: ").lower()
    #when the user choose to add an app
    if signal == "a":
        appname = input("App name to add: ")
        appsize = int(input("App size in GB: "))
        machine.add_app(appname, appsize)
        print("")

    #when the use choose to report
    elif signal == "r":
        machine.report()
        print("")
        
    #when the user choose to remove an app    
    elif signal == "e":
        appname = input("App name to remove: ")
        machine.remove_app(appname)
        print("")

    #when the user choose to reset the phone
    elif signal == "s":
        test = input("Reset phone?  Are you sure?  (yes/no): ").lower()
        if test == "yes":
            machine.reset()
            print("Smartphone has been reset.")
        print("")

    #when the user choose to rename the phone
    elif signal == "n":
        new_name = input("Enter a new name for the phone: ")
        machine.rename(new_name)
        print("")

    #when the user choose to quit
    elif signal == "q":
        print("Goodbye!")
        break

    #when the user entered an invalid input
    else:
        print("Invalid command, try again.")
        print("")
    
