from asyncio.windows_utils import pipe
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

meatball = Item(
    char="!",
    color=(127, 0, 255),
    name="Swedish Meatball",
    consumable=consumable.HealingConsumable(amount=8),
)

bug_zapper = Item(
    char="~",
    color=(255, 255, 0),
    name="Bug Zapper",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

confusing_siren = Item(
    char="~",
    color=(207, 63, 255),
    name="Confusing Siren",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)

hairspray_grenade = Item(
    char="~",
    color=(255, 0, 0),
    name="Hairspray Grenade",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)

shiv = Item(
    char="/", 
    color=(0, 191, 255), 
    name="Shiv", 
    equippable=equippable.Shiv()
)

lead_pipe = Item(
    char="/", 
    color=(0, 191, 255), 
    name="Lead Pipe", 
    equippable=equippable.LeadPipe()
)

stapler_nunchucks = Item(
    char="//",
    color=(56, 192, 255),
    name="Stapler Nunchucks",
    equippable=equippable.StaplerNunchucks()
)

jumpsuit = Item(
    char="[",
    color=(139, 69, 19),
    name="Blue Jumpsuit",
    equippable=equippable.BlueJumpSuit(),
)

cosplay_armor = Item(
    char="[", 
    color=(139, 69, 19), 
    name="Cosplay Armor", 
    equippable=equippable.CosplayArmor()
)

milgradefatigues = Item(
    char="[",
    color=(34, 200, 45),
    name="Mil-Grade Fatigues",
    equippable=equippable.MilGradeFatigues()
)