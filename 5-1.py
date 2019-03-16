#Example 1 || Equality
cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title)
#example 2 || Inequality
requested topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")
# Example 3 || Numerical Comparisons
age = 18
age == 18

answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again")

age_0 = 22 
age_1 = 18
age_0 >= 21 and age_1 >= 21
age_1 = 22
(age_0 >= 21) and (age_1 >= 21)
#Checking List Values
requested_toppings = ['mushrooms','onions','pineapple']
'mushrooms' in requested_toppings
'pepperoni' in requested_toppings

#Conditional Tests
#1
guitar = 'fender'
print("does car == 'fender'? I predict True")
print(guitar == 'fender')

print("\nDoes car == 'yamaha'? I predict False.")
print(guitar == 'yamaha')
#2
car = 'honda'
print(car == 'honda')
print(car == 'toyota')
#3
ISP = 'spectrum'
print(ISP == 'spectrum')
print(ISP == 'verizon')
#4
Speakers = 'bose'
print(Speakers == 'bose')
print(Speakers == 'audio-technica')
#5
tv_Monitors = 'samsung'
print(tv_Monitors == 'samsung')
print(tv_Monitors == 'sony')
