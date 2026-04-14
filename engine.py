import random
import json
import models
import database

def lvl_up(player):
    if player.exp_levele_player >= player.max_exp_levele_player:
        # Вычитаем потраченный опыт, чтобы остаток пошел на следующий уровень
        player.exp_levele_player -= player.max_exp_levele_player
        
        player.lvl_player += 1
        player.max_hp += 2
        player.max_endurace += 50
        player.damage += 1
        player.defense += 1
        player.max_exp_levele_player += 50
        
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
def damage_of_mobs(mob_id, total_damage):
    # 1. Сначала вычитаем урон
    mob_id.mob_hp -= total_damage
    
    # 2. Проверяем, осталось ли HP
    if mob_id.mob_hp <= 0:
        mob_id.mob_hp = 0
        print(f"Существо {mob_id.mob_name} получило {total_damage} урона!")
        print(f"Существо {mob_id.mob_name} было убито!")
        print(f"Вы получили: {mob_id.mob_loot_exp}")
        
        # Если лут есть, показываем его
        if mob_id.mob_loot_table != "None":
            print(f"Вы получили: {mob_id.mob_loot_table}")
    else:
        # Если моб выжил, просто пишем остаток здоровья
        print(f"Существо {mob_id.mob_name} получило {total_damage} урона!")
        print(f"У существа {mob_id.mob_name} осталось: {mob_id.mob_hp} хп!")


#function damage and mob
def damage_of_player(mob_id, player):
    player.hp -= mob_id.mob_damage
    print (f"Существо {player.name} получило {mob_id.mob_damage} урона!")
    print(f"У существа {player.name} осталось: {player.hp} хп!")
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
    
    while player.hp > 0 and mob_id.mob_hp > 0:
        user_input_battle = input("Какие действия совершаем? Доступно: (Атаковать / Увернуться / Бежать): ").lower()
        
        if user_input_battle == 'атаковать':
           total_damage = calculate_damage_player(player.damage, player.crit_chance)
           damage_of_mobs(mob_id, total_damage)
           
           if mob_id.mob_hp > 0:
               damage_of_player(mob_id, player)
               
        elif user_input_battle == 'увернуться':  
            player_dodge(player, mob_id)
            
        elif user_input_battle == 'бежать':
             print("Вы сбежали!")
             return
        
        else:
            print('Неизвестное / Не доступное действие!')