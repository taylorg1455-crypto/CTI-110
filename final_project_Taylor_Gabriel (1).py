# Gabriel Taylor
# 09/30/26
# Final Project
# Game where you create a character and embark on an adventure to save the world


import random, time

def main():
    
    Knight = {'Name': 'Knight', 'Health': 100, 'Damage': 30}
    Samurai = {'Name': 'Samurai', 'Health': 75, 'Damage': 33}
    Archer = {'Name': 'Archer', 'Health': 50, 'Damage': 38}
    Sorcerer = {'Name': 'Sorcerer', 'Health': 20, 'Damage': 50}
    Hollow = {'Name': 'Hollow', 'Health': 60, 'Damage': 10, 'Accuracy': 80}
    Maliketh = {'Name': 'Maliketh', 'Health': 300,  'Damage': 30, 'Accuracy': 100}
    classes = [Knight, Samurai, Archer, Sorcerer]

    print("!!!Read!!!")
    time.sleep(2)
    print("In this game you will have the option to attack or dodge your enemies")
    time.sleep(3)
    print("In order to dodge you will need to react quickly by pressing: (Enter)")
    time.sleep(2)
    print("If you dodge too early or too late you will take damage --> dodge when the enemy attacks")
    claw = 0
    def upgrade(p_class_r):
        time.sleep(2)
        print("You encounter a merchant who gives you the choice of 2 items")
        time.sleep(2)
        print("\nA Health Potion or a Weapon Upgrade")
        p_up = input("Health Upgrade(1)  Weapon Upgrade(2): ")
        if p_up == '1':
            time.sleep(1)
            print("You chose the Health Upgrade --> Health boosted by 50")
            p_class_r['Health'] += 50
        elif p_up == '2':
            time.sleep(1)
            print("You chose the Damage Upgrade --> Damage boosted by 20")
            p_class_r['Damage'] += 20
        else:
            print("You didn't choose an upgrade")
    

    def create_character():
        name = input("Enter Name:\n")
        print(Knight,'\n',Samurai,'\n',Archer,'\n',Sorcerer,'\n')
        pick_class = input("Pick your class: (Input their name)\n")
        
        player_class = {}
        if pick_class == 'Knight':
            player_class = Knight
        elif pick_class == 'Samurai':
            player_class = Samurai
        elif pick_class == 'Archer':
            player_class = Archer
        elif pick_class == 'Sorcerer':
            player_class = Sorcerer
        player_class['Name'] = name
        return player_class
        
        print(f'You picked {pick_class}\n{player_class}')
        
    def player_attack(p_class_r):
        
        attack = random.randint(10,p_class_r['Damage'])
        return attack
    
    def boss_attack(p_class_r):
        boss_att = random.randint(14,Maliketh['Damage'])
        p_class_r['Health'] -= boss_att
        print(f"Maliketh did {boss_att} damage!")
        time.sleep(2)
    
    def boss_dodge(timer, p_class_r):
        if timer < .2:
            time.sleep(1)
            print("\nToo Early")
            boss_attack(p_class_r)
        
        elif timer > .5:
            time.sleep(1)
            print("Too Late")
            boss_attack(p_class_r)
        else:
            print("You dodged the attack")
            time.sleep(1)
            print("\nYou counter-attack")
            time.sleep(1)
            dam = player_attack(p_class_r)
            Maliketh['Health'] -= dam
            print(f"\nYou did {dam} damage")
        time.sleep(2)
    
        
    def enemy_fight(p_class_r):
        time.sleep(3)
        print("\nYou encounter a Hollow whilst traveling through the woods\n")
        time.sleep(3)
        holl_att = Hollow['Accuracy']
        
        while Hollow['Health'] > 0:
            
            att_val = random.randint(1,Hollow['Damage'])
            
            val = random.randint(1,4)
                        
            if val > 1:
                print("\n***Hollow prepares to attack***\n")
                time.sleep(random.uniform(1,4))

                print("Hollow Attacks!")
                start = time.perf_counter()
                p_act = input("Attack(1) or Dodge(Enter)")
                end = time.perf_counter()

                time.sleep(2)
                if p_act == '1':
                    dam = player_attack(p_class_r)
                    Hollow['Health'] -= dam
                    print(f"You did {dam} damage!")

                    if holl_att > random.randint(1,100):
                        p_class_r['Health'] -= att_val
                        print(f"Hollow did {att_val} damage!")
                    else:
                        print('Hollow Missed')
                else:
                    if end-start < .2:
                        print()
                        time.sleep(1)
                        print("You dodged too early!")
                        time.sleep(1)
                        if holl_att > random.randint(1,100):
                            p_class_r['Health'] -= att_val
                            print(f"Hollow did {att_val} damage!")
                        else:
                            time.sleep(2)
                            print('Hollow Missed')
                    elif end-start > .6:
                        time.sleep(1)
                        print("\nYou dodged too late!")
                        time.sleep(1)
                        if holl_att > random.randint(1,100):
                            p_class_r['Health'] -= att_val
                            print(f"Hollow did {att_val} damage!")
                        else:
                            print('Hollow missed')
                    else:
                        print('You dodged the attack!')
                        time.sleep(2)
                        print('You counter-attack')
                        time.sleep(2)
                        dam = player_attack(p_class_r)
                        Hollow['Health'] -= dam
                        print(f"You did {dam} damage")
                        time.sleep(2)
            else:
                print("Hollow Stalls")
                time.sleep(1)
                print('You attack')
                dam = player_attack(p_class_r)
                Hollow['Health'] -= dam
                print(f"You did {dam} damage")
                time.sleep(1)
            print(p_class_r)
            if p_class_r['Health'] <= 0:
                break
            time.sleep(2)
            print(Hollow)
            time.sleep(2)
        if p_class_r['Health'] <= 0:
            print('----You Died----')
        elif Hollow['Health'] <= 0:
            print("You defeated the Hollow!")
    
    def boss_fight(p_class_r):
        time.sleep(3)
        input("You come upon a decrepit castle and encounter: (Enter)")
        time.sleep(2)
        print("Maliketh, The Black Blade")
        time.sleep(2)
        print("Wielder of Death")
        time.sleep(3)
        while Maliketh['Health'] > 0:
                boss_act = random.randint(1,5)
                if boss_act >= 4:
                    print("\n******Maliketh uses Destined Death******\n")
                    
                    time.sleep(random.uniform(1,5))
                    start = time.perf_counter()
                    action = input("Attack(1) or Dodge(Enter)")
                    end = time.perf_counter()
                    timer = end - start
                    
                    if action == '1':
                        p_att = player_attack(p_class_r)
                        Maliketh['Health'] -= p_att
                        print(f"You did {p_att} damage\n")
                        time.sleep(2)
                        p_class_r['Health'] -= 99
                        print("!!!Maliketh did 99 damage!!!\n")
                    else:
                        if timer < .2 or timer > .6:
                            p_class_r['Health'] -= 99
                            time.sleep(1)
                            print("\n!!!You failed to evade!!!\n")
                            print("!!!Maliketh did 99 damage!!!\n")
                        else:
                            time.sleep(1)
                            print("You evaded the attack!\n")
                            time.sleep(2)
                            print("You counter-attack")
                            p_att = player_attack(p_class_r)
                            Maliketh['Health'] -= p_att
                            print(f"You did {p_att} damage\n")
                else:
                    print("\n***Maliketh uses quick swing***\n")
                    time.sleep(random.uniform(1,3))
                    start = time.perf_counter()
                    action = input("Attack(1) or Dodge(Enter)")
                    end = time.perf_counter()
                    timer = end-start
                    
                    if action == '1':
                        p_att = player_attack(p_class_r)
                        Maliketh['Health'] -= p_att
                        print(f"You did {p_att} damage!\n")
                        boss_attack(p_class_r)
                    else:
                        boss_dodge(timer,p_class_r)
                print(Maliketh,'\n',p_class_r,'\n')
                time.sleep(3)
                
                if p_class_r['Health'] <= 0:
                    print("You died")
                    break
                elif Maliketh['Health'] <= 0:
                    print("You defeated Maliketh")
    
    p_class = create_character()
    
    print("You are a traveler from a far off land\n")
    print("In this land nothing can die and life stagnates into corruption because of it\n")
    print("You must defeat the Black Blade in order to bring death back into this world\n")
    begin = input("Press Enter to Begin")
    
    enemy_fight(p_class)
    
    if p_class['Health'] <= 0:
        print()
    else:
        upgrade(p_class)
        boss_fight(p_class)
    
    if Maliketh['Health'] <= 0:
        print("\n--You saved the land and lived to tell the tale!--")
    elif p_class['Health'] and Maliketh['Health'] <= 0:
        print("\n--You died saving the land in the process!--")
    else:
        print("Game Over")

main()


# AI Prompts Used
# Show me a python game where you play as a character who fights a boss (ChatGPT)
# How do i add a reaction based mechanic in python (Claude)
# Can you explain time.perf_counter (Claude)