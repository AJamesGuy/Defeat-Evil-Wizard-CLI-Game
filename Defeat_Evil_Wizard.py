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
        bonus = random.randint(10, 25)
        opponent.health -= self.attack_power + bonus
        print(f"{self.name} uses a powerful slash to attack {opponent.name} for {self.attack_power + bonus} damage!")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
    
    def fireball(self, opponent):
        bonus = random.randint(10, 25)
        opponent.health -= self.attack_power + bonus
        print(f"{self.name} attacks {opponent.name} with a fireball for {self.attack_power + bonus} damage!")
    
    def absord_health(self, opponent):
        damage = random.randint(10, 20)
        self.health += damage
        opponent.health -= damage
        print(f"{self.name} heals for {damage} points and inflicts {damage} damage on {opponent.name}")

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
        bonus = random.randint(10, 25)
        opponent.health -= self.attack_power + bonus
        print(f"{self.name} attacks {opponent.name} for {self.attack_power + bonus} damage!")
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
        bonus = random.randint(10, 30)
        opponent.health -= self.attack_power + bonus
        print(f"{self.name} uses Holy Strike, inflicting {self.attack_power + bonus} damage on {opponent.name}!")
    
    def divine_shield(self, opponent):
        opponent.attack_power = 0
        print(f"{self.name} blocks {opponent.name}'s attack with Divine Shield!")

class BattleMage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
    
    def health_to_damage(self, opponent):
        self.health -= 15
        opponent.health -= 15
        print(f"{self.name} uses his lifeforce to attack {opponent.name} for 15 damage!")
        print(f"{self.name} -15, {opponent.name} -15")

    def magic_sword(self, opponent):
        damage = random.randint(15, 30)
        opponent.health -= self.attack_power + damage
        print(f"{self.name} uses his magic sword to inflict {self.attack_power + damage} points of damage on {opponent.name}!")

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") #Potential Class Add on
    print("4. Paladin")  #Potential Class Add on
    print("5. Battle Mage")

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
    elif class_choice == '5':
        return BattleMage(name)
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
        print("5. QUIT")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Warrior):
                player.power_slash(wizard)
            elif isinstance(player, Mage):
                special = input("--- Select Your Special Ability ---\n1.) Fireball\n2.) Absorb Health\n: ")
                if special == '1':
                    player.fireball(wizard)
                elif special == '2':
                    player.absord_health(wizard)
                else:
                    print("Invalid choice. Try again.")
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
            elif isinstance(player, BattleMage):
                special = input("-- Select Your Special Ability ---\n1.) Health to Damage (WARNING)\n2.) Magic Sword\n: ")
                if special == '1':
                    player.health_to_damage(wizard)
                elif special == '2':
                    player.magic_sword(wizard)
                else:
                    print("Invalid choice. Try again.")
                          # Implement special abilities
        elif choice == '3':
            player.heal()  # Implement heal method
        elif choice == '4':
            player.display_stats(wizard)
        elif choice == '5':
            break
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
