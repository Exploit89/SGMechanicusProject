import sqlite3

database = ('SGDatabase2.db')

connect = sqlite3.connect(database)
cursor = connect.cursor()

cursor.execute("""
    INSERT INTO Ship (Nation, Type, Tier, Name, Role1, TacticalComponent, Superdevice, ProcessorCapacity, PowerCapacity,
    EnergyCapacity, AutoEnergyRecovery, ComponentSlots, Velocity, Agility, ShieldResEM, ShieldResKinetic, 
    ShieldResThermal, ArmorResEM, ArmorResKinetic, ArmorResThermal, Shield, AutoShieldRecovery, Armor,
    AutoArmorRecovery, VolumeFactor, WarpStability, CargoSpaceCapacity, Volume)
    VALUES ('ECD', 'Frigate', 'T1', 'Mist')
""")

names = next(zip(*cursor.description))
print(names)

rows = (cursor.fetchall())

for row in rows:
    print(row)

connect.commit()