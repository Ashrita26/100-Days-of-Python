#Tip Generator
bill=float(input("Enter the Total Bill! ="))
tip=float(input("Enter the percentage of bill you want to give? (Like 1...2...4..5..10..) ="))
ppl=int(input("Enter how many people to split the bill?"))
tip_per=bill*tip/100
each_one=(bill+tip_per)/ppl
print("Each person must pay:",round(each_one,2))