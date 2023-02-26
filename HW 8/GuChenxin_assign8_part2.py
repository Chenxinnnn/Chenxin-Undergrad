# I shared some tips with Yuxuan_Du
# Pokemon lists
pokemon_names = ['charmander', 'squirtle', 'bulbasaur', 'gyrados']
pokemon_amounts = [3, 2, 5, 1]
adoption_fee = [100.00, 50.00, 25.00, 1000.00]
pokemon_types = [['fire'], ['water'], ['grass'], ['water', 'flying']]
total_type = []
for x in pokemon_types:
    for y in x:
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
        if pokemon in pokemon_names:
            location = pokemon_names.index(pokemon)
            amount = pokemon_amounts[location]
            fee = float(adoption_fee[location])
            type_amount = len(pokemon_types[location])
            pokemon_type = ""
            for i in pokemon_types[location][0:type_amount]:
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
        for pokemon in pokemon_names:
            name_length = int(len(pokemon))
            if name_length > space:
                space = name_length
        #Use spaces to control the format
        print("Name" + (space - 2) * " " , "Amount Available  ", "Adoption Fee", "Types(s)")
        for pokemon in pokemon_names:
            location = pokemon_names.index(pokemon)
            space1 = space + 19 - int(len(pokemon))-int(len(str(pokemon_amounts[location])))
            fee_print = format(adoption_fee[location],",.2f")
            fee_lenth = len(fee_print)
            space2 = 15 - fee_lenth
            type_amount = len(pokemon_types[location])
            pokemon_type = ""
            for i in pokemon_types[location][0:type_amount]:
                pokemon_type += (i.capitalize() + " ")
            print(pokemon.capitalize() + space1 * " " + str(pokemon_amounts[location]) + space2 * " " + fee_print + " " + pokemon_type)

    #For search by type
    elif signal == "t":
        space = 0
        for pokemon in pokemon_names:
            name_length = int(len(pokemon))
            if name_length > space:
                space = name_length
        search_type = input("Enter Pokemon type: ").lower()
        if search_type in total_type:
            print("Name" + (space - 2) * " " , "Amount Available  ", "Adoption Fee", "Type(s)" )
            for pokemon in pokemon_names:
                location = pokemon_names.index(pokemon)
                if search_type in pokemon_types[location]:
                    space1 = space + 19 - int(len(pokemon))-int(len(str(pokemon_amounts[location])))
                    fee_print = format(adoption_fee[location],",.2f")
                    fee_lenth = len(fee_print)
                    space2 = 15 - fee_lenth
                    type_amount = len(pokemon_types[location])
                    pokemon_type = ""
                    for i in pokemon_types[location][0:type_amount + 1]:
                        pokemon_type += (i.capitalize() + " ")
                    print(pokemon.capitalize() + space1 * " " + str(pokemon_amounts[location]) + space2 * " " + fee_print + " " + pokemon_type)    
        else:
            print("We have no Pokemon of that type at our Pokemon Center")
    #For a    
    elif signal == "a":
        new = input("Enter name of new pokemon: ").lower()
        if new in pokemon_names:
            print("Duplicate name, add operation cancelled")
        else:
            while True:
                #validate all the input and add each variable to each list if they are valid
                new_amount = input("How many of these Pokemon are you adding? ")
                if new_amount.isdigit():
                    if int(new_amount) > 0:
                        pokemon_amounts.append(new_amount)
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
                    adoption_fee.append(float(new_adopt_fee))
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
                    pokemon_names.append(new)
                    pokemon_types.append(type_duplicate_test)
                    total_type = []
                    for x in pokemon_types:
                        for y in x:
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
        remove = input("Enter name of Pokemon to remove: ")
        if remove in pokemon_names:
            location = pokemon_names.index(remove)
            del pokemon_names[location]
            del pokemon_amounts[location]
            del adoption_fee[location]
            del pokemon_types[location]
            print("Pokemon removed")
        else:
            print("Pokemon not found, cannot remove")

    #For printing out the sumup
    elif signal == "e":
        highest_adoption = max(adoption_fee)
        lowest_adoption = min(adoption_fee)
        high_index = adoption_fee.index(highest_adoption)
        low_index = adoption_fee.index(lowest_adoption)
        highest_pokemon = pokemon_names[high_index].capitalize()
        lowest_pokemon = pokemon_names[low_index].capitalize()
        total_cost = 0
        for price in adoption_fee:
            price_location = adoption_fee.index(price)
            per_amount = float(pokemon_amounts[price_location])
            total_cost += price * per_amount
        print(f"Highest priced Pokemon: {highest_pokemon} @ ${highest_adoption:.2f} per Pokemon")
        print(f"Lowest priced Pokemon: {lowest_pokemon} @ ${lowest_adoption:.2f} per Pokemon")
        print(f"Total cost to adopt all Pokemon in the Center: ${total_cost:.2f}")

    #for invalid commands    
    else:
        print("Unknown command, please try again")
    print("")


