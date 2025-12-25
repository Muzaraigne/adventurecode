# -*- coding: utf-8 -*-
import os
from state import TuringMachine, TestMachine

if __name__ == "__main__" :
    print("--- Jour 25 : Solution ---")
    print("exeptionnellement, le code est perosnalise pour mon entré, pour faire foncionner avec une autre entres, il faut changer les valeurs dans state.py")

    tm = TuringMachine("Machine de Turing")
    test =  TestMachine("Machine de Turing")
    [test.step() for _ in range(6)]  # Exécuter 6 étapes pour la machine de test
    print(test.checksum())
    steps = 12919244  # Nombre d'étapes à exécuter, spécifique
    for _ in range(steps):
        tm.step()
    checksum = tm.checksum()

    print(f"Le checksum après {steps} étapes est : {checksum}")