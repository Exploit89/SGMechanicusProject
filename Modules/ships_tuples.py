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

    'processor_capacity': int(),
    'power_capacity': int(),
    'energy_capacity': int(),
    'auto_energy_recovery': int(),
    'component_slots': int(),
    'velocity': int(),
    'agility': int(),
    'shield_res_em': int(),
    'shield_res_kinetic': int(),
    'shield_res_thermal': int(),
    'armor_res_em': int(),
    'armor_res_kinetic': int(),
    'armor_res_thermal': int(),
    'shield': int(),
    'auto_shield_recovery': int(),
    'armor': int(),
    'auto_armor_recovery': int(),
    'volume_factor': int(),
    'warp_stability': int(),
    'warp_velocity': int(),
    'cargo_space_capacity': int(),
    'volume': int(),

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

    'processor_capacity': int(),
    'power_capacity': int(),
    'energy_capacity': int(),
    'auto_energy_recovery': int(),
    'component_slots': int(),
    'velocity': int(),
    'agility': int(),
    'shield_res_em': int(),
    'shield_res_kinetic': int(),
    'shield_res_thermal': int(),
    'armor_res_em': int(),
    'armor_res_kinetic': int(),
    'armor_res_thermal': int(),
    'shield': int(),
    'auto_shield_recovery': int(),
    'armor': int(),
    'auto_armor_recovery': int(),
    'volume_factor': int(),
    'warp_stability': int(),
    'warp_velocity': int(),
    'cargo_space_capacity': int(),
    'volume': int(),

    'per_level_bonus1': int(),
    'per_level_bonus2': int(),
    'per_level_bonus3': int(),

    'special_bonus1': int(),
    'special_bonus2': int(),
    'special_bonus3': int()
}
Frost = namedtuple('Frost', frost_parts)
frost = Frost(**frost_parts)
