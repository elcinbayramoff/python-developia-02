"""
Hero - Enemy
attack
defense
name
max hp
hp

Hero
inventory: potion, weapon

Character

    Hero
    Enemy

Item
    Weapon
    Potion
Room
Game
"""
import random



class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack_power = attack
        self.defense = defense

    @property
    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, dmg):
        lost_hp = max(dmg - self.defense, 0) # dmg = 2, defense = 5  lost_hp = 0; dmg = 10, defense = 5 lost_hp = 5
        self.hp = max(self.hp - lost_hp, 0)

    def attack(self, target:"Character"):
        if not self.is_alive:
            return
        
        A = [1,1,1,1,2] # 20%
        damage = self.attack_power * random.choice(A)
        #Hero critically damaged Enemy
        #Hero damaged Enemy
        target.take_damage(damage)

class Hero(Character):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)
        self.inventory = []
        self.equipped_weapon = None

    def equip(self, weapon: "Weapon"):
        self.equipped_weapon = weapon
        self.attack_power = weapon.damage

    def show_status(self):
        # if self.equipped_weapon:
        #     weapon_name = self.equipped_weapon.name
        # else:
        #     weapon_name = 'None'
        
        weapon_name = self.equipped_weapon.name if self.equipped_weapon else 'None'

        print(f'{self.name}')
        print(f'HP: {self.hp}/{self.max_hp}') # 70/100
        print(f'Attack: {self.attack_power} Defense: {self.defense}')
        print(f'Weapon: {weapon_name}')
        print('Inventory:')
        if self.inventory:
            for index, item in enumerate(self.inventory, 1):
                print(f'{index}. {item}')

        else:
            print('(Empty)')

    def choose_action(self, enemy):
        while True:
            print('\nChoose action:')
            print('1. Attack')
            print('2. Use item')
            print('3. Inspect Character')
            choice = input('>')

            if choice == '1':
                self.attack(enemy)
                break

            elif choice == '2':
                if not self.inventory:
                    print('Your inventory is empty')
                    continue

                for index, item in enumerate(self.inventory, 1):
                    print(f'{index}. {item}')
                
                try:
                    selection = int(input('>')) - 1
                    _item = self.inventory.pop(selection)
                    _item.use(self)
                    
                except (ValueError, IndexError):
                    print('Invalid choice')
                    item = locals().get('_item')
                    if item:
                        self.inventory.insert(selection, item)
                except:
                    print('Something went wrong')
                
                break

            elif choice == '3':
                self.show_status()
            
            else:
                print('Invalid choice')


class Enemy(Character):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)
        self.kind = name
    
    def __str__(self):
        return f'{self.kind} (HP: {self.hp}/{self.max_hp})'

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, hero: Hero):
        print(f'{self.name} does nothing')
    
    def __str__(self):
        return f"{self.name} - {self.description}"


class Weapon(Item):
    def __init__(self, name, damage):
        super().__init__(name, f'Gives {damage} damage')
        self.damage = damage
    
    def use(self, hero: Hero):
        hero.equip(self)

class Potion(Item):
    def __init__(self, name, heal):
        super().__init__(name, f'Gives {heal} heal')
        self.heal = heal
    
    def use(self, hero: Hero):
        hero.hp
        hero.max_hp
        self.heal
        if hero.hp < hero.max_hp:
            hero.hp += self.heal
            if hero.hp > hero.max_hp:
                hero.hp = hero.max_hp
        
        # hp = 90, max = 100, heal = 15 -> 100
        hero.hp = min(self.heal + hero.hp, hero.max_hp)
                    # 90 + 15, 100 - > 100
                    # 70 + 15, 100 - > 85


class Room:
    def __init__(self, description, enemies, loots, on_clear_text):
        self.description = description
        self.enemies = enemies
        self.loots = loots
        self.on_clear_text = on_clear_text

    def enter(self, hero: Hero):
        #self.description burda
        input('Press Enter to continue')
        for enemy in self.enemies:
            while enemy.is_alive and hero.is_alive:
                hero.choose_action(enemy)
                if enemy.is_alive:
                    enemy.attack(hero)

        if not hero.is_alive:
            ...
            return
        
        print(self.on_clear_text)

        if self.loots:
            ...
            for loot in self.loots:
                hero.inventory.append(loot)


class Game:
    def __init__(self):
        self.player = None
        self.rooms = self._create_world()

    def _create_world(self):
        dusty_sword =  Weapon('Dust Sword', 10) # 50
        fire_sword = Weapon('Fire Sword', 22) # 15
        lightning_sword = Weapon('Lightning Sword', 27) # 10
        bow = Weapon('Bow', 15) # 25
        all_weapons = {dusty_sword:50,fire_sword:15,lightning_sword:10, bow:25}

        potion_small = Potion('Small Potion', 15) # 50
        potion_medium = Potion('Medium Potion', 30) # 30
        potion_big = Potion('Big Potion', 70) # 20
        all_potions = {potion_small: 50, potion_medium: 30, potion_big: 20}

        return [
            Room(
                description='',
                enemies=[Enemy('Goblin',30, 8, 1)],
                loots= self.random_item_selecter(all_weapons) + self.random_item_selecter(all_potions),

            ),
            Room(
                description='',
                enemies=[Enemy('Orc',45, 12, 3)],
                loots= self.random_item_selecter(all_weapons) + self.random_item_selecter(all_potions, 2),

            ),
            Room(
                description='',
                enemies=[Enemy('Dragon',100, 18, 5)],
                loots= [self.random_item_selecter(all_weapons, 2) + self.random_item_selecter(all_potions)],

            ),
        ]
    
    def _create_player(self):
        print('Enter your name, Hero!:')
        name = input('> ').strip() or 'Hero'
        

    
    @staticmethod
    def random_item_selecter(elements: dict, count=1):
        base = []
        for item, percentage in elements.items():
            base += [item] * percentage
        
        for n in random.choices(base, k=count):
            print(n)


"""
a
əgər a cüt ədəddirsə result = 'Cut', tək ədəddirsə, result = 'Tek' a % 2 == 0
result
"""

# if self.equipped_weapon:
#     weapon_name = self.equipped_weapon.name
# else:
#     weapon_name = 'None'

# weapon_name = self.equipped_weapon.name if self.equipped_weapon else 'None'