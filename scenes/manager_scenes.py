from scenes.menus import main_menu
from scenes.ui import inventory
from scenes.world import forest, game_over

def play_game(hero):
    scene_map = {
    "main_menu": main_menu.run,
    "inventory": inventory.run, 
    "forest": forest.run,
    "game_over": game_over.run,
}
    current = "forest"
    while current is not None:
        current = scene_map[current](hero)