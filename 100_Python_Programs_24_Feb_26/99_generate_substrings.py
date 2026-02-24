# Program to generate all substrings

print("Enter a string:")  # message
s = input()  # take string

print("All substrings are:")

for i in range(len(s)):  # start index
    for j in range(i+1, len(s)+1):  # end index
        print(s[i:j])  # print substring
        #OUTPUT
        """
        Enter a string:
string character
All substrings are:
s
st
str
stri
strin
string
string
string c
string ch
string cha
string char
string chara
string charac
string charact
string characte
string character
t
tr
tri
trin
tring
tring
tring c
tring ch
tring cha
tring char
tring chara
tring charac
tring charact
tring characte
tring character
r
ri
rin
ring
ring
ring c
ring ch
ring cha
ring char
ring chara
ring charac
ring charact
ring characte
ring character
i
in
ing
ing
ing c
ing ch
ing cha
ing char
ing chara
ing charac
ing charact
ing characte
ing character
n
ng
ng
ng c
ng ch
ng cha
ng char
ng chara
ng charac
ng charact
ng characte
ng character
g
g
g c
g ch
g cha
g char
g chara
g charac
g charact
g characte
g character

 c
 ch
 cha
 char
 chara
 charac
 charact
 characte
 character
c
ch
cha
char
chara
charac
charact
characte
character
h
ha
har
hara
harac
haract
haracte
haracter
a
ar
ara
arac
aract
aracte
aracter
r
ra
rac
ract
racte
racter
a
ac
act
acte
acter
c
ct
cte
cter
t
te
ter
e
er
r
"""