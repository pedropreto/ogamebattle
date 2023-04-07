#! /usr/bin/env python
# -*- coding: utf-8 -*-

from classes import *
import random

lightfighter_attacker = 1
heavyfighter_defender = 1

ships_attacker, ships_defender = [], []

for i in range(0, lightfighter_attacker):
    ships_attacker.append(Ship.createShip(Ship, "Light Fighter"))

for i in range(0, heavyfighter_defender):
    ships_defender.append(Ship.createShip(Ship, "Heavy Fighter"))


battle = Battle(ships_attacker, ships_defender)

battle_shipsAttack = list(ships_attacker)
battle_shipsDefend = list(ships_defender)

shipsToFireAttacker = list(ships_attacker)
shipsToFireDefender = list(ships_defender)

while len(shipsToFireAttacker) > 0 or len(shipsToFireDefender) > 0:
    chance = random.random()
    if chance > 0.5 and len(shipsToFireAttacker) > 0:
        # attacker first
        print(f'Attacker shoots!')
        shooter, idx_shooter = battle.chooseShooterShip(battle_shipsAttack)

        # choose receiver to be attacked
        receiver, idx_receiver = battle.chooseReceiverShip(ships_defender)
        ships_defender = battle.shooting(shooter, receiver, ships_defender, idx_receiver)
        if len(ships_defender) == 0:
            print('Attacker wins!')
            break

        shipsToFireAttacker = battle.removeToFire(idx_shooter, shipsToFireAttacker)

    elif chance <= 0.5 and len(shipsToFireDefender) > 0:
        # defender first
        print(f'Defender shoots!')
        shooter, idx_shooter = battle.chooseShooterShip(battle_shipsDefend)

        # choose receiver to be attacked
        receiver, idx_receiver = battle.chooseReceiverShip(ships_attacker)
        ships_attacker = battle.shooting(shooter, receiver, ships_attacker, idx_receiver)
        if len(ships_attacker) == 0:
            print('Defender wins!')
            break

        shipsToFireDefender = battle.removeToFire(idx_shooter, shipsToFireDefender)
    else:
        pass

print(ships_attacker)

print(ships_defender)