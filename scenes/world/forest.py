import engine
from scenes.ui.actions import handle_global


def run(player):
    print(f"\n=== ЛЕС ===")
    print(f"HP: {player.hp}/{player.max_hp} | LVL: {player.lvl_player} | EXP: {player.exp_lvl_player}/{player.max_exp_lvl_player}")

    while True:
        cmd = input("\nЧто делаем? (Поиск | Персонаж | Рюкзак | Сохранить | Выход): ").lower().strip()
        result = handle_global(cmd, player, "forest")
        if result is not False:
            return result
        
        if cmd == "поиск":
            if player.hp <= 0:
                print("Вы слишком слабы! Сначала отдохните.")
                continue
            return "encounter"  # переходим в сцену боя


        else:
            print("Неизвестная команда.")
