# эквип и содержимое
from collections import namedtuple

from Images.Equipment import equipment_images

t1r1_s_single_combat_railgun_parts = {
    'weapon_id': int(0),
    'weapon_type': "Railgun",
    'tier': "T1",
    'rank': "R1",
    'weapon_size': "S",
    'weapon_class': "Single",
    'weapon_class_2': "Combat",
    'name': "T1R1 S Single Combat Railgun",

    'ship_image': equipment_images.t1r1_s_single_combat_railgun_image,  # переменная с путем картинки
}

T1R1_S_Single_Combat_Railgun = namedtuple('T1R1 S Single Combat Railgun', t1r1_s_single_combat_railgun_parts)
t1r1_s_single_combat_railgun = T1R1_S_Single_Combat_Railgun(**t1r1_s_single_combat_railgun_parts)

allequip_parts = {
    'T1R1 S Single Combat Railgun': t1r1_s_single_combat_railgun
}

AllEquip = namedtuple('AllEquip', allequip_parts)
allequip = AllEquip(**allequip_parts)
