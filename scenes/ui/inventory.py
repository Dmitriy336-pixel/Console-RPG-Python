import database

def run(player):
    print("\n=== РЮКЗАК ===")

    if not player.backpack:
        print("Там пока пусто...")
    else:
        for item_id, count in player.backpack.items():
            item = database.items_registry.get(item_id)
            if item:
                print(f"  [{item.item_name}] — {count} шт.")
            else:
                print(f"  [{item_id}] — {count} шт.")
    input("\nНажми Enter чтобы вернуться...")
    return "forest"  # возвращаемся обратно в лес
