import json

# List of Pokémon
pokemons = [
    {
        "name": {
            "english": "Pikachu"
        },
        "type": [
            "Electric"
        ],
        "base": {
            "HP": 35,
            "Attack": 55,
            "Defense": 40,
            "Sp. Attack": 50,
            "Sp. Defense": 50,
            "Speed": 90
        }
    },
    {
        "name": {
            "english": "Charmander"
        },
        "type": [
            "Fire"
        ],
        "base": {
            "HP": 39,
            "Attack": 52,
            "Defense": 43,
            "Sp. Attack": 60,
            "Sp. Defense": 50,
            "Speed": 65
        }
    },
    {
        "name": {
            "english": "Squirtle"
        },
        "type": [
            "Water"
        ],
        "base": {
            "HP": 44,
            "Attack": 48,
            "Defense": 65,
            "Sp. Attack": 50,
            "Sp. Defense": 64,
            "Speed": 43
        }
    },
]

def pokemon_data_information(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print('The file does not exist.')
        return []

def save_pokemon_info(file_path, pokemon_data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(pokemon_data, file, indent=4)

def add_new_pokemon(file_path):

    pokemon_data = pokemon_data_information(file_path)


    name = input("Please enter the name of your Pokémon: ")
    type_ = input("What is the type of the Pokémon? ")
    hp = int(input("Please enter the HP: "))
    attack = int(input("Could you please let me know the attack of the new Pokémon? "))
    defense = int(input("What is the defense value? "))
    sp_attack = int(input("Please enter the special attack value: "))
    sp_defense = int(input("Please enter the special defense value: "))
    speed = int(input("What is the speed of your Pokémon? "))



    new_pokemon = {
        "name": {
            "english": name
        },
        "type": [type_],
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed
        }
    }


    pokemon_data.append(new_pokemon)


    save_pokemon_info(file_path, pokemon_data)

    print(f"The new Pokémon {name} has been added to the data based.")


file_path = 'pokemons.json'


add_new_pokemon(file_path)
