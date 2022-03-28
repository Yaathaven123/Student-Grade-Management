#Part 4 - Vertical Histogram (optional extension)

total = 120
levels=[0,0,0,0] #holds value for Progress, Trailer, Retriever, and Excluded respectively
output_1=("Progress")
output_2=('Progress (module trailer)')
output_3=('Do not progress - module retriever')
output_4=('Exclude')
credit_levels = ["pass","deffer","fail"]
category=["Progress   ","Trailer    ","Retriever  ","Excluded   "]
data=[[120,0,0,],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]]

def listed(data): #function to read from the given data
    for j in range(len(data)): #loop for the number of elements in the list
        credit_vol=[]
        for element in range(len(data[j])): #loop for the number of elements in the list within the list
            credit_vol.append(data[j][element]) #add to credit.vol[]
        if (credit_vol[0] == 120) :
             p_outcome = (output_1)
             levels[0] += 1
        elif (credit_vol[0] == 100) :
             p_outcome = (output_2)
             levels[1] += 1
        elif (credit_vol[2] >= 80) :
             p_outcome = (output_4)
             levels[3] += 1
        else :
             p_outcome = (output_3)
             levels[2] += 1
        print(p_outcome,)
    
listed(data) #call the function

total_outcomes=len(data)

print("\n")
for i in range(len(category)): #loop for the number of elements in the list
    print(category[i]  , levels[i] , "   :",("* " * levels[i]))
print("\n")
print(total_outcomes , " outcomes in total\n")
