def solve():
    acc = 0
    for i in range(1,1001):
        acc += numberWord(i)

    print(acc)
  
def numberWord(x):
    if      x < 20:
        return lessThanTwenty(x)
    elif    len(str(x)) == 2:
        return twoDigit(x)
    elif    len(str(x)) == 3:
        return threeDigit(x)
    else:
        return 11 #onethousand

def lessThanTwenty(x):
    if x < 10:  return ones(str(x))
    else:
        return tenToTwenty(str(x))

def twoDigit(x):
    digitSplit = list(str(x))

    if digitSplit[1] == '0':
        return tens(digitSplit[0])
    else:
        return tens(digitSplit[0]) + ones(digitSplit[1])
               
def threeDigit(x):
    digitSplit = list(str(x))

    if digitSplit[1] == '0' and digitSplit[2] == '0':
        return ones(digitSplit[0]) + 7
    elif int(digitSplit[1]) < 2:
        return ones(digitSplit[0]) + 7 + 3 + lessThanTwenty(int(digitSplit[1] + (digitSplit[2])))
    else:
        return ones(digitSplit[0]) + 7 + 3 + tens(digitSplit[1]) + ones(digitSplit[2])

def ones(x):
    if      x == '0': return 0
    elif    x == '1': return 3
    elif    x == '2': return 3
    elif    x == '3': return 5
    elif    x == '4': return 4
    elif    x == '5': return 4 
    elif    x == '6': return 3 
    elif    x == '7': return 5 
    elif    x == '8': return 5 
    else            : return 4 

def tenToTwenty(x):
    if      x == '10': return 3
    elif    x == '11': return 6 
    elif    x == '12': return 6 
    elif    x == '13': return 8 
    elif    x == '14': return 8 
    elif    x == '15': return 7 
    elif    x == '16': return 7 
    elif    x == '17': return 9 
    elif    x == '18': return 8  
    else             : return 8 

def tens(x):
    if        x == '2': return 6
    elif      x == '3': return 6
    elif      x == '4': return 5
    elif      x == '5': return 5
    elif      x == '6': return 5
    elif      x == '7': return 7
    elif      x == '8': return 6
    else              : return 6
     
solve()

#21124


