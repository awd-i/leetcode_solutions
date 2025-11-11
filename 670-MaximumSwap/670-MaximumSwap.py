# Last updated: 11/11/2025, 1:56:00 AM
class Solution:
    def maximumSwap(self, num: int) -> int:

        # first, see if there is an index where some smaller value is more than a current value. Check is numList[i] < numList[i+1]
        numList = list(str(num))
        # Find index where numList[i] < numList[i+1] meaning chance to flip
        for i in range(len(numList)-1):
            if numList[i] < numList[i+1]:
                break
        # if nothing found return num
        else:
            return num
        # find the max value index from where you left off at i+1 and save the value
        maxIdx = i+1
        maxVal = numList[i+1]
        for j in range(i+1, len(numList)):
            if maxVal <= numList[j]:
                maxIdx = j
                maxVal = numList[j]
        # Going right from i now, find the left most value that is less than maxVal. Essentially, find the closest one to the front where its value is lower than maxVal.
        leftIdx = i
        for j in range(i, -1, -1):
            if numList[j] < maxVal:
                leftIdx = j
        
        #swap maximum i and j
        temp = numList[maxIdx]
        numList[maxIdx] = numList[leftIdx]
        numList[leftIdx] = temp

        #return numList
        return int(''.join(numList))


        
            

