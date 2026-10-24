import engine

GLOBAL_OPTIONS = [
    ("Инвентарь","inventory"),
    ("Персонаж","character_info"),
    ("Сохраниться","save"),
    ("Выйти и сохраниться","exit"),
]

def handle_global(cmd, player, current_scene):
    if cmd == "inventory":
        return "inventory"
    
    elif cmd == "character_info":
        return "character_info"
    
    elif cmd == "save":
        engine.save_game(player)
        return current_scene
    
    elif cmd == "exit":
        engine.save_game(player)
        return None
    
    return False