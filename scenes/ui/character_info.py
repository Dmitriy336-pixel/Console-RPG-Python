def run(player):
    print("\n=== ПЕРСОНАЖ ===")
    print(f"  Имя:     {player.player_name}")
    print(f"  Уровень: {player.lvl_player}")
    print(f"  HP:      {player.hp}/{player.max_hp}")
    print(f"  Мана:    {player.mana}/{player.max_mana}")
    print(f"  Урон:    {player.damage}")
    print(f"  Защита:  {player.defense}")
    print(f"  Крит:    {int(player.crit_chance * 100)}%")
    print(f"  Опыт:    {player.exp_lvl_player}/{player.max_exp_lvl_player}")

    print("\n  --- Экипировка ---")
    for slot, item in player.equipment.items():
        print(f"  {slot}: {item if item else 'пусто'}")

    input("\nНажми Enter чтобы вернуться...")
    return "forest"
