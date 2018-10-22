for number in range (100):
    if ((number + 1) % 3 == 0) and ((number + 1) % 5 == 0):
        print ("bum-bác")
    elif ((number + 1) % 3 == 0):
        print ("bum")
    elif ((number + 1) % 5 == 0):
        print ("bác")
    else:
        print (number + 1)
