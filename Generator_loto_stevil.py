# -*- coding: utf-8 -*-

import random

def generacija_stevil(izbira_stevil):
    seznam_stevil = []
    for it in range(0, izbira_stevil):
        while True:
            random_stevilo = random.randint(1,30)
            if random_stevilo not in seznam_stevil:
                break
        seznam_stevil.append(random_stevilo)
    return seznam_stevil


def main():

    print "Pozdravljeni v generatorju Loto števil!:)"


    izbira_stevil = int(raw_input("Prosimo vnesite število željenih naključnih števil: "))

    print "Program je za vas zgeneriral sledeča števila:"
    print generacija_stevil(izbira_stevil)


if __name__ == "__main__":  # this means that if somebody ran this Python file, execute only the code below
    main()
