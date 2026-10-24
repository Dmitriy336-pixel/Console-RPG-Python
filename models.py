class Items():
    item_type = "Предмет"
    def __init__(self, item_name, item_id, item_stacks, item_slots, item_desc=""):
        self.item_name = item_name
        self.item_id = item_id
        self.item_stacks = item_stacks
        self.item_slots = item_slots
        self.item_desc = item_desc
        
class Mobs():
    def __init__(self, mob_name, mob_id, mob_hp, mob_max_hp, mob_damage, mob_behavior, mob_loot_table, mob_loot_exp, mob_locations=None):
        self.mob_name = mob_name
        self.mob_id = mob_id
        self.mob_hp = mob_hp
        self.mob_max_hp = mob_max_hp
        self.mob_damage = mob_damage
        self.mob_behavior = mob_behavior
        self.mob_loot_table = mob_loot_table
        self.mob_loot_exp = mob_loot_exp
        self.mob_locations = mob_locations or {}
        
class Weapons(Items):
    item_type = "Оружие"
    def __init__(self, item_name, item_id, item_stacks, item_slots, item_damage, item_desc=""):
        super().__init__(item_name, item_id, item_stacks, item_slots, item_desc)
        self.item_damage = item_damage
        
class Potions(Items):
    item_type = "Зелье"
    def __init__(self, item_name, item_id, item_stacks, item_slots, item_heal_value, item_desc=""):
        super().__init__(item_name, item_id, item_stacks, item_slots, item_desc)
        self.item_heal_value = item_heal_value
        
