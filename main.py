from player import Player
import engine
from scenes.manager_scenes import play_game


if __name__ == "__main__":
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
            hero = engine.load_game()
            if hero:
                play_game(hero) # Запускаем игру с загруженным героем

        elif command_menu == "выйти":
            print("До встречи!")
            break


