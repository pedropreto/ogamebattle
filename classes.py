#! /usr/bin/env python
# -*- coding: utf-8 -*-

from random import *


class Defence:
    def __init__(self, name, integrity, shield, attack, rapidfire):
        self.name = name
        self.integrity = integrity
        self.shield = shield
        self.attack = attack
        self.rapidfire = rapidfire
        self.original_integrity = integrity
        self.original_shield = shield

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Defence:' + self.name + '\nintegrity:' + str(self.integrity) + "\nshield:" + str(self.shield) \
               + "\nattack:" + str(self.attack) + '\n\n'

    def createDefence(self, name, units, list_defences, techs):
        integrity_data = {"Rocket Launcher": 2000}
        shield_data = {"Rocket Launcher": 20}
        attack_data = {"Rocket Launcher": 80}
        rapidfire_data = {"Rocket Launcher": None}

        increase_integrity = 1 + techs["Armour Technology"] / 10
        increase_shield = 1 + techs["Shield Technology"] / 10
        increase_attack = 1 + techs["Weapon Technology"] / 10

        for i in range(1, units + 1):
            list_defences.append(self(name, integrity_data[name] * increase_integrity,
                                      shield_data[name] * increase_shield,
                                      attack_data[name] * increase_attack,
                                    rapidfire_data[name]))

        return list_defences


class Ship:
    def __init__(self, name, integrity, shield, attack, rapidfire):
        self.name = name
        self.integrity = integrity
        self.shield = shield
        self.attack = attack
        self.rapidfire = rapidfire
        self.original_integrity = integrity
        self.original_shield = shield

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Ship:' + self.name + '\nintegrity:' + str(self.integrity) + "\nshield:" + str(self.shield) \
               + "\nattack:" + str(self.attack) + '\n\n'

    def createShip(self, name, units, list_ships, techs):
        integrity_data = {"Light Fighter": 4000, "Heavy Fighter": 10000, "Cruiser": 27000,
                          "Battleship": 60000, "Battlecruiser": 70000}
        shield_data = {"Light Fighter": 10, "Heavy Fighter": 25, "Cruiser": 50,
                       "Battleship": 200, "Battlecruiser": 400}
        attack_data = {"Light Fighter": 50, "Heavy Fighter": 150, "Cruiser": 400,
                       "Battleship": 1000, "Battlecruiser": 700}
        rapidfire_data = {"Light Fighter": {"Espionage Probe": 5, "Solar Satellite": 5},
                          "Heavy Fighter": {"Small Cargo": 3, "Espionage Probe": 5, "Solar Satellite": 5},
                          "Cruiser": {"Spionage Probe": 5, "Solar Satellite": 5, "Light Fighter": 6,
                                      "Rocket Launcher": 10},
                          "Battleship": {"Spionage Probe": 5, "Solar Satellite": 5},
                          "Battlecruiser": {"Spionage Probe": 5, "Solar Satellite": 5, "Small Cargo": 3,
                                            "Large Cargo": 3, "Heavy Fighter": 4, "Cruiser": 4, "Battleship": 7}
                          }

        increase_integrity = 1 + techs["Armour Technology"] / 10
        increase_shield = 1 + techs["Shield Technology"] / 10
        increase_attack = 1 + techs["Weapon Technology"] / 10

        for i in range(1, units + 1):
            list_ships.append(self(name, integrity_data[name] * increase_integrity,
                                   shield_data[name] * increase_shield,
                                   attack_data[name] * increase_attack,
                                    rapidfire_data[name]))

        return list_ships


class Battle:
    def __init__(self, fleet_attacker, fleet_defender, defences):
        self.fleet_attacker = fleet_attacker
        self.fleet_defender = fleet_defender
        self.defences = defences

    def __str__(self):
        return str(self.attacker) + "vs" + str(self.defender)

    def battleEvent(self):
        rounds = 6

        battle_shipsAttack = list(self.fleet_attacker)
        battle_shipsDefend = list(self.fleet_defender)
        battle_defences = list(self.defences)

        for j in range(1, rounds + 1):
            print(f'Round {j} starting!')

            shipsToFireAttacker = list(self.fleet_attacker)
            shipsToFireDefender = list(self.fleet_defender)
            defencesToFire = list(self.defences)

            battle_shipsAttack, battle_shipsDefend, defences, winner = self.battleround(battle_shipsAttack,
                                                                                   battle_shipsDefend, battle_defences,
                                                                                   shipsToFireAttacker,
                                                                                   shipsToFireDefender, defencesToFire)

            if winner:
                break

            print(f'Round {j} ended!')

        if winner:
            pass
        else:
            print(f'\n\nIt\'s a draw!')

    def battleround(self, battle_shipsAttack, battle_shipsDefend, defences, shipsToFireAttacker,
                    shipsToFireDefender, defencesToFire):

        yetToFire = True
        winner = False
        unitsToFireAttacker = shipsToFireAttacker
        unitsToFireDefender = shipsToFireDefender + defencesToFire

        while yetToFire:
            chance = random()
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

            shooter, idx_shooter = self.chooseShooterUnit(unitsToFire)

            # choose receiver to be attacked
            receiver, idx_receiver = self.chooseReceiverUnit(receivingUnits)
            receivingUnits = self.shooting(shooter, receiver, receivingUnits, idx_receiver, side)
            if len(receivingUnits) == 0:
                print(f'\n\n{side} wins!')
                winner = True
                break

            unitsToFire = self.removeToFire(idx_shooter, unitsToFire)

            if len(unitsToFireAttacker) == 0 and len(unitsToFireDefender) == 0:
                yetToFire = False

        return battle_shipsAttack, battle_shipsDefend, defences, winner

    def removeToFire(self, ship_idx, unitsToFire):
        unitsToFire.pop(ship_idx)
        return unitsToFire

    def chooseShooterUnit(self, listToShoot):
        idx_shooter = randint(1, len(listToShoot)) - 1
        return listToShoot[idx_shooter], idx_shooter

    def chooseReceiverUnit(self, listToReceive):
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

    def shooting(self, shooter, receiver, ships_receiver, idx_receiver, side):
        # first shot
        self.shot(shooter, receiver)
        print(f'{side} shoots! {shooter} tries to take down {receiver} of the opponent')

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

                    receiver, idx_receiver = self.chooseReceiverUnit(ships_receiver)

                    self.shot(shooter, receiver)
                    print(f'{side} shoots! {shooter} tries to take down {receiver} of the opponent')

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
                receiver.integrity = 0
                receiver.shield = 0
                receiver.attack = 0
                print(f'{receiver} exploded!')
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