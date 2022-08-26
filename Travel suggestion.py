#Travelling A to B
time=int(input("Enter the time duration "))
price=int(input("Please enter the desired fare "))
longTime=6
if time>=6:
    highPrice=600
    if price>=600:
        print("Take Train")
    elif price>=300:
        print("Take coach")
    else:
        print("No transport available for the given price\nMinimum Price for this destination is 300 for long journey")

elif time>=1.5:
    highPrice=5000
    if price>=5000:
        print("Take Daytime flight")
    elif price>=2500:
        print("Take Red eye flight")
    else:
         print("No transport available for the given price\nMinimum Price for this destination is 2500 for short journey")

else:
    print("Please enter valid time choice/n Minimum time for this journey is 1 and half hour")