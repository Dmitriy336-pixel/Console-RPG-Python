class Items():
    def __init__(self, item_name, item_id, item_stacks, item_slots):
        self.item_name = item_name
        self.item_id = item_id
        self.item_stacks = item_stacks
        self.item_slots = item_slots
        
class Mobs():
    def __init__(self, mob_name, mob_id, mob_hp, mob_damage, mob_behavior, mob_loot_table):
        self.mob_name = mob_name
        self.mob_id = mob_id
        self.mob_hp = mob_hp
        self.mob_damage = mob_damage
        self.mob_behavior = mob_behavior
        self.mob_loot_table = mob_loot_table
        
class Weapons(Items):
    def __init__(self, item_name, item_id, item_stacks, item_slots, item_damage):
        super().__init__(item_name, item_id, item_stacks, item_slots)
        self.item_damage = item_damage
        
class Potions(Items):
    def __init__(self, item_name, item_id, item_stacks, item_slots, item_heal_value):
        super().__init__(item_name, item_id, item_stacks, item_slots)
        self.item_heal_value = item_heal_value
        
