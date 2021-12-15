from basics import screenClear, pressEnter, confirm
import colours as c
import time
import random as r

def stats(self):
    atStat = "Attack:    "
    for i in range(self.attack):
        atStat += "■"
        if self.attack >= 10:
            atStat = "Attack:    \033[1;32;48m■■■■■■■■■■  MAX\033[1;37;48m"
    for i in range(10 - self.attack):
        atStat += "-"
    defStat = "Defence:   "
    for i in range(self.defence):
        defStat += "■"
        if self.defence >= 10:
            defStat = "Defence:   \033[1;32;48m■■■■■■■■■■  MAX\033[1;37;48m"
    for i in range(10 - self.defence):
        defStat += "-"
    charStat = "Charisma:  "
    for i in range(self.charisma):
        charStat += "■"
        if self.charisma >= 10:
            charStat = "Charisma:  \033[1;32;48m■■■■■■■■■■  MAX\033[1;37;48m"
    for i in range(10 - self.charisma):
        charStat += "-"
    intStat = "Intellect: "
    for i in range(self.intellect):
        intStat += "■"
        if self.intellect >= 10:
            intStat = "Intellect: \033[1;32;48m■■■■■■■■■■  MAX\033[1;37;48m"
    for i in range(10 - self.intellect):
        intStat += "-"
    agStat = "Agility:   "
    for i in range(self.agility):
        agStat += "■"
        if self.agility >= 10:
            agStat = "Agility:   \033[1;32;48m■■■■■■■■■■  MAX\033[1;37;48m"
    for i in range(10 - self.agility):
        agStat += "-"
    return str("Player Stats:\n\n"+atStat+"\n"+defStat+"\n"+charStat+"\n"+intStat+"\n"+agStat+"\nHealth Points: "+str(self.hp)+"\n")

