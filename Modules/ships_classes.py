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

        self.processor_capacity = int()
        self.power_capacity = int()
        self.energy_capacity = int()
        self.auto_energy_recovery = int()
        self.component_slots = int()
        self.velocity = int()
        self.agility = int()
        self.shield_res_em = int()
        self.shield_res_kinetic = int()
        self.shield_res_thermal = int()
        self.armor_res_em = int()
        self.armor_res_kinetic = int()
        self.armor_res_thermal = int()
        self.shield = int()
        self.auto_shield_recovery = int()
        self.armor = int()
        self.auto_armor_recovery = int()
        self.volume_factor = int()
        self.warp_stability = int()
        self.warp_velocity = int()
        self.cargo_space_capacity = int()
        self.volume = int()

        self.per_level_bonus1 = int()
        self.per_level_bonus2 = int()
        self.per_level_bonus3 = int()

        self.special_bonus1 = int()
        self.special_bonus2 = int()
        self.special_bonus3 = int()


class Mist(Ship):
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

    processor_capacity = int()
    power_capacity = int()
    energy_capacity = int()
    auto_energy_recovery = int()
    component_slots = int()
    velocity = int()
    agility = int()
    shield_res_em = int()
    shield_res_kinetic = int()
    shield_res_thermal = int()
    armor_res_em = int()
    armor_res_kinetic = int()
    armor_res_thermal = int()
    shield = int()
    auto_shield_recovery = int()
    armor = int()
    auto_armor_recovery = int()
    volume_factor = int()
    warp_stability = int()
    warp_velocity = int()
    cargo_space_capacity = int()
    volume = int()

    per_level_bonus1 = int()
    per_level_bonus2 = int()
    per_level_bonus3 = int()

    special_bonus1 = int()
    special_bonus2 = int()
    special_bonus3 = int()

