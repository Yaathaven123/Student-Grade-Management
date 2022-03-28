#Part 1 - Student Version

credit_pass = int(input("Please enter your credits at pass :")) #prompt user to input pass marks
credit_deffer = int(input("Please enter your credit at defer :")) #prompt user to input deffer marks
credit_fail = int(input("Please enter your credits at fail :")) #prompt user to input fail marks
if credit_pass == 120 :
   p_outcome = ('Progress')
elif credit_pass == 100 :
   p_outcome = ('Progress (module trailer)')
elif credit_fail >= 80 :
   p_outcome = ('Exclude')
else :
   p_outcome = ('Do not progress - module retriever')
print(p_outcome,) #print the outcome
