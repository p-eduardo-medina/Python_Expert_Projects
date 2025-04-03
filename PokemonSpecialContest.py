#You are given data containing information for the first 
# 100 Pokémon as well as special effectiveness relationships. 
# Use this data to define a function that takes two Pokémon numbers 
# and calculates which Pokémon wins based on their types.
def pk_special_winner(pk1, pk2):
    pk_data = [ { "Number": 1, "Name": "Bulbasaur", "Type1": "grass", "Type2": "poison" }, { "Number": 2, "Name": "Ivysaur", "Type1": "grass", "Type2": "poison" }, { "Number": 3, "Name": "Venusaur", "Type1": "grass", "Type2": "poison" }, { "Number": 4, "Name": "Charmander", "Type1": "fire", "Type2": None }, { "Number": 5, "Name": "Charmeleon", "Type1": "fire", "Type2": None }, { "Number": 6, "Name": "Charizard", "Type1": "fire", "Type2": "flying" }, { "Number": 7, "Name": "Squirtle", "Type1": "water", "Type2": None }, { "Number": 8, "Name": "Wartortle", "Type1": "water", "Type2": None }, { "Number": 9, "Name": "Blastoise", "Type1": "water", "Type2": None }, { "Number": 10, "Name": "Caterpie", "Type1": "bug", "Type2": None }, { "Number": 11, "Name": "Metapod", "Type1": "bug", "Type2": None }, { "Number": 12, "Name": "Butterfree", "Type1": "bug", "Type2": "flying" }, { "Number": 13, "Name": "Weedle", "Type1": "bug", "Type2": "poison" }, { "Number": 14, "Name": "Kakuna", "Type1": "bug", "Type2": "poison" }, { "Number": 15, "Name": "Beedrill", "Type1": "bug", "Type2": "poison" }, { "Number": 16, "Name": "Pidgey", "Type1": "normal", "Type2": "flying" }, { "Number": 17, "Name": "Pidgeotto", "Type1": "normal", "Type2": "flying" }, { "Number": 18, "Name": "Pidgeot", "Type1": "normal", "Type2": "flying" }, { "Number": 19, "Name": "Rattata", "Type1": "normal", "Type2": None }, { "Number": 20, "Name": "Raticate", "Type1": "normal", "Type2": None }, { "Number": 21, "Name": "Spearow", "Type1": "normal", "Type2": "flying" }, { "Number": 22, "Name": "Fearow", "Type1": "normal", "Type2": "flying" }, { "Number": 23, "Name": "Ekans", "Type1": "poison", "Type2": None }, { "Number": 24, "Name": "Arbok", "Type1": "poison", "Type2": None }, { "Number": 25, "Name": "Pikachu", "Type1": "electric", "Type2": None }, { "Number": 26, "Name": "Raichu", "Type1": "electric", "Type2": None }, { "Number": 27, "Name": "Sandshrew", "Type1": "ground", "Type2": None }, { "Number": 28, "Name": "Sandslash", "Type1": "ground", "Type2": None }, { "Number": 29, "Name": "Nidoran", "Type1": "poison", "Type2": None }, { "Number": 30, "Name": "Nidorina", "Type1": "poison", "Type2": None }, { "Number": 31, "Name": "Nidoqueen", "Type1": "poison", "Type2": "ground" }, { "Number": 32, "Name": "Nidoran", "Type1": "poison", "Type2": None }, { "Number": 33, "Name": "Nidorino", "Type1": "poison", "Type2": None }, { "Number": 34, "Name": "Nidoking", "Type1": "poison", "Type2": "ground" }, { "Number": 35, "Name": "Clefairy", "Type1": "normal", "Type2": None }, { "Number": 36, "Name": "Clefable", "Type1": "normal", "Type2": None }, { "Number": 37, "Name": "Vulpix", "Type1": "fire", "Type2": None }, { "Number": 38, "Name": "Ninetales", "Type1": "fire", "Type2": None }, { "Number": 39, "Name": "Jigglypuff", "Type1": "normal", "Type2": None }, { "Number": 40, "Name": "Wigglytuff", "Type1": "normal", "Type2": None }, { "Number": 41, "Name": "Zubat", "Type1": "poison", "Type2": "flying" }, { "Number": 42, "Name": "Golbat", "Type1": "poison", "Type2": "flying" }, { "Number": 43, "Name": "Oddish", "Type1": "grass", "Type2": "poison" }, { "Number": 44, "Name": "Gloom", "Type1": "grass", "Type2": "poison" }, { "Number": 45, "Name": "Vileplume", "Type1": "grass", "Type2": "poison" }, { "Number": 46, "Name": "Paras", "Type1": "bug", "Type2": "grass" }, { "Number": 47, "Name": "Parasect", "Type1": "bug", "Type2": "grass" }, { "Number": 48, "Name": "Venonat", "Type1": "bug", "Type2": "poison" }, { "Number": 49, "Name": "Venomoth", "Type1": "bug", "Type2": "poison" }, { "Number": 50, "Name": "Diglett", "Type1": "ground", "Type2": None }, { "Number": 51, "Name": "Dugtrio", "Type1": "ground", "Type2": None }, { "Number": 52, "Name": "Meowth", "Type1": "normal", "Type2": None }, { "Number": 53, "Name": "Persian", "Type1": "normal", "Type2": None }, { "Number": 54, "Name": "Psyduck", "Type1": "water", "Type2": None }, { "Number": 55, "Name": "Golduck", "Type1": "water", "Type2": None }, { "Number": 56, "Name": "Mankey", "Type1": "fighting", "Type2": None }, { "Number": 57, "Name": "Primeape", "Type1": "fighting", "Type2": None }, { "Number": 58, "Name": "Growlithe", "Type1": "fire", "Type2": None }, { "Number": 59, "Name": "Arcanine", "Type1": "fire", "Type2": None }, { "Number": 60, "Name": "Poliwag", "Type1": "water", "Type2": None }, { "Number": 61, "Name": "Poliwhirl", "Type1": "water", "Type2": None }, { "Number": 62, "Name": "Poliwrath", "Type1": "water", "Type2": "fighting" }, { "Number": 63, "Name": "Abra", "Type1": "psychic", "Type2": None }, { "Number": 64, "Name": "Kadabra", "Type1": "psychic", "Type2": None }, { "Number": 65, "Name": "Alakazam", "Type1": "psychic", "Type2": None }, { "Number": 66, "Name": "Machop", "Type1": "fighting", "Type2": None }, { "Number": 67, "Name": "Machoke", "Type1": "fighting", "Type2": None }, { "Number": 68, "Name": "Machamp", "Type1": "fighting", "Type2": None }, { "Number": 69, "Name": "Bellsprout", "Type1": "grass", "Type2": "poison" }, { "Number": 70, "Name": "Weepinbell", "Type1": "grass", "Type2": "poison" }, { "Number": 71, "Name": "Victreebel", "Type1": "grass", "Type2": "poison" }, { "Number": 72, "Name": "Tentacool", "Type1": "water", "Type2": "poison" }, { "Number": 73, "Name": "Tentacruel", "Type1": "water", "Type2": "poison" }, { "Number": 74, "Name": "Geodude", "Type1": "rock", "Type2": "ground" }, { "Number": 75, "Name": "Graveler", "Type1": "rock", "Type2": "ground" }, { "Number": 76, "Name": "Golem", "Type1": "rock", "Type2": "ground" }, { "Number": 77, "Name": "Ponyta", "Type1": "fire", "Type2": None }, { "Number": 78, "Name": "Rapidash", "Type1": "fire", "Type2": None }, { "Number": 79, "Name": "Slowpoke", "Type1": "water", "Type2": "psychic" }, { "Number": 80, "Name": "Slowbro", "Type1": "water", "Type2": "psychic" }, { "Number": 81, "Name": "Magnemite", "Type1": "electric", "Type2": None }, { "Number": 82, "Name": "Magneton", "Type1": "electric", "Type2": None }, { "Number": 83, "Name": "Farfetchd", "Type1": "normal", "Type2": "flying" }, { "Number": 84, "Name": "Doduo", "Type1": "normal", "Type2": "flying" }, { "Number": 85, "Name": "Dodrio", "Type1": "normal", "Type2": "flying" }, { "Number": 86, "Name": "Seel", "Type1": "water", "Type2": None }, { "Number": 87, "Name": "Dewgong", "Type1": "water", "Type2": "ice" }, { "Number": 88, "Name": "Grimer", "Type1": "poison", "Type2": None }, { "Number": 89, "Name": "Muk", "Type1": "poison", "Type2": None }, { "Number": 90, "Name": "Shellder", "Type1": "water", "Type2": None }, { "Number": 91, "Name": "Cloyster", "Type1": "water", "Type2": "ice" }, { "Number": 92, "Name": "Gastly", "Type1": "ghost", "Type2": "poison" }, { "Number": 93, "Name": "Haunter", "Type1": "ghost", "Type2": "poison" }, { "Number": 94, "Name": "Gengar", "Type1": "ghost", "Type2": "poison" }, { "Number": 95, "Name": "Onix", "Type1": "rock", "Type2": "ground" }, { "Number": 96, "Name": "Drowzee", "Type1": "psychic", "Type2": None }, { "Number": 97, "Name": "Hypno", "Type1": "psychic", "Type2": None }, { "Number": 98, "Name": "Krabby", "Type1": "water", "Type2": None }, { "Number": 99, "Name": "Kingler", "Type1": "water", "Type2": None }, { "Number": 100, "Name": "Voltorb", "Type1": "electric", "Type2": None } ]
    type_effectiveness = {'bug': {'bug': 1, 'electric': 1, 'fighting': 0.5, 'fire': 0.5, 'flying': 0.5, 'ghost': 0.5, 'grass': 2, 'ground': 1, 'ice': 1, 'normal': 1, 'poison': 0.5, 'psychic': 2, 'rock': 1, 'water': 1}, 'electric': {'bug': 1, 'electric': 0.5, 'fighting': 1, 'fire': 1, 'flying': 2, 'ghost': 1, 'grass': 0.5, 'ground': 0, 'ice': 1, 'normal': 1, 'poison': 1, 'psychic': 1, 'rock': 1, 'water': 2}, 'fighting': {'bug': 0.5, 'electric': 1, 'fighting': 1, 'fire': 1, 'flying': 0.5, 'ghost': 0, 'grass': 1, 'ground': 1, 'ice': 2, 'normal': 2, 'poison': 0.5, 'psychic': 0.5, 'rock': 2, 'water': 1}, 'fire': {'bug': 2, 'electric': 1, 'fighting': 1, 'fire': 0.5, 'flying': 1, 'ghost': 1, 'grass': 2, 'ground': 1, 'ice': 2, 'normal': 1, 'poison': 1, 'psychic': 1, 'rock': 0.5, 'water': 0.5}, 'flying': {'bug': 2, 'electric': 0.5, 'fighting': 2, 'fire': 1, 'flying': 1, 'ghost': 1, 'grass': 2, 'ground': 1, 'ice': 1, 'normal': 1, 'poison': 1, 'psychic': 1, 'rock': 0.5, 'water': 1}, 'ghost': {'bug': 1, 'electric': 1, 'fighting': 1, 'fire': 1, 'flying': 1, 'ghost': 2, 'grass': 1, 'ground': 1, 'ice': 1, 'normal': 0, 'poison': 1, 'psychic': 2, 'rock': 1, 'water': 1}, 'grass': {'bug': 0.5, 'electric': 1, 'fighting': 1, 'fire': 0.5, 'flying': 0.5, 'ghost': 1, 'grass': 0.5, 'ground': 2, 'ice': 1, 'normal': 1, 'poison': 0.5, 'psychic': 1, 'rock': 2, 'water': 2}, 'ground': {'bug': 0.5, 'electric': 2, 'fighting': 1, 'fire': 2, 'flying': 0, 'ghost': 1, 'grass': 0.5, 'ground': 1, 'ice': 1, 'normal': 1, 'poison': 2, 'psychic': 1, 'rock': 2, 'water': 1}, 'ice': {'bug': 1, 'electric': 1, 'fighting': 1, 'fire': 0.5, 'flying': 2, 'ghost': 1, 'grass': 2, 'ground': 2, 'ice': 0.5, 'normal': 1, 'poison': 1, 'psychic': 1, 'rock': 1, 'water': 0.5}, 'normal': {'bug': 1, 'electric': 1, 'fighting': 1, 'fire': 1, 'flying': 1, 'ghost': 0, 'grass': 1, 'ground': 1, 'ice': 1, 'normal': 1, 'poison': 1, 'psychic': 1, 'rock': 0.5, 'water': 1}, 'poison': {'bug': 1, 'electric': 1, 'fighting': 1, 'fire': 1, 'flying': 1, 'ghost': 0.5, 'grass': 2, 'ground': 0.5, 'ice': 1, 'normal': 1, 'poison': 0.5, 'psychic': 1, 'rock': 0.5, 'water': 1}, 'psychic': {'bug': 1, 'electric': 1, 'fighting': 2, 'fire': 1, 'flying': 1, 'ghost': 1, 'grass': 1, 'ground': 1, 'ice': 1, 'normal': 1, 'poison': 2, 'psychic': 0.5, 'rock': 1, 'water': 1}, 'rock': {'bug': 2, 'electric': 1, 'fighting': 0.5, 'fire': 2, 'flying': 2, 'ghost': 1, 'grass': 1, 'ground': 0.5, 'ice': 2, 'normal': 1, 'poison': 1, 'psychic': 1, 'rock': 1, 'water': 1}, 'water': {'bug': 1, 'electric': 1, 'fighting': 1, 'fire': 2, 'flying': 1, 'ghost': 1, 'grass': 0.5, 'ground': 2, 'ice': 1, 'normal': 1, 'poison': 1, 'psychic': 1, 'rock': 2, 'water': 0.5}}
    pokemons = [pk_data[pk1-1],pk_data[pk2-1]]
    values = []
    for k in [0,1]:
        attackValue = 0
        for i in [1,2]:
            attackType = pokemons[k]["Type"+str(i)]
            if attackType is not None:
                for j in [1,2]:
                    attackedType = pokemons[int(not(bool(k)))]["Type"+str(j)]
                    if attackedType is not None:  
                        attackValue+=type_effectiveness[attackType][attackedType]
        values.append(attackValue)
    if values[0]==values[1]:
        return -1
    else:
        index = values.index(max(values))
        return pokemons[index]["Number"]
    
    
        