def healthBar(self):
    hpAmount = '|'
    for i in range(self.hp//3):
        hpAmount += "■"
    for i in range((100 - self.hp)//3):
        hpAmount += "-"
    hpAmount += "| "+str(self.hp)+"%"
    print(hpAmount)

class Adib():
    def __init__(self): #overall balanced
        screenClear()
        self.attack = 3
        self.defence = 3
        self.charisma = 2
        self.intellect = 2
        self.agility = 3
        self.hp = 100
        self.name = 'Adib'
        #self.moto = "Mumei best girl >:)"
    #def levelUp(self):
        #for i in self.stats:
            #i += 1

    def __repr__(self):
        return stats(self)
        
class Mathieu():
    def __init__(self): #dominant in defence
        screenClear()
        self.attack = 3
        self.defence = 5
        self.charisma = 1
        self.intellect = 2
        self.agility = 2
        self.hp = 100
        self.name = 'Mathieu'
        #self.moto = "Looks like I'm gonna have to Miracle Johnson on you."

    def __repr__(self):
        return stats(self)

class Jacob():
    def __init__(self): #dominant in agility
        screenClear()
        self.attack = 2
        self.defence = 1
        self.charisma = 3
        self.intellect = 2
        self.agility = 5
        self.hp = 100
        self.name = 'Jacob'
        #self.moto = "I'm gonna Dust-eze out of here, the fish are calling me. *SCREECH*"

    def __repr__(self):
        return stats(self)

class Ali():
    def __init__(self): #dominant in charisma
        screenClear()
        self.attack = 3
        self.defence = 3
        self.charisma = 5
        self.intellect = 0
        self.agility = 2
        self.hp = 100
        self.name = 'Ali-Hassan'
        #self.moto = "MY FEET ARE NUMB MAN! UEEEAAAAAAAHHHHHHHH!!"

    def __repr__(self):
        return stats(self)

class Hadi():
    def __init__(self): #dominant in intellect
        screenClear()
        self.attack = 3
        self.defence = 1
        self.charisma = 2
        self.intellect = 5
        self.agility = 2
        self.hp = 100
        self.name = 'Hadi'
        #self.moto = "I'm gonna have to finish you, I don't care about your #DISTAVIE."

    def __repr__(self):
        return stats(self)

class Hussein():
    def __init__(self): #dominant in attack
        screenClear()
        self.attack = 5
        self.defence = 2
        self.charisma = 2
        self.intellect = 1
        self.agility = 3
        self.hp = 100
        self.name = 'Hussein'
        #self.moto = "Ayo fait attention sinon je vais te sucer les fesses >:)"

    def __repr__(self):
        return stats(self)

def levelUp(player):
    print(stats(player))
    print("Choose a stat to level up:\n'1' for Attack\n'2' for Defence\n'3' for Charisma\n'4' for Intellect\n'5' for Agility\n")
    while True:
        statChoice = str(input("Enter your choice: "))
        match statChoice:
            case '1':
                if confirm("Are you sure you want to level up attack? (y or n): ") == True:
                    player.attack += 1
                    break
            case '2':
                if confirm("Are you sure you want to level up defence? (y or n): ") == True:
                    player.defence += 1
                    break
            case '3':
                if confirm("Are you sure you want to level up charisma? (y or n): ") ==  True:
                    player.charisma += 1
                    break
            case '4':
                if confirm("Are you sure you want to level up intellect? (y or n): ") ==  True:
                    player.intellect += 1
                    break
            case '5':
                if confirm("Are you sure you want to level up agility? (y or n): ") ==  True:
                    player.agility += 1
                    break
            case _:
                c.red("Please input a number displayed.")        
                time.sleep(1.5)
    
    print(stats(player))
    pressEnter()
    screenClear()

def battle(player, opponent):
    print("Your HP:      ", player.hp, "\nOpponents HP: ", opponent.hp, "\n\nWhat will you do?")
    c.red("Attack:")
    print("1)Swift face punch from the left.\n2)Break dance hit from the right.\n3)Drop kick from the front.")
    c.red("Block:")
    print("4)Cover your left.\n5)Cover your right.\n6)Brace yourself for the hit.")
    c.red("Other:")
    print("7)Run away.\n8)Beg for mercy/surrender.\n\n")

    choices = []
    choices.append(str(input("Enter the number code of the action you want to take: ")))

    #below is the opponent decision algorithm

  #IT IS UNFINISHED FOR NOW  also dont worry i will optimise it with match cases later
    if choices[0] != '7':
        if choices[0] != '8':
            if opponent.intellect > player.intellect: #opponent makes a 'smart' decision
                if opponent.hp < 10: #if the opponent has low hp, they try to run or surrender
                    choices = []
                    choices.append('0')
                    if r.randint(1,2) == 1:
                        choices.append(7) #they run
                    else:
                        choices.append(8) #they surrender
                elif choices[0] <= '3':
                    choices.append(r.randint(4,6)) #if player attack, then Block
                elif choices[0] >= '5' and choices[0] <= '6':
                    choices.append(r.randint(1,3)) #if player blocks, then attack
        

            elif opponent.intellect == player.intellect: #makes a mediocre decision
                if choices[0] >= '3':
                    choices.append(r.randint(1,3)) #if player attack, then Block
                elif choices[0] <= '4' and choices[0] >= '6':
                    choices.append(r.randint(4,6)) #if player blocks, then attack
       
            
            else:
                choices.append(str(r.randint(1,6))) #makes a random decision (will not choose run or surrender because.. they're being stupid :))
        else:
            choices.append(0)
    else:
        choices.append(0)
    dmgO = 0 #dmg done to opponent
    dmgP = 0 #dmg done to player
    rand = 0 #the 'random' variable, see dmg calculator in any case below
    battleOver = False
    screenClear()
    print(choices) #REMOVE LATER
    match choices:
        case '1', 1: #player: punch, opp: punch
            if r.randint(1,2) == 1:
                rand = r.randint(4,7)
                dmgP = (rand*opponent.attack)//player.defence
                dmgO = (rand*player.attack)//opponent.defence
                print("You both throw a punch at each other.\nYou inflicted \033[1;31;48m"+str(dmgO)+"00000\033[1;37;48m point of dammage while taking \033[1;31;48m"+str(dmgP)+"00000\033[1;37;48m back.")  
            else:
                print("You both try to throw a punch at each other, however both powers cancel each other out thus causing \033[1;31;48mno dammage \033[1;37;48mto be done at all.")
        case '2', 1: 
            print(choices)
            
        case '3', 1:
            dmgO = (r.randint(6,8)*player.attack)//opponent.defence
            print("You drop kick on", opponent.name, ", kocking a tooth out and inflicting \033[1;31;48m"+str(dmgO)+"00000\033[1;37;48m points of dammage.")
            
        case '4', 1:
            print(opponent.name, "attempted to send a punch to your face, but you successfully blocked it with yo mousklees.")
            
        case '5', 1:
            dmgP = (r.randint(4,7)*opponent.attack)//player.defence
            print("You try put up your guard on your right, but", opponent.name, "sends a punch to your left dealing you \033[1;31;48m"+str(dmgP)+"00000\033[1;37;48m points of dammage.")
            
        case '6', 1:
            print(choices)


            
        case '1', 2: #player: punch, opp: bd
            rand = r.randint(3,6)
            dmgP = (rand*opponent.attack)//player.defence
            print("You attemp to throw a punch but ",opponent.name, "sweeps you off your feet with a low kick.\nYou were inflicted with \033[1;31;48m"+str(dmgP)+"00000\033[1;37;48m points of dammage.")
            
        case '2', 2:
            print(choices)
            
        case '3', 2:
            print(choices)
            
        case '4', 2:
            print(choices)
            
        case '5', 2:
            print(choices)
            
        case '6', 2:
            print(choices)

            


        case '1', 3:
            dmgP = (r.randint(6,8)*opponent.attack)//player.defence
            print("You block your left, but all you see is an eclipse of ", opponent.name, " falling from the sky and drop kicking the life outta you dealing \033[1;31;48m"+str(dmgP)+"00000\033[1;37;48m points of dammage.")
            
        case '2', 3:
            print(choices)
            
        case '3', 3:
            print(choices)
            
        case '4', 3:
            print(choices)
            
        case '5', 3:
            print(choices)
            
        case '6', 3:
            print(choices)

            


        case '1', 4:
            print(choices)
            
        case '2', 4:
            print(choices)
            
        case '3', 4:
            print(choices)

            


        case '1', 5:
            print(choices)
            
        case '2', 5:
            print(choices)
            
        case '3', 5:
            print(choices)


        case '1', 6 | '2', 6 | '3', 6: #player: punch/bd/dk, opp: braced
            dmgP = ((r.randint(1,3))*opponent.attack)//player.defence
            print(opponent.name, "braced himself for the attack.\nYou swiftly preform your signiture move!\nYou inflicted a total of \033[1;31;48m"+str(dmgP)+"00000\033[1;37;48m points of dammage.")
            

        case '0', 8:
            print(opponent.name, "begs you for mercy.")
            if player.charisma > opponent.charisma:
                print("Because of your supperior amount of charisma, you spare him and accept and easy win.")
            else:
                dmgO = 100
                print("You disregard his pathetic begging and prepare yourself to throw the final blow.")

        case '8', 0:
            print("You beg for mercy, surrendering your pride.")
            if opponent.charisma > player.charisma:
                print("with", opponent.name, "and his outstanding amount of charisma, he spares you. You must now accept defeat.")
            else:
                dmgP = 100
                print(opponent.name ,", not showing any signs of empathy kicks you arross the face while you lay there on your knees. Making you release your last breath.")
                    
        case '7', 0:
            if player.agility > opponent.agility:
                print("You succefully ran away like the coward you are.")
            else:
                print(opponent.name, "caught you by the leg and dragged you back to continue the fight. Not today ya coward.")
        case '0', 7:
            if oppoenent.agility > player.agility:
                print("Darn..", opponent.name, "\033[1;31;48mgot away \033[1;37;48m.")
            else:
                print("You caught up to", opponent.moto, "and dragged him by the leg to finish the fight. Not today cheif.")

        case '4', 4 | '5', 4 | '6', 4 | '4', 5 | '5', 5 | '6', 5 | '4', 6 | '5', 6 | '6', 6: #for any case that has both sides chosing a defensive move
            print("You both played defensively causing \033[1;31;48mno dammage \033[1;37;48mto be done at all.")

        case _:
            c.red("Please input a number displayed.")     
            time.sleep(1.5)
    
    opponent.hp -= dmgO
    player.hp -= dmgP
    print("\nYour HP:")
    healthBar(player)
    print("\nOpponent's HP:")
    healthBar(opponent)
    #if opponent.hp <= 0:
    
    pressEnter()



    #if opponent.hp <= 0:
        #playerXP += 5 * enemyLvl
        #if playerXP > 100:
            #playerXP -= 100
            #p.levelUp()
        #break