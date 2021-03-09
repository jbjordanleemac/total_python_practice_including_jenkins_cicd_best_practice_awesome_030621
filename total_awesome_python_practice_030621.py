#!/usr/bin/python

print('Morning, Jordan !!!')

import mymodule_030621
import json
from optparse import OptionParser

parser=OptionParser()
parser.add_option("-f", "--file", action="store", type="string", dest="file", help="<file>")

(options, args)=parser.parse_args()

if options.file == None:
  print("Please use --help for options")
  sys.exit(1)
else:
  x=open("item","ro")
  print(x.read())
  

class weekend():
  extra_day_off="yes extra day off"
  relax_little_bit="yes relax little bit"

  def __init__(self, whatday, dowhat):
    self.whatday=whatday
    self.dowhat=dowhat

  def location(self, where):
    print('During weekend like in ' + self.whatday + ' activity like ' + self.dowhat + ' at ' + where + ' which will be unique')

w1=weekend('Sat', 'Outage')
print(w1.dowhat)  

w1.location('Home')

class weekend2(weekend):
  pass

w2=weekend2('Sun', 'Hiking')
w2.location('Lake Chabot')

# dict

thisdict={
  "Mon": "One",
  "Tue": "Two",
  "Wed": "Three"
}

print("print out dict json string next")
print(json.dumps(thisdict))

print("length of this dict is " + str(len(thisdict)))

if "Wed" in thisdict:
  print("Wed is in thisdict")
else:
  print("Wed is NOT in in thisdict")

for a in thisdict:
  print(a)

for b in thisdict:
  print(thisdict[b])

for c in thisdict.keys():
  print(c)

for d in thisdict.values():
  print(d)

for e,f in thisdict.items():
  print(e,f)

print(thisdict)

# add key value in dict

thisdict["Thurs"]="Four"
print(thisdict)

# modify key value in dict

thisdict["Thurs"]="Fourr"
print(thisdict)

# how to invert dict

invert={}

for g in thisdict:
  invert[thisdict[g]]=g

print(invert)

# list

thatlist=["one", "two", "three"]

for h in thatlist:
  print(h)

# how to append two list together

i=["A", "B", "C"]
j=["D", "E", "F"]

for k in j:
  i.append(k)

print(i)

# how to get rid of duplicate items in list

l=[1, 2, 4, 2, 3, 6, 7, 2]
m=[]

for n in l:
  if n not in m:
    m.append(n)

print(m)

# if else

today="Sat"

if today == "Sat":
  print("Today is Sat")
else:
  print("Today is NOT Sat")

# try except

City="Dublin"

try:
  print(Cityy)
except:
  print("Cityy is NOT defined")

# while 

grade=7
print("You are attending grade " + str(grade) + " now ")

while grade <= 12:
  print("You will be attending grade " + str(grade) + " Next ")
  grade+=1

print("Congrats, You have just about to go college next ")

# split method

p="Hello Jordan"
print(p.split())

# strip method 

q="  Hello Tom "
print(q)
print(q.strip())


# function

def hello(weather):
  print("It is a hot day today with " + weather + " temparature")
 
hello("Warm")

# running method inside module

mymodule_030621.greeting("Warren")

# play with json

r='{"mon":"one", "tue":"two", "wed":"three"}'
s=json.loads(r)
print(s["mon"])

# get rid of duplicated items in array

t=[3, 4, 2, 4, 5, 2, 1]
u=[]

print("before " + str(t))

for v in t:
  if v not in u:  
    u.append(v)

print("after get rid of duplicate items becomes: " + str(u))
 
# open function and read method

w=open("item", "ro")
print(w.read())

# format 1

print("your name is {fname} and your age is {age}".format(fname="Frank Hole", age=21))

# format 2

carbrand="Toyota"

print("your car model is %s" % carbrand)
