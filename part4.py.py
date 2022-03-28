#Part 4 - Vertical Histogram (optional extension)

total = 120
levels=[0,0,0,0] #holds value for Progress, Trailer, Retriever, and Excluded respectively
output_1=("Progress")
output_2=('Progress (module trailer)')
output_3=('Do not progress - module retriever')
output_4=('Exclude')
credit_levels = ["pass","deffer","fail"]
credit_vol=[0,0,0] #holds value for pass, deffer and fail respectively
category=["Progress   ","Trailer    ","Retriever  ","Excluded   "]
total_outcomes=0

def inputs(credit_answer):
    while True: #loop until the input is within range
        try: #loop until the input is an integer
            credit_answer=int(input("Please enter your credits at " + credit_levels[x] + " : "))
            if (credit_answer < 0) or (credit_answer > 120) or (credit_answer % 20 != 0):
                print('Out of range.\n')
                continue       
            else:
                return credit_answer
                break #break the loop
        except :
            print('Integer required\n')

while True:
    for x in range(len(credit_vol)): #loop for the number of elements in the list
        credit_vol[x] = inputs(credit_levels[x])
    if credit_vol[0] + credit_vol[1] + credit_vol[2] != total :
        print("Total Incorrect\n")
        continue
    if (credit_vol[0] == 120) :
        p_outcome = (output_1)
        levels[0] += 1
        total_outcomes += 1
    elif (credit_vol[0] == 100) :
        p_outcome = (output_2)
        levels[1] += 1
        total_outcomes += 1
    elif (credit_vol[2] >= 80) :
        p_outcome = (output_4)
        levels[3] += 1
        total_outcomes += 1
    else :
        p_outcome = (output_3)
        levels[2] += 1
        total_outcomes += 1
    print(p_outcome,)
    print("\nWould you like to enter another set of data?")
    response = str(input("Enter 'y' for yes or 'q' to quit and view results: "))
    if response==("y") :
        print("\n")
        continue
    else :
        print("\n")
        break #break the loop

print("Horizontal Histogram")
for i in range(len(category)): #loop for the number of elements in the list
    print(category[i]  , levels[i] , "   :",("* " * levels[i]))
print("\n")
print(total_outcomes , " outcomes in total\n")

def vert_histogram(): #print a star or a space accordingly
    if levels[0] >= 1 :
        print("     *     ", end = '')
        levels[0] -= 1
    else :
        print("           ", end = '')
    if levels[1] >= 1 :
        print("     *     ", end = '')
        levels[1] -= 1
    else :
        print("           ", end = '')
    if levels[2] >= 1 :
        print("     *     ", end = '')
        levels[2] -= 1
    else :
        print("           ", end = '')
    if levels[3] >= 1 :
        print("     *     ", end = '\n')
        levels[3] -= 1
    else :
        print("           ", end = '\n')

print(category[0] , category[1] , category[2] , category[3])
for i in range(total_outcomes): #loop for the number of elements in the list
    vert_histogram()
