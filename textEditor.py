#Petia Nikolova
#002
#pbni222@g.uky.edu
#December 7, 2016

#from graphics import * 

#Purpose: An online multiple choice grader. Has many purposes: loads a data file, displays scores, finds a specified student's score, shows biggest or smallest score, makes a bar graph of scores, or creates a new file which contains scores.
#Pre-conditions: Text file containing user Questions numbers, ID's, test-takers answers, & the KEY.
#Post-conditions: menu choices, prompts for filenames,  prompts for Enter to continue
#grades displayed on screen, grades displayed as bar chart on graphics window



#purpose:  display menu, validate user choice, return choice
#pre-condition:  no parameters
#post-condition:  displays menu, returns validated choice as lowercase letter in "ldfbsacwq"
def get_menu_choice():
    
    #print menu
    print("Multiple Choice Grader\n\nMain Menu\n\n(L)oad a data file\n(D)isplay the scores\n(F)ind a student's score\n(B)iggest score\n(S)mallest score\n(A)verage score\n(C)hart the scores in a bar graph\n(W)rite the scores to a file\n(Q)uit the program\n")
    
    #user inputs choice from menu, remove whitespace, make all lowercase
    usr_inp = input("Enter your choice: ")
    usr_inp = usr_inp.strip()
    usr_inp = usr_inp.lower()
    
    return (usr_inp)





#pre-conditions: no parameters, asks user for valid filename
#post-conditions: returns a 2-d list of student IDs and grades
#purpose: get data from given file, grade the responses, produce
#list of student ids and corresponding grades
def get_data():
    open_file = False
    while not open_file:
	#user enters file name until true
        try:
            usr_file_inp = input("What is the file name? ")
            infile = open(usr_file_inp, "r")
            open_file = True
            print("File loaded")
        except IOError:
            print("Try Again", usr_file_inp)    
    
    #create an empty list to sep and write data
    data = []
    for line in infile:
        key_ids = line.split() 
        data.append(key_ids) 
    #print(data)
    
    final_grades =  grader(data)
    
    print("grades done")
    input("Press Enter to Continue ")
		
    return(final_grades)



#pre-conditions:  the 2-d list from the input file
#post-conditions:  the 2-d list of student ids and grades
#purpose:  find the students' scores by comparing key responses to student responses,
#finding what percent responses are correct, build list of student ids and grades
def grader(grades):
	
	scores = []
	for i in range(2, len(grades)):
		#if ((grades[i][0] != "Student") or (grades[i][0] != "KEY"):
		scores.append([grades[i][0], len(grades[1])-1])
		#scores[i].append(grades[i][0])
		#scores[i].append(len(grades[1]))
	#print(scores) 

	for i in range(2, len(grades)):
		for k in range(1, len(grades[1])):
			if (grades[1][k] != grades[i][k]):
				scores[i-2][1] = scores[i-2][1] - 1
			#print(i)
	for i in range(len(scores)):
		scores[i][1] = (scores[i][1] / (len(grades[1]) - 1)) * 100
	
	return(scores)




#purpose:  print out grades list on shell window
#pre-conditions: grades list (ids and scores)
#post-conditions: if grades list is not empty,
#prints the information in the grades list to the shell in a nice 
#columnar format otherwise says "no scores" no return value
def print_data(print_scores):
        #for loop, for len of data, read and write from array, and sep with 
	#space
	for i in range(len(print_scores)):
		for k in range(len(print_scores[0])):
			print(print_scores[i][k], end=" ")
		print('\n')
	input("Press Enter to Continue")
	
	return()





#precondition:  grades list (ids and grades)
#postcondition:  returns average if grades list is not empty (sum of column 1 divided by length of list)
     #or zero if grades list is empty
#purpose:  find average grade from all grades in grades list
def get_average(avg_scores):

	average = 0.0
	for i in range(len(avg_scores)):
		average = average + avg_scores[i][1]
	average = average / (len(avg_scores)) 
	
	return(average)






#purpose:  ask  user for ID, search for ID in grades list, report the first one found
#if any found, report "no student found" if none found
#pre-condition:  grades list as parameter, as user for ID to search for
#postcondition:  reports first ID that matches user input and corresponding grade
#if no match, report "no student found" no return value
def search(search_scores):

    #set flag to false 
    ID_not_found = False
    user_inp = input("Enter the Student ID you want to find the data for: ")
    user_inp = user_inp.replace(" ", "")
    
    #for loop to seach the two-d array and compare to see if ID found
    for i in range(len(search_scores)):
        if (user_inp) == search_scores[i][0]:
                print(search_scores[i][0], search_scores[i][1])
                ID_not_found = True
    #if ID not found, say it, tell to press enter, and exit
    if ID_not_found == False:
        print("ID not found\n")
    input("\nPress Enter to Continue ")

    return()




#purpose:  find largest grade from all grades in grades list
#precondition:  grades list
#postcondition: position of largest grade (in column 1) if list is empty, returns 0
def get_largest(big_score):
   
    #set max to 0 so there will always be someone more than 0 
    max_score = -1
    location = 0
    for i in range(len(big_score)):
        #print(big_score[i][1])
        if max_score < big_score[i][1]:
                max_score = big_score[i][1]
                location = i
    #largest = max(big_score[1])
    return(location)





