class Peigne:
    def __init__(self, liste):
        self.list = liste
        self.len_list = len(self.list)

    def comb_sort(self):
        gap = self.len_list
        shrink = 1.3
        sorted = False

        while not sorted:
            # Update the gap value for a next comb
            gap = int(gap / shrink)
            if gap <= 1:
                gap = 1
                sorted = True  # If there are no swaps, the list is sorted

            i = 0
            while i + gap < self.len_list:
                if self.list[i] > self.list[i + gap]:
                    # Swap elements at positions i and i+gap
                    self.list[i], self.list[i + gap] = self.list[i + gap], self.list[i]
                    sorted = False  # If a swap occurs, the list is not fully sorted
                i += 1

        return self.list


pei = Peigne([5, 3, 2, 1, 4, 8, 6, 9, 7, 10])
print (pei.comb_sort())