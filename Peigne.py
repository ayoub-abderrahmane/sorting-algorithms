class Peigne():
    def __init__(self, liste):
        self.list = liste
    
    def check_numbers(self, first_value, second_value):
        if self.list[first_value] > self.list[second_value]:
            self.list [first_value] ,self.list[second_value] = self.list[second_value] ,self.list[first_value]

    def sorting(self):
        print ("Initial list : " ,self.list)
        first_index = 0
        second_index = 7
        for index ,numbers in enumerate(self.list):
            for i in range(len(self.list)):
                self.check_numbers(first_index,second_index)
                first_index += 1
                second_index -= 1
                

        print(self.list)



pei = Peigne([5,3,2,1,4,8,6,9,7,10])
# pei.check_numbers()
pei.sorting()