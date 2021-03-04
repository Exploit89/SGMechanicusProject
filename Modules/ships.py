# шипы и их содержимое


class Ship:
    """Конструктор класса шипа"""
    def __init__(self):
        self.ship_id = "ship_id"
        self.nation = "nation"
        self.ship_type = "ship_type"
        self.tier = "tier"
        self.name = "name"
        self.role_1 = "role_1"
        self.role_2 = "role_2"
        self.tactical_component = "tactical_component"
        self.super_device = "super_device"
        self.ship_image = ""


mist = Ship()
ship_id = 0
nation = "ECD"
ship_type = "Frigate"
tier = "T1"
name = "Mist"
role_1 = "role_1"
role_2 = "role_2"
tactical_component = "tactical_component"
super_device = "super_device"
ship_image = ""  # ссылка на картинку

test = Ship()
print(test.name, test.tier)
