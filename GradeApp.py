#GUI FCAI GPA calculator using python, OOP, tkinter
from tkinter import *
import tkinter.messagebox

def cal_GPA(grades,credit_hours):
    points = 0
    total_credit_hours = sum(credit_hours)
    grading_classes = {'A+':4,'A':3.7,'B+':3.3,'B':3,'C+':2.7,'C':2.4,'D+':2.2,'D':2,'F':0}
    if grades and credit_hours:
        for i in range(len(grades)):
            grade = grades[i]
            credit_hour= credit_hours[i]
            if grade not in grading_classes:
                return 'Invalid Grade'
            points += grading_classes[grade]*credit_hour
        gpa = points / total_credit_hours
        return gpa
    else:
        return None
class GradeApp:
    def __init__(self,parent):
        self.parent = parent
        self.parent.title("FCAI GPA Calculator")
        self.parent.geometry("500x400")
        self.parent.configure(bg="#282C34")
        self.center_window(700, 300)

        title_label = Label(self.parent, text="FCAI GPA Calculator", font=("Arial", 20, "bold"), fg="white", bg="#282C34")
        title_label.pack(pady=10)
        
        self.frame_1 = Frame(parent, bg="#282C34")
        self.frame_1.pack()
        
        self.sub_count = 1
        self.grades = []
        self.credit_hours = []
        Label(self.frame_1, text="Course Name: ",font=("Arial", 12), bg="#282C34", fg="white").grid(row=0,column = 0, padx=10, pady=5)
        Label(self.frame_1, text="Grade: ",font=("Arial", 12), bg="#282C34", fg="white").grid(row=0,column = 1, padx=10, pady=5)
        Label(self.frame_1, text="Credits: ",font=("Arial", 12), bg="#282C34", fg="white").grid(row=0,column = 2, padx=10, pady=5)

        self.course_name = Entry(self.frame_1,font=("Arial", 12))        
        self.course_name.grid(row=self.sub_count,column=0, padx=10, pady=5)

        self.grade_entry = Entry(self.frame_1,font=("Arial", 12))        
        self.grade_entry.grid(row=self.sub_count,column=1, padx=10, pady=5)

        self.credit_hour_entry = Entry(self.frame_1,font=("Arial", 12))        
        self.credit_hour_entry.grid(row=self.sub_count,column=2, padx=10, pady=5)

        self.btn_1 = Button(parent, text='+', font=("Arial", 12, "bold"), bg="#61AFEF", fg="white",
                                     activebackground="#56B6C2",
                            command=self.add_courses)
        self.btn_1.pack(pady=10)
        
        self.btn_2 = Button(parent,text="Find GPA", font=("Arial", 12, "bold"), bg="#61AFEF", fg="white",
                                     activebackground="#56B6C2",
                            command=self.calc)
        self.btn_2.pack(pady=10)
        
    def center_window(self, width, height, window=None):
        if window is None:
            window = self.parent
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f'{width}x{height}+{x}+{y}')

    def add_courses(self):
        self.sub_count += 1
        
        course_name = Entry(self.frame_1,font=("Arial", 12))        
        course_name.grid(row=self.sub_count,column=0, padx=10, pady=5)

        grade_entry = Entry(self.frame_1,font=("Arial", 12))        
        grade_entry.grid(row=self.sub_count,column=1, padx=10, pady=5)

        credit_hour_entry = Entry(self.frame_1,font=("Arial", 12))        
        credit_hour_entry.grid(row=self.sub_count,column=2, padx=10, pady=5)
        
        self.grades.append(grade_entry)
        self.credit_hours.append(credit_hour_entry)
    def calc(self):
        grades = []
        credit_hours = []
        
        for grade_entry,credit_hour_entry in zip(self.grades, self.credit_hours):
            if grade_entry.get() != "" and credit_hour_entry.get() != "":
                grades.append(grade_entry.get())
                try:
                    credit_hours.append(float(credit_hour_entry.get()))
                except ValueError:
                    tkinter.messagebox.showerror("Invalid Input", "Credit hours should be a number")
                    return
        gpa = cal_GPA(grades, credit_hours)
        if gpa is not None:
            self.show_gpa_window(gpa)
        else:
            tkinter.messagebox.showerror("Error", "Please enter valid grades and credit hours")

    def show_gpa_window(self, gpa):
        result_window = Toplevel(self.parent)
        result_window.title("GPA Result")
        result_window.geometry("300x150")
        result_window.configure(bg="#282C34")
        self.center_window(300, 150, window=result_window)  

        result_label = Label(result_window, text=f"Your GPA is: {gpa:.2f}", font=("Arial", 16, "bold"), fg="white", bg="#282C34")
        result_label.pack(pady=30)

        ok_button = Button(result_window, text="OK", font=("Arial", 12, "bold"), bg="#98C379", fg="white", command=result_window.destroy)
        ok_button.pack()

root = Tk()
app = GradeApp(root)
root.mainloop()
