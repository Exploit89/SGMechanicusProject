# шипы и их содержимое
from collections import namedtuple

from Images.Ships import ship_images

mist_parts = {
    'ship_id': int(0),
    'nation': "ECD",
    'ship_type': "Frigate",
    'tier': "T1",
    'name': "Mist",
    'role_1': "role_1",
    'role_2': "role_2",
    'tactical_component': "tactical_component",
    'super_device': "super_device",
    'ship_image': ship_images.mist_image,  # переменная с путем картинки

    'processor_capacity': int(220),
    'power_capacity': int(118),
    'energy_capacity': int(1187),
    'auto_energy_recovery': int(12),
    'component_slots': int(2),
    'velocity': int(721),
    'agility': int(693),
    'shield_res_em': int(50),
    'shield_res_kinetic': int(30),
    'shield_res_thermal': int(10),
    'armor_res_em': int(5),
    'armor_res_kinetic': int(20),
    'armor_res_thermal': int(35),
    'shield': int(1967),
    'auto_shield_recovery': int(1),
    'armor': int(1845),
    'auto_armor_recovery': int(0),
    'volume_factor': int(140),
    'warp_stability': int(1),
    'warp_velocity': int(),
    'cargo_space_capacity': int(100),
    'volume': int(700),

    'per_level_bonus1': int(),
    'per_level_bonus2': int(),
    'per_level_bonus3': int(),

    'special_bonus1': int(),
    'special_bonus2': int(),
    'special_bonus3': int()
}
Mist = namedtuple('Mist', mist_parts)
mist = Mist(**mist_parts)

frost_parts = {
    'ship_id': int(1),
    'nation': "ECD",
    'ship_type': "Frigate",
    'tier': "T1",
    'name': "Frost",
    'role_1': "role_1",
    'role_2': "role_2",
    'tactical_component': "tactical_component",
    'super_device': "super_device",
    'ship_image': ship_images.frost_image,  # переменная с путем картинки

    'processor_capacity': int(218),
    'power_capacity': int(119),
    'energy_capacity': int(1160),
    'auto_energy_recovery': int(12),
    'component_slots': int(2),
    'velocity': int(704),
    'agility': int(693),
    'shield_res_em': int(50),
    'shield_res_kinetic': int(30),
    'shield_res_thermal': int(10),
    'armor_res_em': int(5),
    'armor_res_kinetic': int(20),
    'armor_res_thermal': int(35),
    'shield': int(1922),
    'auto_shield_recovery': int(1),
    'armor': int(1802),
    'auto_armor_recovery': int(0),
    'volume_factor': int(140),
    'warp_stability': int(1),
    'warp_velocity': int(),
    'cargo_space_capacity': int(100),
    'volume': int(700),

    'per_level_bonus1': int(),
    'per_level_bonus2': int(),
    'per_level_bonus3': int(),

    'special_bonus1': int(),
    'special_bonus2': int(),
    'special_bonus3': int()
}
Frost = namedtuple('Frost', frost_parts)
frost = Frost(**frost_parts)

allships_parts = {
    'mist': mist,
    'frost': frost
}

AllShips = namedtuple('AllShips', allships_parts)
allships = AllShips(**allships_parts)

"""блок исключительно для проверки"""

itemnamesomething = 'mist'

if itemnamesomething in allships_parts:
    print(allships.mist[9])
else:
    print('ass')