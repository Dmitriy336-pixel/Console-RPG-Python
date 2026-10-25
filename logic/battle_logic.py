import random
import database
from logic import inventory_main_logic, leveling
from ui import ui



#function damage and player
def calculate_damage_player(damage, crit_chance):
    if random.random() < crit_chance:
        ui.say ("Нанесен критичческий урон!")
        return damage * 2
    return damage




# Функция применения урона к мобу
def damage_of_mobs(mob, total_damage, player):
    # 1. Сначала вычитаем урон
    mob.mob_hp -= total_damage
    
    # 2. Проверяем, осталось ли HP
    if mob.mob_hp <= 0:
        mob.mob_hp = 0
        ui.say(f"Существо {mob.mob_name} получило {total_damage} урона!")
        ui.say(f"Существо {mob.mob_name} было убито!")
        ui.say(f"Вы получили: {mob.mob_loot_exp} опыта!")
        player.exp_lvl_player += mob.mob_loot_exp 
        leveling.lvl_up(player)
        
        # Если лут есть, показываем его
        drops = roll_loot(mob)
        if drops:
            names = ", ".join(f"{database.item_name(i)} x{n}" for i, n in drops.items())
            ui.say(f"Вы получили: {names}")
            for item_id, n in drops.items():
                inventory_main_logic.add_items_backpack(player, item_id, n)

                
    else:
        # Если моб выжил, просто пишем остаток здоровья
        ui.say(f"Существо {mob.mob_name} получило {total_damage} урона!")
        ui.say(f"У существа {mob.mob_name} осталось: {mob.mob_hp} хп!")


#function damage and mob
def damage_of_player(mob, player):
    player.hp -= mob.mob_damage
    ui.say (f"Существо {player.player_name} получило {mob.mob_damage} урона!")
    ui.say(f"У существа {player.player_name} осталось: {player.hp} хп!")
    if player.hp <= 0:
        player.hp = 0
        ui.say ("вы погибли!")
        
        
def player_dodge(player, mob):
   damage_taken = int(mob.mob_damage * 0.50)
   player.hp = max(0, player.hp - damage_taken)
   ui.say (f"Вы увернулись и получили {damage_taken} Урона!")
    
    

        
def start_battle(mob, player):
    mob.mob_hp = mob.mob_max_hp
    ui.title(f"--- Начался бой с {mob.mob_name}! ---")
    
    # Этот цикл крутится ДО ТЕХ ПОР, пока оба живы
    while player.hp > 0 and mob.mob_hp > 0:
        command = ui.choose("Ваши действия:",[
            ("Атаковать","attack"),
            ("Увернуться","dodge"),
            ("Пытаться сбежать","run"),
            ],cancel_value="quit")
        
        if command == 'attack':
            total_damage = calculate_damage_player(player.damage, player.crit_chance)
            damage_of_mobs(mob, total_damage, player)
            
            # Проверяем: если моб УЖЕ умер после нашей атаки, 
            # мы НЕ даем ему бить в ответ и выходим из цикла
            if mob.mob_hp <= 0:
                break 
                
            damage_of_player(mob, player)
               
        elif command == 'dodge':  
            player_dodge(player, mob)
            
        elif command == 'run':
            ui.say("Вы сбежали!")
            return "fled" # Тут return уместен, так как мы прерываем бой
    

    # --- ВАЖНО: ЭТОТ БЛОК ДОЛЖЕН БЫТЬ ВНЕ WHILE ---
    # Видишь? Он стоит на одном уровне с 'while', а не внутри него.
    if player.hp <= 0:
        return "dead"
    else:
        return "win"

    

    

def roll_loot(mob):
    """Бросает кубик по таблице лута. Возвращает {id предмета: количество}."""
    drops = {}
    for entry in mob.mob_loot_table:
        if random.random() < entry.get("chance", 1.0):
            count = random.randint(entry.get("min", 1), entry.get("max", 1))
            drops[entry["item"]] = drops.get(entry["item"], 0) + count
    return drops
