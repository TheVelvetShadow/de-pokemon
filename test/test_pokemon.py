from src.pokemon import Pokemon, Water, Fire, Normal, Grass, Pokeball


def test_pokemon_attributes():
    test_poke = Pokemon("Charizard", 10, 6, "Fireball")
    assert test_poke.name == "Charizard"
    assert test_poke.hit_points == 10
    assert test_poke.attack_damage == 6
    assert test_poke.move == "Fireball"

def test_use_move():
    test_poke = Pokemon("Charizard", 10, 6, "Fireball")
    assert test_poke.use_move() == "Charizard used Fireball."

def test_take_damage():
    test_poke = Pokemon("Charizard", 10, 6, "Fireball")
    damage = 4
    test_poke.take_damage(damage)
    assert test_poke.hit_points == 6

def test_has_fainted_True():
    test_poke = Pokemon("Charizard", 10, 6, "Fireball")
    test_poke.take_damage(11)
    assert test_poke.has_fainted() == True

def test_has_fainted_False():
    test_poke = Pokemon("Charizard", 10, 6, "Fireball")
    test_poke.take_damage(3)
    assert test_poke.has_fainted() == False

def test_pokemon_type_test_attributes():
    charizard = Fire("Charizard", 10, 6, "Fireball")
    squirtle = Water("Squirtle", 10, 6, "Splash")
    diglet = Normal("Diglet", 10, 6, "Scratch")
    bulbasaur = Grass("Bulbasaur", 10, 6, "Leaf Wind")

    assert charizard.strong_against == ["Grass"]
    assert charizard.weak_against == ["Water"]

    assert squirtle.strong_against == ["Fire"]
    assert squirtle.weak_against == ["Grass"]

    assert diglet.strong_against == None
    assert diglet.weak_against == None

    assert bulbasaur.strong_against == ["Water"]
    assert bulbasaur.weak_against == ["Fire"]
    
    
def test_pokemon_type_multiplier_same():
    charizard = Water("Charizard", 10, 6, "Fireball")
    squirtle = Water("Squirtle", 10, 6, "Splash")
    assert squirtle.get_multiplier(charizard) == 1

def test_pokemon_type_multiplier_different():
    charizard = Fire("Charizard", 10, 6, "Fireball")
    squirtle = Water("Squirtle", 10, 6, "Splash")
    assert squirtle.get_multiplier(charizard) == 1.5

def test_pokeball_none_given():
    test_pokeball = Pokeball()
    assert test_pokeball.stored == None






