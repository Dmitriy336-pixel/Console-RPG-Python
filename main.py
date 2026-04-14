from player import Player
import engine
import database


def menu_loop():
    print("--- ДОБРО ПОЖАЛОВАТЬ В Console-RPG ---")
    
    while True:
        
        command_menu = input("\n Новая игра | Загрузить игру | Выйти\n>Ввод: ").lower().strip()
        
        if command_menu == "новая игра":
            nickname = input('Введите Имя персонажа: ')
            
            # Передаем nickname прямо в скобки!
            hero = Player(nickname) 
            
            print("Создание персонажа...")
            print(f"Персонаж {hero.player_name} создан!")
            return hero
         
        elif command_menu == "загрузить игру":
            print("Поиск сохранений...")
            
            pass
        elif command_menu == "выйти":
            print("До встречи!")
            exit()
        else:
            print("Команда не распознана. Повторите попытку.")
if __name__ == "__main__":
    # Запускаем меню и сохраняем созданного героя в переменную
    current_hero = menu_loop()
    
    # Теперь, когда герой у нас есть, запускаем основной цикл игры
    print(f"\nМир Console-RPG открыт для тебя, {current_hero.player_name}!")
    
    while True:
        cmd = input("\nЧто делаем? (Поиск / Инфо / Выход): ").lower().strip()
        
        if cmd == "поиск":
           pass
       
        elif cmd == "инфо":
            print(f"Имя: {current_hero.player_name} | HP: {current_hero.hp}")
            
        elif cmd == "выход":
            print("Сохранение (в разработке) и выход...")
            break