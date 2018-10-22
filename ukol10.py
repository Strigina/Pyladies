multiply1 = 0
multiply2 = 0
for run in range (5):
    for run in range (5):
        if (multiply1 != 4):
            print (multiply1 * multiply2, end = " ")
        else:
            print (multiply1 * multiply2)
        multiply1 = multiply1 + 1
    multiply1 = 0
    multiply2 = multiply2 + 1
