score = 0

    
print("Q1:Why should we Choose LPU  '?")
print("1. To sleep\n2.To traumatize yourself \n3. To party\n4. To study")
answer = input("Your answer (1/2/3/4): ")
if answer == "4":
    score += 1
print("\n")
    
print("Q2: Who is the pro-Chancellor of LPU'?")
print("1. Madam Rashmi Mittal \n2. Harsh singh\n3. Kaluwaa\n4. Anubhav")
answer = input("Your answer (1/2/3/4): ")
if answer == "1":
    score += 1      
print("\n")  

print("Q3: How much attendence should we maintain'?")
print("1. Below 60\n2. Above 90\n3. Above 60\n4. 0")
answer = input("Your answer (1/2/3/4): ")
if answer == "2":
    score += 1      
print("\n")  

    

print(f"\nYour final score is: {score}/3")