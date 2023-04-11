#! /usr/bin/env python
# -*- coding: utf-8 -*-

from classes import *
import random


def battleround(battle_shipsAttack, battle_shipsDefend, defences, shipsToFireAttacker, shipsToFireDefender,
                                                                 defencesToFire):
    yetToFire = True
    winner = False
    unitsToFireAttacker = shipsToFireAttacker
    unitsToFireDefender = shipsToFireDefender + defencesToFire

    while yetToFire:
        chance = random.random()
        if chance > 0.5:
            if len(shipsToFireAttacker) == 0:
                continue

            # attacker first
            side = 'Attacker'

            receivingUnits = battle_shipsDefend + defences
            unitsToFire = unitsToFireAttacker

        elif chance <= 0.5:
            if len(shipsToFireDefender) == 0 and len(defencesToFire) == 0:
                continue

            # defender first
            side = 'Defender'

            receivingUnits = battle_shipsAttack
            unitsToFire = unitsToFireDefender

        else:
            pass

        shooter, idx_shooter = battle.chooseShooterUnit(unitsToFire)

        # choose receiver to be attacked
        receiver, idx_receiver = battle.chooseReceiverUnit(receivingUnits)
        receivingUnits = battle.shooting(shooter, receiver, receivingUnits, idx_receiver, side)
        if len(receivingUnits) == 0:
            print(f'\n\n{side} wins!')
            winner = True
            break

        unitsToFire = battle.removeToFire(idx_shooter, unitsToFire)

        if len(unitsToFireAttacker) == 0 and len(unitsToFireDefender) == 0:
            yetToFire = False

    return battle_shipsAttack, battle_shipsDefend, defences, winner


ships_attacker, ships_defender = [], []
defences = []

attacker_units = {"Light Fighter": 0,
                  "Heavy Fighter": 0,
                  "Cruiser": 0,
                  "Battleship": 0,
                  "Battlecruiser": 1}

defender_units = {"Light Fighter": 0,
                  "Heavy Fighter": 1,
                  "Cruiser": 0,
                  "Battleship": 0,
                  "Battlecruiser": 0}

defence_units = {"Rocket Launcher": 1}

# ships attacker
for key, value in attacker_units.items():
    ships_attacker = Ship.createShip(Ship, name=key, units=value, list_ships=ships_attacker)

# ships defender
for key, value in defender_units.items():
    ships_defender = Ship.createShip(Ship,name=key, units=value, list_ships=ships_defender)

# defences
for key, value in defence_units.items():
    defences = Defence.createDefence(Defence, name=key, units=value, list_defences=defences)


battle = Battle(ships_attacker, ships_defender)
rounds = 6

for j in range(1, rounds + 1):
    print(f'Round {j} starting!')

    battle_shipsAttack = list(ships_attacker)
    battle_shipsDefend = list(ships_defender)
    battle_defences = list(defences)

    shipsToFireAttacker = list(ships_attacker)
    shipsToFireDefender = list(ships_defender)
    defencesToFire = list(defences)

    battle_shipsAttack, battle_shipsDefend, defences, winner = battleround(battle_shipsAttack, battle_shipsDefend, defences,
                                                         shipsToFireAttacker, shipsToFireDefender, defencesToFire)

    if winner:
        break

    print(f'Round {j} ended!')

if winner:
    pass
else:
    print(f'\n\nIt\'s a draw!')



