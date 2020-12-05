import math
import time
import random


def get_pri_range(rng):
    """return a list of all primes until rng included"""
    prime = [2]
    for i in range(2, rng + 1):
        flag2 = True
        for pri in prime:
            if pri > (round((i) ** 0.5 + 0.5) + 1):
                break
            if i % pri == 0:
                flag2 = False
                if i == rng:
                    flag1 = False
                break
        if flag2:
            prime.append(i)
    return prime


def find_init_est(num):
    """finds the initial score to be a prime number"""
    rng = get_pri_range(42)
    score = 0
    for i in rng:
        x = (math.sin(math.pi * num / i)) ** 2
        if x < 0.000001 and (num not in [2,3,5,7,11,13,17,19,23,29,31,37,41]):
            score = -1
            break
        score += x
    return (round(score / len(rng) * 10))