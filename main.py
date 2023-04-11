#! /usr/bin/env python
# -*- coding: utf-8 -*-

from classes import *
import random


def battleround(battle_shipsAttack, battle_shipsDefend, shipsToFireAttacker, shipsToFireDefender):
    yetToFire = True
    winner = False

    while yetToFire:
        chance = random.random()
        if chance > 0.5:
            if len(shipsToFireAttacker) == 0:
                continue

            # attacker first
            side = 'Attacker'
            shootingShips = battle_shipsAttack
            receivingShips = battle_shipsDefend
            shipsToFire = shipsToFireAttacker

        elif chance <= 0.5:
            if len(shipsToFireDefender) == 0:
                continue

            # defender first
            side = 'Defender'
            shootingShips = battle_shipsDefend
            receivingShips = battle_shipsAttack
            shipsToFire = shipsToFireDefender

        else:
            pass

        shooter, idx_shooter = battle.chooseShooterShip(shipsToFire)

        # choose receiver to be attacked
        receiver, idx_receiver = battle.chooseReceiverShip(receivingShips)
        receivingShips = battle.shooting(shooter, receiver, receivingShips, idx_receiver, side)
        if len(receivingShips) == 0:
            print(f'{side} wins!')
            winner = True
            break

        shipsToFire = battle.removeToFire(idx_shooter, shipsToFire)

        if len(shipsToFireAttacker) == 0 and len(shipsToFireDefender) == 0:
            yetToFire = False

    return battle_shipsAttack, battle_shipsDefend, winner


ships_attacker, ships_defender = [], []

attacker_units = {"Light Fighter": 0,
                  "Heavy Fighter": 0,
                  "Cruiser": 0,
                  "Battleship": 5,
                  "Battlecruiser": 10}

defender_units = {"Light Fighter": 10,
                  "Heavy Fighter": 0,
                  "Cruiser": 0,
                  "Battleship": 0,
                  "Battlecruiser": 0}

for key, value in attacker_units.items():
    ships_attacker = Ship.createShip(Ship, name=key, units=value, list_ships=ships_attacker)

for key, value in defender_units.items():
    ships_defender = Ship.createShip(Ship,name=key, units=value, list_ships=ships_defender)


battle = Battle(ships_attacker, ships_defender)
rounds = 6

for j in range(1, rounds + 1):
    print(f'Round {j} starting!')

    battle_shipsAttack = list(ships_attacker)
    battle_shipsDefend = list(ships_defender)

    shipsToFireAttacker = list(ships_attacker)
    shipsToFireDefender = list(ships_defender)

    battle_shipsAttack, battle_shipsDefend, winner = battleround(battle_shipsAttack, battle_shipsDefend,
                                                         shipsToFireAttacker, shipsToFireDefender)

    if winner:
        break

    print(f'Round {j} ended!')



