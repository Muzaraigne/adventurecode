# -*- coding: utf-8 -*- 

from numba import njit 

FACTOR_A = 16807
FACTOR_B = 48271
DIVISEUR = 2147483647
MASK = 0xFFFF 

@njit
def judge_numba(v1, v2) -> int:
    if (v1 & MASK) == (v2 & MASK):
        return 1
    return 0

@njit
def simu_1_optimized(a, b, num_iterations: int) -> int:
    res = 0
    for _ in range(num_iterations):
        a = a * FACTOR_A % DIVISEUR
        b = b * FACTOR_B % DIVISEUR
        res += judge_numba(a, b)
    return res

@njit
def simu_2_optimized(a_start: int, b_start: int, num_iterations: int) -> int:
    a, b = a_start, b_start
    res = 0
    for _ in range(num_iterations):
        while True:
            a = a * FACTOR_A % DIVISEUR
            if a % 4 == 0:
                break
        while True:
            b = b * FACTOR_B % DIVISEUR
            if b % 8 == 0:
                break
        res += judge_numba(a, b)
    return res

if __name__ == "__main__" : 
    data_test = (65, 8921)
    data = (699, 124)
    
    print("--- Jour 15 : Solution (Numba Optimized) ---") 
    print("----- Test (Partie 1) -----")
    print(f"Résultat: {simu_1_optimized(data_test[0], data_test[1], 40000000)}") 
    
    print("----- Test (Partie 2) -----")
    print(f"Résultat: {simu_2_optimized(data_test[0], data_test[1], 5000000)}")

    print("----- Partie 1 -----")
    print(f"Résultat: {simu_1_optimized(data[0], data[1], 40000000)}")
    
    print("----- Partie 2 -----")
    print(f"Résultat: {simu_2_optimized(data[0], data[1], 5000000)}")
