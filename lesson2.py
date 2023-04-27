r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3)) #3がどの場所にあるかを示す
print(r.index(3 , 3))#３が３番目以降のどこにあるか示す

print(r.count(3)) #3が何個あるか示す

if 100 in r:
    print("exist")

r.sort()#rを小さい順に並び替える
print(r)
r.sort(reverse = True) #rを大きい順に並び替える　reverse = True であるようにする）
print(r)
r.sort(reverse = False)
print(r)
r.reverse()#メソッドで反転することもできる
print(r)

s = 'My name is Mike.'
to_split = s.split(' ') # ''の中にあるもので分けてリストに入れてくれる
print(to_split)


x = ' '.join(to_split) #joinはリストを受け入れられるメソッド ''の中にあるもので繋げてくれる
print(x)
#print(help(list))でメソッドの一覧が見られる

#値渡しと参照渡しの違い
i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j = ', j)
print('j = ', i)

x = [1, 2, 3, 4, 5]
y = x.copy()    #y = x[:]でも同じことができるが普通は.copy()を用いる
y[0] = 100
print('y = ', y)
print('x = ', x)

#値渡し
X = 20
Y = X
Y = 5
print(id(X)) #どこに保存されているか示す
print(id(Y)) #上のと比較すると番号が異なっていることがわかる
print(X)
print(Y)
#参照渡し
print("#####")
X = ['a', 'b']
Y = X
Y[0] = 'p'
print(id(X)) #どこに保存されているか示す
print(id(Y)) #上のと比較すると番号が同じになっていることがわかる
print(X)
print(Y)
print("######")

num_tuple = (10, 20)
print(num_tuple)

#ｘ、ｙそれぞれにnum_tupleを分配している
x, y = num_tuple
print(x, y)

#tupleには（）がなくても宣言できるので、、、
x, y = 10, 20
print(x, y)
#ただし、長くなると見づらいので一つ一つ改行して入力する

#tupleのアンパッキング
print('#######')
i = 10
j = 20
tmp = i
i = j
j = tmp
print(i, j)
#入れ替えることができるが、3行のコードが必要なので、tupleのアンパッキングを利用する
a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)
#上の行がtupleのアンパッキング
print('#######')

chose_from_two = ('A', 'B', 'C')

answer = []
answer.append('A')
answer.append('C')

print(chose_from_two)
print(answer)
print('#######')

# 辞書型
x = {'a':1}
y = x
y['a'] = 1000
print(x)
print(y)
x = {'a' : 1}
y = x.copy()
y['a'] = 100
print(x)
print(y)
print('#####')

fruits = {
    'apple': 100,
    'grape': 200,
    'orange': 300,
}
print(fruits['apple'])

#集合
print('######')
my_friends = {'A', 'B', 'D'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_friends & A_friends)

f = ['apple', 'banana', 'apple', 'banana']
kind = set(f) #集合を使って型変換して重複したものを一つにする
print(kind)
