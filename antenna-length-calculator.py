import time

print("""***************************************
Monopole/Dipole Antenna Length Calculator
***************************************
1-Monopole Antenna\n2-Dipole Antenna\nq-Quit
***************************************""")

while True:

    i = input("Choose one:")

    if i == "q":

        print("So long...")
        time.sleep(0.5)
        break

    elif i == "1":

        mhz = float(input("Frequency(MHz):"))
        L = round(71.3232 / mhz , 4)
        print("Length of Antenna:",L,"meter")

    elif i == "2":

        mhz = float(input("Frequency(MHz):"))
        L = round(142.6464 / mhz , 4)
        E = round(L / 2 , 4)

        print("Length of One Piece of Antenna: {} meter\nTotal Length of Antenna: {} meter".format(L, E))

    else:

        print("Please Input A Correct Value!")
