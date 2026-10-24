from scenes.ui.actions import handle_global, GLOBAL_OPTIONS
from ui import ui


def run(player):
    ui.title("ЛЕС")
    ui.say(f"HP: {player.hp}/{player.max_hp} | LVL: {player.lvl_player} | EXP: {player.exp_lvl_player}/{player.max_exp_lvl_player}")

    while True:
        cmd = ui.choose("Что делаем?", [("Поиск", "search")] + GLOBAL_OPTIONS)
        if not cmd:  # Ctrl+C: просто остаёмся в лесу
            continue

        result = handle_global(cmd, player, "forest")
        if result is not False:
            return result

        if cmd == "search":
            if player.hp <= 0:
                ui.say("Вы слишком слабы! Сначала отдохните.")
                continue
            return "encounter"