#purpose:  find smallest grade from all grades in grades list
#precondition:  grades list
#postcondition: position of smallest grade (in column 1) if list is empty, returns 0
def get_smallest(small_score):
    
    #make min score 101 so there will always be someone less than the set min
    min_score = 101
    location = 0
    for i in range(len(small_score)):
        #print(small_score[i][1])
        if min_score > small_score[i][1]:
                min_score = small_score[i][1]
                location = i
    return(location)




#purpose:  writes out grades list to desired file, one student per line
#pre-condition:  grades list (ids and scores)
#post-conditions: if grades list is not empty, 
#output grades list to new file with user-supplied name, each student on a separate line,
#id and grade delimited by whitespace otherwise report "empty list, no file created"
def write_grades(write_score):
    
    #user inputs wanted file name to write grades over to 
    usr_inp = input("Please enter a file name to store scores: ")
    new_file = open(usr_inp, 'w')
    
    #for length of data, add whitespace between each obj from array, and newline
    for i in range(len(write_score)):
        temp_write = str(write_score[i][0] + " " + str(write_score[i][1]) + "\n")
        #write line by line into new_file, save, and close
        new_file.write(temp_write)
    new_file.close() 
    return()



#purpose:  draw chart scaled to window
#precondition:  grades list, click by user to cause program to continue
#postcondition:  bar chart drawn from info in grades list, no return value
'''def draw_bar(draw_scores):
    #Create window with title "bar chart"
    win = GraphWin("Bar Chart", 650, 650)
    
    #"set y-axis coordinates to exam grades(by 5)"
    coord1 = Text(Point(100, 560), "0")
    coord2 = Text(Point(100, 532), "5")
    coord3 = Text(Point(100, 504), "10")
    coord4 = Text(Point(100, 476), "15")
    coord5 = Text(Point(100, 448), "20")
    coord6 = Text(Point(100, 420), "25")
    coord7 = Text(Point(100, 392), "30")
    coord8 = Text(Point(100, 364), "35")
    coord9 = Text(Point(100, 336), "40")
    coord10 = Text(Point(100, 308), "45")
    coord11 = Text(Point(100, 280), "50")
    coord12 = Text(Point(100, 252), "55")
    coord13 = Text(Point(100, 224), "60")
    coord14 = Text(Point(100, 196), "65")
    coord15 = Text(Point(100, 168), "70")
    coord16 = Text(Point(100, 140), "75")
    coord17 = Text(Point(100, 112), "80")
    coord18 = Text(Point(100, 84), "85")
    coord19 = Text(Point(100, 56), "90")
    coord20 = Text(Point(100, 28), "95")
    coord20 = Text(Point(100, 15), "100")
    exit_message = Text(Point(325,580), "Student Scores - Click To Close!")
    
    coord1.draw(win)
    coord2.draw(win)
    coord3.draw(win)
    coord4.draw(win)
    coord5.draw(win)
    coord6.draw(win)
    coord7.draw(win)
    coord8.draw(win)
    coord9.draw(win)
    coord10.draw(win)
    coord11.draw(win)
    coord12.draw(win)
    coord13.draw(win)
    coord14.draw(win)
    coord15.draw(win)
    coord16.draw(win)
    coord17.draw(win)
    coord18.draw(win)
    coord19.draw(win)
    coord20.draw(win)
    
    exit_message.draw(win)
    win.getMouse()
    win.close()    
    
    #for i in range(len(draw_scores)):
	#new_id = str(draw_scores[i][1])
	#stu_id = Text(Point(400,400), new_id)
	#draw.stu_id(win)
    
    return()'''





#purpose:  to input student answers for a multiple-choice,
    #produce the student grades, display them for the user in different ways 
#pre-conditions:  user menu choices, filename to read from, filename to write to
     #click on graphics window, Enter to make program proceed
     #handles ANY number of students, any number of responses per student
#post-conditions:  menu choices, prompts for filenames,  prompts for Enter to continue
     #grades displayed on screen, grades displayed as bar chart on graphics window
def main():
    
    choice_made = ''
    get_data_answer = ''
    
    #create while loop for different user input options
    while (choice_made != 'q'):
        choice_made = get_menu_choice()
        if choice_made == 'l':
            get_data_answer = get_data()
	    #get_data_answer not == scores
        elif choice_made == 'd':
            print_data(get_data_answer)
        elif choice_made == 'f':
            search_student = search(get_data_answer)
        elif choice_made == 'b':
            biggest_score = get_largest(get_data_answer)
            print("Largest score is: ", get_data_answer[biggest_score][0], " ", get_data_answer[biggest_score][1])
        elif choice_made == 's':
            smallest_score = get_smallest(get_data_answer)
            print("Smallest score is: ", get_data_answer[smallest_score][0], " ", get_data_answer[smallest_score][1])
        elif choice_made == 'a':
            get_average_score = get_average(get_data_answer) 
            print("The average score is: ",get_average_score)
        elif choice_made == 'c':
            #draw_bar(get_data_answer)
            print("Draw Graph")
        elif choice_made == 'w':
            write_grades(get_data_answer)              
        else:
            if choice_made != 'q':
		#if button is not is not an option, print "Try again"
                print("Try Again!")
    print("Thank you for using the Multiple Choice Grader!")
main()

