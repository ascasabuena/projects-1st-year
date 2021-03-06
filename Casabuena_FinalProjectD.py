

"""
Created on Tue Apr 23 17:48:48 2019

@author: Aliah Casabuena

Title: Moodly: Daily Mood Tracker
"""



class Array(object):
    #instantiating array object
    def __init__(self, capacity, fillValue = None):
        self.items = list()
        for count in range(capacity):
            self.items.append(fillValue)
    def __len__(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)
    def __iter__(self):
        return iter(self.items)
    def __getitem__(self,index):
        return self.items[index]
    def __setitem__(self,index,newValue):
        self.items[index] = newValue
        
class Grid(object):
    #instantiating grid object
    def __init__(self,rows,cols, fillValue = None):
        self.data = Array(rows)
        for count in range(rows):
            self.data[count] = Array(cols, fillValue)
    def getRow(self):
        return len(self.data)
    def getCol(self):
        return len(self.data[0])
    def __getitem__(self,index):
        return self.data[index]
    def __setitem__(self,index1,index2,newValue):
        self.data[index1][index2] = newValue
    def stop(self):
        return 0
    def __str__(self):
        result = ""
        for row in range(self.getRow()):
            for col in range(self.getCol()):
                result += str(self.data[row][col]) + "\t"  
            result += "\n"
        return result
    
#creating tables    
table = Grid(32,13,"X")

#print the numbering of days for each month
for row in range (table.getRow()):
    for col in range(table.getCol()):
        table[row][col] = " "
        table[0][0] = 1 
        table[1][0] = 2
        table[2][0] = 3
        table[3][0] = 4
        table[4][0] = 5
        table[5][0] = 6
        table[6][0] = 7
        table[7][0] = 8
        table[8][0] = 9
        table[9][0] = 10        
        table[10][0] = 11
        table[11][0] = 12
        table[12][0] = 13
        table[13][0] = 14 
        table[14][0] = 15
        table[15][0] = 16
        table[16][0] = 17
        table[17][0] = 18
        table[18][0] = 19
        table[19][0] = 20
        table[20][0] = 21
        table[21][0] = 22
        table[22][0] = 23
        table[23][0] = 24
        table[24][0] = 25
        table[25][0] = 26
        table[26][0] = 27 
        table[27][0] = 28
        table[28][0] = 29
        table[29][0] = 30
        table[30][0] = 31

def monthlyEvaluation(values):
    
    import random #for random picking of advice in a list
    #each rating from the user will be sort as a list, 
    #then each list will be compared for evaluation when this function is called.
    #this function is called every last day of the month for evaluation
    rate_one = []
    rate_two = []
    rate_three = []
    rate_four = []
    rate_five = [] 
    
    
#sorting and appending of the collected ratings from the user 
# where rate = user input per day
    for rate in values:
        if rate == 1:
            rate_one.append(rate)
        elif rate == 2:
            rate_two.append(rate)
        elif rate == 3:
            rate_three.append(rate)
        elif rate == 4:
            rate_four.append(rate)
        elif rate == 5:
            rate_five.append(rate)
            
            
#getting the lenght of the a certain rating to see how frequent it was answered by the user.
    overall_element = len(values)
    element1= len(rate_one)
    element2 = len(rate_two)
    element3 = len(rate_three)
    element4 = len(rate_four)
    element5 = len(rate_five)
    
    
#converting the frequency into percentage, "overall_element" as the total(100%) number of inputs
    percentage = [((element1/overall_element)*100), ((element2/overall_element)*100), ((element3/overall_element)*100), ((element4/overall_element)*100), ((element5/overall_element)*100)]
    percent_sum = sum(percentage)

#output showing the percentage for each rating, rounded off to tens 
    print("Bad: ", "\t", round(percentage[0]),"%")
    print("Sad: ", "\t", round(percentage[1]),"%")
    print("Meh: ", "\t", round(percentage[2]),"%")
    print("Good: ", "\t", round(percentage[3]),"%")
    print("Happy: ", round(percentage[4]),"%")
    print("TOTAL: ", round(percent_sum),"%")

#List of advices according to feelings. 
#--*this part can be easily modified by deleting or adding more helpful advices for the user. 
    advice_sad = [" Knowing your emotions helps you understand and accept yourself. If you feel sad, notice it.",
                  "Remind yourself that sadness will pass and you'll feel better.", 
                  "When things don't go your way, don't give up! Stay in the game. There's always next time.",
                  "Even if you're sad, think of one or two good things about yourself or your situation. Believe in yourself.",
                  "The people in your life who believe in you and care can comfort you when you feel sad.",
                  "Shake off a sad mood by doing things that put you in a more positive mood. Play a game or sport.",]
    advice_happy = [" Stay true to yourself.", 
                    "To stay happy,  Do what you love not what you're told to love.", 
                    "To stay happy, Create the environment that's right for you.",
                    "To stay happy, Choose your friends wisely.", 
                    "To stay happy, Develop positive habits.", 
                    "To stay happy, Create certainty and leave room for uncertainty.", 
                    "To stay happy, Be vulnerable."]
    advice_normal = ["Try to spend time with people who love you to elevate your emotions.", 
                     "Make a new friend or new relationship for a new kind of feeling. ", 
                     "You can adopt a pet, they will help you feel something.",
                     "Be more kind to others, this will help you to feel more fulfilled.", 
                     "Talk to a trusted friend about your feeling.", 
                     "Continue tracking your mood.",
                     "You can try meditation to explore your feelings.", 
                     "Find a meaning in your everyday life.", "Do something new to you.", ]

    
