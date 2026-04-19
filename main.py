from player import Player
import engine
import database
# import commands_db # если не используешь - можно скрыть

def play_game(current_hero):
    print(f"\nМир Console-RPG открыт для тебя, {current_hero.player_name}!")
    
    while True: 
        cmd = input("\nЧто делаем? (Поиск | Инфо | Рюкзак | Сохранить | Меню | Выход): ").lower().strip()

        if cmd == "поиск":
            if current_hero.hp <= 0:
                print("Вы слишком слабы для боя! Сначала нужно отдохнуть или подлечиться.")
                continue
            
            target_mob = database.slime 
            target_mob.mob_hp = target_mob.mob_max_hp 
            print(f"Опа! Из-за кустов выпрыгивает {target_mob.mob_name}!")
            
            result = engine.start_battle(target_mob, current_hero)
            if result == "dead":
                print("\n--- ГЕРОЙ ПАЛ В БОЮ ---")
                # Спрашиваем игрока напрямую
                dead_choice = input("Загрузить последнее сохранение или выйти в Меню? (Загрузить / Меню): ").lower().strip()
                
                if dead_choice == "загрузить":
                    print("Загрузка...")
                    loaded_hero = engine.load_game()
                    if loaded_hero:
                        
                        current_hero.__dict__.update(loaded_hero.__dict__)
                        print("Загрузка последнего сохранения!")
                        continue # Возвращаемся в начало цикла while
                    else:
                        print("Файл сохранения не найден. Возврат в меню.")
                        return 
                else:
                    print("Возврат в главное меню...")
                    return # Выход в menu_loop
                
                
        elif cmd == "инфо":
            print(f"Имя: {current_hero.player_name} | HP: {current_hero.hp}/{current_hero.max_hp} | LVL: {current_hero.lvl_player} | Exp: {current_hero.exp_lvl_player}/{current_hero.max_exp_lvl_player}")

        elif cmd == "рюкзак":
            print(f"\n--- РЮКЗАК ---")
            if not current_hero.backpack:
                print("Там пока пусто...")
            else:
                for name, counts in current_hero.backpack.items():
                    print(f"[*] {name} — {counts} шт.")

        elif cmd == "сохранить":
            engine.save_game(current_hero)

        elif cmd == "меню":
            engine.save_game(current_hero)
            return # Выход из функции play_game обратно в menu_loop

        elif cmd == "выход":
            engine.save_game(current_hero)
            print("До встречи!")
            exit()

def menu_loop():
    print("--- ДОБРО ПОЖАЛОВАТЬ В Console-RPG ---")
    while True:
        command_menu = input("\n Новая игра | Загрузить игру | Выйти\n>Ввод: ").lower().strip()
        
        if command_menu == "новая игра":
            nickname = input('Введите Имя персонажа: ')
            hero = Player(nickname) 
            print(f"Персонаж {hero.player_name} создан!")
            play_game(hero) # Запускаем игру
            
        elif command_menu == "загрузить игру":
            print("Поиск сохранений...")
            loaded_hero = engine.load_game()
            if loaded_hero:
                play_game(loaded_hero) # Запускаем игру с загруженным героем

        elif command_menu == "выйти":
            print("До встречи!")
            break

if __name__ == "__main__":
    menu_loop()