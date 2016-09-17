#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

print(os.getcwd())
print(os.path.exists(os.getcwd()))
print(os.listdir(os.getcwd()))
print(os.path.dirname(os.path.abspath("__file__")))
print(os.path.pardir)
print(os.path.join(os.path.dirname("__file__"), os.path.pardir))
print(os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir)))

parentDir = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
print(parentDir + "\\testdir123")

if not (os.path.exists(parentDir + "\\testdir123")):
    os.mkdir(parentDir + "\\testdir123")
print(os.listdir(parentDir))


