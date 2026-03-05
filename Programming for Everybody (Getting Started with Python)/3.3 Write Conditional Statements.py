'''
3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.
'''
score = input("Enter Score: ")
s = float(score)
if s >= 0.9 and s <= 1.0:
    print('A')
elif s >= 0.8:
    print('B')
elif s >= 0.7:
    print('C')
elif s >= 0.6:
    print('D')
elif s < 0.6 and s >=0 :
    print('F')
else:
    print('Error')