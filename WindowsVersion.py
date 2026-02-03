import os
import random
from time import sleep

class World:
    difficulty: int
    level = 1

class Modifier:
    name: str
    description: str

class Weapon:
    name: str
    rarity: str
    damage: int
    critChance: float
    critDamage: float
    modifier = Modifier()

class Player:
    maxhp = 10
    hp = 10
    weapon = Weapon()
    inv = [] # Not used!
    playerClass: str

class Food: # Not used!
    hpGain: int
    
class Enemy:
    maxhp: int
    hp: int
    damage: int

def clear():
    os.system('cls')

class modifiers:
    none = Modifier()
    none.name = "None"
    none.description = ""

    lifesteal = Modifier()
    lifesteal.name = "Lifesteal"
    lifesteal.description = "Has a chance to heal, increasing with damage."

    healBoost = Modifier()
    healBoost.name = "Heal Boost"
    healBoost.description = "Increases the chance of healing more."

    itemFinder = Modifier()
    itemFinder.name = "Weapon Luck"
    itemFinder.description = "Increases the chance to find Weapons"

    maxHpBoost = Modifier()
    maxHpBoost.name = "Health Bonus"
    maxHpBoost.description = "+1 Max Hp per Fight"

    chaos = Modifier()
    chaos.name = "\033[95mChaos\033[0m"
    chaos.description = "Has a chance to \033[92increase\033[0m or \033[91decrease\033[0m weapon stats"

def randomModifier() -> Modifier:
    return random.choice([modifiers.lifesteal, modifiers.healBoost, modifiers.itemFinder, modifiers.maxHpBoost, modifiers.chaos])

class starterWeapons:
    # I bet there is a much easier way of doing this
    # but too late I've already done it like this.
    meleeStarter = Weapon()
    meleeStarter.name = "Starter Sword"
    meleeStarter.rarity = "Common"
    meleeStarter.damage = 2
    meleeStarter.critChance = 0.1
    meleeStarter.critDamage = 1.0
    meleeStarter.modifier = modifiers.none

    rangeStarter = Weapon()
    rangeStarter.name = "Starter Bow"
    rangeStarter.rarity = "Common"
    rangeStarter.damage = 1
    rangeStarter.critChance = 0.5
    rangeStarter.critDamage = 2.0
    rangeStarter.modifier = modifiers.none

def randomPrefix() -> str:
    return random.choice(["Strong", "Powerful", "Odd", "Unique", "Hurtful", "Forceful", "Agile", "Bloodthirsty", "Nasty", "Sharp", "Repaired", "Ancient"])

def randomSwordName() -> str:
    return random.choice(["Claymore", "Broadsowrd", "Longsword", "Dagger", "Katana", "Cutlass", "Knife", "Sword", "Hammer", "Bat"])

def randomBowName() -> str:
    return random.choice(["Bow", "Crossbow", "Slingshot", "Longbow", "Shortbow", "Pistol", "Shotgun", "Handgun", "Rifle", "Revolver"])

def randomRarity() -> str:
    randNum = random.randrange(1,101)
    if randNum <= 64: # 64%
        return "Common"
    elif randNum <= 84: # 20%
        return "Uncommon"
    elif randNum <= 94: # 10%
        return "Rare"
    elif randNum <= 99: # 5%
        return "Epic"
    elif randNum > 99: # 1%
        return "Legendary"
    else:
        return "Error"

def rarityBonus(weapon: Weapon) -> float:
    if weapon.rarity == "Common":
        return 0
    elif weapon.rarity == "Uncommon":
        return 1
    elif weapon.rarity == "Rare":
        return 3
    elif weapon.rarity == "Epic":
        return 5
    elif weapon.rarity == "Legendary":
        return 10

