enter = input("""Instructions:read the instructions carefully before attempting the paper.
         Total marks:30                      Total questions:10
         1)Enter the key of the objectives you think is right.
         2)If you want to skip a question ,press key 's'.
         3)Each correct question will award you 4 marks.
         4)A wrong answer will lead to the deduction of 5 marks (negative marking of 1 mark).
         5)if you want to again view skipped questions at the end,enter key 'yes'.
         6)To start the exam press enter key and click start exam button. """)

import time
import tkinter as tk

clock_window = tk.Tk()
clock_window.title("Countdown timer")
clock_window.geometry("100x100")
clock_window.config(background = 'orange')
min = tk.StringVar()
sec = tk.StringVar()
min.set("00")
sec.set("00")
label1 = tk.Label(clock_window,textvariable = min)
label2 = tk.Label(clock_window,textvariable = sec)
label1.pack()
label2.pack()
clock_window.mainloop()



def timer():
    my_time = 20
    for x in range(my_time,0,-1):
        seconds = x % 60
        minutes = int(x / 60)
        sec.set(f"{seconds:02}")
        min.set(f"{minutes:02}")
        clock_window.update()
        time.sleep(1)
    print("TIMES UP!!!!!")

def exam_start():
    if enter == '':
        q1 = input("""Question no 1 : If A is a square matrix such that A2 = A, 
                        then (I – A)3 + A is equal to:
              A)I                    B)0
              c)I-A                  D)I+A """)
        q2 = input("""Question no 2:If (d/dx) f(x) is g(x), 
                      then the antiderivative of g(x) is
               A)f(x)                B)f’(x)
               C)g’(x)               D)None of these """)
        q3 = input("""Question no 3:Which of the following does not belong 
                      in the category of electrochemical cells?
               A) Voltaic cell      B) Photovoltaic cell
               C) Electrolytic cell   D) Fuel Cell """)
        q4 = input("""Question no 4:As an electroplated protective covering,
                      what metal is used?
                A) Plutonium         B) Chromium
                C) Nickel            D) Iron """)
        q5 = input("""Question no 5: Which of the following statements is true?
                A)A metal plate can be heated by passing either a 
                direct current or an alternating current through the plate.
                B)A metal plate can be heated by placing it
                 in a time-invariant magnetic field.
                C)A metal plate can be heated by placing it
                 in a time-variant magnetic field
                D)Both (a) and (c) """)
        q6 = input("""Question no 6:Three capacitors of Capacitance 1microfarad 
         each are connected in series.Their equivalent capacitance is?
                A)0.03microF          B)0.03nanoFarad
                C)1.5microF           D)1.5nanoFarad """)
        q7 = input("""Question no 7: Complete sentence.
            It was so quiet_____(can) hear a pin drop.
               A)can                 B)could
               C)shall               D)will """)
        q8 = input("""Question no 8: Correct Grammar.
               Work hard lest you_______fail.
               A)could               B)should
               C)want to             D)will """)
        q9 = input("""Question no 9: The coefficient of the middle term 
               in the expansion of (2+3x)4 is:
               A)5!                   B)6
               C)216                  D)8! """)
        q10 = input("""Question no 10: The number of squares that can be 
                formed on a chessboard is:
                A)64                  B)160
                C)224                 D)204 """)
        answers = []
        answers.append(q1.upper())
        answers.append(q2.upper())
        answers.append(q3.upper())
        answers.append(q4.upper())
        answers.append(q5.upper())
        answers.append(q6.upper())
        answers.append(q7.upper())
        answers.append(q8.upper())
        answers.append(q9.upper())
        answers.append(q10.upper())
        final_ans = tuple(answers)
        key = ('A', 'A', 'B', 'B', 'D', 'C', 'B', 'B', 'C', 'D')
        def correct_questions():
            correct = 0
            i = 0
            for options in range(0, len(final_ans)):
                if key[i] == final_ans[options]:
                    correct += 1
                i = i + 1
            return correct

        def skip():
            count = 0
            for each_ans in answers:
                if each_ans == 'S':
                    count += 1
            return count

        wrong = 0
        j = 0
        for i in range(0, len(answers)):
            if key[j] != answers[i]:
                wrong += 1
            if answers[i] == 'S':
                wrong = wrong - 1
            j += 1
        total_correct = correct_questions()
        skipped_q = skip()
        marks = (total_correct * 4) - wrong
        print(f"Your total correct questions are:{total_correct}")
        print(f"The skipped questions are:{skipped_q}")
        print(f"Your total marks count is:{marks}")
        print(f"The no of qs wrong are:{wrong}")
        if marks <= 20:
            print("Oops sorry,you are not granted admission in UET.Better luck next time!.")
        else:
            print("Congrats!!!! You are accepted into UET.")

roots = tk.Tk()
roots.title("Exam Timer")
roots.geometry("120x100")
roots_button = tk.Button(roots,text="Start Exam",command=lambda:[exam_start(),timer()])
roots_button.pack()
roots.mainloop()


















