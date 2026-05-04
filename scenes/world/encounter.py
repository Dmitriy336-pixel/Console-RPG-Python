import engine
import database
import random
def run(player):
    print("\n=== ВСТРЕЧА ===")

    possible_mobs = [
        database.slime,
        database.big_slime,
    ]

    mob = random.choice(possible_mobs)
    mob.mob_hp = mob.mob_max_hp
    print(f"Из-за кустов выпрыгивает {mob.mob_name}!")

    result = engine.start_battle(mob, player)

    if result == "win":
        print("Ты победил! Возвращаешься в лес.")
        return "forest"

    elif result == "fled":
        print("Ты сбежал обратно в лес.")
        return "forest"

    elif result == "dead":
        return "game_over"
