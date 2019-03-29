#
#Kristina Woods
#COP4533 Algorithmic Design and Development
#
#Assigment 2 a html checker



#Stack Class
class Stack:
#define stack functions
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


#Function to check if tagLists are balanced
def testTagsBalance(htmlStr):
    #build stack
    stack = Stack()
    htmlLen = len(htmlStr)
    #set count
    i = 0
    #find < in file
    while i < htmlLen:
        tagList = []
        openTag = True
        if htmlStr[i] == '<':
            # add < to tagList
            tagList.append('<')
            # increase count
            i += 1
            #check for end tagLists /
            if htmlStr[i] == '/':
                openTag = False
                i += 1
            #move through spaces in string or where not = >
            while (i < htmlLen) and htmlStr[i] == ' ' or (i < htmlLen) and htmlStr[i] != '>':
                i += 1
            #move through other characters and add them to htmlString if numeric or alphabetic 
            while (i < htmlLen) and (htmlStr[i].isdigit() or htmlStr[i].isalpha()):
                tagList.append(htmlStr[i])
                i += 1
                #add to length count if htmlStr not >
            if (i >= htmlLen):
                return False
            #add the > to tagList
            tagList.append(htmlStr[i])
            htmTag = ''.join(tagList)
            #Check if openTag is true. 
            if openTag:
                #Add to stack if true
                stack.push(htmTag)
            elif stack.is_empty():
                #return false is empty
                return False
            else:
                #Remove from stack if false
                topTag = stack.pop()
                if topTag != htmTag:
                    return False
        i += 1
        #if stack is not empty tagLists don't balance
    if not stack.is_empty():
        return False
    #else return true
    return True




def match_endings(text):

    # split the text
    words = text.split()
    #find find end tagLists
    findends = [s for s in words if "</" in s]
    endtagLists= [s.replace('</', '') for s in findends]
    #find beginning tabs
    findbegin = [s for s in words if "<" in s and not "</" in s]
    begintagLists = [s.replace('<', '') for s in findbegin]
    #sort tagLists
    endtagLists.sort()
    begintagLists.sort()
    #check if tagList types match
    if endtagLists == begintagLists:
        return True
    else:
        return False
    
        
#main function
def main():
    #prompt user for file location.
    htmlPath = input("Please enter the file path for your html page :")
    with open(htmlPath, 'r') as myfile:
        #clean data to make it readable
        data=myfile.read().replace('\n', ' ')
        data =data.replace('<', ' <')
        data =data.replace('>', '> ')
        #Call and return results of both functions
        isMatch =match_endings(data)
        isValid = testTagsBalance(data)
        #Return if tagLists are valid or not
        if isValid and isMatch:
            print("Valid HTML")
        else:
            print("Invalid HTML, mismatched opening and closing braces")
#call main function
main()

#main function

        
def benchmark_function():
    with open('html.txt', 'r') as myfile:
        #clean data to make it readable
        data=myfile.read().replace('\n', ' ')
        data =data.replace('<', ' <')
        data2 =data.replace('>', '> ')
   
        isMatch =match_endings(data2)
        isValid = testTagsBalance(data2)
        #Return if tagLists are valid or not
        if isValid and isMatch:
            print("Valid HTML")
        else:
            print("Invalid HTML, mismatched opening and closing braces")