print(pk_special_winner(4, 14) == 4)
print(pk_special_winner(71, 54) == 71)
print(pk_special_winner(43, 44) == -1)
print(pk_special_winner(83, 33) == -1)
print(pk_special_winner(41, 45) == 41)
print(pk_special_winner(5, 80) == 80)
print(pk_special_winner(92, 51) == 51)
print(pk_special_winner(27, 12) == 12)
print(pk_special_winner(18, 72) == -1)
print(pk_special_winner(17, 7) == -1)
print(pk_special_winner(68, 6) == 6)
print(pk_special_winner(60, 97) == -1)
print(pk_special_winner(63, 74) == -1)
print(pk_special_winner(81, 30) == -1)
print(pk_special_winner(49, 37) == 37)
print(pk_special_winner(24, 76) == 76)
print(pk_special_winner(91, 82) == 82)
print(pk_special_winner(34, 68) == 34)
print(pk_special_winner(63, 51) == -1)
print(pk_special_winner(90, 17) == -1)
print(pk_special_winner(61, 65) == -1)
print(pk_special_winner(31, 40) == -1)
print(pk_special_winner(20, 3) == -1)
print(pk_special_winner(58, 69) == 58)
print(pk_special_winner(87, 65) == -1)
print(pk_special_winner(92, 47) == 92)
print(pk_special_winner(71, 66) == 71)
print(pk_special_winner(9, 62) == -1)
print(pk_special_winner(85, 17) == -1)
print(pk_special_winner(1, 33) == 33)
print(pk_special_winner(12, 13) == 12)
print(pk_special_winner(52, 9) == -1)
print(pk_special_winner(87, 14) == -1)
print(pk_special_winner(33, 28) == 28)
print(pk_special_winner(77, 52) == -1)
print(pk_special_winner(19, 78) == -1)
print(pk_special_winner(24, 89) == -1)
print(pk_special_winner(72, 99) == -1)
print(pk_special_winner(77, 18) == -1)
print(pk_special_winner(25, 44) == 44)
print(pk_special_winner(57, 51) == -1)
print(pk_special_winner(60, 22) == -1)
print(pk_special_winner(36, 65) == -1)
print(pk_special_winner(98, 34) == 98)
print(pk_special_winner(26, 12) == 26)
print(pk_special_winner(51, 56) == -1)
print(pk_special_winner(59, 94) == -1)
print(pk_special_winner(70, 44) == -1)
print(pk_special_winner(67, 13) == 13)
print(pk_special_winner(31, 33) == 31)
print(pk_special_winner(37, 85) == -1)
print(pk_special_winner(3, 86) == 3)
print(pk_special_winner(96, 71) == 96)
print(pk_special_winner(93, 34) == 34)
print(pk_special_winner(63, 99) == -1)
print(pk_special_winner(69, 65) == 65)
print(pk_special_winner(41, 8) == -1)
print(pk_special_winner(13, 53) == -1)
print(pk_special_winner(84, 35) == -1)
print(pk_special_winner(73, 70) == -1)
print(pk_special_winner(84, 70) == 84)
print(pk_special_winner(72, 14) == 72)
print(pk_special_winner(74, 22) == 74)
print(pk_special_winner(61, 90) == -1)
print(pk_special_winner(6, 46) == 6)
print(pk_special_winner(58, 77) == -1)
print(pk_special_winner(39, 46) == -1)
print(pk_special_winner(79, 20) == -1)
print(pk_special_winner(72, 68) == 72)
print(pk_special_winner(80, 98) == -1)
print(pk_special_winner(42, 97) == 97)
print(pk_special_winner(26, 19) == -1)
print(pk_special_winner(65, 35) == -1)
print(pk_special_winner(12, 65) == 12)
print(pk_special_winner(35, 49) == -1)
print(pk_special_winner(58, 89) == -1)
print(pk_special_winner(18, 67) == 18)
print(pk_special_winner(75, 69) == 69)
print(pk_special_winner(2, 4) == 4)
print(pk_special_winner(83, 49) == 83)
print(pk_special_winner(11, 57) == -1)
print(pk_special_winner(56, 87) == 56)
print(pk_special_winner(33, 17) == -1)
print(pk_special_winner(79, 96) == -1)
print(pk_special_winner(33, 4) == -1)
print(pk_special_winner(80, 77) == 80)
print(pk_special_winner(52, 57) == 57)
print(pk_special_winner(68, 26) == -1)
print(pk_special_winner(9, 38) == 9)
print(pk_special_winner(99, 42) == -1)
print(pk_special_winner(61, 86) == -1)
print(pk_special_winner(51, 22) == 22)
print(pk_special_winner(21, 77) == -1)
print(pk_special_winner(32, 26) == -1)
print(pk_special_winner(73, 47) == 73)
print(pk_special_winner(29, 92) == 92)
print(pk_special_winner(7, 37) == 7)
print(pk_special_winner(12, 63) == 12)
print(pk_special_winner(53, 88) == -1)
print(pk_special_winner(34, 60) == 60)