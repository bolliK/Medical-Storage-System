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

    def weight_warning(self):
        if self.num <= .25 and self.weight >= 15.4:
            print("\nOVERWEIGHT")

        if self.num <= .25 and self.weight <= 6.0:
            print("\nUNDERWEIGHT")

        if (self.num >= .25) and (self.num <= .5) and self.weight >= 18.3:
            print("\nOVERWEIGHT")

        if (self.num >= .25) and (self.num <= .5) and self.weight <= 13.3:
            print("\nUNDERWEIGHT")

        if (self.num >= .5) and (self.num <= .75) and self.weight >= 20.1:
            print("\nOVERWEIGHT")

        if (self.num >= .5) and (self.num <= .75) and self.weight <= 15.8:
            print("\nUNDERWEIGHT")

        if (self.num >= .75) and (self.num <= 1) and self.weight >= 21.8:
            print("\nOVERWEIGHT")

        if (self.num >= .75) and (self.num <= 1) and self.weight <= 18.1:
            print("\nUNDERWEIGHT")

        if (self.num >= 1) and (self.num <= 1.5) and self.weight >= 24.6:
            print("\nOVERWEIGHT")

        if (self.num >= 1) and (self.num <= 1.5) and self.weight <= 19.9:
            print("\nUNDERWEIGHT")

        if (self.num >= 1.5) and (self.num <= 2) and self.weight >= 31.0:
            print("\nOVERWEIGHT")

        if (self.num >= 1.5) and (self.num <= 2) and self.weight <= 23.0:
            print("\nUNDERWEIGHT")

        if (self.num >= 2) and (self.num <= 3) and self.weight <= 36.0:
            print("\nOVERWEIGHT")

        if (self.num >= 2) and (self.num <= 3) and self.weight <= 23.4:
            print("\nUNDERWEIGHT")

        if (self.num >= 3) and (self.num <= 4) and self.weight >= 40.5:
            print("\nOVERWEIGHT")

        if (self.num >= 3) and (self.num <= 4) and self.weight <= 26.5:
            print("\nUNDERWEIGHT")

        if (self.num >= 4) and (self.num <= 5) and self.weight >= 45.5:
            print("\nOVERWEIGHT")

        if (self.num >= 4) and (self.num <= 5) and self.weight <= 31.5:
            print("\nUNDERWEIGHT")

        if (self.num >= 5) and (self.num <= 6) and self.weight >= 50.5:
            print("\nOVERWEIGHT")

        if (self.num >= 5) and (self.num <= 6) and self.weight <= 34.0:
            print("\nUNDERWEIGHT")

        if (self.num >= 6) and (self.num <= 7) and self.weight >= 56.5:
            print("\nOVERWEIGHT")

        if (self.num >= 6) and (self.num <= 7) and self.weight <= 39.5:
            print("\nUNDERWEIGHT")

        if (self.num >= 7) and (self.num <= 8) and self.weight >= 63.0:
            print("\nOVERWEIGHT")

        if (self.num >= 7) and (self.num <= 8) and self.weight <= 44.0:
            print("\nUNDERWEIGHT")

        if (self.num >= 8) and (self.num <= 9) and self.weight >= 70.5:
            print("\nOVERWEIGHT")

        if (self.num >= 8) and (self.num <= 9) and self.weight <= 49.5:
            print("\nUNDERWEIGHT")

        if (self.num >= 9) and (self.num <= 10) and self.weight >= 78.5:
            print("\nOVERWEIGHT")

        if (self.num >= 9) and (self.num <= 10) and self.weight <= 57.0:
            print("\nUNDERWEIGHT")

        if (self.num >= 10) and (self.num <= 11) and self.weight >= 88.0:
            print("\nOVERWEIGHT")

        if (self.num >= 10) and (self.num <= 11) and self.weight <= 62.0:
            print("\nUNDERWEIGHT")

        if (self.num >= 11) and (self.num <= 12) and self.weight >= 100.0:
            print("\nOVERWEIGHT")

        if (self.num >= 11) and (self.num <= 12) and self.weight <= 70.5:
            print("\nUNDERWEIGHT")

        if (self.num >= 12) and (self.num <= 13) and self.weight >= 112.0:
            print("\nOVERWEIGHT")

        if (self.num >= 12) and (self.num <= 13) and self.weight <= 81.5:
            print("\nUNDERWEIGHT")

        if (self.num >= 13) and (self.num <= 14) and self.weight >= 123.5:
            print("\nOVERWEIGHT")

        if (self.num >= 13) and (self.num <= 14) and self.weight <= 91.5:
            print("\nUNDERWEIGHT")

        if (self.num >= 14) and (self.num <= 15) and self.weight >= 134.0:
            print("\nOVERWEIGHT")

        if (self.num >= 14) and (self.num <= 15) and self.weight <= 101.0:
            print("\nUNDERWEIGHT")

        if (self.num >= 15) and (self.num <= 16) and self.weight >= 142.0:
            print("\nOVERWEIGHT")

        if (self.num >= 15) and (self.num <= 16) and self.weight <= 105.0:
            print("\nUNDERWEIGHT")

        if (self.num >= 16) and (self.num <= 17) and self.weight >= 147.5:
            print("\nOVERWEIGHT")

        if (self.num >= 16) and (self.num <= 17) and self.weight <= 115.0:
            print("\nUNDERWEIGHT")

        if (self.num >= 17) and (self.num <= 18) and self.weight >= 152.0:
            print("\nOVERWEIGHT")

        if (self.num >= 17) and (self.num <= 18) and self.weight <= 118.0:
            print("\nUNDERWEIGHT")

        if (self.num >= 18) and (self.num <= 19) and self.weight >= 155.0:
            print("\nOVERWEIGHT")

        if (self.num >= 18) and (self.num <= 19) and self.weight <= 120.0:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 57) and self.weight >= 103:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 57) and self.weight <= 72:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 58) and self.weight >= 110:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 58) and self.weight <= 77:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 59) and self.weight >= 117:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 59) and self.weight <= 81:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 60) and self.weight >= 123:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 60) and self.weight <= 86:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 61) and self.weight >= 130:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 61) and self.weight <= 90:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 62) and self.weight >= 136:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 62) and self.weight <= 95:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 63) and self.weight >= 143:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 63) and self.weight <= 99:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 64) and self.weight >= 150:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 64) and self.weight <= 104:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 65) and self.weight >= 156:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 65) and self.weight <= 108:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 66) and self.weight >= 163:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 66) and self.weight <= 113:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 67) and self.weight >= 169:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 67) and self.weight <= 117:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 68) and self.weight >= 176:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 68) and self.weight <= 122:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 69) and self.weight >= 183:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 69) and self.weight <= 126:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 70) and self.weight >= 189:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 70) and self.weight <= 131:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 71) and self.weight >= 196:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 71) and self.weight <= 135:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 72) and self.weight >= 202:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 72) and self.weight <= 140:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 73) and self.weight >= 209:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 73) and self.weight <= 144:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 74) and self.weight >= 216:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 74) and self.weight <= 149:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 75) and self.weight >= 216:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 75) and self.weight <= 153:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 76) and self.weight >= 229:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 76) and self.weight <= 158:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 77) and self.weight >= 235:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 77) and self.weight <= 162:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 78) and self.weight >= 242:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 78) and self.weight <= 167:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 79) and self.weight >= 249:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 79) and self.weight <= 171:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 80) and self.weight >= 255:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 80) and self.weight <= 176:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 81) and self.weight >= 262:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 81) and self.weight <= 180:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 82) and self.weight >= 268:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 82) and self.weight <= 185:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 83) and self.weight >= 275:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 83) and self.weight <= 189:
            print("\nUNDERWEIGHT")

        if (self.num >= 19) and (self.height <= 84) and self.weight >= 280:
            print("\nOVERWEIGHT")

        if (self.num >= 19) and (self.height <= 84) and self.weight <= 194:
            print("\nUNDERWEIGHT")

    def blood_warning(self):
        if self.sys <= 90 and self.dia <= 60:
            print("\nLOWBLOODPRESSURE")

        if self.sys >= 120 and self.dia >= 80:
            print("\nHIGHBLOODPRESSURE")

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
            print(f"{family_medical}")


bollinger_kalei = Patient('Kalei', 'Bollinger', '06-05-2001', 115, 65, 'Female', '120', '80', 'O-',
                          ['Abnormal Aortic Aneurysm', 'Chiari Malformation', 'Crohns Disease'], 18,
                          ['CRPS', 'Sacroilitis'], ['Bees', 'Tramidol'], None, ['Zoloft', 'Lutera'])

bollinger_kalei.weight_warning()
bollinger_kalei.type_warning()
