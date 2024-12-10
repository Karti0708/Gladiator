import random
import time
import os
import pygame


pygame.mixer.init()
talking = pygame.mixer.Sound("talking2.mp3")

os.system("cls")
class Gladiator:
    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense

    def attack(self, opponent, attack_type):
        if attack_type == "snabb":
            attack_value = random.randint(5, self.attack_power - 5)
            slow_print(f"{self.name} utför en snabb attack!\n")
        elif attack_type == "kraftfull":
            attack_value = random.randint(self.attack_power - 5, self.attack_power + 5)
            slow_print(f"{self.name} utför en kraftfull attack!\n")
        else:
            attack_value = self.attack_power  
            slow_print(f"{self.name} utför en precis attack!\n")
        
        damage = max(attack_value - opponent.defense, 0)
        opponent.health -= damage
        slow_print(f"{self.name} attackerar {opponent.name} och orsakar {damage} skada!\n")
        return damage

    def is_alive(self):
        return self.health > 0

def slow_print(text, delay=0.02):
    i = 0
    for char in text:
        i+=1
        if i % 2 == 1:
            talking.play()
        print(char, end="", flush= True)
        
        time.sleep(delay)
    time.sleep(1)
    print()

def intro():
    slow_print("Välkommen till gladiatorarenan!")
    slow_print("Folket jublar och marken skakar av deras rop.")
    slow_print("Du, en ny gladiator, möter arenans mästare, Tybrus.")
    slow_print("Kommer du att kunna besegra honom och vinna ära och frihet?\n")

def main():
    intro()

    player_name = input("Ange ditt namn, kämpe: ")
    player_gladiator = Gladiator(player_name, 100, 20, 8)
    tybrus = Gladiator("Tybrus", 100, 18, 10)

    slow_print(f"\n{player_name}, du möter den mäktiga Tybrus i en episk kamp!\n")
    
    
    round_number = 1
    while player_gladiator.is_alive() and tybrus.is_alive():
        slow_print(f"\nRunda {round_number}:")

        
        slow_print("Välj din attack:")
        slow_print("1. Snabb (lägre skada men större chans att träffa)")
        slow_print("2. Kraftfull (högre skada men varierar)")
        slow_print("3. Precis (maximal skada men sällan)")
        choice = input("Ange ditt val (1/2/3): ")

        if choice == "1":
            player_attack_type = "snabb"
        elif choice == "2":
            player_attack_type = "kraftfull"
        else:
            player_attack_type = "precis"

       
        player_gladiator.attack(tybrus, player_attack_type)

        
        if tybrus.is_alive():
            
            tybrus_attack_type = random.choice(["snabb", "kraftfull", "precis"])
            tybrus.attack(player_gladiator, tybrus_attack_type)

        slow_print(f"{player_gladiator.name} hälsa: {player_gladiator.health}")
        slow_print(f"{tybrus.name} hälsa: {tybrus.health}")
        round_number += 1

    
    if player_gladiator.is_alive():
        slow_print(f"{player_gladiator.name} har segrat över Tybrus och vunnit sin frihet!")
    else:
        slow_print(f"Tybrus har besegrat {player_gladiator.name}. Äran är hans!")

if __name__ == "__main__":
    main()

