
def birthdayCakeCandles(ar):
    first = True
    maxHeight = 0
    nrOfCandles = 0
    for candleHeight in ar:
        if first:
            maxHeight = candleHeight
            nrOfCandles = 1
            first = False
            continue
        elif candleHeight>maxHeight:
            maxHeight = candleHeight
            nrOfCandles = 1
        elif candleHeight == maxHeight:
            nrOfCandles += 1
    return nrOfCandles

print(birthdayCakeCandles([3,2,1,3]))