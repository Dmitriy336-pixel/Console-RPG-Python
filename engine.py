import random
import json
import models
import database
import player
import os
from ui import ui



def lvl_up(player):
    if player.exp_lvl_player >= player.max_exp_lvl_player:
        # Вычитаем потраченный опыт, чтобы остаток пошел на следующий уровень
        player.exp_lvl_player -= player.max_exp_lvl_player
        
        player.lvl_player += 1
        player.max_hp += 2
        player.max_endurance += 50
        player.damage += 1
        player.defense += 1
        player.max_exp_lvl_player += 50
        
        # Полное исцеление при повышении уровня (по желанию)
        player.hp = player.max_hp
        player.endurance = player.max_endurance
        
        ui.title(f"--- УРОВЕНЬ ПОВЫШЕН! Теперь у вас {player.lvl_player} лвл ---")
        

#function damage and player
def calculate_damage_player(damage, crit_chance):
    if random.random() < crit_chance:
        ui.say ("Нанесен критичческий урон!")
        return damage * 2
    return damage



# Функция применения урона к мобу
def damage_of_mobs(mob_id, total_damage, player):
    # 1. Сначала вычитаем урон
    mob_id.mob_hp -= total_damage
    
    # 2. Проверяем, осталось ли HP
    if mob_id.mob_hp <= 0:
        mob_id.mob_hp = 0
        ui.say(f"Существо {mob_id.mob_name} получило {total_damage} урона!")
        ui.say(f"Существо {mob_id.mob_name} было убито!")
        ui.say(f"Вы получили: {mob_id.mob_loot_exp} опыта!")
        player.exp_lvl_player += mob_id.mob_loot_exp 
        lvl_up(player)
        
        # Если лут есть, показываем его
        drops = roll_loot(mob_id)
        if drops:
            names = ", ".join(f"{database.item_name(i)} x{n}" for i, n in drops.items())
            ui.say(f"Вы получили: {names}")
            for item_id, n in drops.items():
                add_items_backpack(player, item_id, n)

                
    else:
        # Если моб выжил, просто пишем остаток здоровья
        ui.say(f"Существо {mob_id.mob_name} получило {total_damage} урона!")
        ui.say(f"У существа {mob_id.mob_name} осталось: {mob_id.mob_hp} хп!")


#function damage and mob
def damage_of_player(mob_id, player):
    player.hp -= mob_id.mob_damage
    ui.say (f"Существо {player.player_name} получило {mob_id.mob_damage} урона!")
    ui.say(f"У существа {player.player_name} осталось: {player.hp} хп!")
    if player.hp <= 0:
        player.hp = 0
        ui.say ("вы погибли!")
        
        
def player_dodge(player, mob_id):
   damage_taken = int(mob_id.mob_damage * 0.50)
   player.hp = max(0, player.hp - damage_taken)
   ui.say (f"Вы увернулись и получили {damage_taken} Урона!")
    
    

        
def start_battle(mob_id, player):
    mob_id.mob_hp = mob_id.mob_max_hp
    ui.title(f"--- Начался бой с {mob_id.mob_name}! ---")
    
    # Этот цикл крутится ДО ТЕХ ПОР, пока оба живы
    while player.hp > 0 and mob_id.mob_hp > 0:
        command = ui.choose("Ваши действия:",[
            ("Атаковать","attack"),
            ("Увернуться","dodge"),
            ("Пытаться сбежать","run"),
            ],cancel_value="quit")
        
        if command == 'attack':
            total_damage = calculate_damage_player(player.damage, player.crit_chance)
            damage_of_mobs(mob_id, total_damage, player)
            
            # Проверяем: если моб УЖЕ умер после нашей атаки, 
            # мы НЕ даем ему бить в ответ и выходим из цикла
            if mob_id.mob_hp <= 0:
                break 
                
            damage_of_player(mob_id, player)
               
        elif command == 'dodge':  
            player_dodge(player, mob_id)
            
        elif command == 'run':
            ui.say("Вы сбежали!")
            return "fled" # Тут return уместен, так как мы прерываем бой
    

    # --- ВАЖНО: ЭТОТ БЛОК ДОЛЖЕН БЫТЬ ВНЕ WHILE ---
    # Видишь? Он стоит на одном уровне с 'while', а не внутри него.
    if player.hp <= 0:
        return "dead"
    else:
        return "win"

    
def remove_item_backpack(player, item_id, count=1):
    if player.backpack.get(item_id, 0) < count:
        return False
    player.backpack[item_id] -= count
    if player.backpack[item_id] <= 0:
        del player.backpack[item_id]   # пустую запись убираем, иначе в списке будет "0 шт."
    return True

def add_items_backpack(player, item_id, count=1):
    player.backpack[item_id] = player.backpack.get(item_id, 0) + count

def use_potion(player, item_id):
    item = database.items_registry[item_id]
    if player.hp >= player.max_hp:
        ui.say("Здоровье уже полное.")
        return
    remove_item_backpack(player, item_id)
    before = player.hp
    player.hp = min(player.max_hp, player.hp + item.item_heal_value)
    ui.say(f"Выпито: {item.item_name}. +{player.hp - before} HP")
        
        

    

def roll_loot(mob):
    """Бросает кубик по таблице лута. Возвращает {id предмета: количество}."""
    drops = {}
    for entry in mob.mob_loot_table:
        if random.random() < entry.get("chance", 1.0):
            count = random.randint(entry.get("min", 1), entry.get("max", 1))
            drops[entry["item"]] = drops.get(entry["item"], 0) + count
    return drops

    
    
def save_game(player_obj):
    data = player_obj.to_dict()
    with open("player_save.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        ui.say("Прогресс успешно сохранен!")
     
def load_game():
    
    # Проверяем, существует ли файл И не пустой ли он
    if not os.path.exists("player_save.json") or os.path.getsize("player_save.json") == 0:
        ui.say("Файл сохранений пуст или отсутствует.")
        return None
    
    try:
        with open("player_save.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            
            new_hero = player.Player(data["name"])
            new_hero.hp = data["hp"]
            new_hero.max_hp = data["max_hp"]
            new_hero.endurance = data["endurance"]
            new_hero.max_endurance = data["max_endurance"]
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
            new_hero.current_location = data["current_location"]
            return new_hero
    except json.JSONDecodeError:
        ui.say("Ошибка: Файл сохранения поврежден!")
        return None
    except Exception as e:
        ui.say(f"Непредвиденная ошибка при загрузке: {e}")
        return None