class Insertion():
    def __init__(self, liste):
        self.list = liste
        self.len_list = len(self.list)
    

    def sorting(self):
        # print ("Initial list : " ,self.list)
        for i in range(self.len_list):
            key = self.list[i]
            j = i - 1
            while j >= 0 and self.list[j] > key:
                self.list[j+1] = self.list[j]
                j -= 1
                self.list[j+1] = key
        return self.list



insert = Insertion([5,3,2,1,4,9,6,8,10,7])
insert.sorting()