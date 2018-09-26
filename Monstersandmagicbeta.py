import random, sys, time, copy
sys.tracebacklimit = 0
print("Welcome to MONSTERS AND MAGIC BETA")
name = input("What is your name?\n")
if name.lower() == "miles":
    print("Hello God!")
else:
    print("Hello carbon based creature who is inferior to Miles!")
time.sleep(0.50)

if name.lower() != "miles":
    race = str(input("What race do you want to be (you can be a human, dwarf, or elf)\n")).lower()
elif name.lower() == "miles":
    race = "elf"
    print("You are an elf.")
time.sleep(0.50)

if race != "dwarf" and race != "human" and race != "elf":
    raise Exception("IBM Error (Idiot Behind Machine)")
else:
    print("Hello", name, "the", race)
yourturn = True
coins = 20
points = 0
#make how to check money
def checkmoney():
    print("You have", coins, "gold pieces!")


#check how much money you have
checkmoney()

class Creature:
    def __init__(self, health, damage, speed, dead=False):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.dead = dead


    def update(self):
        if self.health <= 0:
            print("You killed the your enemey, you got one point")
            points += 1
            self.dead = True
            del self
class Player:
    def __init__(self, health, damage, speed, dead=False):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.dead = dead
    def update(self):
        if self.health <= 0:
            print("You died the game is now over. You got", points, "points!")
            self.dead = True
            sys.exit(0)

#stats are out of 10
goblin = Creature(4, 5, 8)
bandit = Creature(7, 7, 5)
orc = Creature(8, 8, 2)
you = Player(20, 20, 20)

def health_check(creature_name):
    print(creature_name.health)
#make how to fight
def fight():
    global coins
    global yourturn
    global points
    enemies = random.randint(1,5)
    enemyrace = random.randint(1,3)
    if enemyrace == 1:
        if enemies == 1:
            enemyname = "Goblin"
            enemytype = copy.copy(goblin)
            #RESET
            enemytype = copy.copy(goblin)
        if enemies !=  1:
            enemyname = "Goblins"
            enemytype = copy.copy(goblin)
            #RESET
            enemytype = copy.copy(goblin)

    if enemyrace == 2:
        if enemies == 1:
            enemyname = "Orc"
            enemytype = copy.copy(orc)
            #RESET
            enemytype = copy.copy(orc)

        if enemies !=  1:
            enemyname = "Orcs"
            enemytype = copy.copy(orc)
            #RESET
            enemytype = copy.copy(orc)


    if enemyrace == 3:
        if enemies == 1:
            enemyname = "Bandit"
            enemytype = copy.copy(bandit)
            #RESET
            enemytype = copy.copy(bandit)
        if enemies !=  1:
            enemyname = "Bandits"
            enemytype = copy.copy(bandit)
            #RESET
            enemytype = copy.copy(bandit)
    #you see your enemies
    print()
    print("You see", enemies, enemyname + "!")
    action = str(input("What do you want to do? (fight, run, pay)\n")).lower()
    if action != "fight" and action != "run" and action != "pay":
        raise Exception("IBM Error (Idiot Behind Machine)")

    #your attack phase starts
    while True:
        if action == "fight" or action == "f":
            if yourturn == True:

                attack_choice = input("Would you like to attack or defend\n")
                print("It's your turn!")
                yourturn = False
            if attack_choice == "defend" or attack_choice == "d":
                print("The", enemyname, "are coming")
                dodgechance = random.randint(1, enemytype.speed)
                if dodgechance > 5:
                    print("You dodged, good job, now you are going to attack")
                if dodgechance < 5:
                    print("Oh no, the", enemyname, "hit you! You lose", str(enemytype.damage) + "!")
                    you.health -= enemytype.damage
                    you.update()
                    enemytype.update()

                attack_choice = "attack"
                yourturn = True
                continue

            elif attack_choice == "attack" or attack_choice == "a":
                print("You are now going to attack the enemy")
                print("*Clashing Sounds*")
                time.sleep(1.50)
                enemydodgechance = random.randint(1, you.speed)
                if enemydodgechance > 8:
                    print("The enemy dodged your attack!")
                elif enemydodgechance <= 5:
                    print("You hit the enemy!")
                    print("The enemy took", you.damage, "damage!")
                    enemytype.health -= you.damage
                    enemytype.update()
                    you.update()
                    if enemytype.dead:
                        break

                #switch attack phases
                attack_choice = "defend"
                continue

        #if you are going to run
        elif action == "run" or action == "r":
            print("Rolling dice...")
            runchance = random.randint(1,20)
            time.sleep(2)
            if runchance >= enemytype.speed:
                print("You rolled a", runchance, "and you needed", enemytype.speed)
                print("Good job, you escaped!")
                break
            elif runchance < enemytype.speed:
                print("You rolled a", runchance, "and you needed", enemytype.speed)
                print("Since you didn't escape you are going to fight the", enemyname)

        elif action == "pay" or action == "p":
            if coins >= 5:
                print("You are paying 5 gold pieces!")
                coins -= 5
                checkmoney()
                break
            elif coins < 5:
                print("You broke child, and you can't afford this so you gonna fight the", enemyname)
                continue



#the game actualy starts
fight()
print("You did it!")
