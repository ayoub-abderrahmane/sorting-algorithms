liste = [4, 13, 11, 6, 9, 7 ,10, 12, 1, 5, 15, 3, 8, 14,2]

def tri_selection(liste):
    lenght= len(liste)
    while lenght != 0:
        for i in range(lenght):
            selection = [0]
            for j in range(lenght):
                if selection[0] < liste[j] :
                    selection = [liste[j]]
                    index= j

            lenght -=1
            liste[index] = liste[lenght]
            liste[lenght]=selection[0] 

            selection = [liste[0]]
    print(liste)

tri_selection(liste)
