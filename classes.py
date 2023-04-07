#! /usr/bin/env python
# -*- coding: utf-8 -*-

from random import *


class Ship:
    def __init__(self, name, integrity, shield, attack, rapidfire):
        self.name = name
        self.integrity = integrity
        self.shield = shield
        self.attack = attack
        self.rapidfire = rapidfire
        self.original_integrity = integrity
        self.original_shield = shield
        self.shot = False

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'ship:' + self.name + '\nintegrity:' + str(self.integrity) + "\nshield:" + str(self.shield) \
               + "\nattack:" + str(self.attack) + '\n\n'

    def createShip(self, name):
        integrity_data = {"Light Fighter": 4000, "Heavy Fighter": 10000}
        shield_data = {"Light Fighter": 10, "Heavy Fighter": 25}
        attack_data = {"Light Fighter": 500, "Heavy Fighter": 150}
        rapidfire_data = {"Light Fighter": {"Heavy Fighter": 50},
                          "Heavy Fighter": {"Light Fighter": 80}}
        return self(name, integrity_data[name], shield_data[name], attack_data[name], rapidfire_data[name])


class Battle:
    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    def __str__(self):
        return str(self.attacker) + "vs" + str(self.defender)

    def removeToFire(self, ship_idx, shipsToFire):
        shipsToFire.pop(ship_idx)
        return shipsToFire

    def chooseShooterShip(self, listToShoot):
        idx_shooter = randint(1, len(listToShoot)) - 1
        return listToShoot[idx_shooter], idx_shooter

    def chooseReceiverShip(self, listToReceive):
        idx_receiver = randint(1, len(listToReceive)) - 1
        return listToReceive[idx_receiver], idx_receiver

    def shot(self, shooter, receiver):
        remaining_attack = 0
        if receiver.shield > 0:
            # if receiver has shield, shield absorbs part of the attack
            remaining_attack = shooter.attack - receiver.shield
            receiver.shield -= shooter.attack
        else:
            # if not, attack goes directly to hull
            receiver.integrity -= shooter.attack

        if remaining_attack > 0:
            # after destroying the shield completely, goes for the hull
            receiver.integrity -= remaining_attack


    def shooting(self, shooter, receiver, ships_receiver, idx_receiver):
        # first shot
        self.shot(shooter, receiver)

        # end of first shot, check if it explodes and exits from battle
        ships_receiver = self.takeShipfromBattle(receiver, idx_receiver, ships_receiver)
        if len(ships_receiver) == 0:
            return ships_receiver


        # rapidfire shots
        RapidFire = True
        while RapidFire:
            valueRapidFire = self.checkRapidFire(shooter, receiver)

            if valueRapidFire != 0:
                chance_reshoot = random()
                if chance_reshoot <= (valueRapidFire - 1) / valueRapidFire:
                    print(f'Attacker shoots!')
                    receiver, idx_receiver = self.chooseReceiverShip(ships_receiver)

                    self.shot(shooter, receiver)

                    # end of nth shot, check if it explodes and exits from battle
                    ships_receiver = self.takeShipfromBattle(receiver, idx_receiver, ships_receiver)
                    if len(ships_receiver) == 0:
                        return ships_receiver

                else:
                    RapidFire = False
            else:
                RapidFire = False

        return ships_receiver

    def checkRapidFire(self, shooter, receiver):
        if shooter.rapidfire is not None:
            for key, value in shooter.rapidfire.items():
                if key == receiver.name:
                    return value
        return 0

    def shipExplodes(self, receiver):
        explode_threshold = 0.7
        relative_integrity = receiver.integrity / receiver.original_integrity
        if relative_integrity < explode_threshold:
            explode_chance = 1 - relative_integrity
            chance = random()
            if chance <= explode_chance:
                return True
            else:
                return False
        else:
            return False

    def takeShipfromBattle(self, receiver, idx_receiver, ships_receiver):
        explodeReceiver = self.shipExplodes(receiver)
        if explodeReceiver:
            ships_receiver.pop(idx_receiver)
        return ships_receiver