import database

import models
from ui import ui
from logic import inventory_main_logic
PAGE_SIZE = 10


def type_of(item):
    return item.item_type if item else "Прочее"


def sub_of(item):
    # подтипа может не быть: тогда предмет попадает в "Разное"
    return getattr(item, "item_subtype", "") or "Разное"


def ids_of(player, category, subtype=None):
    """id предметов рюкзака из выбранной категории (и подкатегории)."""
    result = []
    for item_id in player.backpack:
        item = database.items_registry.get(item_id)
        if type_of(item) != category:
            continue
        if subtype is not None and sub_of(item) != subtype:
            continue
        result.append(item_id)
    return result


def category_menu(player):
    counts = {}
    for item_id, n in player.backpack.items():
        t = type_of(database.items_registry.get(item_id))
        counts[t] = counts.get(t, 0) + n
    options = [("Закрыть рюкзак", "close")]
    options += [(f"{t} ({n})", t) for t, n in sorted(counts.items())]
    return ui.choose("Рюкзак:", options, cancel_value="close")


def subtype_menu(player, category, ids):
    counts = {}
    for item_id in ids:
        s = sub_of(database.items_registry.get(item_id))
        counts[s] = counts.get(s, 0) + player.backpack[item_id]
    options = [("Закрыть рюкзак", "close"), ("Назад", "back")]
    options += [(f"{s} ({n})", s) for s, n in sorted(counts.items())]
    return ui.choose(f"{category}:", options, cancel_value="back")


def item_list_menu(player, ids, page, title):
    pages = max(1, (len(ids) + PAGE_SIZE - 1) // PAGE_SIZE)
    page = max(0, min(page, pages - 1))
    chunk = ids[page * PAGE_SIZE:(page + 1) * PAGE_SIZE]

    options = [("Закрыть рюкзак", "close"), ("Назад", "back")]
    options += [(f"{database.item_name(i)}  x{player.backpack[i]}", i) for i in chunk]
    if page > 0:
        options.append(("Предыдущая страница", "prev"))
    if page < pages - 1:
        options.append(("Следующая страница", "next"))

    choice = ui.choose(f"{title} (стр. {page + 1}/{pages}):", options, cancel_value="back")
    return choice, page


def item_screen(player, item_id):
    """Экран предмета. Возвращает "close", если игрок закрыл рюкзак."""
    while item_id in player.backpack:
        item = database.items_registry[item_id]

        lines = [f"Тип: {item.item_type}", f"В рюкзаке: {player.backpack[item_id]} шт."]
        if item.item_desc:
            lines.append(item.item_desc)
        if isinstance(item, models.Potions):
            lines.append(f"Лечит: {item.item_heal_value} HP")
        if isinstance(item, models.Weapons):
            lines.append(f"Урон: {item.item_damage}")
            lines.append(f"Слот: {item.item_slots}")
        ui.panel(item.item_name, "\n".join(lines))

        options = []
        if isinstance(item, models.Potions):
            options.append(("Использовать", "use"))
        if isinstance(item, models.Weapons):
            options.append(("Надеть", "equip"))
        options += [("Выбросить 1 шт.", "drop"),
                    ("Назад в рюкзак", "back"),
                    ("Закрыть рюкзак", "close")]

        action = ui.choose("Что делаем?", options, cancel_value="back")

        if action == "use":
            inventory_main_logic.use_potion(player, item_id)
        elif action == "equip":
            slot = item.item_slots
            old = player.equipment.get(slot)
            if old:
                inventory_main_logic.add_items_backpack(player, old)
            inventory_main_logic.remove_item_backpack(player, item_id)
            player.equipment[slot] = item_id
            ui.say(f"Надето: {item.item_name}")
        elif action == "drop":
            if ui.confirm(f"Выбросить {item.item_name}?"):
                inventory_main_logic.remove_item_backpack(player, item_id)
        elif action == "close":
            return "close"
        else:
            return None
    return None


def run(player):
    ui.title("РЮКЗАК")
    category = None
    subtype = None
    page = 0

    while True:
        if not player.backpack:
            ui.say("Там пока пусто...")
            return "forest"

        # уровень 1: категории
        if category is None:
            choice = category_menu(player)
            if choice == "close":
                return "forest"
            category, subtype, page = choice, None, 0
            continue

        ids = ids_of(player, category)
        if not ids:                       # в категории всё закончилось
            category = None
            continue

        # уровень 2: подкатегории (только если они есть)
        has_subtypes = {sub_of(database.items_registry.get(i)) for i in ids} != {"Разное"}
        if has_subtypes and subtype is None:
            choice = subtype_menu(player, category, ids)
            if choice == "close":
                return "forest"
            if choice == "back":
                category = None
                continue
            subtype, page = choice, 0
            continue

        if has_subtypes:
            ids = ids_of(player, category, subtype)
            if not ids:
                subtype = None
                continue

        # уровень 3: список предметов по страницам
        choice, page = item_list_menu(player, ids, page, subtype or category)
        if choice == "close":
            return "forest"
        elif choice == "back":
            if has_subtypes:
                subtype = None
            else:
                category = None
            page = 0
        elif choice == "next":
            page += 1
        elif choice == "prev":
            page -= 1
        else:
            if item_screen(player, choice) == "close":
                return "forest"