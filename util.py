def parent_child_parser(parser, string_to_find, attribute_to_find='h3'):
    try:

        finder = parser.find(attribute_to_find, string=string_to_find)
        found = finder.parent.find("a")
        if not found:
            found = finder.parent.find("div")
        return found.text
    except:
        return "No Data"
    
species_dictionary = {
    "Humans":1,
    "Kristang":2,
    "Ruhar":3,
    "Thuranin":4,
    "Bosphuraq":5,
    "Jeraptha":6,
    "Rindhalu":7,
    "Maxolhx":8,
    "Elders":9,
    "Lemoostra":10,
    "Verd-kris":11,
    "Wurgalan":12,
    "Torgalau":13,
    "Urgar":14,
    "No Data":15,
}

episode_dictionary = {
    'ExForce 1: Columbus Day': 1,	
    'ExForce 2: Spec Ops': 2,	
    'ExForce 3: Paradise': 3,	
    'ExForce 3.5: Trouble on Paradise': 4,	
    'ExForce 4: Black Ops': 5,	
    'ExForce 5: Zero Hour': 6,	
    'ExForce 6: Mavericks': 7,	
    'ExForce 7: Renegades': 8,	
    'ExForce 7.5: Homefront': 9,	
    'Mavericks Book 1: Deathtrap': 10,
    'ExForce 8: Armageddon': 11,	
    'ExForce 9: Valkyrie': 12,
    'Mavericks Book 2: Freefall': 13,	
    'ExForce 10: Critical Mass': 14,	
    'ExForce 11: Brushfire': 15,	
    'ExForce 12: Breakaway': 16,	
    'ExForce 13: Fallout': 17,	
    'ExForce 14: Match Game': 18,
    'ExForce 15: Failure Mode': 19,
    'ExForce 16: Aftermath': 20,
    'ExForce 17: Task Force Hammer': 21
}