import random

HP = 10
weapon = 'iron axe'
cont = 'What would you like to do next?'
name = input('What is your name?')
potions = 0
vamp_health = 5
vdmg = (abs(1),abs(2),abs(3),abs(5),abs(6))
pdmg = (abs(3),(4))
vhit1 = random.choice(vdmg)
hit1 =  random.choice(pdmg)
vhit2 = random.choice(vdmg)
hit2 =  random.choice(pdmg)
rat_health = 3
rdmg = (abs(3),abs(5))
phit1 = random.choice(pdmg)
rhit1 = random.choice(rdmg)

def forest():
    print('You enter a large empty clearing and spot what appears to be an entrance to an abandoned crypt on the other side...')
    print(cont)
    player_choice4 = input('\n1: Approach the crypt\n2: Return to the village\n')
    if player_choice4 == str(1):
        crypt()
    if player_choice4 == str(2):
        village()

def village():
    print('You approach the village gate and are greeted by a brawny gnome')
    print('Guard: "What is your business here?"')
    player_choice =input('\n1: Ask for directions\n2: Attack the guard\n3: Turn back and explore the forest\n')
    if player_choice == str(1):
        print('You ask the guard for directions back to your hometown')
        print('Guard: "Of course I know how to get there, but before I tell you, I need your help with an infestation of rats been bothering the locals. They\'re in that cave over yonder"')
        print(cont)
        player_choice2 = input('\n1: Sure, I can help you\n2: Can\'t you just tell me?\n3: Turn back and explore the forest\n')
        if player_choice2 == str(1):
            cave()
        if player_choice2 == str(2):
            print('Guard: "Not unless you come back with some gold, the other guards have been trying to make me head in there, Even I\'m not that crazy."')
            print(cont)
            player_choice3 = input('\n1:Fine, I\'ll enter the cave \n2:Turn back and explore the forest\n')
            if player_choice3 == str(1):
                cave()
            if player_choice3 == str(2):
                forest()
        if player_choice2 == str(3):
            forest()
    if player_choice == str(2):
        print(f'You attempt to attack the guard with your {weapon}, but he draws his sword and stabs you in the chest dealing 10HP!')
        print(f'Remaining Health:{HP - 10}')
        print(f'You have died!')
        input('Press RETURN to continue:')
    if player_choice == str(3):
        forest()

def crypt():
    print('You approach the dark and mysterious crypt, it looks as if it hasn\'t been touched in ages, there is a staircase leading down into the darkness...')
    print(cont)
    player_choice5 = input('\n1: Light your torch, descend the staircase and enter the crypt\n2: Return to the forest\n')
    if player_choice5 == str(1):
        path()
    if player_choice5 == str(2):
        forest()

