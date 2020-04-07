class Patient:
    def __init__(self, age, height, weight):
        self.age=age
        self.weight=weight
        self.height=height
        self.ages=[0.25, 0.5, 0.75, 1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        self.heights=list(range(57,85))
        self.min_weight=[6.0, 13.3, 15.8, 18.1, 19.9, 23.0, 23.4, 26.5, 31.5, 34.0, 39.5, 44.0, 49.5,
                    57.0, 62.0, 70.5, 81.5, 91.5, 101.0, 105.0, 115.0, 118.0, 120.0]
        self.max_weight=[15.4, 18.3, 20.1, 21.8, 24.6, 31.0, 36.0, 40.5, 45.5, 50.5, 56.5, 63.0, 70.5,
                    78.5, 88.0, 100.0, 112.0, 123.5, 134.0, 142.0, 147.5, 152.0, 155.0]
        self.go=0

    def check_weight(self):
        # For this method to work it's very important that the user inputs an age that is an integer, not a float
        for i in range(0,len(self.ages)):
            if self.ages[i]==self.age:
                self.go=i
                break
            elif self.age>=19:
                self.go=19
                break

        if self.go==19:
            self.min_weight=[72, 77, 81, 86, 90, 95, 99, 104, 108, 113, 117, 122, 126, 131,
                             135, 140, 144, 149, 153, 158, 162, 167, 171, 176, 180, 185, 189, 194]
            self.max_weight=[103, 110, 117, 123, 130, 136, 143, 150, 156, 163, 169, 176, 183, 189,
                             196, 202, 209, 216, 223, 229, 235, 242, 249, 255, 262, 268, 275, 280]
            for i in range(0,len(self.heights)):
                if self.heights[i]==self.height:
                    self.go=i
                    break
                
        if int(self.min_weight[self.go])<=self.weight<=int(self.max_weight[self.go]):
            print('healthy weight')
        if self.weight < self.min_weight[self.go]:
            print('underweight')
        if self.weight > self.max_weight[self.go]:
            print('overweight')
        
        

jay=Patient(21, 70, 130)
jay.check_weight()
dee=Patient(18, 71, 140)
dee.check_weight()
