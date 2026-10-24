import engine
import database
import random
from ui import ui
location_mobs = {
    "forest": database.forest_mobs
}

def run(player):
    ui.title("\n=== ВСТРЕЧА ===")

    mobs = location_mobs.get(player.current_location, database.forest_mobs)
    mob = database.pick_mob("forest")
    

    ui.say(f"Из-за кустов выпрыгивает {mob.mob_name}!")

    result = engine.start_battle(mob, player)

    if result == "win":
        ui.say("Ты победил! Возвращаешься в лес.")
        return "forest"

    elif result == "fled":
        ui.say("Ты сбежал обратно в лес.")
        return "forest"

    elif result == "dead":
        return "game_over"