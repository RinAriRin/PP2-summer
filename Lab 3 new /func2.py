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

#ex 1 
def imdb(movies):
    if (movies[n]['imdb'] >= 5.5):
        return True
    else:
        return False
    
n = int(input())

if imdb(movies):
    print ("True")
else:
    print ("False")

#ex 2 
def score(imdb):
    if(imdb > 5.5 ):
        return True
    else:
        return False
 
list1 = []
for i in range(len(movies)):
    if score(movies[i]['imdb']):
        list1.append(movies[i])
for i in list1:
        print(i)

#ex 3 
  def category(movies, m):
    for i in range(len(movies)):
        if movies[i]['category'] == m:
            print (movies[i])
    
m = input()
category(movies, m)

#ex 4
def avg(movies):
    a = 0
    for i in range(len(movies)):
        a += movies[i]['imdb']
    a = a/len(movies)
    print (a)
avg(movies)

#ex 5 
def ctg_and_avg(movies, m):
    cnt = 0
    cnt1 = 0
    for i in range(len(movies)):
        if movies[i]['category'] == m:
           cnt+=1
           cnt1+=movies[i]['imdb']
    print (cnt1/cnt)

ctg_and_avg(movies, m)