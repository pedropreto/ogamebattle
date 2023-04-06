#! /usr/bin/env python
# -*- coding: utf-8 -*-

from classes import *
import random

ship = Ship.createLightFighter(Ship)

lightfighter_attacker = 1
heavyfighter_defender = 1

ships_attacker, ships_defender = [], []

for i in range(0, lightfighter_attacker):
    ships_attacker.append(Ship.createLightFighter(Ship))

for i in range(0, heavyfighter_defender):
    ships_defender.append(Ship.createHeavyFighter(Ship))


battle = Battle(ships_attacker, ships_defender)

battle_shipsAttack = list(ships_attacker)
battle_shipsDefend = list(ships_defender)


while len(battle_shipsAttack) > 0 or len(battle_shipsDefend) > 0:
    chance = random.random()
    if chance > 0.5 and len(battle_shipsAttack) > 0:
        # attacker first
        print(f'Attacker shoots!')
        shooter, idx_shooter = battle.chooseShooterShip(battle_shipsAttack)
        battle_shipsAttack = battle.removeShooter(battle_shipsAttack, idx_shooter)
        # choose receiver to be attacked
        receiver, idx_receiver = battle.chooseReceiverShip(ships_defender)
        battle.shooting(shooter, receiver)

        RapidFire = True
        while RapidFire:
            valueRapidFire = battle.checkRapidFire(shooter, receiver)

            if valueRapidFire != 0:
                chance_reshoot = random.random()
                if chance_reshoot < (valueRapidFire - 1) / valueRapidFire:
                    print(f'Attacker shoots!')
                    receiver, idx_receiver = battle.chooseReceiverShip(ships_defender)
                    battle.shooting(shooter, receiver)
                else:
                    RapidFire = False
            else:
                RapidFire = False

    elif chance <= 0.5 and len(battle_shipsDefend) > 0:
        # defender first
        print(f'Defender shoots!')
        shooter, idx_shooter = battle.chooseShooterShip(battle_shipsDefend)
        battle_shipsDefend = battle.removeShooter(battle_shipsDefend, idx_shooter)
        # choose receiver to be attacked
        receiver, idx_receiver = battle.chooseReceiverShip(ships_attacker)
        battle.shooting(shooter, receiver)
    else:
        pass

print(ships_attacker)

print(ships_defender)