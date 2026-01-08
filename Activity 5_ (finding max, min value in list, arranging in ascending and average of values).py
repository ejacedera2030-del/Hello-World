scores = []
#creaion of list

amount = int(input("How many students have taken the test? "))
#the amount of test scores it accepts for the list

for i in range(0,amount):
    score = int(input(f"Enter your test score: "))
    #gathers test scores for the list
    
    scores.append(score)
    scores.sort()
    #adds input and sorts the list in ascending order then loops depending on "amount" input value

print("\n--------------------------------------") #roof for the list
print(scores) #displaying the organized list
print("--------------------------------------") #floor for the list
print(f"\n|The highest score in the test is: {max(scores)}.\n|The lowest is {min(scores)}.\n|And the average of all test scores is {sum(scores)/len(scores)}.")
#displays the HIGHEST score, LOWEST and the AVERAGE of ALL scores
#(new line for HIGHEST,LOWEST, and AVERAGE)