def randomWeapon(player: Player) -> Weapon:
    newWeapon = Weapon()

    if player.playerClass == "Melee":
        newWeapon.name = randomPrefix() + " " + randomSwordName()

        newWeapon.rarity = randomRarity()

        newWeapon.damage = 1
        for i in range(5):
            newWeapon.damage += int(random.randrange(1, 6 + rarityBonus(newWeapon)) / 5)
        
        newWeapon.critChance = 0.1
        for i in range(5):
            newWeapon.critChance += int(random.randrange(1, 8 + rarityBonus(newWeapon)) / 5) * 0.1
        
        newWeapon.critDamage = 0.5
        for i in range(5):
            newWeapon.critDamage += int(random.randrange(1, 11 + rarityBonus(newWeapon) * 5) / 8) * 0.1
        
        if rarityBonus(newWeapon) < 10:
            if int(random.randrange(1 + rarityBonus(newWeapon), 11) / 10) == 1:
                newWeapon.modifier = randomModifier()
            else:
                newWeapon.modifier = modifiers.none
        else:
            if int(random.randrange(1 + rarityBonus(newWeapon), 12) / 10) == 1:
                newWeapon.modifier = randomModifier()
            else:
                newWeapon.modifier = modifiers.none

        newWeapon.critChance = round(newWeapon.critChance, 1)
        newWeapon.critDamage = round(newWeapon.critDamage, 1)

        return newWeapon

    elif player.playerClass == "Range":
        newWeapon.name = randomPrefix() + " " + randomBowName()

        newWeapon.rarity = randomRarity()

        newWeapon.damage = 1
        for i in range(5):
            newWeapon.damage += int(random.randrange(1, 11 + rarityBonus(newWeapon)) / 10)
        
        newWeapon.critChance = 0.1
        for i in range(5):
            newWeapon.critChance += int(random.randrange(1, 8 + rarityBonus(newWeapon)) / 5) * 0.25
        
        newWeapon.critDamage = 0.5
        for i in range(5):
            newWeapon.critDamage += int(random.randrange(1, 11 + rarityBonus(newWeapon) * 3) / 8) * 0.2
        
        newWeapon.critChance = round(newWeapon.critChance, 1)
        newWeapon.critDamage = round(newWeapon.critDamage, 1)

        if rarityBonus(newWeapon) < 10:
            if int(random.randrange(1 + rarityBonus(newWeapon), 11) / 10) == 1:
                newWeapon.modifier = randomModifier()
            else:
                newWeapon.modifier = modifiers.none
        else:
            if int(random.randrange(1 + rarityBonus(newWeapon), 12) / 10) == 1:
                newWeapon.modifier = randomModifier()
            else:
                newWeapon.modifier = modifiers.none

        return newWeapon
    else:
        newWeapon = starterWeapons.meleeStarter
        newWeapon.name = "An error has occurred"



def playerAttack(player: Player, enemy: Enemy):
    damage = player.weapon.damage

    critChance = player.weapon.critChance

    critDamage = player.weapon.critDamage

    finalDamage = damage
    crits = 0

    for crit in range(int(critChance)):
        finalDamage *= (critDamage + 1)
        crits += 1
    
    if random.randrange(1, 100) <= (critChance * 100) % 100:
        finalDamage *= (critDamage + 1)
        crits += 1
    
    finalDamage = int(finalDamage)

    if player.weapon.modifier.name == "Lifesteal":
        healAmount = 1
        for i in range(int(finalDamage)):
            healAmount += int(random.randrange(0, 6) / 5)
        if healAmount > 0:
            player.hp += healAmount
            if player.hp > player.maxhp:
                player.hp = player.maxhp
            sleep(0.1)
            print(f"Lifesteal healed: {healAmount} HP")
            sleep(0.1)
            print(f"Your HP is now {player.hp}")
            
    
    enemy.hp -= finalDamage
    if crits != 0:
        print(f"You dealt {finalDamage} Damage and Crit {crits} times!")
    else:
        print(f"You dealt {finalDamage} Damage")



