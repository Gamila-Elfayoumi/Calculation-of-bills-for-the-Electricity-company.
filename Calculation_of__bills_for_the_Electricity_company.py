def Residential (kilowatt):
    print( "The cost of the electricity used = ",kilowatt * 10.5,"$")
def commercial (kilowatt):
    if kilowatt<= 2000 :
         print ("The cost of the electricity used = ", "1000$")
    else :
        print ("The cost of the electicity used = ", 1000 + (0.005*kilowatt),"$")
def industrial (kilowatt):
    if kilowatt< 4000:
        print ("The cost of the electicity used = ","1000$")
    elif kilowatt>4000 and kilowatt<10000:
        print ("The cost of the electicity used = ","2000$")
    elif kilowatt>10000:
        print ("The cost of the electicity used = ","3000$")

customor = (input ("Enter the type of R if you are Residential and C if you are Commercial and I if you are Industrial : "))
kilowatt = int (input ("Enter the kilowatt used : "))
if customor =='R':
    Residential (kilowatt)
elif customor == 'c':
    commercial (kilowatt)
else:
    industrial (kilowatt)


