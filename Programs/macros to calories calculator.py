'''
Calculate calories in food by macros
Created by Robert Davis on 7 Feb 2018
Last update on 7 Feb 2018
'''

# declare macros, fiber, and servings
fat = int(input('Enter grams of fat:  '))
protein = int(input('Enter grams of protein:  '))
carbs = int(input('Enter grams of carbs:  '))
#fiber = int(input('Enter grams of fiber:  '))
servings = int(input('Enter number of servings:  '))

# calculate calories / gram of macros
calfat = fat * 9
calpro = protein * 4
calcho = carbs * 4

# calculate kcal subtracting fiber from carbs
caltotal = (calpro + calfat + calcho) * servings
#caltotal = (calpro + calfat + (calcho - fiber)) * servings

print('Total calories = %s'% caltotal)