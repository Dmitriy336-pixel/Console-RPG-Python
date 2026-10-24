import json
import random
from pathlib import Path
import copy
from models import Items, Weapons, Potions, Mobs

DATA_DIR = Path(__file__).parent / "data"


# Items - предметы пока остаются здесь

Arc_en_Ciel = Weapons("Арк_ан_Сиэль", "id:arc_en_ciel", 1, "right_hand", 150, "Меч администратора")

small_healing_potion = Potions("Зелье Востановления 1", "id:small_healing_potion", 10, None, 5, "Лечит пользователя")

normal_healing_potion = Potions("Зелье Востановления 2", "id:normal_healing_potion", 5, None, 8, "Лечит пользователя")

big_healing_potion = Potions("Зелье Востановления 3", "id:big_healing_potion", 3, None, 15, "Лечит пользователя")

# Реестр предметов: чтобы по ID узнавать имя и статы
items_registry = {
    "id:small_healing_potion": small_healing_potion,
    "id:normal_healing_potion": normal_healing_potion,
    "id:big_healing_potion": big_healing_potion,
    "id:arc_en_ciel": Arc_en_Ciel,
}

def item_name(item_id):
    item = items_registry.get(item_id)
    return item.item_name if item else item_id


# Mobs - мобы описаны в data/mobs.json

def _parse_locations(raw):
    """Список ["forest"] = все мобы равновероятны, словарь {"forest": 70} = вес."""
    if isinstance(raw, dict):
        return raw
    return {location: 1 for location in raw}


def load_mobs():
    mobs = {}
    with open(DATA_DIR / "mobs.json", "r", encoding="utf-8") as f:
        raw = json.load(f)

    for mob_id, d in raw.items():
        loot = d.get("loot", [])
        for entry in loot:  # опечатка в id падает при старте, а не посреди боя
            if entry["item"] not in items_registry:
                raise ValueError(f"{mob_id}: в луте неизвестный предмет {entry['item']}")
        mobs[mob_id] = Mobs(
            d["name"], mob_id, d["hp"], d["hp"], d["damage"],
            d.get("behavior", "aggressive"), loot, d["exp"],
            _parse_locations(d.get("locations", [])),
        )
    return mobs


mobs_registry = load_mobs()


def spawn_mob(mob_id):
    """Новый экземпляр моба по шаблону из реестра."""
    return copy.deepcopy(mobs_registry[mob_id])


def pick_mob(location):
    """Случайный моб для локации с учётом весов. None, если там никто не живёт."""
    candidates = [m for m in mobs_registry.values() if location in m.mob_locations]
    if not candidates:
        return None
    weights = [m.mob_locations[location] for m in candidates]
    chosen = random.choices(candidates, weights=weights)[0]
    return spawn_mob(chosen.mob_id)


# Старые имена, чтобы остальной код не сломался. Потом можно удалить.
slime = mobs_registry["id:mob_slime"]
big_slime = mobs_registry["id:mob_big_slime"]
#king_slime = mobs_registry["id:mob_king_slime"]
forest_mobs = [m for m in mobs_registry.values() if "forest" in m.mob_locations]