#Comparing each mood, majority of the answer will be considered as the emotion or mood for the whole month. 
    negative_feeling = percentage[0] + percentage[1] 
    neutral_feeling = percentage[2]
    happy_feeling = percentage[3] + percentage[4]

#Display of bar graph for each month 
    import matplotlib.pyplot as graph
    
    names = ['Negative', 'Neutral', 'Positive']
    values = [negative_feeling, neutral_feeling, happy_feeling]

    graph.figure(figsize=(6, 3),facecolor= 'w')

    graph.subplot()
    graph.bar(names, values,color='mcy')

    graph.suptitle('Classification of Moods')
    graph.show()
#Output or printing of advice. Advice were chosen randomly from the list of Advices according to feelings
    if negative_feeling > (neutral_feeling + happy_feeling):
        print("\n","Majority of your mood was observed to be negative...",random.choice(advice_sad))
    

    elif happy_feeling > (neutral_feeling + negative_feeling):
        print("\n","It is observed that majority of your mood was positive this month...",random.choice(advice_happy))

    elif neutral_feeling > (happy_feeling + negative_feeling) : 
        print("\n","Seems that you don't have enough significant feelings/moods this month...",random.choice(advice_normal))
    else:
        #if there is not enough data to be compared this advice will be printed.
        
        print("\nGetting a consistent check on your mood can help you find what's wrong.") 
        print( "Please input your Mood for the following days and stay healthy ^_^ ")
    print("\n")



