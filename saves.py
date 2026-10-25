import json
from pathlib import Path

from player import Player
from ui import ui

SAVE_PATH = Path(__file__).parent / "player_save.json"

def save_game(player_obj):
    data = player_obj.to_dict()
    with open("player_save.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        ui.say("Прогресс успешно сохранен!")
     
def load_game():
    
    # Проверяем, существует ли файл И не пустой ли он
    if not SAVE_PATH.exists() or SAVE_PATH.stat().st_size == 0:
        ui.say("Файл сохранений пуст или отсутствует.")
        return None
    
    try:
        with open(SAVE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return Player.from_dict(data)
            
    except json.JSONDecodeError:
        ui.say("Ошибка: Файл сохранения поврежден!")
        return None
    except Exception as e:
        ui.say(f"Непредвиденная ошибка при загрузке: {e}")
        return None