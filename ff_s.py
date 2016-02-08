#!/usr/bin/env
# -*- coding:utf-8 -*-

def check_connection(connections, first, second):
    pairs = [c.split('-') for c in list(connections[:])]
    stack = []
    tree = []
    while pairs:
        stack = pairs.pop(0)
        print stack


check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3")
