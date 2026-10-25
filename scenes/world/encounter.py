
import database
import random
from ui import ui
from logic import battle_logic


def run(player):
    ui.title("\n=== ВСТРЕЧА ===")

    
    mob = database.pick_mob(player.current_location)
    

    ui.say(f"Из-за кустов выпрыгивает {mob.mob_name}!")

    result = battle_logic.start_battle(mob, player)

    if result == "win":
        ui.say("Ты победил! Возвращаешься в лес.")
        return "forest"

    elif result == "fled":
        ui.say("Ты сбежал обратно в лес.")
        return "forest"

    elif result == "dead":
        return "game_over"