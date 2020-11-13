# this program does a temperature conversion

def main():
    #get temperature in centigrade
    temp=float(input('Enter the temperature in centigrade: '))

    #get temp. in Farenheit
    temp_far=fahrenheit(temp)

    #display result
    print('The temperature in Fahrenheit is: ',temp_far)
# end of main function

def fahrenheit(temp):
    #convert centigrade to fahrenheit
    #using standard formula
    result = temp*1.8 +32
    return result
# end of fahrenheit function

# call main function
main()


