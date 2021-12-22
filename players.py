from basics import screenClear, pressEnter, slowType, confirm
import colours as c
import battle as b
import random as r
import time, json

def save(slot, self='blank', newFile=False):

    save = {}
    save['player'] = []
    save['progression'] = []
    if newFile == True:
        slowType("Creating save file... ")
        save['player'].append({
        'character': 'blank',
        'level': '0',
        'xp': '0',
        'hp': '0',
        'attack': '0',
        'defence': '0',
        'charisma': '0',
        'intellect': '0',
        'agility': '0',
        })
    else:
        slowType("Do not turn off the power. Saving your progress... ")
        save['player'].append({
        'character': self.name,
        'level': self.level,
        'xp': self.xp,
        'hp': self.hp,
        'attack': self.attack,
        'defence': self.defence,
        'charisma': self.charisma,
        'intellect': self.intellect,
        'agility': self.agility,
        })

        self.attack = 3
        self.defence = 3
        self.charisma = 2
        self.intellect = 2
        self.agility = 3
        self.hp = 100
        self.xp = 0
        self.level = 1
        self.name = 'Adib'

    with open("LAL_saveSlots/slot"+slot+'.txt', 'w') as outfile:
        json.dump(save, outfile)
    time.sleep(1) #simulates saving time (we just have so little data to save..)
    slowType("All done.")


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

