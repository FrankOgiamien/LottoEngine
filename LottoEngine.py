# Generate a specified number of random lotto number sets from the provided list of suitable numbers
# A lotto selection
#   - should have a sum between 90 and 205                  reduces odds 24,752
#   - should have 1 to 5 even values                        reduces odds 134,596 and 177,100
#   - should not have more than 2 numbers in sequence. eg   10,11,12
import random

FromList = [4, 12, 14, 15, 17, 20, 22, 24, 25, 27, 28, 30, 31, 36, 39, 40, 44, 45, 48, 49]

SetsReq = 40
ListLen = len(FromList)
MyNumbers = "C:\\projects\\lotto\\my_numbers_" + str(ListLen) + "_" + str(SetsReq) + ".txt"

print FromList
print ""

i = 0
f = open(MyNumbers, "w")

while i <= SetsReq:
    random.seed()
    LottoSet = []
    SeqCount = 0
    while len(LottoSet) < 6:
        x = random.randrange(1, 49, 1)
        if x in FromList and x not in LottoSet:
            LottoSet.append(x)
    LottoSet.sort()
    SetSum = int(LottoSet[0]) + int(LottoSet[1]) + int(LottoSet[2]) + int(LottoSet[3]) + int(LottoSet[4]) + int(LottoSet[5])
    OddCount = (int(LottoSet[0]) % 2) + (int(LottoSet[1]) % 2) + (int(LottoSet[2]) % 2) + (int(LottoSet[3]) % 2) + (int(LottoSet[4]) % 2) + (int(LottoSet[5]) % 2) 

    sc = 5
    while sc > 0:
        if LottoSet[sc] - LottoSet[sc-1] == 1:
            SeqCount += 1
        sc -= 1

    print str(LottoSet) + "    (Sum: " + str(SetSum) + ", Odd: " + str(OddCount) + ", Seq:" + str(SeqCount) + ")"

    if SetSum > 95 and SetSum < 205 and OddCount > 0 and OddCount < 6 and SeqCount <= 3:
        f.write(str(LottoSet[0]) + ", " + str(LottoSet[1]) + ", " + str(LottoSet[2])+ ", " + str(LottoSet[3]) + ", " + str(LottoSet[4]) + ", " + str(LottoSet[5]) + "\n")
    i += 1
f.close()
