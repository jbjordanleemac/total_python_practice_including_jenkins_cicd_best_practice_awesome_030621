#!/usr/bin/python

print('Morning, Jordan !!!')

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


