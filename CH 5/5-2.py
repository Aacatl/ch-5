#equality and inequality 
cleats = 'Nike'

cleats_wanted = 'adidas'

if cleats_wanted != 'nike':
    print('No, thank you.')

if cleats_wanted == 'adidas':
    print('Drool')

#Test using the lower() function

cleat_brand = 'Adidas'
cleat_brand.lower() == 'adidas' # lower funtion is used to return a COPY of the string in lowercase

#numerical tests involving equality, inequality, greater than and less than, greater than equal to and less than equal to 
#equality
my_dogs_age = 8
my_dogs_age == 18
#inequality
answer = 100

if answer != 40:
    print("That is not the correct answer, MMMMkay")
#greater than and less than

score_1 = 20
score_2 = 40

score_1 > 20
score_2 < 41

#and and or key words

score_1 = 20
score_2 = 40

score_1 > 19 and score_2 < 39
score_1 > 19 or score_2 < 39

#greater than and equal to and less than equal to

score_3 = 200
score_4 = 100

score_3 >= 500
score_4 <= 100

#Test wether an items in a list, or not in a list
cleat_companies = ['Adidas','Nike', 'Puma', 'Mizuno', 'Umbro']
'Adidas' in cleat_companies
'Kush' in cleat_companies