def path():
    print('While making your way through the crypt you find a branching path...')
    print(cont)
    player_choice6 = input('\n1: Go left\n2: Go right\n3: Return to the forest\n')
    if player_choice6 == str(1):
        print('You head left and find an old store room filled with wooden crates')
        print(cont)
        player_choice7 = input(' 1: Search the crates\n 2: Go back to the branching path\n')
        if player_choice7 == str(1):
            print('You search the crates and find an Iron axe!')
            print(f'New Weapon Obtained:{weapon}')
            print(cont)
            input(' 1:Go back to the branching path\n')
            path()
        if player_choice7 == str(2):
            path()
    if player_choice6 == str(2):
        print('You enter a dark room with a stone coffin against the wall')
        print(cont)
        player_choice8 = input(' 1: Approach the coffin \n 2: Return to the branching path\n')
        if player_choice8 == str(2):
            path()
        if player_choice8 == str(1):
            print('You approach the coffin, the stone cover slides off and a vampire climbs out')
            print('Vampire: "How dare you disturb my slumber?"')
            print(cont)
            player_choice9 = input(' 1:Attack the vampire \n 2:Run out of the crypt and return to the forest\n')
            if player_choice9 == str(2):
                forest()
            if player_choice9 == str(1):
                global vamp_health
                vamp_health = vamp_health - hit1
                print(f'You swing your {weapon} at the vampire dealing {hit1} damage!')
                print(f'The vampire has {vamp_health} HP remaining!')
                print('The vampire screams out in pain and bites down hard on your shoulder!')
                global HP
                HP = HP - vhit1
                print(f'The bite deals {vhit1} damage!')
                print(f'You have {HP} HP remaining!')
                print(cont)
                player_choice10 = input(' 1:Attack the vampire again \n 2:Run out of the crypt and return to the forest\n')
                if player_choice10 == str(2):
                    forest()
                if player_choice10 == str(1):
                    vamp_health = vamp_health - hit2
                    print(f'You swing your {weapon} at the vampire dealing {hit2} damage!')
                    print(f'The vampire has {vamp_health} HP remaining!')
                    print('The vampire screams out in pain and bites down hard on your shoulder!')
                    HP = HP - vhit2
                    print(f'The bite deals {vhit2} damage!')
                    print(f'You have {HP} HP remaining!')
                if vamp_health <= 0:
                    print('The vampire dies and turns to dust...!\n')
                if HP <= 0:
                    print('You have died! you suck')
                    input('\nPress RETURN to continue:')
                print(cont)
                player_choice11 =input(' 1:Search the vampires coffin \n 2:Return to the Forest\n')
                if player_choice11 == str(2):
                    forest()
                if player_choice11 == str(1):
                    print('You find a large gold amulet! This could be worth a lot of money...')
                    print(cont)
                    player_choice12 = input(' 1:Return to the village guard\n')
                    if player_choice12 == str(1):
                        end1()




    if player_choice6 == str(3):
        forest()

def cave():
    print('You\'re standing outside the entrance to the cave that the gnome guard told you about.')
    print(cont)
    player_choice12 = input(' 1:Enter the cave \n 2:Return to the village\n')
    if player_choice12 == str(2):
        village()
    if player_choice12 == str(1):
        print('You make your way into the rat infested cave with your torch in one hand and an iron dagger in the other.')
        print('Suddenly, a giant rat peers out from a corner before scurrying away...')
        print(cont)
        player_choice13 =input(' 1: Venture deeper into the cave \n 2:Return to the village\n')
        if player_choice13 == str(2):
            village()
        if player_choice13 == str(1):
            print('You continue your adventure into the cave and are attacked by a giant rat!')
            print(f'The rat bites you in the ankle dealing {rhit1} damage! ')
            global HP
            HP = HP - rhit1
            print(f'You have {HP} HP remaining!')
            print(cont)
            player_choice14 = input(' 1:Attack the rat \n 2:Flee the cave and return to the village\n')
            if player_choice14 == str(1):
                print(f'You swing your {weapon} at the rat dealing {phit1} damage!')
                global rat_health
                rat_health = rat_health - phit1
                print(f'The rat has {rat_health} HP remaining!')
                print('The giant rat screeches and dies!')
                print(cont)
                player_choice15 = input(' 1:Return to the guard and tell him you are finished\n')
                if player_choice15 == str(1):
                    end2()

def end1():
    print('You make your way back to the village guard and hand over the amulet')
    print('Guard: "Fine, I guess since you got me this amulet I can tell you how to get home"')
    print('A battalion of gnomes leads you back to your home village, The End!')
    input('Press RETURN to close')



def end2():
    print('You make your way back to the village guard and tell him you took care of his rat problem')
    print('Guard: Fine, I guess since you helped me out I can tell you how to get home"')
    print('A battalion of gnomes leads you back to your home village, The End!')
    input('Press RETURN to close')

print(f"{name}, you are an adventurer lost in a large, dense forest...")
print("You come across a small gnome village deep in the forest")
print(cont)
player_choice1 = input('\n1: Approach the village\n2: Turn back and explore the forest\n')
if player_choice1 == str(1):
    village()
if player_choice1 == str(2):
    forest()
