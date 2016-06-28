# -*- coding: utf-8 -*-


class AttackException(Exception):
    pass


class ActionException(Exception):
    pass


class Player(object):
    def __init__(self, ws):
        self.level = 1
        self.energy = 0
        self.ws = ws

    def attack(self):
        if self.energy <= 0:
            raise AttackException
        _energy = self.energy
        self.energy = 0
        return _energy

    def add_energy(self):
        if self.energy < 5:
            self.energy += 1
        return self.energy

    def __eq__(self, other):
        return self.ws == other.ws


class GamePlayers(object):
    ATTACK = 1
    DEFEND = 2
    ADD = 3

    P1_DEAD = -1
    P2_DEAD = 1
    DRAW = 0

    def __init__(self):
        self.p1 = None
        self.p2 = None

    def add(self, player):
        if not self.p1:
            self.p1 = player
        elif not self.p2:
            self.p2 = player
        else:
            return False
        print player
        return True

    def handle(self, p1_action, p2_action):
        if p1_action == self.ATTACK and p2_action == self.ATTACK:
            p1_attack = self.p1.attack()
            p2_attack = self.p2.attack()
            if p1_attack > p2_attack:
                return self.P2_DEAD
            elif p1_attack < p2_attack:
                return self.P1_DEAD
            return self.DRAW
        elif p1_action == self.ATTACK and p2_action == self.DEFEND:
            p1_attack = self.p1.attack()
            if p1_attack >= 5:
                return self.P2_DEAD
            return self.DRAW
        elif p1_action == self.ATTACK and p2_action == self.ADD:
            self.p1.attack()
            return self.P2_DEAD
        elif p1_action == self.DEFEND and p2_action == self.ATTACK:
            p2_attack = self.p2.attack()
            if p2_attack >= 5:
                return self.P1_DEAD
            return self.DRAW
        elif p1_action == self.DEFEND and p2_action == self.DEFEND:
            return self.DRAW
        elif p1_action == self.DEFEND and p2_action == self.ADD:
            self.p2.add_energy()
            return self.DRAW
        elif p1_action == self.ADD and p2_action == self.ATTACK:
            self.p2.attack()
            return self.P1_DEAD
        elif p1_action == self.ADD and p2_action == self.DEFEND:
            self.p1.add_energy()
            return self.DRAW
        elif p1_action == self.ADD and p2_action == self.ADD:
            self.p1.add_energy()
            self.p2.add_energy()
            return self.DRAW
        raise ActionException
