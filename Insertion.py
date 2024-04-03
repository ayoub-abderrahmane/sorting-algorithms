class Insertion():
    def __init__(self, liste):
        self.list = liste
    
    def check_numbers(self, first_value, second_value):
        if self.list[first_value] > self.list[second_value]:
            self.list [first_value] ,self.list[second_value] = self.list[second_value] ,self.list[first_value]

    def sorting(self):
        print ("Initial list : " ,self.list)
        for index ,numbers in enumerate(self.list):
            self.check_numbers(0,1)
            # index += 1
            # print(index)
            self.check_numbers(1,2)
            self.check_numbers(2,3)
            self.check_numbers(3,4)
                # if self.list[0] > self.list[1]:
                #     self.list [0] ,self.list[1] = self.list[1] ,self.list[0]
                # elif self.list[1] > self.list[2]:
                #     self.list [1] ,self.list[2] = self.list[2] ,self.list[1]
                # if self.list[2] > self.list[3]:
                #     self.list [2] ,self.list[3] = self.list[3] ,self.list[2]
                # elif self.list[3] > self.list[4]:
                #     self.list [3] ,self.list[4] = self.list[4] ,self.list[3]
        print(self.list)



insert = Insertion([5,3,2,1,4])
# insert.check_numbers()
insert.sorting()