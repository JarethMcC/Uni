# Import functions from the circle.py file in the same folder
from circle import area
from circle import circumference

# The stillRunning function allows the user to continue to check for new numbers
# without having to restart the program
def stillRunning():
    yOrN = input('if you would like to calculate another number type y, if not press enter: ')
    if yOrN == 'y':
        print('1. Area')
        print('2. Circumference')
    else:
        print('Thank you for using the program!')
        exit()

# Initial text the user will see
print('Hello this program will allow you calculate the area or circumference of a circle')
print('Please select which you would like to calculate')
print('1. Area')
print('2. Circumference')
print('3. Exit')

# Setting the variable for the while loop to be True so that it runs
running = True

# This while loop will first ask which option the user would like to choose and then executes it
# The stillRunning function is called at the end of each option to see if the user would like to continue
while running == True:
    option = int(input(''))
    if option == 1:
        radiusA = int(input('Please enter the radius of the circle you would like to calculate the area of: '))
        print('%.2f' %  area(radiusA))
        stillRunning()
    elif option == 2:
        radiusC = int(input('Please enter the circumference of the circle to calculate the area of:'))
        print('%.2f' %  circumference(radiusC))
        stillRunning()
    elif option == 3:
        print('Thank you for using the program!')
        exit()
        


