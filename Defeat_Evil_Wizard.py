import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
        if isinstance(self, EvilWizard):
            self.attack_power = 15

    def display_stats(self, opponent):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
        print(f"{opponent.name}'s Stats - Health: {opponent.health}/{opponent.max_health}, Attack Power: {opponent.attack_power}")

    def heal(self):
        if self.health <= self.max_health - 25:
            self.health += 25
            print(f"{self.name} heals for 25 points!")
        else:
            self.health = self.max_health
            print(f"{self.name} heals to full health!")
# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def power_slash(self, opponent):
        opponent.health -= self.attack_power*2
        print(f"{self.name} uses a powerful slash to attack {opponent.name} for {self.attack_power*2} damage!")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
    
    def fireball(self, opponent):
        bonus = random.randint(10, 25)
        opponent.health -= self.attack_power + bonus
        print(f"{self.name} attacks {opponent.name} with a fireball for {self.attack_power + bonus} damage!")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        if self.health <= self.max_health - 5:
            self.health += 5
            print(f"{self.name} regenerates 5 health! Current health: {self.health}")
        else:
            print(f"{self.name}'s Health is full!")

# Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)
    
    def quick_shot(self, opponent):
        opponent.health -= self.attack_power*2
        print(f"{self.name} attacks {opponent.name} for {self.attack_power*2} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    
    def evade(self, opponent):
        opponent.attack_power = 0
        print(f"{self.name} evades {opponent.name}'s attack!")
    


# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=25)
    
    def holy_strike(self, opponent):
        opponent.health -= self.attack_power*2.5
        print(f"{self.name} uses Holy Strike, inflicting {self.attack_power*2.5} damage on {opponent.name}!")
    
    def divine_shield(self, opponent):
        opponent.attack_power = 0
        print(f"{self.name} blocks {opponent.name}'s attack with Divine Shield!")

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") #Potential Class Add on
    print("4. Paladin")  #Potential Class Add on

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)  # Implement Archer class
    elif class_choice == '4':
        return Paladin(name) # Implement Paladin class
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Warrior):
                player.power_slash(wizard)
            elif isinstance(player, Mage):
                player.fireball(wizard)
            elif isinstance(player, Archer):
                special = input((f"--- Select Your Special Ability ---\n1.) Quick Shot\n2.) Evade\n: "))
                if special == '1':
                      player.quick_shot(wizard)
                elif special == '2':
                      player.evade(wizard)
                else:
                    print("Invalid choice. Try again.")
            elif isinstance(player, Paladin):
                special = input("Select Your Special Ability\n1.) Holy Strike\n2.) Divine Shield\n: ")
                if special == '1':
                    player.holy_strike(wizard)
                elif special == '2':
                    player.divine_shield(wizard)
                else:
                    print("Invalid choice. Try again.")
                          # Implement special abilities
        elif choice == '3':
            player.heal()  # Implement heal method
        elif choice == '4':
            player.display_stats(wizard)
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0 and choice != '4':
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"{wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
