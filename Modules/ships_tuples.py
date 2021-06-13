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

glimmer_parts = {
    'ship_id': int(2),
    'nation': "ECD",
    'ship_type': "Frigate",
    'tier': "T1",
    'name': "Glimmer",
    'role_1': "role_1",
    'role_2': "role_2",
    'tactical_component': "tactical_component",
    'super_device': "super_device",
    'ship_image': ship_images.glimmer_image,  # переменная с путем картинки

    'processor_capacity': int(245),
    'power_capacity': int(106),
    'energy_capacity': int(1072),
    'auto_energy_recovery': int(12),
    'component_slots': int(2),
    'velocity': int(581),
    'agility': int(693),
    'shield_res_em': int(50),
    'shield_res_kinetic': int(30),
    'shield_res_thermal': int(10),
    'armor_res_em': int(5),
    'armor_res_kinetic': int(20),
    'armor_res_thermal': int(35),
    'shield': int(1596),
    'auto_shield_recovery': int(1),
    'armor': int(1497),
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
Glimmer = namedtuple('Glimmer', glimmer_parts)
glimmer = Glimmer(**glimmer_parts)

sprinkle_parts = {
    'ship_id': int(3),
    'nation': "ECD",
    'ship_type': "Frigate",
    'tier': "T2",
    'name': "Sprinkle",
    'role_1': "role_1",
    'role_2': "role_2",
    'tactical_component': "tactical_component",
    'super_device': "super_device",
    'ship_image': ship_images.sprinkle_image,  # переменная с путем картинки

    'processor_capacity': int(856),
    'power_capacity': int(173),
    'energy_capacity': int(2375),
    'auto_energy_recovery': int(25),
    'component_slots': int(3),
    'velocity': int(721),
    'agility': int(693),
    'shield_res_em': int(75),
    'shield_res_kinetic': int(45),
    'shield_res_thermal': int(10),
    'armor_res_em': int(5),
    'armor_res_kinetic': int(35),
    'armor_res_thermal': int(65),
    'shield': int(4524),
    'auto_shield_recovery': int(3),
    'armor': int(4242),
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
Sprinkle = namedtuple('Sprinkle', sprinkle_parts)
sprinkle = Sprinkle(**sprinkle_parts)

snowflake_parts = {
    'ship_id': int(4),
    'nation': "ECD",
    'ship_type': "Frigate",
    'tier': "T2",
    'name': "Snowflake",
    'role_1': "role_1",
    'role_2': "role_2",
    'tactical_component': "tactical_component",
    'super_device': "super_device",
    'ship_image': ship_images.snowflake_image,  # переменная с путем картинки

    'processor_capacity': int(912),
    'power_capacity': int(184),
    'energy_capacity': int(2319),
    'auto_energy_recovery': int(25),
    'component_slots': int(3),
    'velocity': int(704),
    'agility': int(693),
    'shield_res_em': int(75),
    'shield_res_kinetic': int(45),
    'shield_res_thermal': int(10),
    'armor_res_em': int(5),
    'armor_res_kinetic': int(35),
    'armor_res_thermal': int(65),
    'shield': int(4419),
    'auto_shield_recovery': int(3),
    'armor': int(4145),
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
Snowflake = namedtuple('Snowflake', snowflake_parts)
snowflake = Snowflake(**snowflake_parts)

rainbow_parts = {
    'ship_id': int(5),
    'nation': "ECD",
    'ship_type': "Frigate",
    'tier': "T2",
    'name': "Rainbow",
    'role_1': "role_1",
    'role_2': "role_2",
    'tactical_component': "tactical_component",
    'super_device': "super_device",
    'ship_image': ship_images.rainbow_image,  # переменная с путем картинки

    'processor_capacity': int(1028),
    'power_capacity': int(164),
    'energy_capacity': int(2145),
    'auto_energy_recovery': int(25),
    'component_slots': int(3),
    'velocity': int(580),
    'agility': int(693),
    'shield_res_em': int(75),
    'shield_res_kinetic': int(45),
    'shield_res_thermal': int(10),
    'armor_res_em': int(5),
    'armor_res_kinetic': int(35),
    'armor_res_thermal': int(65),
    'shield': int(3673),
    'auto_shield_recovery': int(3),
    'armor': int(3444),
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
Rainbow = namedtuple('Rainbow', rainbow_parts)
rainbow = Rainbow(**rainbow_parts)

shower_parts = {
    'ship_id': int(6),
    'nation': "ECD",
    'ship_type': "Frigate",
    'tier': "T2",
    'name': "Shower",
    'role_1': "role_1",
    'role_2': "role_2",
    'tactical_component': "tactical_component",
    'super_device': "super_device",
    'ship_image': ship_images.shower_image,  # переменная с путем картинки

    'processor_capacity': int(3618),
    'power_capacity': int(240),
    'energy_capacity': int(4274),
    'auto_energy_recovery': int(44),
    'component_slots': int(4),
    'velocity': int(721),
    'agility': int(693),
    'shield_res_em': int(75),
    'shield_res_kinetic': int(45),
    'shield_res_thermal': int(10),
    'armor_res_em': int(5),
    'armor_res_kinetic': int(35),
    'armor_res_thermal': int(65),
    'shield': int(9207),
    'auto_shield_recovery': int(5),
    'armor': int(8633),
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
Shower = namedtuple('Shower', shower_parts)
shower = Shower(**shower_parts)

allships_parts = {
    'mist': mist,
    'frost': frost,
    'glimmer': glimmer,
    'sprinkle': sprinkle,
    'snowflake': snowflake,
    'rainbow': rainbow,
    'shower': shower
}

AllShips = namedtuple('AllShips', allships_parts)
allships = AllShips(**allships_parts)

"""блок исключительно для проверки"""

itemnamesomething = 'mist'

for i in allships_parts.items():
    #print(i[0], i[1][0])
    shipsss = 'sprinkle'
    if i[0] == shipsss:
        iii = (i[1][0])
        print(i[1][0])

if itemnamesomething in allships_parts:
    print(allships[iii][8])
else:
    print('ass')
