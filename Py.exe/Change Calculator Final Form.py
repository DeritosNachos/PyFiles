import time
print('''
            This is a correct change calculator, 
            it will ask for the price of an item and the amount paid by the customer. 
            
            The program will then render the exact change to be returned
            Enter values in this format: 00.00 without a dollar sign
''')         
def final():
    replay = input('Would you like to run this again? yes or no: ').lower()
    if replay == 'yes':
        calc()
    elif replay == 'no' or replay == 'No':
        print("Thanks for playing!")
    else:
        print("I don't understand that...")
        time.sleep(2)
        final()   

def calc():
    
#there is a problem with floats not giving proper values so program had to be written in terms of integers
    price = input('Enter the price of an item: ')
    pay = input('How much did the customer give you? ')
    pricecal = float(price) * (10**2)
    paycal = float(pay) * (10**2)
    dif = int(paycal) - int(pricecal)
    diff = int(dif)
    #print(diff)
    count_dollars = 0
    count_quartz = 0
    count_dimes = 0
    count_nicks = 0
    count_pens = 0
    while diff > 0:
        if diff >= 100:
            diff -= 100
            count_dollars += 1
        elif diff >= 25:
            diff -= 25
            count_quartz += 1
        elif diff >= 10:
            diff -= 10
            count_dimes += 1
        elif diff >= 5:
            diff -= 5
            count_nicks += 1
        else:
            diff -= 1
            count_pens += 1

    #print(diff)
    print('Your change is:')
    print(f'                         {str(count_dollars)} dollars')
    print(f'                         {str(count_quartz)} quarters')
    print(f'                         {str(count_dimes)} dimes')
    print(f'                         {str(count_nicks)} nickels')
    print(f'                         {str(count_pens)} pennies')
    final()    

    
calc()
        

