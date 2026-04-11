class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 21
        self.max_hp = 20
        self.endurance = 100
        self.max_endurace = 100
        self.max_mana = 1
        self.mana = 1
        self.lvl_mana = 1
        self.exp_mana = 0
        self.max_exp_mana = 1
        self.damage = 1
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
        
        self.backpack = []
        
        self.inventory = []