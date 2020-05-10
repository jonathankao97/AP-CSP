def blastoff(counter):
    counter = int(counter)
    if counter == 0:
        return "BlastOff!"
    return str(counter) + " " + str(blastoff(counter-1))


counter = input("How many seconds until blastoff?: ")
print(blastoff(counter))

