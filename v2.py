class Patient:
    def __init__(self, age, height, weight, sex, blood_systolic, blood_diastlic, blood_type, med_history=None):
        self.age = age
        self.tall = height
        self.fat = weight
        self.sex = sex
        self.sys = blood_systolic
        self.dia = blood_diastlic
        self.type = blood_type
        self.issue = med_history
        self.ages=[0.25, 0.5, 0.75, 1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        self.heights=list(range(57,85))
        self.min_weight=[6.0, 13.3, 15.8, 18.1, 19.9, 23.0, 23.4, 26.5, 31.5, 34.0, 39.5, 44.0, 49.5,
                    57.0, 62.0, 70.5, 81.5, 91.5, 101.0, 105.0, 115.0, 118.0, 120.0]
        self.max_weight=[15.4, 18.3, 20.1, 21.8, 24.6, 31.0, 36.0, 40.5, 45.5, 50.5, 56.5, 63.0, 70.5,
                    78.5, 88.0, 100.0, 112.0, 123.5, 134.0, 142.0, 147.5, 152.0, 155.0]

    # This tests for a healthy weight
    def weight_warning(self):
        for i in range(0,len(self.ages)):
            if self.ages[i]==self.num:
                self.go=i
                break
            elif self.num>=19:
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

    # Blood donation and transfusion, a person may need to know the blood type they can give to and recieve from
    def type_warning(self):
        if self.type == 'O-':
            print("\tThis patient may only receive O- blood")

        if self.type == 'O+':
            print("\tThis patient may only receive O- and O+ blood")

        if self.type == 'A-':
            print("\tThis patient may only receive O- and A- blood")

        if self.type == 'A+':
            print("\tThis patient may only receive O-, O+, A-, and A+ blood")

        if self.type == 'B-':
            print("\tThis patient may only receive O- and B- blood")

        if self.type == 'B+':
            print("\tThis patient may only receive O-, O+, B-, and B+ blood")

        if self.type == 'AB-':
            print("\tThis patient may only receive O-, A-, B-, and AB- blood")

        if self.type == 'AB+':
            print("\tThis patient may receive any blood type")

    # Sometimes illness can be genetic, family medical history can tell a person illnesses they are at a higher risk for
    def family_warning(self):
        fam_med = self.issue
        if self.issue is not None:
            print(f"\tThis patient is at risk of the following: {fam_med}")

        else:
            print("\tNo expected medical risks")

    # This tells a person whether or not they have a healthy blood pressure
    def blood_pressure(self):
        if (90 <= self.sys <= 120) and (60 <= self.dia <= 80):
            print("\tHealthy Blood Pressure")

        if (70 <= self.sys <= 89) and (40 <= self.dia <= 59):
            print("\tLow Blood Pressure")

        if (121 <= self.sys <= 140) and (81 <= self.dia <= 90):
            print("\tPre-high Blood Pressure")

        if self.sys >= 141 and self.dia >= 91:
            print("\tHigh Blood Pressure")
