"""warnings"""


class Patient:

    def __init__(self, first_name, last_name, birth_date, weight, height, gender, blood_systolic, blood_diastolic,
                 blood_type, warnings, age, medical_history=None, allergies=None, recent_travel=None, medictions=None):
        if recent_travel is None:
            recent_travel = []
        if allergies is None:
            allergies = []
        if medical_history is None:
            medical_history = []
        if medictions is None:
            medictions = []
        self.first = first_name
        self.last = last_name
        self.date = birth_date
        self.weight = weight
        self.height = height
        self.gender = gender
        self.sys = blood_systolic
        self.dia = blood_diastolic
        self.type = blood_type
        self.history = medical_history
        self.allergic = allergies
        self.travel = recent_travel
        self.meds = medictions
        self.issue = warnings
        self.num = age
        self.ages=[0.25, 0.5, 0.75, 1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        self.heights=list(range(57,85))
        self.min_weight=[6.0, 13.3, 15.8, 18.1, 19.9, 23.0, 23.4, 26.5, 31.5, 34.0, 39.5, 44.0, 49.5,
                    57.0, 62.0, 70.5, 81.5, 91.5, 101.0, 105.0, 115.0, 118.0, 120.0]
        self.max_weight=[15.4, 18.3, 20.1, 21.8, 24.6, 31.0, 36.0, 40.5, 45.5, 50.5, 56.5, 63.0, 70.5,
                    78.5, 88.0, 100.0, 112.0, 123.5, 134.0, 142.0, 147.5, 152.0, 155.0]
        self.go=0

    def weight_warning(self):
        # For this method to work it's very important that the user inputs an age that is an integer, not a float
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

    def blood_warning(self):
        if (self.sys <= 90) and (self.dia <= 60):
            print("\nLOWBLOODPRESSURE")

        if (self.sys >= 120) and (self.dia >= 80):
            print("\nHIGHBLOODPRESSURE")

        else:
            print("\nNORMAL BLOODPRESSURE")

    def type_warning(self):
        if self.type == 'O-':
            print("This patient may only receive O- blood")

        if self.type == 'O+':
            print("This patient may only receive O- and O+ blood")

        if self.type == 'A-':
            print("This patient may only receive O- and A- blood")

        if self.type == 'A+':
            print("This patient may only receive O-, O+, A-, and A+ blood")

        if self.type == 'B-':
            print("This patient may only receive O- and B- blood")

        if self.type == 'B+':
            print("This patient may only receive O-, O+, B-, and B+ blood")

        if self.type == 'AB-':
            print("This patient may only receive O-, A-, B-, and AB- blood")

        if self.type == 'AB+':
            print("This patient may receive any blood type")

    def family_warning(self):
        family_medical = self.issue
        if self.issue is not None:
            print(f"This patient is at risk of the following: {family_medical}")


bollinger_kalei = Patient('Kalei', 'Bollinger', '06-05-2001', 125, 65, 'Female', 120, 80, 'O-',
                          ['Abnormal Aortic Aneurysm', 'Chiari Malformation', 'Crohns Disease'], 18,
                          ['CRPS', 'Sacroilitis'], ['Bees', 'Tramidol'], None, ['Xylitol', 'Humara'])

bollinger_kalei.weight_warning()
