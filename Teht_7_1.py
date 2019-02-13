# -*- coding: cp1252 -*-

import random

def main():

    
    kierros = 0

    print("Heitetään kolikkoa viidesti:")
    
    while kierros < 5:
        numero = random.randint(0,1)
        if numero == 0:
            print("Klaava")
        else:
            print("Kruuna")
        kierros += 1
if __name__ == "__main__":
    main()
