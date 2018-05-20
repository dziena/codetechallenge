#!/usr/bin/env python
import sys
import numpy as np
import math


arg = sys.argv[1]
ln = len(arg)
e_ln = int(math.sqrt(ln))
result = ""
elements = np.array(list(arg))
poczatek = e_ln**2 - 1
if e_ln % 2 == 0:
    koniec = int(e_ln * (e_ln / 2 - 1) + e_ln / 2)
else:
    koniec = int(poczatek / 2)
i = e_ln - 1
j = e_ln - 1
kierunek = "LEWO"

while True:
    result += elements[e_ln * i + j]
    if e_ln * i + j == koniec:
        break;
    elif i == j and i < e_ln/2:
        j += 1
        kierunek = "PRAWO"
    elif i == j - 1 and i >= e_ln/2:
        j -= 1
        kierunek = "LEWO"
    elif i + j == e_ln - 1 and i < j:
        i += 1
        kierunek = "DOL"
    elif i + j == e_ln - 1 and i > j:
        i -= 1
        kierunek = "GORA"
    elif kierunek == "PRAWO":
        j += 1
    elif kierunek == "LEWO":
        j -= 1
    elif kierunek == "GORA":
        i -= 1
    elif kierunek == "DOL":
        i += 1

print(result, end='')




