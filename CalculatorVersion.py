import random

def sleep(a):
    pass

class World:
    difficulty = 0
    level = 1

class Modifier:
    name = ""
    description = ""

class Weapon:
    name = ""
    rarity = ""
    damage = 0
    critChance = 0.0
    critDamage = 0.0
    modifier = Modifier()

class Player:
    maxhp = 10
    hp = 10
    weapon = Weapon()
    inv = [] # Not used!
    playerClass = ""

class Food: # Not used!
    hpGain = 0
    
class Enemy:
    maxhp = 0
    hp = 0
    damage = 0

def clear():
    for i in range(2):
        print("\n")

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
    chaos.name = "Chaos"
    chaos.description = "Has a chance to increase or decrease weapon stats"

def randomModifier():
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

def randomPrefix():
    return random.choice(["Strong", "Powerful", "Odd", "Unique", "Hurtful", "Forceful", "Agile", "Bloodthirsty", "Nasty", "Sharp", "Repaired", "Ancient"])

def randomSwordName():
    return random.choice(["Claymore", "Broadsowrd", "Longsword", "Dagger", "Katana", "Cutlass", "Knife", "Sword", "Hammer", "Bat"])

def randomBowName():
    return random.choice(["Bow", "Crossbow", "Slingshot", "Longbow", "Shortbow", "Pistol", "Shotgun", "Handgun", "Rifle", "Revolver"])

def randomRarity():
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

def rarityBonus(weapon):
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

def randomWeapon(player):
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
            if int(random.randrange(rarityBonus(newWeapon), 11) / 10) == 1:
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
            if int(random.randrange(rarityBonus(newWeapon), 11) / 10) == 1:
                newWeapon.modifier = randomModifier()
            else:
                newWeapon.modifier = modifiers.none

        return newWeapon
    else:
        newWeapon = starterWeapons.meleeStarter
        newWeapon.name = "An error has occurred"



def playerAttack(player, enemy):
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
            print("Lifesteal healed: " + str(healAmount) + " HP")
            sleep(0.1)
            print("Your HP is " + str(player.hp))
            
    
    enemy.hp -= finalDamage
    if crits != 0:
        print("You did " + str(finalDamage) + " Damage and Crit " + str(crits) + " times!")
    else:
        print("You did " + str(finalDamage) + " Damage")



def heal(player):
    healAmount = 1
    if player.weapon.modifier.name == "Heal Boost":
        for i in range(int(player.maxhp)):
            healAmount += int(random.randrange(0, 8) / 5)
    else:
        for i in range(int(player.maxhp / 1.5)):
            healAmount += int(random.randrange(0, 6) / 5)
    return healAmount

def playerFightAction():
    action = ""
    while action != "fight" and action != "heal" and action != "f" and action != "h":
        action = input("\nFight or Heal?: ")
    return action

def main():
    player = Player()
    world = World()

    def fight(): # Returns True if the battle was won.
        enemy = Enemy()
        enemy.maxhp = 5 + int((world.level**2) / 100 * world.difficulty)
        enemy.hp = enemy.maxhp
        enemy.damage = int((((world.level)**2) / 1000 * world.difficulty) + 1)

        while player.hp > 0 and enemy.hp > 0:
            sleep(0.5)
            playerAction = playerFightAction()
            if playerAction == "fight" or playerAction == "f":
                playerAttack(player,enemy)
                sleep(0.1)
                if enemy.hp > 0:
                    print("The Enemy has " + str(enemy.hp) + " HP")
            elif playerAction == "heal" or playerAction == "h":
                healAmount = heal(player)
                player.hp += healAmount
                if player.hp > player.maxhp:
                    player.hp = player.maxhp
                print("You healed " + str(healAmount) + " HP")

            if enemy.hp > 0:
                sleep(0.5)
                enemyDamageDealt = enemy.damage + random.randint(-1, 1)
                player.hp -= enemyDamageDealt
                print("The Enemy dealt " + str(enemyDamageDealt) + " damage")
                if enemyDamageDealt > 0:
                    sleep(0.1)
                    print("Your HP is " + str(player.hp))
        
        if enemy.hp <= 0:
            print("You won!\n")
            world.level += 1
            if player.weapon.modifier.name == "Health Bonus":
                player.maxhp += 1
                sleep(0.25)
                print("Health Bonus! +1 Max Hp")
                sleep(0.1)
                print("Your HP is " + str(player.maxhp) + "")
            if player.weapon.modifier.name == "Chaos":
                randStat = random.randrange(1,4)
                if randStat == 1:
                    randChange = random.randrange(-1,2)
                    player.weapon.damage += randChange
                    if randChange > -0.01:
                        print("Chaos! Damage +" + str(randChange))
                    else:
                        print("Chaos! Damage " + str(randChange))
                elif randStat == 2:
                    randChange = random.randrange(-5,6) / 10
                    player.weapon.critChance += randChange
                    if randChange > -0.01:
                        print("Chaos! Crit Chance +" + str(int(randChange * 100)) + "%")
                    else:
                        print("Chaos! Crit Chance " + str(int(randChange * 100)) + "%")
                elif randStat == 3:
                    randChange = random.randrange(-5,6) / 10
                    player.weapon.critDamage += randChange
                    if randChange > -0.01:
                        print("Chaos! Crit Damage +" + str(int(randChange * 100)) + "%")
                    else:
                        print("Chaos! Crit Damage " + str(int(randChange * 100)) + "%")
            return True
        elif player.hp <= 0:
            print("You Lost!")
            print("Died at level " + str(world.level))
            return False
    
    def compareStats(weapon1, weapon2):
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
        
        print("\n" + str(weapon1.name) + " " + str(weapon2.name))
        print(str(weapon1.rarity) + " " + str(weapon2.rarity))
        print(str(weapon1.damage) + " " + str(weapon2.damage))
        print(str(int(weapon1.critChance * 100)) + "%" + " " + str(int(weapon2.critChance * 100)) + "%")
        print(str(int(weapon1.critDamage * 100)) + "%" + " " + str(int(weapon2.critDamage * 100)) + "%")
        print(str(weapon1.modifier.name) + " " + str(weapon2.modifier.name))
        
        decision = ""
        while decision != "swap" and decision != "s" and decision != "drop" and decision != "d":
            decision = input("\nSwap or Drop this new weapon?: ")
            decision.lower()
        if decision == "swap" or decision == "s":
            player.weapon = weapon2
            print("Swapped weapon")
            return
        elif decision == "drop" or decision == "d":
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
                print("+" + str(healAmount) + " Max HP")
            else:
                if player.weapon.modifier.name == "Weapon Luck":
                    print("Weapon Luck!")
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
            print("You healed " + str(healAmount) + " HP")
        elif lootRNG == 10: # Mostly Nothing
            if player.weapon.modifier.name == "Weapon Luck":
                print("Weapon Luck!")
                compareStats(player.weapon, randomWeapon(player))
            else:
                print("You got nothing!")

    classInput = ""
    while classInput != "melee" and classInput != "m" and classInput != "range" and classInput != "r":
        clear()
        classInput = input("Pick a Class\n" \
        "Melee: High Damage, Low Crit\n" \
        "Range: Low Damage, High Crit\n\n" \
        "Select a class: ")
        classInput.lower()
    if classInput == "melee" or classInput == "m":
        player.weapon = starterWeapons.meleeStarter
        player.playerClass = "Melee"
    elif classInput == "range" or classInput == "r":
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









