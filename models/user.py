# -*- coding: utf-8 -*-

from flask_login import UserMixin
from leancloud import Object


class _User(UserMixin, Object):
    @property
    def username(self):
        return self.get('username')

    @property
    def nickname(self):
        return self.get('nickname')


class WaitUser(Object):
    @property
    def user(self):
        return self.get('user')


class PlayingUser(Object):
    @property
    def user1(self):
        return self.get('user1')

    @property
    def user2(self):
        return self.get('user2')

    def _get_u1_level(self):
        return self.get('user1_level')
    def _set_u1_level(self, level):
        self.set('user1_level', level)
    user1_level = property(_get_u1_level, _set_u1_level)

    def _get_u2_level(self):
        return self.get('user2_level')
    def _set_u2_level(self, level):
        self.set('user2_level', level)
    user2_level = property(_get_u2_level, _set_u2_level)

    def _get_around(self):
        return self.get('around')
    def _set_around(self, a):
        self.set('around', a)
    around = property(_get_around, _set_around)

    def _get_actions(self):
        return self.get('actions')
    def _set_actions(self, a):
        return self.set('actions', a)
    actions = property(_get_actions, _set_actions)
