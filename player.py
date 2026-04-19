class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.hp = 20
        self.max_hp = 20
        self.endurance = 100
        self.max_endurace = 100
        self.max_mana = 1
        self.mana = 1
        self.lvl_mana = 1
        self.exp_mana = 0
        self.max_exp_mana = 1
        self.damage = 1
        self.crit_chance = 0.10
        self.defense = 0
        self.lvl_player = 1
        self.exp_lvl_player = 0
        self.max_exp_lvl_player = 10
        self.equipment = {
            "right_hand": None,
            "left_hand": None,
            "body_armor": None,
            "head_armor": None
        }
        self.spells = []
        
        self.skills = []
        
        self.backpack = {}
        
        self.inventory = []
        
    def to_dict(self):
        return{
        "name": self.player_name,
        "hp": self.hp,
        "max_hp": self.max_hp,
        "endurance": self.endurance,
        "max_endurace": self.max_endurace,
        "max_mana": self.max_mana,
        "mana": self.mana,
        "lvl_mana": self.lvl_mana,
        "exp_mana": self.exp_mana,
        "max_exp_mana": self.max_exp_mana,
        "damage": self.damage,
        "crit_chance": self.crit_chance,
        "defense": self.defense,
        "lvl_player": self.lvl_player,
        "exp_lvl_player": self.exp_lvl_player,
        "max_exp_lvl_player": self.max_exp_lvl_player,
        "equipment": self.equipment,
        "spells": self.spells,
        "skills": self.skills,
        "backpack": self.backpack,
        "inventory": self.inventory
    }