def healthBar(self): #when you want to display someone's health, just do healthBar(player) for example
    hpAmount = self.name+'\'s HP:\n|'
    for i in range(self.hp//3):
        hpAmount += "■"
    for i in range((100 - self.hp)//3):
        hpAmount += "-"
    hpAmount += "| "+str(self.hp)+"%"
    print(hpAmount)

def xpBar(self, xp):
    xpAmountpre = '('
    xpAmountnew = ''
    xpAmountend = ''
    xpTotal = self.xp + xp
    for i in range(self.xp//2):
        xpAmountpre += "■"
    while xpTotal >= 100:
        self.level += 1
        xpTotal -= 100
        xp -= 100
    for i in range(xp//2):
        xpAmountnew += "□"
    for i in range((100 - xpTotal)//2):
        xpAmountend += "-"
    self.xp = xpTotal
    print(xpAmountpre+xpAmountnew+xpAmountend+") "+str(xpTotal)+"%\nCurrent level: "+str(self.level)+"\nLevel up in: "+str(100-xpTotal)+"xp")


def levelUp(self):
  slowType("Congratulations monke man, you have levelled up!")
  slowType("What would you like to improve? You have one",level_point,"to spend.\n"
  "A --- ATK"
  "B --- DEF"
  "C --- INT"
  "D --- CHA"
  "E --- AGI")
  levelChoice=input()
  try:
    if levelChoice=="A" or "ATK":
      self.attack+=1
      slowType("You have levelled up your attack. Congratulations, may you clap the cheeks of your enemies. Your attack is now", self.attack,".")
    elif levelChoice=="B" or "DEF":
      self.defence+=1
      slowType("You have levelled up your defense. Congratulations, may you be able to tank more damage, you filthy masoschist. Your defense is now",self.attack,".")
    elif levelChoice=="C" or "INT":
      self.intellect+=1
      slowType("You have levelled up your intellect. Congratulations, you are evolving from monke to ape, may your gorilla powers manifest themselves. Your intellect is now",self.intellect,".")
    elif levelChoice=="D" or "CHA":
      self.charisma+=1
      slowType("You have levelled up your charisma. Congratulations, you sexy beast, the laws of physics bend to your way with words :flushed:. Your charisma is now",self.charisma,".")
    elif levelChoice=="E" or "AGI":
      self.agility+=1
      slowType("You have levelled up your agility. Congratulations, you speedy boi, may you move faster than le jongleur eventually.",self.agility,".")
  except ValueError:
      slowType("Please select a valid option, note that the system is cap sensitive.")

class Adib():
    def __init__(self): #overall balanced
        screenClear()
        self.attack = 3
        self.defence = 3
        self.charisma = 2
        self.intellect = 2
        self.agility = 3
        self.hp = 100
        self.xp = 0
        self.level = 1
        self.name = 'Adib'
        self.moto = "Mumei best girl >:)"
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
        self.xp = 0
        self.level = 1
        self.name = 'Mathieu'
        self.moto = "Looks like I'm gonna have to Miracle Johnson on you."

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
        self.xp = 0
        self.level = 1
        self.name = 'Jacob'
        self.moto = "I'm gonna Dust-eze out of here, the fish are calling me. *SCREECH*"

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
        self.xp = 0
        self.level = 1
        self.name = 'Ali-Hassan'
        self.moto = "MY FEET ARE NUMB MAN! UEEEAAAAAAAHHHHHHHH!!"

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
        self.xp = 0
        self.level = 1
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
        self.xp = 0
        self.level = 1
        self.name = 'Hussein'
        self.moto = "Ayo fait attention sinon je vais te sucer les fesses >:)"

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
    battleOver = 0 #if 1, player lost. if 2, opponent lost.
    while battleOver == 0:
        dmgO = 0 #dmg done to opponent
        dmgP = 0 #dmg done to player
        rand = 0 #the 'random' variable, see dmg calculator in any case below
        screenClear()
        healthBar(player)
        healthBar(opponent)
        print("\nWhat will you do?")
        c.red("Attack:")
        print("1)Swift punch to the face\n2)Drop kick strike.\n3)Break dance on the monkster.") #Change if you want but 1) light attack 2) medium attack 3) heavy attack
        c.red("Block:")
        print("4)Cover your left.\n5)Cover your right.\n6)Brace yourself for the hit.")
        c.red("Other:")
        print("7)Run away.\n8)Beg for mercy/surrender.\n\n")
        while True:
            choices = [] #REMOVE
            choices.append(str(input("Enter the number code of the action you want to take: ")))
            if int(choices[0]) < 1 or int(choices[0]) > 8:
                c.red("Please input a number displayed.")     
                time.sleep(1.5)
                print("\033[A                                   \033[A") #reverts a line
                print("\033[A\033[A") #reverts a second line to reask the quesion without reprinting all the choices
            else:
                break
        
        
        #below is the opponent decision algorithm

    #IT IS UNFINISHED FOR NOW  also dont worry i will optimise it with match cases later
        if choices[0] != '7' and choices[0] != '8':
            if opponent.intellect > player.intellect: #opponent makesa 'smart' decision
                if opponent.hp <= 15: #if the opponent has low hp, they try to run or surrender
                    choices = []
                    choices.append('0')
                    if r.randint(1,2) == 1:
                        choices.append(7) #they run
                    else:
                        choices.append(8) #they surrender
                elif choices[0] <= '3':
                    if r.randint(1,4) == 2: #one on four chances of not blocking
                        choices.append(r.randint(1,3))
                    else:
                        choices.append(r.randint(4,6)) #if player attack, then Block
                elif choices[0] >= '5' and choices[0] <= '6':
                    if r.randint(1,4) == 2: #one on four chances of not attacking
                        choices.append(r.randint(4,6))
                    else:
                        choices.append(r.randint(1,3)) #if player blocks, then attack
                
            else:
                if r.randint(1,3): 
                    choices.append((r.randint(1,6)))
                else:
                    choices.append((r.randint(1,8)))
        else:
            choices.append(0)

        choices = []
        choices.append(str(1))
        choices.append(int(1))

        screenClear()
        print(choices) #REMOVE LATER
        b.Dmg()
        match choices:
            case '1', 1: #player: punch, opp: punch
                if r.randint(1,2) == 1:
                    rand = r.randint(7,11)
                    base_player_damage=rand*opponent.attack
                    base_player_defense=(rand*opponent.attack)*(player.defence/10)
                    base_opponent_damage=rand*player.attack
                    base_opponent_defense=(rand*player.attack)*(opponent.defence/10)
                    dmgP = base_player_damage-base_player_defense
                    dmgO = base_opponent_damage-base_opponent_defense
                    rounded_dmgP=round(dmgP,0)
                    rounded_dmgO=round(dmgO,0)
                    slowType("You both throw a punch at each other.\nYou inflicted \033[1;31;48m"+str(rounded_dmgO)+"00000\033[1;37;48m point of damage while taking \033[1;31;48m"+str(rounded_dmgP)+"00000\033[1;37;48m back.")  
                else:
                    slowType("You both try to throw a punch at each other, however both powers cancel each other out thus causing \033[1;31;48mno damage \033[1;37;48mto be done at all.")
            case '2', 1: 
                slowType("You show off your dance-fighting skills but only manage to intercept "+opponent.name+"'s flying fist causing \033[1;31;48mno damage \033[1;37;48mto be done.")
        
            case '3', 1:
                dmgO = (r.randint(14,17)*player.attack)//opponent.defence
                slowType("You drop kick on "+opponent.name+", kocking a tooth out and inflicting \033[1;31;48m"+str(dmgO)+"00000\033[1;37;48m points of damage.")
                
            case '4', 1:
                slowType(opponent.name+" attempted to send a punch to your face, but you successfully blocked it with yo mousklees.")
                
            case '5', 1:
                dmgP = (r.randint(14,17)*opponent.attack)//player.defence
                slowType("You try put up your guard on your right, but "+opponent.name+" sends a punch to your left dealing you \033[1;31;48m"+str(dmgP)+"00000\033[1;37;48m points of damage.")

            case '1', 2: #player: punch, opp: bd
                rand = r.randint(16,19)
                dmgP = (rand*opponent.attack)//player.defence
                slowType("You attemp to throw a punch but "+opponent.name+" sweeps you off your feet with a low kick.\nYou were inflicted with \033[1;31;48m"+str(dmgP)+"00000\033[1;37;48m points of damage.")
                
            case '2', 2:
                slowType("You try to do a nice high kick with style, but notice that "+opponent.name+" is doing the exact same and you both end up just dancing, causing \033[1;31;48mno damage \033[1;37;48mto be done. IS THIS A DANCE OFF OR WHAT??!")
                
            case '3', 2:
                dmgP = (r.randint(8,15)*opponent.attack)//player.defence
                slowType("You jump high in the air to land a drop kick on "+opponent.name+".\nBut he saw it coming. He punched your leg not the way its supposed to go before you could land your hit. Dealing you \033[1;31;48m"+str(dmgP)+"00000\033[1;37;48m points of damage.")
                
            case '4', 2:
                dmgP = (r.randint(10,14)*opponent.attack)//player.defence
                slowType('"'+opponent.moto+'!" screams '+opponent.name+'.\nWhile you foolishly attempt to cover your left side, '+opponent.name+' does an impressive spin kick and kocks you on the ground dealing you \033[1;31;48m'+str(dmgP)+'00000\033[1;37;48m points fo damage.') 
                
            case '5', 2:
                slowType(opponent.name+" attemps to do an upsidedown kick in ya face!\nBut this time, you were ready and successfully blocked it causing \033[1;31;48mno damage \033[1;37;48mto be dealt at all.")

            case '1', 3:
                dmgO = (r.randint(9,16)*player.attack)//opponent.defence
                slowType(opponent.name+" attempted to drop kick you but you take this oppoeruninty to upper-cut-punch the life energy out of him, dealing \033[1;31;48m"+str(dmgO)+"00000\033[1;37;48m points of damage.")
                
            case '2', 3:
                dmgO = (r.randint(10,17)*player.attack)//opponent.defence
                slowType("You wait for your oppenent's move, and as they attack you straight in the front, you feint and land a blow to their right, possibly shattering a rib, you say 'crounch', when the blow lands, dealing \033[1;31;48m"+str(dmgO)+"00000\033[1;37;48m points of damage.")
                
            case '3', 3:
                rand = r.randint(12,16)
                dmgP = (rand*opponent.attack)//player.defence
                dmgO = (rand*player.attack)//opponent.defence
                slowType("You lift up your leg, aiming directly for your opponent's face, but they punch in the same direction, and your blows connect. As they hit, time seems to slow, as massive amounts of energy are released, knocking you both back, as you take \033[1;31;48m"+str(dmgP)+"00000\033[1;37;48m point of damage while "+opponent.name+" takes \033[1;31;48m"+str(dmgO)+"00000\033[1;37;48m.")
                
            case '4', 3:
                dmgP = (r.randint(14,17)*opponent.attack)//player.defence
                slowType("You block your left, but all you see is an eclipse of "+ opponent.name+" falling from the sky and drop kicking the life outta you dealing \033[1;31;48m"+str(dmgP)+"00000\033[1;37;48m points of damage.")
                
            case '5', 3:
                dmgP = (r.randint(14,18)*opponent.attack)//player.defence
                slowType("Your opponent makes for your gut, however, as you raise your guard, they switch stance and hammer your side with a powerful kick. 'Damn, I wasn't able to rupture your kidney', your opponent says, nonetheless, you nearly retch from the pain, taking \033[1;31;48m"+str(dmgP)+"00000\033[1;37;48m points of damage.")

            case '1', 4:
                slowType("You attack quickly for your opponent's left, but they raise a block just in time, and your attack does \033[1;31;48m no damage\033[1;37;48m. You miraculously disengage before they can seize your arm and throw you over their shoulder.")
                
            case '2', 4:
                dmgO = (r.randint(11,16)*player.attack)//opponent.defence
                slowType("Your opponent prepares to block their left, but you throw all your weight behind a flap palm hit to their stomach's left, channeling your inner chi. As the blow hits, you approach them whispering to them 'Shit yourself yet?'. You do \033[1;31;48m"+str(dmgO)+"00000\033[1;37;48m points of damage.")
                
            case '3', 4:
                dmgO = (r.randint(13,17)*player.attack)//opponent.defence
                slowType(opponent.name+" prepares for your next move, anticipating an attack from the left, but you instead strike like a cobra, hitting them with your hand rigid and extended like a dagger, crushing the cartilage of their nose, doing \033[1;31;48m"+str(dmgO)+"00000\033[1;37;48m points of damage.")

            case '1', 5:
                dmgO = (r.randint(12,15)*player.attack)//opponent.defence
                slowType("You make for your opponent's right, forcing them to commit to a block, and once their block is set, you switch directions, and karate chop them in the left of their gut. You do \033[1;31;48m"+str(dmgO)+"00000\033[1;37;48m points of damage.")
                
            case '2', 5:
                dmgP = (r.randint(12,17)*opponent.attack)//player.defence
                slowType("You make for your opponent's right, where they seize your arm and smash a karate chop into your arm, dislocating it at the elbow, dealing massive damage, although by sacrificing your life chi to pop it back in place, you take \033[1;31;48m"+str(dmgP)+"00000\033[1;37;48m damage points.")
                
            case '3', 5:
                dmgO = (r.randint(11,16)*player.attack)//opponent.defence
                slowType("You make your opponent commit to a right block, but you strike, pouncing like a tiger and tackling them forward, knocking the air out of them and smashing your fist into their ribs, doing \033[1;31;48m"+str(dmgO)+"00000\033[1;37;48m damage.")

            case ['6', 1] | ['6', 2] | ['6', 3]: #player braces
                dmgp = ((r.randint(5,7))*player.attack)//opponent.defence
                slowType("You brace yourself, preparing for whatever comes.\n"+opponent.name+" takes a good smack at you. However, thanks to your mental preperation, you took a small \033[1;31;48m"+str(dmgp)+"00000\033[1;37;48m points of damage.")

            case ['1', 6] | ['2', 6] | ['3', 6]: #opponent braces
                dmgO = ((r.randint(5,7))*player.attack)//opponent.defence
                slowType(opponent.name+" braced himself for the attack.\nYou swiftly preform your signiture move!\nYou inflicted a total of \033[1;31;48m"+str(dmgO)+"00000\033[1;37;48m points of damage.")
            
            case '0', 8: #opponent surrenders
                slowType(opponent.name, "begs you for mercy.")
                if player.charisma > opponent.charisma:
                    battleOver = 2
                    slowType("\nThanks to your supperior amount of charisma, you spare him and accept and \033[1;31;48measy win\033[1;37;48m.")
                else:
                    dmgO = 100
                    slowType("You disregard his pathetic begging and prepare yourself to throw the final blow.")

            case '8', 0: #player surrenders
                slowType("You beg for mercy, surrendering your pride.")
                if opponent.charisma > player.charisma:
                    battleOver = 1
                    slowType("\nWith "+opponent.name+"'s outstanding amount of charisma, he spares you. \033[1;31;48mYou must now accept defeat.\033[1;37;48m")
                else:
                    dmgP = 100
                    slowType("\n"+opponent.name+", looks at you with disdain, and cruelly laughs as he lift you up from the neck with a single arm. As he crushes your windpipe with an iron grip, your world goes dark, you have \033[1;31;48mlost the fight\033[1;37;48m.")
                    
            case '7', 0: #player runs
                if player.agility > opponent.agility:
                    battleOver = 1
                    slowType("You succefully ran away like the coward you are.")
                else:
                    slowType(opponent.name+" caught you by the leg and dragged you back to continue the fight. Not today, coward.")
            case '0', 7: #opponent runs
                if oppoenent.agility > player.agility:
                    battleOver = 2
                    slowType("Darn.. "+opponent.name+"\033[1;31;48m got away \033[1;37;48m.")
                else:
                    slowType("You caught up to "+opponent.name+" and dragged him by the leg to finish the fight. Not today chief.")

            case ['4', 4] | ['5', 4] | ['6', 4] | ['4', 5] | ['5', 5] | ['6', 5] | ['4', 6] | ['5', 6] | ['6', 6]: #for any case that has both sides chosing a defensive move
                slowType("You both played defensively causing \033[1;31;48mno damage \033[1;37;48mto be done at all.")
            case _:
                c.red("An error occured. Please Try again.")     
                pressEnter()
    
        opponent.hp -= int(rounded_dmgO)
        player.hp -= int(rounded_dmgP)
        if opponent.hp <= 0 and player.hp <= 0:
            battleOver = 3  #if its a tie
            opponent.hp = 0
            player.hp = 0
        elif opponent.hp <= 0:
            battleOver = 2  #if opponent is dead
            opponent.hp = 0
        elif player.hp <= 0:
            battleOver = 1  #if player is dead
            player.hp = 0
        print("\n\nYour HP:")
        healthBar(player)
        print("\n"+opponent.name+"'s HP:")
        healthBar(opponent)

        pressEnter()

    if battleOver == 2:
        slowType("\n\033[1;36;48mYou win.\033[1;37;48m", 0.2)
    elif battleOver == 1:
        slowType("\n\033[1;31;48mYou lost.\033[1;37;48m", 0.2)
    else:
        slowType("\033[1;32;48mIt's a tie.\033[1;37;48m", 0.2)
    pressEnter()


    #if opponent.hp <= 0:
        #playerXP += 5 * enemyLvl
        #if playerXP > 100:
            #playerXP -= 100
            #p.levelUp()
        #break