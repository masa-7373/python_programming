#x = 10

x = 0
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')

y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2

#あまり好ましくない
if not a == b:
    print('Not equal')
#こちらの方が好ましい
if a != b:
    print('Not equal')

#notのつかいどき

#is_ok = True
is_ok = 0
if is_ok: #is_ok == Trueとしなくてもよい　この場合にnotを使うとスッキリしたコード
    print('OK')
else:
    print('No')

#値に何か変数が入力されていればTrueとなる

is_empty = None
#print(help(is_empty))

if is_empty is None:
    print('None')

print(1 == True)
print(1 is True)
print(True is True)
#is の判定はオブジェクトが一致しているかどうかをみる特にNoneかどうかを判定するとき

#whileループ

count = 0
while count < 5:
    print(count)
    count += 1

count = 0
while True:
    if count >= 5:
        break
    print(count)
    count += 1


count = 0

while count < 5:
    print(count)
    count += 1
else:
    print('done')

#input関数
#while True:
#    word = input('Enter:')
#    num = int(word)
#    if num == 100:
#        break
#    print('next')


some_list =[1, 2, 3, 4, 5]

#i = 0
#while 1 < len(some_list):
#    print(some_list)
#    i += 1


for i in some_list:
    print(i)

for s in 'anoel':
    print(s)

for word in ["My", "name", "is", "Mike"]:
    if word == "name":
        break
    print(word)


for fruit in ["apple", "banana", "orange"]:
    if fruit  == "banana":
        print("stop eating")
        break
    print(fruit)
else:
    print('I ate all!')

#range関数
#下のプログラムでもできないことはないが、、、
num_list = [0, 1, 2, 3, 4, 5, 6, 7]
for i in num_list:
    print(i)
#このようにrange()を使う方が効率的
for i in range(10):
    print(i)

for i in range(2, 10, 3):
    print(i)
#_（アンダースコア）を用いることでfor の次の数字は使わないことを明示できる
for _ in range(10):
    print('hello')

#enumerate関数
i = 0
for fruit in ["apple", "orange", "banana"]:
    print(i, fruit)
    i += 1
#i = 0, i += 1のコードが手間なので、、

for i, fruit in enumerate(["apple", "orange", "banana"]):
    print(i, fruit)

#zip関数
days = ["Monday", 'Tuesday', 'Wednesday']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

#iがいっぱいで見づらいので
for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])

# zip関数を用いることでインデックスをいちいち設定しなくても良いので
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)


# ディクショナリーをforループ

d = {'x': 100, 'y' : 200}
#dのkeyであるx,yが出力される
for v in d:
    print(v)

d = {'x' : 100, 'y' : 200}
#dのkeyとvalueの両方が出力されるメソッドのitems ':'で:をkeyとvalueの間に入れて出力される
for k, v in d.items():
    print(k, ':', v)

print(d.items()) #リストの中にタプルの形で出力される　よく使われるディクショナリのメソッド

