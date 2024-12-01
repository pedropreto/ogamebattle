#! /usr/bin/env python
# -*- coding: utf-8 -*-

from classes import *
import random


ships_attacker, ships_defender = [], []
defences = []

attacker_units = {"Light Fighter": 0,
                  "Heavy Fighter": 0,
                  "Cruiser": 2,
                  "Battleship": 0,
                  "Battlecruiser": 0}

defender_units = {"Light Fighter": 0,
                  "Heavy Fighter": 0,
                  "Cruiser": 0,
                  "Battleship": 0,
                  "Battlecruiser": 0}

defence_units = {"Rocket Launcher": 10}

attacker_techs = {"Weapon Technology": 10, "Shield Technology": 10, "Armour Technology": 10}
defender_techs = {"Weapon Technology": 10, "Shield Technology": 10, "Armour Technology": 10}

# ships attacker
for key, value in attacker_units.items():
    ships_attacker = Ship.createShip(Ship, name=key, units=value, list_ships=ships_attacker, techs=attacker_techs)

# ships defender
for key, value in defender_units.items():
    ships_defender = Ship.createShip(Ship,name=key, units=value, list_ships=ships_defender, techs=defender_techs)

# defences
for key, value in defence_units.items():
    defences = Defence.createDefence(Defence, name=key, units=value, list_defences=defences, techs=defender_techs)


battle = Battle(ships_attacker, ships_defender, defences)

battle.battleEvent()

