import engine

def handle_global(cmd, player, current_scene):
    if cmd == "рюкзак":
        return "inventory"
    
    elif cmd == "персонаж":
        return "character_info"
    
    elif cmd == "сохранить":
        engine.save_game(player)
        return current_scene
    
    elif cmd == "выйти":
        engine.save_game(player)
        return None
    
    return False