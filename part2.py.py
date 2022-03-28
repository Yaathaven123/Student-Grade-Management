#Part 2 – Student Version (Validation)

total = 120
output_1=("Progress")
output_2=('Progress (module trailer)')
output_3=('Do not progress - module retriever')
output_4=('Exclude')
while True : #loop until the inputs add up tp 120
    while True: #loop until the input is within range
        try : #loop until the input is an integer
            credit_pass = int(input("Please enter your credits at pass : "))
            if (credit_pass < 0 or credit_pass > 120 or credit_pass % 20 != 0):
                print('Out of range.\n')
            else :
                break #break the loop
        except ValueError:
            print('Integer required\n')
    while True: #loop until the input is within range
        try : #loop until the input is an integer
            credit_deffer = int(input("Please enter your credits at deffer : "))
            if (credit_deffer < 0 or credit_deffer > 120 or credit_deffer % 20 != 0):
                print('Out of range.\n')
            else :
                break #break the loop
        except ValueError:
            print('Integer required\n')
    while True: #loop until the input is within range
        try : #loop until the input is an integer
            credit_fail = int(input("Please enter your credits at fail : "))
            if (credit_fail < 0 or credit_fail > 120 or credit_fail % 20 != 0):
                print('Out of range.\n')
            else :
                break #break the loop
        except ValueError:
            print('Integer required\n')
    if (credit_pass + credit_deffer + credit_fail != total) :
        print('Total incorrect.\n')
    else :
           break #break the loop
if (credit_pass == 120) :
    p_outcome = (output_1)
elif (credit_pass == 100) :
    p_outcome = (output_2)
elif (credit_fail >= 80) :
    p_outcome = (output_4)
else :
    p_outcome = (output_3)
print(p_outcome,) #print the outcome
