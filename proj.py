
print("\n\nwelcome to  KBC")
questions=[["what is the capital of india","Indor","Mumbai","Delhi","Kolkata",3],
           ["how many colors are there in the rainbow","five","seven","nine","three",2],
           ["national bird of india is ","crow","owl","eagle","peacock",4],
           ["in which year india gain independent",1947,1948,1950,1857,1],
           ["what is the boiling point of water","100c","85c","120c","135c",1],
           ["what is currancy of united states","pound","euro","dollar","yen",3],
           ["the value of PI is ",3.142,3.231,3.421,2.142,1],
           ["chemical symbol of water is","H3o","H2o","CO2","CH3",2],
           ["the hardest natural substance on earth is","steel","gold","copper","diamond",4],
           ["who perposed the theory of relativity","j openhimer","thomas edison","elbert einstein","newton",3],
           ["in which year the titanic sink",1915,1912,1812,1919,2]
           
]  
level=(1000,3000,5000,10000,25000,50000,100000,500000,1000000,5000000,10000000) 
money=0
for i in range(0,  len(questions)):
    question=questions[i]

    print(f"\nqustionn for {level[i] } is" ) 
    print(f" {question[0]} ")

    print(f"1.{question[1]}         2.{question[2]}")
    print(f"3.{question[3]}         4.{question[4]}")

    try:
        reply = int(input("\nEnter 0 to quit or your option: "))
        if reply == 0:
            money = level[i - 1] if i > 0 else 0
            print("You chose to quit.")
            break
        elif reply == question[-1]:
            print(f"Correct answer! You have won Rs. {level[i]}.")
            money = level[i]
        else:
            print("Wrong answer!")
            if i >=8:
                money=level[7]
            elif i >=4:
                money=level[3]
            else:
                money=0
            
            break
    except ValueError:
      print("invalid input please enter number between 0-4")
      break              
print (f"the money is you going with home is {money}")
    


           
           
        