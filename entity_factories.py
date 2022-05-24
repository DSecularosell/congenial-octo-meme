from components.ai import ConfusedEnemy, HostileEnemy
from components import consumable, equippable
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=100, base_regen=1, base_defense=2, base_power=3),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200)
)
dork = Actor(
    char="d",
    color=(63, 100, 180),
    name="Dork",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=20, base_regen=0, base_defense=1, base_power=5),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)
lumpus = Actor(
    char="L",
    color=(0, 127, 0),
    name="Lumpus",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=45, base_regen=0, base_defense=1, base_power=8),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
)

hall_monitor = Actor(
    char='H',
    color=(89,0,34),
    name='Hall Monitor',
    ai_cls=HostileEnemy, 
    equipment=Equipment(),
    fighter=Fighter(hp=120, base_regen=0, base_defense=4, base_power=5),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=300),
)

health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Swedish Meatball",
    consumable=consumable.HealingConsumable(amount=8),
)

lightning_scroll = Item(
    char="~",
    color=(255, 255, 0),
    name="Bug Zapper",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

confusion_scroll = Item(
    char="~",
    color=(207, 63, 255),
    name="Confusing Siren",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)

fireball_scroll = Item(
    char="~",
    color=(255, 0, 0),
    name="Hairspray Grenade",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)

dagger = Item(
    char="/", 
    color=(0, 191, 255), 
    name="Dagger", 
    equippable=equippable.Dagger()
)

sword = Item(
    char="/", 
    color=(0, 191, 255), 
    name="Sword", 
    equippable=equippable.Sword()
)

leather_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="Leather Armor",
    equippable=equippable.LeatherArmor(),
)

chain_mail = Item(
    char="[", color=(139, 69, 19), name="Chain Mail", equippable=equippable.ChainMail()
)