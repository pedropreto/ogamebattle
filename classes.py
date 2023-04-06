#! /usr/bin/env python
# -*- coding: utf-8 -*-

from random import *


class Ship:
    def __init__(self, name, integrity, shield, attack, ship_type, rapidfire):
        self.name = name
        self.integrity = integrity
        self.shield = shield
        self.attack = attack
        self.ship_type = ship_type
        self.shot = False
        self.rapidfire = rapidfire

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'ship:' + self.name + '\nintegrity:' + str(self.integrity) + "\nshield:" + str(self.shield) \
               + "\nattack:" + str(self.attack) + '\n\n'

    def createLightFighter(self):
        return self('Light Fighter', 4000, 10, 50, 1, {"Heavy Fighter": 100})

    def createHeavyFighter(self):
        return self('Heavy Fighter', 10000, 25, 150, 2, None)


class Battle:
    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    def __str__(self):
        return str(self.attacker) + "vs" + str(self.defender)

    def removeShooter(self, ships, indexToRemove):
        ships.pop(indexToRemove)
        return ships

    def chooseShooterShip(self, listToShoot):
        idx_shooter = randint(1, len(listToShoot)) - 1
        return listToShoot[idx_shooter], idx_shooter

    def chooseReceiverShip(self, listToReceive):
        idx_receiver = randint(1, len(listToReceive)) - 1
        return listToReceive[idx_receiver], idx_receiver

    def shooting(self, shooter, receiver):
        remaining_attack = 0
        if receiver.shield > 0:
            remaining_attack = shooter.attack - receiver.shield
            receiver.shield -= shooter.attack
        else:
            receiver.integrity -= shooter.attack

        if remaining_attack > 0:
            receiver.integrity -= remaining_attack

    def checkRapidFire(self, shooter, receiver):
        if shooter.rapidfire is not None:
            for key, value in shooter.rapidfire.items():
                if key == receiver.name:
                    return value
        return 0

