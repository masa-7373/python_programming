print('New File')

num = 1
name = '1'
is_ok = True

#print(num, type(num))
#print(name, type(name))
#print(is_ok, type(is_ok))


new_num = int(name)

print(new_num, type(new_num))

print('Hi', 'Mike')

s ='test'
print(s)
print("I don't know")
print('I don\'t know')
print('say "I don\'t know"')
print("say \"I don't know\"")
print('hello. \nHow are you?')
print('C\name\name')
#ame
#ame
print(r'C\name\name')
#namename

print("""
line 1
line 2
line 3
""")

print("############")
print("""\
line 1
line 2
line 3\
""")
print("############")

print('Hi,' * 2 + 'Mike')
print('py' + 'thon')
prefix = 'Py'
print(prefix + 'thon')

word = 'python'
print(word[0])
print(word[-1])
print(word[0:2])
print(word[2:5])

print("#############")
print(word[:4])
print(word[0:4])
print("#############")
print(word[:7])
print("###########")
#word[0] = 'J'  I cannnot do it
word = 'J' + word[1:]
print(word)
n = len(word)
print(n)

s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('my')
print(is_start)

print("##########")

print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize()) ##一番最初以外は小文字になる
print(s.title()) ##すべての文字の頭文字が大文字になる
print(s.upper()) ##すべてが大文字になる
print(s.lower())
print(s.replace('Mike', 'Nancy'))
