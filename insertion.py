class Insertion():
    def __init__(self, liste):
        self.list = liste
    
    def sorting(self):
        print ("Initial list : " ,self.list)
        for index ,numbers in enumerate(self.list):
            for i in range(len(self.list)):
                if self.list[0] > self.list[1]:
                    self.list [0] ,self.list[1] = self.list[1] ,self.list[0]
                elif self.list[1] > self.list[2]:
                    self.list [1] ,self.list[2] = self.list[2] ,self.list[1]
                elif self.list[2] > self.list[3]:
                    self.list [2] ,self.list[3] = self.list[3] ,self.list[2]
                elif self.list[3] > self.list[4]:
                    self.list [3] ,self.list[4] = self.list[4] ,self.list[3]
        print(self.list)



insert = Insertion([5,4,3,2,1])
insert.sorting()