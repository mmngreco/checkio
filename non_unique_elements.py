#!/usr/bin/env
# -*- coding:utf-8 -*-
# Non_unique_Elements.py


def elementos_unicos(lista):
    lista_filtrada = list()

    for e in lista:
        if lista.count(e) <= 1:
            continue
        lista_filtrada.append(e)
    return lista_filtrada

lista = [1, 1, 1, 3, 4, 5, 4, 5]

print elementos_unicos(lista)
