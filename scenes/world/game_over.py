import saves
from ui import ui
def run(player):
    ui.title("\n=== ГЕРОЙ ПАЛ В БОЮ ===")

    choice = ui.choose("Загрузить последнее сохранение или выйти:",[
        ("Загрузиться","load"),
        ("Выйти в главное меню","exit"),
        ])

    if choice == "load":
        loaded = saves.load_game()
        if loaded:
            player.__dict__.update(loaded.__dict__)
            ui.say("Сохранение загружено!")
            return "forest"
        else:
            ui.say("Файл сохранения не найден.")
            return None

    return None  # выход в главное меню