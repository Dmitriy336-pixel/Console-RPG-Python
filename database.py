from models import Items, Weapons, Potions, Mobs


# Location - This block contains all the locations in the game.




# Items - This block contains all the items in the game.

Arc_en_Ciel = Weapons("Арк_ан_Сиэль", "id:arc_en_ciel", 1, "right_hand", 150)

small_healing_potion = Potions("Зелье Востановления 1", "id:small_healing_potion", 10, None, 5)

normal_healing_potion = Potions("Зелье Востановления 2", "id:normal_healing_potion", 5, None, 8)

big_healing_potion = Potions("Зелье Востановления 3", "id:big_healing_potion", 3, None, 15)



# Mobs - This block contains all the mobs in the game.

slime = Mobs("Слизень", "id:mob_slime", 5, 5, 2, "aggressive", ["id:small_healing_potion"], 3)
big_slime = Mobs("Большой Слизень", "id:mob_big_slime", 10, 10, 8, "aggressive", None, 15)

# Реестр мобов: связываем строковый ID с реальным объектом
mobs_registry = {
    "id:mob_slime": slime,
    "id:mob_big_slime": big_slime
}

# Реестр предметов: чтобы по ID узнавать имя и статы
items_registry = {
    "id:small_healing_potion": small_healing_potion,
    "id:normal_healing_potion": normal_healing_potion,
    "id:big_healing_potion": big_healing_potion,
    "id:arc_en_ciel": Arc_en_Ciel,
}