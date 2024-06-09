# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.
# Student ID : 20220855 / w2053019
# Date: 2023/11/13

#My Assumptions:
#User is able to select student or staff version by enetering 1 for student version and 2 for staff.
#If user prompts 2 or any other number(except 1), programm selects the staff version.
#Displaying the Histogram and text file records are only for staff version.
#Only in text file part, program writes the outcome results to the text file in the order of user inputs(entering order).

#import libraries
from graphics import *

#Inizialize variables
credit = 0
level = ""
pass_ = 0
defer_ = 0
fail_ = 0
progress = []
module_trailer = []
module_retriever = []
exclude = []
list_ = []

#Define functions
def credit_validation(level):
    "function to validate inputs"
    enter_credit = True
    while enter_credit:
        try:
            credit = int(input("Please enter your credits at "+ level +": "))
            if credit in (0,20,40,60,80,100,120):
                enter_credit = False
            else:
                print("Out of range.\n")        
        except ValueError:
            print("Integer required\n")
    return (credit)

def progression(pass_,defer_,fail_):
    "Produce the progression outcome - progress /module trailer/ retriever/ exclude"
    outcome = ""                                        
    if (pass_ == 120):
        outcome = "Progress"
        progress.append("progress - "+str(pass_)+", "+str(defer_)+", "+str(fail_))  #appending to the list
    elif (pass_ == 100):
        outcome = "Progress (module trailer)"
        module_trailer.append("Progress (module_trailer) - "+str(pass_)+", "+str(defer_)+", "+str(fail_))
    elif (fail_ >= 80):
        outcome = "Exclude"
        exclude.append("Exclude - "+str(pass_)+", "+str(defer_)+", "+str(fail_))
    else:
        outcome = "Module retriever"
        module_retriever.append("Module retriever - "+str(pass_)+", "+str(defer_)+", "+str(fail_))
    return (outcome)

def display_histogram():
    "This will diplay the histogram"
    #display the window
    win = GraphWin("The Histogram window", 700,500)
    win.setBackground("mint cream")
    title = Text(Point(120,60),"Histogram Results")
    title.setSize(15)
    title.setStyle("bold")
    title.draw(win)

    colour = ("#aef8a1","#a0c689","#a7bc77","#d2b6b5")
    outcome_lable = ("Progress","Trailer","Retriever","Excluded")
    count_values =(len(progress),len(module_trailer),len(module_retriever),len(exclude))
    
    #Draw a line and the bar graph
    graph_line = Line(Point(20,400),Point(650,400))
    graph_line.draw(win)
    for i in range(4):
        rectangle = Rectangle(Point(50 +i * 150, 400), Point(150+ i*150, 400 - count_values[i] * 50))
        rectangle.setFill(colour[i])
        rectangle.draw(win)         
        rectangle_label = Text(Point(100+i*150, 420),"{}: {}".format(outcome_lable[i],count_values[i]))
        rectangle_label.setStyle("bold")
        rectangle_label.draw(win)
        
    #display the total
    total_line = Text(Point(300, 460), "{} outcomes in Total".format(sum(count_values)))
    total_line.setSize(12)
    total_line.setStyle("bold")
    total_line.draw(win)

    try:
        win.getMouse()  #wait for a click before closing window
        win.close()
    except:
        win.close()
   
def main_programm():
    try:
        text_file = open("output.txt","w")  #only for opening a new file and close it 
        text_file.close()
    except :
        print("File create error")        
    print("Part 1:\n")
    version = int(input("Please select a version.(Student/Staff)\nEnter 1 for student version, 2 for staff version : "))
    programe_exit = False
    while not (programe_exit) :
        #prompt user inputs and validate by callig function 
        while True:           
            credit_pass = credit_validation("pass")
            credit_defer = credit_validation("defer")
            credit_fail = credit_validation("fail")
            #validate total 
            if (credit_pass + credit_defer + credit_fail != 120):
                print("Total incorrect.\n")
            else:
                break
     
        #Call function to produce the progression outcome
        progression_outcome=progression(credit_pass,credit_defer,credit_fail)
        print(progression_outcome,"\n")

        #part 3 - write progression outcome to a text file                
        try:
            text_file = open("output.txt","a")
            text_file.write(progression_outcome+" - "+str(credit_pass)+", "+str(credit_defer)+", "+str(credit_fail) +"\n")
            text_file.close()
        except :
            print("File open error")
           
        while True:
            if version == 1:
                programe_exit = True
                break
            else: #when 2 or any other number given It's staff version
                print("Would you like to enter another set of data? ")
                enter_another = input("Enter 'y' for yes or 'q' to quit and view results:")
                print("")
                if (enter_another == "q"):
                    programe_exit = True
                    print("Display histrogram")
                    print("Click on the histogram to continue.\n")
                    display_histogram() #function calling for histogram

                    #part 2 list extension
                    list_.append(progress)
                    list_.append(module_trailer)
                    list_.append(module_retriever)
                    list_.append(exclude)
                    print("Part 2:\n")
                    for x in range(len(list_)):
                        for i in list_[x]:
                            print(i)

                    #part 3 - Display the outcome by reading text file               
                    try:
                        print("\nPart 3:\n")
                        text_file = open("output.txt","r")
                        print(text_file.read())
                        text_file.close()

                    except:
                        print("file not found")
                    break       #To exit the loop when 'q' is entered
                elif(enter_another == "y"):
                    break
                else:
                    print("Please enter 'y' or 'q' ")
                    continue
    
#----------------Main Programme--------------------#
main_programm()
