class Peigne():
    def __init__(self, liste):
        self.list = liste
        self.len_list = len(self.list)
    
    def check_numbers(self, first_value, second_value):
        if self.list[first_value] > self.list[second_value]:
            self.list [first_value] ,self.list[second_value] = self.list[second_value] ,self.list[first_value]

    def sorting(self):
        print ("Initial list : " ,self.list)
        for i in range(self.len_list - 5):
            pass
                

        print(self.list)



pei = Peigne([5,3,2,1,4,8,6,9,7,10])
# pei.check_numbers()
pei.sorting()