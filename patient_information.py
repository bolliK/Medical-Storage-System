# This  program is written for adults because most kids do not know their medical information
if 1 == 1:
    print("You must be 18 years or older to use this program!")


# This is basically a user class with basic medical information
class Patient:
    def __init__(self, age, height, weight, gender, blood_systolic, blood_diastlic, blood_type, med_history=None):
        self.age = age
        self.tall = height
        self.fat = weight
        self.sex = gender
        self.sys = blood_systolic
        self.dia = blood_diastlic
        self.type = blood_type
        self.issue = med_history

    # This tests for a healthy weight
    def weight_check(self):
        if self.age == 17:
            print("You are not old enough to use this program")
        # Females and Males have different weight scales. The first group here is the female weights
        if self.sex == 1:
            if (57 <= self.tall <= 61) and (self.fat <= 106):
                print("\tUnder Weight")

            if (57 <= self.tall <= 61) and (self.fat >= 140):
                print("\tOver Weight")

            if (62 <= self.tall <= 66) and (self.fat <= 116):
                print("\tUnder Weight")

            if (62 <= self.tall <= 66) and (self.fat >= 160):
                print("\tOver Weight")

            if (67 <= self.tall <= 72) and (self.fat <= 136):
                print("\tUnder Weight")

            if (67 <= self.tall <= 72) and (self.fat >= 180):
                print("\tOver Weight")

            if (73 <= self.tall <= 77) and (self.fat <= 156):
                print("\tUnder Weight")

            if (73 <= self.tall <= 77) and (self.fat >= 200):
                print("\tOver Weight")
        # Mail weights
        if self.sex == 2:
            if (61 <= self.tall <= 65) and (self.fat <= 131):
                print("\tUnder Weight")

            if (61 <= self.tall <= 65) and (self.fat >= 160):
                print("\tOver Weight")

            if (66 <= self.tall <= 70) and (self.fat <= 141):
                print("\tUnder Weight")

            if (66 <= self.tall <= 70) and (self.fat >= 180):
                print("\tOver Weight")

            if (71 <= self.tall <= 75) and (self.fat <= 161):
                print("\tUnder Weight")

            if (71 <= self.tall <= 75) and (self.fat >= 200):
                print("\tOver Weight")

            if (76 <= self.tall <= 80) and (self.fat <= 171):
                print("\tUnder Weight")

            if (76 <= self.tall <= 80) and (self.fat >= 220):
                print("\tOver Weight")

        else:
            print("\tHealthy Weight")

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


doe_john = Patient(30, 72, 170, '2', 125, 83, 'AB-', 'hypertension, diabetes')

doe_john.weight_check()
doe_john.family_warning()
doe_john.type_warning()
doe_john.blood_pressure()