def main():
    import datetime #for getting the current date (computer system based)
    values = []
    
    for col in range(1,13):
        for row in range(0,32):
            #Printing of everyday date. 
            d = datetime.datetime.today()
            if col == 1 and row <= 30:
                print("January", row+1, d.year)
            elif col == 2 and row <= 27:
                print("February", row+1,d.year)
            elif col == 3 and row <= 30:
                print("March", row+1,d.year)
            elif col == 4 and row <= 29:
                print("April", row+1,d.year)
            elif col == 5 and row <= 30:
                print("May", row+1,d.year)
            elif col == 6 and row <= 29:
                print("June", row+1,d.year)
            elif col == 7 and row <= 30:
                print("July", row+1,d.year)
            elif col == 8 and row <= 30:
                print("August", row+1,d.year)
            elif col == 9 and row <= 29:
                print("September", row+1,d.year)
            elif col == 10 and row <= 30:
                print("Octoer", row+1,d.year)
            elif col == 11 and row <= 29:
                print("November", row+1,d.year)
            elif col == 12 and row <= 30:
                print("December", row+1,d.year)
            else:
                print("  ")
            
            
                   
            #calling the monthlyEvaluation() function to evaluate inputs when it reach the last day of the month
            #JANUARY
            if col == 1 and row == 31:
                month1 = values[0:32]
                print("MONTHLY REPORT OF MOOD")
                print("\nFOR THE MONTH OF JANUARY YOU FEEL: ")
                monthlyEvaluation(month1)
            #FEBRUARY
            elif col == 2 and row == 28:
                month2 = values[31:60]
                print("MONTHLY REPORT OF MOOD")
                print("\nFOR THE MONTH OF FEBRUARY YOU FEEL: ")
                monthlyEvaluation(month2)
            #MARCH
            elif col == 3 and row == 31:
                month3 = values[59:91]
                print("MONTHLY REPORT OF MOOD")
                print("\nFOR THE MONTH OF MARCH YOU FEEL: ")
                monthlyEvaluation(month3)
            #APRIL
            elif col == 4 and row == 30:
                month4 = values[90:121]
                print("MONTHLY REPORT OF MOOD")
                print("\nFOR THE MONTH OF APRIL YOU FEEL: ")
                monthlyEvaluation(month4)
            #MAY
            elif col == 5 and row == 31:
                month5 = values[120:152]
                print("MONTHLY REPORT OF MOOD")
                print("\nFOR THE MONTH OF MAY YOU FEEL: ")
                monthlyEvaluation(month5)
            #JUNE
            elif col == 6 and row == 30:
                month6 = values[151:182]
                print("MONTHLY REPORT OF MOOD")
                print("\nFOR THE MONTH OF JUNE YOU FEEL: ")
                monthlyEvaluation(month6)
            #JULY
            elif col == 7 and row == 31:
                month7 = values[181:213]
                print("MONTHLY REPORT OF MOOD")
                print("\nFOR THE MONTH OF JULY YOU FEEL: ")
                monthlyEvaluation(month7)
            #AUGUST
            elif col == 8 and row == 31:
                month8 = values[212:244]
                print("MONTHLY REPORT OF MOOD")
                print("\nFOR THE MONTH OF AUGUST YOU FEEL: ")
                monthlyEvaluation(month8)
            #SEPTEMBER
            elif col == 9 and row == 30:
                month9 = values[243:274]
                print("MONTHLY REPORT OF MOOD")
                print("\nFOR THE MONTH OF SEPTEMBER YOU FEEL: ")
                monthlyEvaluation(month9)
            #OCTOBER
            elif col == 10 and row == 31:
                month10 = values[273:305]
                print("MONTHLY REPORT OF MOOD")
                print("\nFOR THE MONTH OF OCTOBER YOU FEEL: ")
                monthlyEvaluation(month10)
            #NOVEMBER
            elif col == 11 and row == 30:
                month11 = values[304:335]
                print("MONTHLY REPORT OF MOOD")
                print("\nFOR THE MONTH OF NOVEMBER YOU FEEL: ")
                monthlyEvaluation(month11)
            #DECEMBER
            elif col == 12 and row == 31:
                month12 = values[344:366]
                print("MONTHLY REPORT OF MOOD")
                print("\nFOR THE MONTH OF DECEMBER YOU FEEL: ")
                monthlyEvaluation(month12)
                
            #YEAR END REPORT. calling of evaluation function when it reach the end of the year
                print("A YEAR REPORT OF YOUR MOOD")
                print("\nFOR THE WHOLE YEAR YOU FEEL: ")
                monthlyEvaluation(values)
                print ("END OF THE YEAR!!!!, MAY YOU MAKE CHANGES FOR THE BETTER ^_^")
            
            #modifying exceptions of days according to months
            elif col == 2 and row > 28:
                table.__setitem__(row,col,"-")
                
            elif (col == 4 or col == 6 or col == 9 or col == 11) and row > 30:
                 table.__setitem__(row,col,"-")                            
           
            else:
            #if the day is not the current date, it will autoamically input "X" 
            #which means that the user were not able to have a monitoring for that day
                d = datetime.datetime.today()
                if col < int(d.month):
                    x = "X"                    
                    
                else:
            ##if day is the current day the program will allow the user to input mood for start of monitoring
                    if col == int(d.month) and row < (int(d.day)-1):
                        x = "X"
                    else:
                        print("Rate how you feel today")
                        print("1 - I'm worst","\n2 - I'm sad","\n3 - I'm not sure, I don't feel any","\n4 - It's a nice day!","\n5 - Today was exceptionally happy!")
                        x = input("How are you Today? ")
                        
            ##check if the string is numeric.   
                if x.isnumeric():
                    x = int(x) 
                    if x > 0 and x <= 5:
            #if it is. Input will be append to the list.
                        values.append(x)
                        table.__setitem__(row,col,x)
                        print ("Day","\tJan","\tFeb","\tMar","\tApr","\tMay","\tJun","\tJul","\tAug","\tSep","\tOct","\tNov","\tDec")
                        print(table)
                    else: 
            #if not in range 1-5. It will be append to the list but will show "X" or error. 
                        print("Error: Acceptable input is 1 to 5")
                        values.append(x)
                        table.__setitem__(row,col,"X")
                        print ("Day","\tJan","\tFeb","\tMar","\tApr","\tMay","\tJun","\tJul","\tAug","\tSep","\tOct","\tNov","\tDec")
                        print(table)
                        continue
            #if not numeric, it will show "X" or error then append 0 to the list. 
                else:
                    print("Error: No input for the day / Input is not numeric")
                    x = 0
                    values.append(x)
                    table.__setitem__(row,col,"X")
                    print ("Day","\tJan","\tFeb","\tMar","\tApr","\tMay","\tJun","\tJul","\tAug","\tSep","\tOct","\tNov","\tDec")
                    print(table)
                    continue

print("\tMoodLY: Daily Mood Tracker")
print("\nMoodLy is a mood tracker that encourages you to have a reflective notes without writting anything.")
print("The app works by rating your daily mood and evaluating this moods for you.")
print("\tTake care of your mental health becasue it matters. ")
print("\nStart the program? ")
start = input("Yes/No:___ :" )

while start != "no":
    if start == "yes":
        main()
        break;
    else:
        print("error")
        start = input("Yes/No:___ :" )
else:
    print("\nGetting a consistent check on your mood can help you find what's wrong.")
    print("End of program")
        