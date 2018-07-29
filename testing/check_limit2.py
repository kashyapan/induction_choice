import csv
import allocation_choice
global max

def allocate(choices,course_contents,course_students,pending):    
    if choices[1] in course_contents:
        secondid = course_contents.index(choices[1])
        if len(course_students[secondid])<max:
            course_students[secondid].append(choices[0])
            print choices[0], "in course", course_contents[secondid]
        elif choices[2] in course_contents:
            thirdid = course_contents.index(choices[2])
            if len(course_students[thirdid])<max:
                course_students[thirdid].append(choices[0])
                print choices[0], "in course", course_contents[thirdid]
            elif choices[3] in course_contents:
                fourthid = course_contents.index(choices[3])
                if len(course_students[fourthid])<max:
                    course_students[fourthid].append(choices[0])
                    print choices[0], "in course", course_contents[fourthid]
                elif choices[4] in course_contents:
                    fifthid = course_contents.index(choices[4])
                    if len(course_students[fifthid])<max:
                        course_students[fifthid].append(choices[0])
                        print choices[0], "in course", course_contents[fifthid]
                    else:
                        pending.append(choices[0])
                        
                       
                        
                     
    
    

max = 33
coursea = allocation_choice.coursea
courseb = allocation_choice.courseb
coursec = allocation_choice.coursec
coursed = allocation_choice.coursed
coursee = allocation_choice.coursee
coursef = allocation_choice.coursef

lefta =[]
leftb = []
leftc = []
leftd = []
lefte = []
leftf = []

course_students = [coursea,courseb,coursec,coursed,coursee,coursef]
#print "testing", course_students[2]
course_contents = ["a","b","c","d","e","f"]
leftout = [lefta,leftb,leftc,leftd,lefte,leftf]
print "--------------------------------------------------"
#truncate the list of students in each class to 33
for num in range(len(course_students)):
    if len(course_students[num])>max:
        leftout[num] = course_students[num][max:]
        course_students[num] = course_students[num][:max]
        
print "---------------------------------------------------"   

print "Number of students in each course after truncating to maximum"
print "--------------------------------------------------------------"     
for i in range (len(course_students)):
    print "course ",  course_contents[i], ":", len(course_students[i])
print "Number of students left out after choice 1"
print "-------------------------------------------"
for i in range(len(leftout)):
    print "course ",i+1,":", len(leftout[i])
    #----------------------------------------------------------

#print "testing", len(course_students[2])
pending = []
#print leftout[0],len(leftout[0])
with open('choice.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
    entire_details = readCSV
    for row in entire_details:
        for i in range(len(leftout)):
            for student in leftout[i]:
                if ((student in leftout[i]) and (student not in course_students[i])):                
                    if student == row[1]:
                        second = row[3]
                        third = row[4]
                        fourth = row[5]
                        fifth = row[6]
                        print row
                        
                        #print len(course_students[0])
                        choices = [student,second,third,fourth,fifth]
                        allocate(choices,course_contents,course_students,pending)
                            #print "testing2", len(course_students[2])
                        for i in range (len(course_students)):
                            print "course ",  course_contents[i], ":", len(course_students[i])
                        

                            
print "Pending students", pending, len(pending)
for n1 in range(len(pending)):
    for course in course_students:
        if len(course)<max:
            course.append(pending[n1])
print "Number of students in each course - final"
print "------------------------------------------"
for i in range (len(course_students)):
    print "course ",  course_contents[i], ":", len(course_students[i])

 