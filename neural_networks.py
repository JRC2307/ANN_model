import fileinput
import math
import random

if __name__ == "__main__":
    training_set = []
    test_data = []
    weights = []

    iterations = 200
    threshold = random.randrange(1,10)

    dimensionality = int(input())
    training_set_length = int(input())
    test_set_length = int(input())

    for i in range(training_set_length):
        values = []
        inp = input()
        inp = inp.replace('\n', '').replace('\r', '').replace(' ', '')
        inp = inp.split(',')
        aux = []
        for l in inp[0:-1]:
            aux.append(float(l))
        t_data = [aux, float(inp[-1])]
        training_set.append(t_data)

    for i in range(test_set_length):
        values = []
        inp = input()
        inp = inp.replace('\n', '').replace('\r', '').replace(' ', '')
        inp = inp.split(',')
        for l in inp:
            values.append(float(l))
        test_data.append(values)

    for i in range(dimensionality):
        rand = random.randrange(0, 1)
        weights.append(rand)

    error = 0
    for i in range(iterations):
        # calculate error
        print('error aqui')
