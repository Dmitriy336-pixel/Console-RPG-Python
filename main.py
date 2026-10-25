from player import Player
import saves
from scenes.manager_scenes import play_game
from ui import ui

if __name__ == "__main__":
    
    ui.title("--- ДОБРО ПОЖАЛОВАТЬ В Console-RPG ---")
    while True:
        command = ui.choose("Главное меню:",[
            ("Новая игра","new"),
            ("Загрузить сохранение","load"),
            ("Выйти","quit"),
        ], cancel_value="quit")
        
        if command == "new":
            nickname = ui.ask_text('Введите Имя персонажа: ')
            hero = Player(nickname) 
            ui.say(f"Персонаж {hero.player_name} создан!")
            play_game(hero) # Запускаем игру
            
        elif command == "load":
            ui.say("Поиск сохранений...")
            hero = saves.load_game()
            if hero:
                play_game(hero) # Запускаем игру с загруженным героем
                

        elif command == "quit":
            ui.say("До встречи!")
            break


