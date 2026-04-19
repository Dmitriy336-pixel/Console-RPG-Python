import random
import json
import models
import database
import player



def lvl_up(player):
    if player.exp_lvl_player >= player.max_exp_lvl_player:
        # Вычитаем потраченный опыт, чтобы остаток пошел на следующий уровень
        player.exp_lvl_player -= player.max_exp_lvl_player
        
        player.lvl_player += 1
        player.max_hp += 2
        player.max_endurace += 50
        player.damage += 1
        player.defense += 1
        player.max_exp_lvl_player += 50
        
        # Полное исцеление при повышении уровня (по желанию)
        player.hp = player.max_hp
        player.endurace = player.max_endurace
        
        print(f"--- УРОВЕНЬ ПОВЫШЕН! Теперь у вас {player.lvl_player} лвл ---")
        

#function damage and player
def calculate_damage_player(damage, crit_chance):
    if random.random() < crit_chance:
        print ("Нанесен критичческий урон!")
        return damage * 2
    return damage



# Функция применения урона к мобу
def damage_of_mobs(mob_id, total_damage, player):
    # 1. Сначала вычитаем урон
    mob_id.mob_hp -= total_damage
    
    # 2. Проверяем, осталось ли HP
    if mob_id.mob_hp <= 0:
        mob_id.mob_hp = 0
        print(f"Существо {mob_id.mob_name} получило {total_damage} урона!")
        print(f"Существо {mob_id.mob_name} было убито!")
        print(f"Вы получили: {mob_id.mob_loot_exp} опыта!")
        player.exp_lvl_player += mob_id.mob_loot_exp 
        lvl_up(player)
        
        # Если лут есть, показываем его
        if mob_id.mob_loot_table != "None":
            print(f"Вы получили: {mob_id.mob_loot_table}")
            for item in mob_id.mob_loot_table:
    # Вызываем функцию, которую мы написали для словаря
                add_items_backpack(player, item)
    else:
        # Если моб выжил, просто пишем остаток здоровья
        print(f"Существо {mob_id.mob_name} получило {total_damage} урона!")
        print(f"У существа {mob_id.mob_name} осталось: {mob_id.mob_hp} хп!")


#function damage and mob
def damage_of_player(mob_id, player):
    player.hp -= mob_id.mob_damage
    print (f"Существо {player.player_name} получило {mob_id.mob_damage} урона!")
    print(f"У существа {player.player_name} осталось: {player.hp} хп!")
    if player.hp <= 0:
        player.hp = 0
        print ("вы погибли!")
        
        
def player_dodge(player, mob_id):
   damage_taken = int(mob_id.mob_damage * 0.50)
   player.hp -= damage_taken
   print (f"Вы увернулись и получили {damage_taken} Урона!")
    
    
        
        
def start_battle(mob_id, player):
    mob_id.mob_hp = mob_id.mob_max_hp
    print(f"--- Начался бой с {mob_id.mob_name}! ---")
    
    # Этот цикл крутится ДО ТЕХ ПОР, пока оба живы
    while player.hp > 0 and mob_id.mob_hp > 0:
        user_input_battle = input("Действие (Атаковать / Увернуться / Бежать): ").lower().strip()
        
        if user_input_battle == 'атаковать':
            total_damage = calculate_damage_player(player.damage, player.crit_chance)
            damage_of_mobs(mob_id, total_damage, player)
            
            # Проверяем: если моб УЖЕ умер после нашей атаки, 
            # мы НЕ даем ему бить в ответ и выходим из цикла
            if mob_id.mob_hp <= 0:
                break 
                
            damage_of_player(mob_id, player)
               
        elif user_input_battle == 'увернуться':  
            player_dodge(player, mob_id)
            
        elif user_input_battle == 'бежать':
            print("Вы сбежали!")
            return "fled" # Тут return уместен, так как мы прерываем бой
    
        else:
            print('Неизвестное действие!')

    # --- ВАЖНО: ЭТОТ БЛОК ДОЛЖЕН БЫТЬ ВНЕ WHILE ---
    # Видишь? Он стоит на одном уровне с 'while', а не внутри него.
    if player.hp <= 0:
        return "dead"
    else:
        return "win"

    
def add_items_backpack(player, item_id):
    if item_id in player.backpack:
        player.backpack [item_id] += 1
    else:
        player.backpack [item_id] = 1
        
        
def reward_player(player, mob_id):
    loot_list = mob_id.mob_loot_table
    for item in loot_list:
        add_items_backpack(player, item)
    
    
def save_game(player_obj):
    data = player_obj.to_dict()
    with open("player_save.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        print("Прогресс успешно сохранен!")
     
def load_game():
    import os
    # Проверяем, существует ли файл И не пустой ли он
    if not os.path.exists("player_save.json") or os.path.getsize("player_save.json") == 0:
        print("Файл сохранений пуст или отсутствует.")
        return None
    
    try:
        with open("player_save.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            
            new_hero = player.Player(data["name"])
            new_hero.hp = data["hp"]
            new_hero.max_hp = data["max_hp"]
            new_hero.endurance = data["endurance"]
            new_hero.max_endurace = data["max_endurace"]
            new_hero.max_mana = data["max_mana"]
            new_hero.mana = data["mana"]
            new_hero.lvl_mana = data["lvl_mana"]
            new_hero.exp_mana = data["exp_mana"]
            new_hero.max_exp_mana = data["max_exp_mana"]
            new_hero.damage = data["damage"]
            new_hero.crit_chance = data["crit_chance"]
            new_hero.defense = data["defense"]
            new_hero.lvl_player = data["lvl_player"]
            new_hero.exp_lvl_player = data["exp_lvl_player"]
            new_hero.max_exp_lvl_player = data["max_exp_lvl_player"]
            new_hero.equipment = data["equipment"]
            new_hero.spells = data["spells"]
            new_hero.skills = data["skills"]
            new_hero.backpack = data["backpack"]
            new_hero.inventory = data["inventory"]
            return new_hero
    except json.JSONDecodeError:
        print("Ошибка: Файл сохранения поврежден!")
        return None
    except Exception as e:
        print(f"Непредвиденная ошибка при загрузке: {e}")
        return None