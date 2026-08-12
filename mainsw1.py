# Seatwork 1 python
from pyscript import display, document
# all three below this comment are strings
name = 'Stephanie'
age = 'fifteen'
height= '162.56 cm'
# list
thislist = ['Hong Kong','Japan','Korea']
# bool
def student_type() :
    return False
if student_type: False
print ("a student in OB that has been here a few years, so safe to say I am not really new.")

# dict
thisdict = {
    "car_brand":"ford territory",
    "shoe_size": 8,
    "best_friend": "Angela",
}
# set
thisset = (['mangos','grapes','apples','bananas','pomegranates'])
#tuple
thistuple = ('monday','tuesday','wednesday','thursday','friday','saturday','sunday')

display(type(name), target='result1')
display(f' * Hello chat!! My name is {name}, and I just recently turned {age} years old! By this point, I have grown to be a solid height of {height}. Thinking back on my previous travels a few years from now, the countries I wanna go back to the most are most probably {thislist}, and, when it comes to eating healthy, my top favorite fruits are {thisset}!<br><br> * Here is a bit more random trivia about me as well: the brand of the red car my parents own is a {"car_brand"}, my shoe size (If I remember correctly TwT) is shoe size {"shoe_size"}, and a best friend I have that I can never forget any nice memories with, is a girl by the name of {"best_friend"}, who is in another school from me. Speaking of schools: I, of course, am a {student_type}. And the most basic of knowledge I know from the method of schooling are my days of the week, the days being {thistuple}.', target="result1")

document.getElementById('result1').innerHTML = f' * Hello chat!! My name is {name}, and I just recently turned {age} years old! By this point, I have grown to be a solid height of {height}. Thinking back on my previous travels a few years from now, the countries I wanna go back to the most are most probably {thislist}, and, when it comes to eating healthy, my top favorite fruits are {thisset}!<br><br> * Here is a bit more random trivia about me as well: the brand of the red car my parents own is a {"car_brand"}, my shoe size (If I remember correctly TwT) is shoe size {"shoe_size"}, and a best friend I have that I can never forget any nice memories with, is a girl by the name of {"best_friend"}, who is in another school from me. Speaking of schools: I, of course, am a {student_type}. And the most basic of knowledge I know from the method of schooling are my days of the week, the days being {thistuple}.'

