from ui import ui



def lvl_up(player):
    if player.exp_lvl_player >= player.max_exp_lvl_player:
        # Вычитаем потраченный опыт, чтобы остаток пошел на следующий уровень
        player.exp_lvl_player -= player.max_exp_lvl_player
        
        player.lvl_player += 1
        player.max_hp += 2
        player.max_endurance += 50
        player.damage += 1
        player.defense += 1
        player.max_exp_lvl_player += 50
        
        # Полное исцеление при повышении уровня (по желанию)
        player.hp = player.max_hp
        player.endurance = player.max_endurance
        
        ui.title(f"--- УРОВЕНЬ ПОВЫШЕН! Теперь у вас {player.lvl_player} лвл ---")
        
