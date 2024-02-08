#--------------------------------------classes--------------------------------------
#1
class string_methods:
    def __init__(self):
        self.str = ""
    
    def getString(self):
        self.str = input()

    def printString(self):
        print(self.str.upper())

use = string_methods()
use.getString()
use.printString()

#2
class Shape:
    def area():
        print(0)

class Square(Shape):
    def __init__(self,length):
        self.length = length
    
    def area(self):
        print(self.length*self.length)

sh = Shape()
sq = Square(6)
print(sh.area()," ",sq.area())

#3
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        print(self.length*self.width)

rec = Rectangle(4,6)
rec.area()

#4
import math
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x, self.y)
    
    def move(self,x1,y1):
        self.x = x1
        self.y = y1
    
    def dist(self,x1,y1):
        print(math.sqrt((self.x-x1)**2+(self.y-y1)**2))

points = Point(4,5)
points.move(2,4)
points.dist(1,3)

#5
class bank_account():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,dep):
        self.deposit =+ dep
    
    def withdraw(self,withd):
        if self.withdraw > withd:
            self.withdraw=-withd
        else:
            print("Sizdin balans molsheri zhetpeidi")

bank = bank_account("Aibar", 1000)
bank.deposit(600)
bank.withdraw(1500)

#6
def prime_filter(number):
    if number == 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    else:
        return True

num = [15,12,2,13,23]

prime = list(filter(lambda x: prime_filter(x), num))
print(prime)


#--------------------------------------function1--------------------------------------
#1
def convert(grams):
    ounces = 28.3495231 * grams
    return ounces

grams = 10
print(convert(grams))

#2
def F_to_C(F):
    C = (5 / 9) * (F - 32)
    return C

Fahrenheit = 123
print(F_to_C(Fahrenheit))

#3
def solve(heads,legs):
    for chik in range(heads+1):
        rab = heads-chik
        if(2*chik+4*rab) == legs:
            return chik, rab

heads = 35
legs = 94

print(solve(heads,legs))

#4
def prime_filter(number):
    if number == 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    else:
        return True
    
numbers = "1 2 3 7 8 10 5"
numlist = map(int,numbers.split())
print(list(filter(prime_filter, numlist)))

#5
def string_permutation(str,str1 = ""):
    for i in range(len(str)):
        next = str[i]
        rem = str[:i]+str[i+1:]
        string_permutation(rem,str1+next)


str = input()
print(string_permutation(str))

#6
def reverse():
    str = input()
    str1 = str.split()
    str = " ".join(str1[::-1])
    return str

print(reverse())

#7
def check(arr):
    for i in range(len(arr)):
        if arr[i] == arr[i+1] and arr[i] == 3:
            return True
    return False

arr = [2,4,3,2,3,3,1]
print(check(arr))

#8
def spy_game(nums):
    for i in range(len(nums)):
        if arr[i] == 0 and arr[i+1] == 0 and arr[i+2] == 7:
            return True
    return False

nums = [1,6,4,7,6,3,0,0,7,3]
print(spy_game(nums))

#9
def sphere(r):
    v = 4/3 * 3.14 * r**3
    return v

r = 9
print(sphere(r))

#10
def unique(arr, arr1):
    for i in arr:
        if i not in arr1:
            arr1.append(i)

arr = [1, 2, 6, 4, 8, 2, 7, 4, 8, 4, 5]
arr1 = []
unique(arr, arr1)
print(arr1)

#11
def polyndrom(str):
    if str == str[::-1]:
        return("palyndrom")
str = input()
print(polyndrom(str))

#12
def histogram(num):
    for i in num:
        print(i*"*")

histogram([4,9,7])

#13
import random
def num_guess(num,q = 0,n = False):
    while n == False:
        q+=1
        g = int(input("Take a guess:"))
        if g == num:
            print("Good job, KBTU! You guessed my number in ",q," guesses!")
            n = True
        elif g < num:
            print("Your guess is too low.")
        elif g > num:
            print("Your guess is too much.")


num = random.randint(1,20)
name = input("Hello! What is your name?:")
print("Well, KBTU, I am thinking of a number between 1 and 20.")
num_guess(num)

#--------------------------------------function2--------------------------------------

# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
def single_movie(a,movies):
    return movies[a]["imdb"] > 5.5

a = random.randint(0,14)
print(single_movie(a,movies))

#2
def movies_sublist(movies):
    good_movies = []
    for i in movies:
        if i["imdb"] > 5.5:
            good_movies.append(i)
    return good_movies

print(movies_sublist(movies))

#3
def movies_categories(movies,categories):
    movie_cat = []
    for i in movies:
        if i["category"] == categories:
            movie_cat.append(i)
    return movie_cat

categories = "Suspense"
print(movies_categories(movies,categories))

#4
def avarage_rating(movies,a,b,s=0):
    for i in range(len(movies)):
        if a <= i < b:
            s+=movies[i]["imdb"]
    return s/(b-a)

a = random.randint(0,14)
b = random.randint(a,14)
print(avarage_rating(movies,a,b))

#5
def avarage_rating_categori(movies,cat,s=0,s1=0):
    for i in movies:
        if i["category"] == cat:
            s+=i["imdb"]
            s1+=1
    return s/s1

a = random.randint(0,14)
cat = movies[a]["category"]
print(avarage_rating_categori(movies,cat))