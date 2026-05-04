import engine

def run(player):
    print("\n=== ГЕРОЙ ПАЛ В БОЮ ===")

    choice = input("Загрузить последнее сохранение или выйти? (Загрузить / Выйти): ").lower().strip()

    if choice == "загрузить":
        loaded = engine.load_game()
        if loaded:
            player.__dict__.update(loaded.__dict__)
            print("Сохранение загружено!")
            return "forest"
        else:
            print("Файл сохранения не найден.")
            return None

    return None  # выход в главное меню