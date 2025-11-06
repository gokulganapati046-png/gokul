# MARKS CALCULATOR #
students =["Gokul" ,"Harry", "Rahul", "Poonam"]

subjects =["English","Hindi", "maths","science"]

student_total ={}
for student in students:
    total =0
    print(f" Entering the marks of {student}")
    for subject  in subjects:
        while True:
            marks = int(input(f"Enter the marks of {subject} :"))
            if 0<= marks<=100:
               break
            else:
               print("invalid number")
        total+=marks
        if  marks>=91 and marks<=100:
            print("Grade = A")
        elif marks>=81 and marks<=90:
            print("Grade = B")
        elif marks>=71 and marks<=80:
            print("Grade = C")           
        elif marks>=60 and marks<=70:
            print("Grade = D") 
        elif marks<60:
            print("Grade = F")                                                
    print(f"total marks of {student}:{total}")


    avg_marks_of_student = total/len(subjects)
     
    print(f"avaerage marks of {student} : {avg_marks_of_student}") 

    student_total[student]=total

print(student_total)

low_scorer =min(student_total,key=student_total.get)
print(f"Lowest scorer student is {low_scorer}")

max_student = max(student_total,key=student_total.get)
max_total = student_total[max_student]                     # it prints the max marks, who got
print("highest scorer is ",max_student)




    



