def main():
    time=input("What time is it? ")
    x=convert(time)
   
                
def convert(t):
    hours, minutes=(t.split(':'))
    hours=float(hours)
    minutes=float(minutes)/60
    result=hours+minutes
    if result >= 7 and result <=8 :
        print("breakfast time")
    if result >= 12 and result <=13 :
        print("lunch time")
    if result >= 18 and result <=19 :
        print("dinner time")
    else:
        print("")

main()
