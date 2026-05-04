from scenes.world import forest, encounter, game_over
from scenes.ui import inventory, character_info

def play_game(hero):
    scene_map = {
    #интерфейс
    "inventory": inventory.run,
    "character_info": character_info.run,
    #мир 
    "forest": forest.run,
    "encounter": encounter.run,
    "game_over": game_over.run,
}
    current = "forest" # стартовая сцена после меню
    
    while current is not None:
        scene_func = scene_map.get(current)
        if scene_func is None:
            print(f"[Ошибка] Сцена '{current}' не найдена!")
            break
        current = scene_func(hero)