#First open the file. If file does not exist, write a new file.
try:
    file = open("my_pokemon.txt", "r")
    alldata = file.read()
    file.close()
    alldatas = alldata.split("\n")

except:
    file = open("my_pokemon.txt", "w")
    file.close()
    alldatas = ""
    
#Slipt the file into parts and build up our dictionary.
pokemons = {}
for foo in alldatas:
    try:
        split_name = foo.split(":")
        name = split_name[0]
        foobar = split_name[1]
        pokemons[split_name[0]] = {}
        properties = foobar.split(",")
        for bar in properties:
            pokemons[split_name[0]]["quantity"] = int(properties[0])
            pokemons[split_name[0]]["fee"] = float(properties[1])
            pokemons[split_name[0]]["powers"] = []
            types = properties[2].split(" ")
            for foooo in types:
                pokemons[split_name[0]]["powers"].append(foooo)
    except:
        print("", end = "")

valid_pokemon_types = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water']

total_type = []
for x in pokemons.keys():
    for y in pokemons[x]["powers"]:
        if y in total_type:
            continue
        else:
            total_type.append(y)
valid_pokemon_types = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water']

#Put everthing else into the while loop
while True:
    print("Welcome to the Pokemon Center!")
    signal = input("(a)dd, (r)emove, r(e)port, (s)earch by name, search by (t)ype, (l)ist or (q)uit: ").lower()
    #for s
    if signal == "s":
        pokemon = input("Name of Pokemon to search for: ").lower()
        pokemon_name = pokemon.capitalize()
        if pokemons.get(pokemon) != None:
            amount = pokemons[pokemon]["quantity"]
            fee = float(pokemons[pokemon]["fee"])
            pokemon_type = ""
            for i in pokemons[pokemon]["powers"]:
                pokemon_type += (i.capitalize() + " ")
                
            print(f"We have {amount} {pokemon_name} at the Pokemon Center")
            print(f"It will cost ${fee:,.2f} to adopt this Pokemon")
            print(f"{pokemon} has the following types: {pokemon_type}")
        else:
            print(f"We do not have any {pokemon_name} at the Pokemon Center")

    #For quit
    elif signal == "q":
        print("See you next time!")
        break
    
    #For list
    elif signal == "l":      
        space = 0
        for pokemon in pokemons.keys():
            name_length = int(len(pokemon))
            if name_length > space:
                space = name_length
        #Use spaces to control the format
        print("Name" + (space - 2) * " " , "Amount Available  ", "Adoption Fee", "Types(s)")
        for pokemon in sorted(pokemons.keys()):
            
            space1 = space + 19 - int(len(pokemon))-int(len(str(pokemons[pokemon]["quantity"])))
            fee_print = format(pokemons[pokemon]["fee"],",.2f")
            fee_lenth = len(fee_print)
            space2 = 15 - fee_lenth
            type_amount = len(pokemons[pokemon]["powers"])
            pokemon_type = ""
            for i in pokemons[pokemon]["powers"]:
                pokemon_type += (i.capitalize() + " ")
            print(pokemon.capitalize() + space1 * " " + str(pokemons[pokemon]["quantity"]) + space2 * " " + fee_print + " " + pokemon_type)
    
    #For search by type
    elif signal == "t":
        space = 0
        for pokemon in pokemons.keys():
            name_length = int(len(pokemon))
            if name_length > space:
                space = name_length
        search_type = input("Enter Pokemon type: ").lower()
        if search_type in total_type:
            print("Name" + (space - 2) * " " , "Amount Available  ", "Adoption Fee", "Type(s)" )
            for pokemon in sorted(pokemons.keys()):
                if search_type in pokemons[pokemon]["powers"]:
                    space1 = space + 19 - int(len(pokemon))-int(len(str(pokemons[pokemon]["quantity"])))
                    fee_print = format(pokemons[pokemon]["fee"],",.2f")
                    fee_lenth = len(fee_print)
                    space2 = 15 - fee_lenth
                    type_amount = len(pokemons[pokemon]["powers"])
                    pokemon_type = ""
                    for i in pokemons[pokemon]["powers"]:
                        pokemon_type += (i.capitalize() + " ")
                    print(pokemon.capitalize() + space1 * " " + str(pokemons[pokemon]["quantity"]) + space2 * " " + fee_print + " " + pokemon_type)    
        else:
            print("We have no Pokemon of that type at our Pokemon Center")
    #For a    
    elif signal == "a":
        new = input("Enter name of new pokemon: ").lower()
        if new in pokemons.keys():
            print("Duplicate name, add operation cancelled")
        else:
            pokemons[new] = {}
            while True:
                #validate all the input and add each variable to each list if they are valid
                new_amount = input("How many of these Pokemon are you adding? ")
                if new_amount.isdigit():
                    if int(new_amount) > 0:
                        pokemons[new]["quantity"] = new_amount
                        break
                print("Invalid, please try again")
            while True:
                new_adopt_fee = input("What is the adoption fee for this Pokemon? ")
                new_adopt_fee_test = []
                test = True
                if new_adopt_fee == ".":
                    test = False
                    
                for digit in new_adopt_fee:
                    if digit.isalpha() or (digit.isdigit() == False and digit not in "."):
                        test = False
                        break
                    elif digit == ".":
                        if digit in new_adopt_fee_test:
                            test = False
                            break
                        else:
                            new_adopt_fee_test.append(digit)

                if test == True and float(new_adopt_fee) > 0:
                    pokemons[new]["fee"] = float(new_adopt_fee)
                    break
                else:
                    print("Invalid, please try again")
            print("Next you will be prompted to enter the 'types' for this Pokemon.  Pokemon can have multiple types. Type 'help' to view all possible Pokemon types, and type 'end' to stop entering types. You must enter at least one valid 'type'")
            type_duplicate_test = []
            while True:
                new_type = input("What type of Pokemon is this? ").lower()
                if new_type == "help":
                    for a in valid_pokemon_types:
                        print(f"* {a}")
                elif new_type in valid_pokemon_types:
                    if new_type in type_duplicate_test:
                        print("Duplicate type")
                    else:
                        type_duplicate_test.append(new_type)
                        print(f"Type {new_type} applied")
                elif new_type == "end":
                    if type_duplicate_test == []:
                        print("Must enter a type")
                    else:
                        pokemons[new]["powers"] = type_duplicate_test
                        for x in pokemons.keys():
                            for y in pokemons[x]["powers"]:
                                if y in total_type:
                                    continue
                                else:
                                    total_type.append(y)
                        print("Pokemon added!")
                        break
                else:
                    print("This is not a valid type, please try again")
                    
    #for removing pokemons, delete everything if the pokemon is in the list
    elif signal == "r":
        remove = input("Enter name of Pokemon to remove: ").lower()
        if remove in pokemons.keys():
            pokemons.pop(remove)
            print("Pokemon removed")
        else:
            print("Pokemon not found, cannot remove")

    #For printing out the sumup
    elif signal == "e":
        current_pokemon = pokemons.keys()
        highest_adoption = 0
        total_cost = 0
        for some in current_pokemon:
            if pokemons[some]["fee"] >= highest_adoption:
                highest_adoption = pokemons[some]["fee"]
                highest_pokemon = some
        lowest_adoption = highest_adoption
        for some in current_pokemon:
            if pokemons[some]["fee"] <= lowest_adoption:
                lowest_adoption = pokemons[some]["fee"]
                lowest_pokemon = some
            total_cost += int(pokemons[some]["quantity"]) * float(pokemons[some]["fee"])
                

        print(f"Highest priced Pokemon: {highest_pokemon} @ ${highest_adoption:,.2f} per Pokemon")
        print(f"Lowest priced Pokemon: {lowest_pokemon} @ ${lowest_adoption:,.2f} per Pokemon")
        print(f"Total cost to adopt all Pokemon in the Center: ${total_cost:,.2f}")

    #for invalid commands    
    else:
        print("Unknown command, please try again")
    file = open('my_pokemon.txt', 'w')
    for oof in pokemons.keys():
        its_type_mixed = ""
        its_type = pokemons[oof]["powers"]
        for rab in its_type:
            its_type_mixed += rab + " "
        new_line = oof + ":" + str(pokemons[oof]["quantity"]) + "," + str(pokemons[oof]["fee"]) + "," + its_type_mixed + "\n"
        file.write(new_line)
    file.close()
    print("")




