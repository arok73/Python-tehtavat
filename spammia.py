#!/usr/bin/env python
"""Example on how how to override instance method in Python.
See http://stackoverflow.com/q/4243586
"""
import types
from operator import methodcaller


class Spam:
    def update(self):
        print('updating spam!')


class SpamLite(Spam):
    def update(self):
        Spam.update(self)
        print('this spam is lite!')


def poison(spam):
    tmp = spam.update

    def newUpdate(self):
        tmp()
        print('this spam has been poisoned!')
    spam.update = types.MethodType(newUpdate, spam, spam.__class__)


def poisonSpam():
    old = Spam.update

    def newUpdate(self):
        old(self)
        print('poison whole class')
    Spam.update = types.UnboundMethodType(newUpdate, None, Spam)


L = [Spam(), SpamLite()]

map(methodcaller('update'), L)

print("*"*79)
poisonSpam()
map(methodcaller('update'), L)

print("*"*79)
map(poison, L)
map(methodcaller('update'), L)