def heal(player: Player) -> int:
    healAmount = 1
    if player.weapon.modifier.name == "Heal Boost":
        for i in range(int(player.maxhp)):
            healAmount += int(random.randrange(0, 8) / 5)
    else:
        for i in range(int(player.maxhp / 1.5)):
            healAmount += int(random.randrange(0, 6) / 5)
    return healAmount

def playerFightAction() -> str:
    action = ""
    while action != "Fight" and action != "Heal":
        action = input("\nWould you like to Fight or Heal?: ")
    return action

def main():
    player = Player()
    world = World()



    def fight() -> bool: # Returns True if the battle was won.
        enemy = Enemy()
        enemy.maxhp = 5 + int((world.level**2) / 100 * world.difficulty)
        enemy.hp = enemy.maxhp
        enemy.damage = int((((world.level)**2) / 1000 * world.difficulty) + 1)

        while player.hp > 0 and enemy.hp > 0:
            sleep(0.5)
            playerAction = playerFightAction()
            if playerAction == "Fight":
                playerAttack(player,enemy)
                sleep(0.1)
                if enemy.hp > 0:
                    print(f"The Enemy has {enemy.hp} HP left")
            elif playerAction == "Heal":
                healAmount = heal(player)
                player.hp += healAmount
                if player.hp > player.maxhp:
                    player.hp = player.maxhp
                print(f"You healed {healAmount} HP")

            if enemy.hp > 0:
                sleep(0.5)
                enemyDamageDealt = enemy.damage + random.randint(-1, 1)
                player.hp -= enemyDamageDealt
                print(f"The Enemy dealt {enemyDamageDealt} damage")
                if enemyDamageDealt > 0:
                    sleep(0.1)
                    print(f"Your HP is now {player.hp}")
        
        if enemy.hp <= 0:
            print("You won!\n")
            world.level += 1
            if player.weapon.modifier.name == "Health Bonus":
                player.maxhp += 1
                sleep(0.25)
                print("Health Bonus increased your Max Hp by 1")
                sleep(0.1)
                print(f"Your HP is now {player.maxhp}")
            if player.weapon.modifier.name == "\033[95mChaos\033[0m":
                randStat = random.randrange(1,4)
                if randStat == 1:
                    randChange = random.randrange(-1,2)
                    player.weapon.damage += randChange
                    print(f"\033[95mChaos!\033[0m Damage changed by {randChange}")
                elif randStat == 2:
                    randChange = random.randrange(-5,6) / 10
                    player.weapon.critChance += randChange
                    print(f"\033[95mChaos!\033[0m Crit Chance changed by {int(randChange * 100)}%")
                elif randStat == 3:
                    randChange = random.randrange(-5,6) / 10
                    player.weapon.critDamage += randChange
                    print(f"\033[95mChaos!\033[0m Crit Damage changed by {int(randChange * 100)}%")
            return True
        elif player.hp <= 0:
            print("You Lost!")
            print(f"You made it to level {world.level}")
            return False
    
    def compareStats(weapon1: Weapon, weapon2: Weapon):
        rarityColor1 = ""
        if weapon1.rarity == "Common":
            rarityColor1 = "\033[97m"
        elif weapon1.rarity == "Uncommon":
            rarityColor1 = "\033[92m"
        elif weapon1.rarity == "Rare":
            rarityColor1 = "\033[94m"
        elif weapon1.rarity == "Epic":
            rarityColor1 = "\033[95m"
        elif weapon1.rarity == "Legendary":
            rarityColor1 = "\033[93m"
        rarityColor2 = ""
        if weapon2.rarity == "Common":
            rarityColor2 = "\033[97m"
        elif weapon2.rarity == "Uncommon":
            rarityColor2 = "\033[92m"
        elif weapon2.rarity == "Rare":
            rarityColor2 = "\033[94m"
        elif weapon2.rarity == "Epic":
            rarityColor2 = "\033[95m"
        elif weapon2.rarity == "Legendary":
            rarityColor2 = "\033[93m"
        
        print(f"\nYour weapon: {weapon1.name}" + f"New weapon: {weapon2.name}".rjust(40))
        print("Rarity: " + rarityColor1 + f"{weapon1.rarity}\033[0m" + "Rarity: ".rjust(40) + rarityColor2 + f"{weapon2.rarity}\033[0m")
        print(f"Damage: {weapon1.damage}" + f"Damage: {weapon2.damage}".rjust(40))
        print(f"Crit Chance: {int(weapon1.critChance * 100)}%" + f"Crit Chance: {int(weapon2.critChance * 100)}%".rjust(40))
        print(f"Crit Damage: {int(weapon1.critDamage * 100)}%" + f"Crit Damage: {int(weapon2.critDamage * 100)}%".rjust(40))
        print(f"\nModifier: {weapon1.modifier.name}" + f"Modifier: {weapon2.modifier.name}".rjust(40))
        print(f"{weapon1.modifier.description}" + f"{weapon2.modifier.description}".rjust(40))
        
        decision = ""
        while decision != "Swap" and decision != "S" and decision != "Drop" and decision != "D":
            decision = input("\nWould you like to Swap or Drop this new weapon?: ")
        if decision == "Swap" or decision == "S":
            player.weapon = weapon2
            print("Swapped weapon")
            return
        elif decision == "Drop" or decision == "D":
            return
    
    def loot():
        lootRNG = random.randrange(1, 12)
        if lootRNG <= 3: # Item
            print("You found a new weapon!")
            compareStats(player.weapon, randomWeapon(player))
        elif lootRNG <= 5: # MaxHP Increase
            healAmount = 1
            for i in range(10): # Reusing the heal code but with lower chances.
                healAmount += int(random.randrange(0, 11) / 10)
            player.maxhp += healAmount
            if healAmount > 0:
                print(f"Max HP has been increased by {healAmount} HP")
            else:
                if player.weapon.modifier.name == "Weapon Luck":
                    print("Weapon Luck! You found a new weapon!")
                    compareStats(player.weapon, randomWeapon(player))
                else:
                    print("You got nothing!")
        elif lootRNG <= 9: # A free Heal
            print("You got a free heal!")
            sleep(0.1)
            healAmount = heal(player)
            player.hp += healAmount
            if player.hp > player.maxhp:
                player.hp = player.maxhp
            print(f"You healed {healAmount} HP")
        elif lootRNG == 10: # Mostly Nothing
            if player.weapon.modifier.name == "Weapon Luck":
                print("Weapon Luck! You found a new weapon!")
                compareStats(player.weapon, randomWeapon(player))
            else:
                print("You got nothing!")

    classInput = ""
    while classInput != "Melee" and classInput != "M" and classInput != "Range" and classInput != "R":
        clear()
        print("\033[91mPLEASE NOTE EVERYTHING IS CASE SENSITIVE\033[0m\n")
        classInput = input("Which class would you like to pick?\n" \
        "\033[91mMelee\033[0m: High Damage, Low Crit\n" \
        "\033[94mRange\033[0m: Low Damage, High Crit\n\n" \
        "Select a class: ")
    if classInput == "Melee" or classInput == "M":
        player.weapon = starterWeapons.meleeStarter
        player.playerClass = "Melee"
    elif classInput == "Range" or classInput == "R":
        player.weapon = starterWeapons.rangeStarter
        player.playerClass = "Range"
    else:
        return(1)
    difficultyInput = 0
    while difficultyInput <= 0:
        clear()
        difficultyInput = int(input("Choose the difficulty\n1 = Easy, 2 = Normal, 3 = Hard, and can be increased basically infinitely (but no decimal)\nDifficulty: "))
    world.difficulty = difficultyInput

    while fight():
        sleep(0.5)
        loot()
    sleep(1)
    input("Press Enter to continue")
    main()

main()

