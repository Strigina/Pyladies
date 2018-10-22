j = 0
for i in range (6):
    if (i == 0) or (i == 5):
        for run in range (6):
            j = j + 1
            if (j == 6):
                print ("X")
            else:
                print ("X", end = " ")
    else:
        print ("X         X")
    i = i + 1
