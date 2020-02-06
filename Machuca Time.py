currentTimeStr = input("What is the current time (in hours 0-23)?")


currentTimeInt = int(currentTimeStr)
if (currentTimeInt>23) or currentTimeInt<0:
    print ("Sorry invalid number")
else:
    print (currentTimeStr)

    waitTimeStr = input("How many hours do you want to wait?")

    waitTimeInt = int(waitTimeStr)


    finalTimeInt = ((currentTimeInt + waitTimeInt) % 24)
    print(finalTimeInt)
