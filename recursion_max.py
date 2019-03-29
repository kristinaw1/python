#
#Kristina Woods
#COP4533 Algorithmic Design and Development
#
#Assigment 2 c recursion max


#recursion
def maxValue(nList):
    #check if len is 1, return first postion in list
    if len(nList) == 1:
        return nList[0]
    else:
    #run recursion to get max value
        max = maxValue( nList[1:])
        return max if max > nList[0] else nList[0]

def main():
    #list1
    nList =[19,12,18,10,12]
    #list2
    n2List = [88,200,21,38,198,123,89]
    #return highest value
    print("The highest value of the first list is: ", maxValue(nList))
    print("The highest value of the second list is: ", maxValue(n2List))
    

main()
#main function called
