class Bulles():
    def __init__(self, liste):
        self.list = liste # Initialization of the list
        self.len_list = len(self.list) # Take the len of the list
    
    def sorting(self):
        # print ("Initial list : " ,self.list) # Print the list before sorting
        verif = True
        j = 0
        while verif:
            verif = False
            j += 1
            for i in range(0, (self.len_list) - j):
                if self.list[i] > self.list[i+1]:
                    self.list[i], self.list[i+1] = self.list[i+1], self.list[i]
                    verif = True

        return self.list



bulles = Bulles([5,3,2,1,4,9,6,10,8,7])
bulles.sorting()