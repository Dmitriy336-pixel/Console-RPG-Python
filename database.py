from models import Items, Weapons, Potions, Mobs, Locations


# Location - This block contains all the locations in the game.




# Items - This block contains all the items in the game.

arc_en_Ciel = Weapons("Арк_ан_Сиэль", "id:arc_en_ciel","right_hand", 1, 150)

small_healing_potion = Potions("Зелье Востановления 1", "id:small_healing_potion", "None", 10, 5)

normal_healing_potion = Potions("Зелье Востановления 2", "id:normal_healing_potion", "None", 5, 8)

big_small_healing_potion = Potions("Зелье Востановления 3", "id:big_healing_potion", "None", 3, 15)



# Mobs - This block contains all the mobs in the game.

slime = Mobs("Слизень", "id:mob_slime", 5, 2, "aggressive")
big_slime = Mobs("Большой Слизень", "id:mob_big_slime", 10, 8, "aggressive")

