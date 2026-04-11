import random
import json


#function damage player
def calculate_damage_player(damage, crit_chance):
    if random.random() < crit_chance:
        print ("Нанесен критичческий урон!")
        return damage * 2
    return damage



# Функция расчета урона (с критом)
def calculate_damage_player(damage, crit_chance):
    if random.random() < crit_chance:
        print("Нанесен критический урон! ♡")
        return damage * 2
    return damage

# Функция применения урона к мобу
def damage_of_mobs(mob_id, total_damage):
    # 1. Сначала вычитаем урон
    mob_id.mob_hp -= total_damage
    
    # 2. Проверяем, осталось ли HP
    if mob_id.mob_hp <= 0:
        mob_id.mob_hp = 0
        print(f"Существо {mob_id.mob_name} получило {total_damage} урона!")
        print(f"Существо {mob_id.mob_name} было убито!")
        
        # Если лут есть, показываем его
        if mob_id.mob_loot_table != "None":
            print(f"Вы получили: {mob_id.mob_loot_table}")
    else:
        # Если моб выжил, просто пишем остаток здоровья
        print(f"Существо {mob_id.mob_name} получило {total_damage} урона!")
        print(f"У существа осталось: {mob_id.mob_hp} хп!")
