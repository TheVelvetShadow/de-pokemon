

class Pokemon:
    def __init__(self, name, hit_points, attack_damage, move):
        self.name = name
        self.hit_points = hit_points
        self.attack_damage = attack_damage
        self.move = move

    
    def use_move(self):
        return f"{self.name} used {self.move}."
    
    def take_damage(self, damage):
        self.hit_points = self.hit_points - damage
    
    def has_fainted(self):
        if self.hit_points < 1:
            return True
        else:
            return False
        
    def get_multiplier(self, another_pokemon):
        if [another_pokemon.type] == self.strong_against:
            return 1.5
        if [another_pokemon.type] == self.weak_against:
            return 0.5
        return 1
    
        
class Water(Pokemon):
    def __init__(self,name, hit_points, attack_damage, move):
        super().__init__(name, hit_points, attack_damage, move)
        self.type = "Water"
        self.strong_against = ["Fire"]
        self.weak_against = ["Grass"]

class Fire(Pokemon):
    def __init__(self,name, hit_points, attack_damage, move):
        super().__init__(name, hit_points, attack_damage, move)
        self.type = "Fire"
        self.strong_against = ["Grass"]
        self.weak_against = ["Water"]

class Grass(Pokemon):
    def __init__(self,name, hit_points, attack_damage, move):
        super().__init__(name, hit_points, attack_damage, move)
        self.type = "Grass"
        self.strong_against = ["Water"]
        self.weak_against = ["Fire"]
    
class Normal(Pokemon):
    def __init__(self,name, hit_points, attack_damage, move):
        super().__init__(name, hit_points, attack_damage, move)
        self.type = "Normal"
        self.strong_against = None
        self.weak_against = None

class Pokeball:
    
    def __init__(self, caught_pokemon=None):
        self.caught_pokemon = caught_pokemon
       

    #Method - Takes Pokemon as object

    def catch(self, caught_pokemon):
        if self.caught_pokemon:
            raise Exception("Pokeball already has a Pokemon stored in it!")
        else:
            self.caught_pokemon = caught_pokemon

    def is_pokeball_empty(self):
        
        if self.caught_pokemon == None:
            return True     
        else: 
            return False


    



    


    

