# Tkinter frame written by Jaden Costa (@Q_flat on Github)

from tkinter import *
import tkinter.messagebox as tm
import v2

class Frame:
    def __init__(self, master):
        self.master=master
        master.title('Medical Project')

        self.f_label=Label(master,text='First Name: ')
        self.f_label.grid(row=0,column=0)
        self.f=Entry(master)
        self.f.grid(row=0,column=1)

        self.l_label=Label(master,text='Last Name: ')
        self.l_label.grid(row=1,column=0)
        self.l=Entry(master)
        self.l.grid(row=1,column=1)

        self.age_label=Label(master,text='Age: ')
        self.age_label.grid(row=2,column=0)
        self.age=StringVar()
        self.age_choice=[0.25, 0.5, 0.75, 1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, '19+']
        self.menu=OptionMenu(master,self.age,*self.age_choice)
        self.menu.grid(row=2,column=1)

        self.ft_label=Label(master,text='Feet: ')
        self.ft_label.grid(row=3,column=0)
        self.feet=StringVar()
        self.ft_choice=list(range(0,8))
        self.ft_menu=OptionMenu(master,self.feet,*self.ft_choice)
        self.ft_menu.grid(row=3,column=1)

        self.in_label=Label(master,text='Inches: ')
        self.in_label.grid(row=4,column=0)
        self.inches=StringVar()
        self.in_choice=list(range(0,13))
        self.in_menu=OptionMenu(master,self.inches,*self.in_choice)
        self.in_menu.grid(row=4,column=1)

        self.sex_label=Label(master,text='Sex:')
        self.sex_label.grid(row=5,column=0)
        self.sex=StringVar()
        self.sexes=['Male','Female']
        self.sexes_menu=OptionMenu(master,self.sex,*self.sexes)
        self.sexes_menu.grid(row=5,column=1)

        self.sys_label=Label(master,text='Systolic: ')
        self.sys_label.grid(row=6,column=0)
        self.s=Entry(master)
        self.s.grid(row=6,column=1)

        self.dia_label=Label(master,text='Diastlic: ')
        self.dia_label.grid(row=7,column=0)
        self.d=Entry(master)
        self.d.grid(row=7,column=1)

        self.blood_label=Label(master,text='Blood Type: ')
        self.blood_label.grid(row=8,column=0)
        self.blood_types=['A-','A+','B-','B+','AB-','AB+','O-','O+']
        self.blood_type=StringVar()
        self.blood_menu=OptionMenu(master,self.blood_type,*self.blood_types)
        self.blood_menu.grid(row=8,column=1)

        self.info_label=Label(master,text='Any other medical history: ')
        self.info_label.grid(row=9,column=0)
        self.i=Entry(master)
        self.i.grid(row=9,column=1)

        self.b=Button(master,text='Submit',command=self.submit)
        self.b.grid(row=10)

    def submit(self):
        global dia
        dia=self.d.get()
        global sys
        sys=self.s.get()
        global info
        info=self.i.get()
        global first
        first=self.f.get()
        global last
        last=self.l.get()
        string=first+','+last+','+str(self.age.get())+','+str(self.feet.get())+','+str(self.inches.get())+','+str(self.sex.get())+','+str(sys)+','+str(dia)+','+str(self.blood_type.get())+','+str(info)
        try:
            f=open('patients.txt','a')
            f.write(string+'\n')
            f.close()
        except PermissionError:
            tm.showerror('Unable to Add Patient','Please Close File Before Adding Patient')
        self.master.destroy()
