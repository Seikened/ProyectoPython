from poketload import get_all_pokemons
from pprint import pprint
import random






#/2 profile =

#/2 Esto va a genrar una lista en la cual nos genera 3 iteraciones y a cada iretaración se va a ejecutar este codigo "random.randing(len(pokemon_list))"  y esto sera el contenido de la lista final
                                                                                    #/2 Aqui nos hemos ahoprrado esta linea de codigo                                                                                 
                                                                                    #/2  for a in range(3):
                                                                                    #/2      profile["pokemon_inventory"].append(random.randing(len(pokemon_list)))
        

def get_player_profile(pokemon_list):
    
    return  { 
        "player_name": input("¿Cual es tu nombre? "),
        "pokemon_inventory": [random.choice(pokemon_list) for a in range(3)], 
        "combats":0,
        "pokeballs": 0,
        "heat_potion": 0,
    }                                                                               

                                                                                    
def any_player_pokemon_lives(player_profile):
   return sum( [pokemon["current_health"] for pokemon in player_profile["pokemon_inventory"]]) > 0 # Si la suma de todas las vidas de los pokemon es mayor a 0 devolvera un True si no un False


def fight(player_profile,enemy_pokemon):
    #ENEMY POKEMON
    select_attack = random.choice(enemy_pokemon["attacks"])
    ##Min_Level
    if select_attack["min_livel"] > enemy_pokemon["level"]:
        select_attack = random.choice(enemy_pokemon["attacks"])
    enemy_damage = select_attack["damage"]
    enemy_name_attack = select_attack["name"]
    enemy_type_attack = select_attack["type"]
    ####################################################################












def main():
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)
    pprint(player_profile)

    while any_player_pokemon_lives(player_profile):
        enemy_pokemon = random.choice(pokemon_list)
        fight(player_profile,enemy_pokemon)
        
    print("Has perdido en el combate numero {}".format(player_profile["combats"]))

if __name__ == "__main__":
    main()




