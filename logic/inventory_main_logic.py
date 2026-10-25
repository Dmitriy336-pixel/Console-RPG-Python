import database
from ui import ui


def remove_item_backpack(player, item_id, count=1):
    if player.backpack.get(item_id, 0) < count:
        return False
    player.backpack[item_id] -= count
    if player.backpack[item_id] <= 0:
        del player.backpack[item_id]   # пустую запись убираем, иначе в списке будет "0 шт."
    return True




def add_items_backpack(player, item_id, count=1):
    player.backpack[item_id] = player.backpack.get(item_id, 0) + count




def use_potion(player, item_id):
    item = database.items_registry[item_id]
    if player.hp >= player.max_hp:
        ui.say("Здоровье уже полное.")
        return
    remove_item_backpack(player, item_id)
    before = player.hp
    player.hp = min(player.max_hp, player.hp + item.item_heal_value)
    ui.say(f"Выпито: {item.item_name}. +{player.hp - before} HP")
        
        
