while True:
    is_even = input("Napiš mi číslo: ")
    if (is_even == "konec"):
        break
    elif (int(is_even) % 2) == 0:
        print ("Číslo je sudé")
    elif(int(is_even) % 2) != 0:
        print ("Číslo je liché")
