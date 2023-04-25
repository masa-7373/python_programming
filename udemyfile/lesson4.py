# 関数定義
def say_something() :
    print('Hi')

# 関数を呼び出すときは定義した関数を出すだけ ()は必要
say_something()
print(type(say_something)) #say_somethingはfunctionという型なので
f = say_something #このときは()は不要
f()

#返り値
def say_anything() :
    s = 'hi'
    return s #ｓを返したいとき

result = say_anything()
print(result)

#引数
def what_is_this(color): #colorが引数　（）の中にあるもの
    #redが引数の時はtomatoを返す
    if color == "red":
        return 'tomato'
    # greenが引数の時はgreen pepperを返す
    elif color == 'green':
        return 'green pepper'
    # それ以外の場合はI don't knowを返す
    else:
        return "I don't know."
#result = what_is_this()の()中には""を書かないとエラーが出る
result = what_is_this("")
print(result)

num: int = 10 #:でint として値を入れると

def add_num(a: int, b: int) -> int:
    # a: intでaはintであることを示し、->で返り値もintであることを示している。
    return a + b

r = add_num(10, 20)
#引数がintで定義しているのに引数をstrなどでしてもエラーは出ないが、気をつける
print(r)

#関数の引数
#def menu(entree, drink, dessert):
    #print('entree = ', entree)
    #print('drink = ', drink)
    #print('dessert = ', dessert)
#順番が大事になってくるので、その順番を間違いたくない場合にはkeyword argument
#menu(entree='beef', dessert='ice', drink='beer')

#デフォルト引数
def menu(entree = 'beef', drink = 'wine', dessert = 'ice'):
    print('entree=', entree)
    print('drink=', drink)
    print('desset=', dessert)
menu()
#引数を何も入れてない場合には元々定義していたものが出力される

#デフォルト引数で気をつけること
def test_funk(x,l=[]):
    l.append(x)
    return l

# y = [1, 2, 3]
# r = test_funk(100, y)
# print(r)
# y = [1, 2, 3]
# r = test_funk(200, y)
# print(r)

# 一つだけなら問題ないが、、
r = test_funk(100)
print(r)
# 二つだとリストに同じものが存在してしまう、、バグになる可能性が、、出力結果は[100, 100]
r = test_funk(100)
print(r)
# →pythonではリストはデフォルト引数で与えるべきではないという暗黙の了解がある
# リストは参照渡しになっているから
# 解決策は、、、
# リストにするものをNoneとしてif文で空のリストを作って初期化して処理する
def test_funk_2(x, l = None):
    if l is None:
        l =[]
    l.append(x)
    return l

r = test_funk_2(100)
print(r)
r = test_funk_2(100)
print(r)

#位置引数のタプル化
# 引数の前に*をつけることでタプルに勝手に入れてくれる
# forループで回してみると、、
# １引数とも一緒に使える

def say_something(word, *args):
    print('word = ', word)
    for arg in args:
        print(arg)

say_something('Hi!', 'Mike', 'Nancy')
# 先にタプルを作ってやってみた場合には、、上と同じになるが、今は上のプログラムが普通
# t = ('Mike', 'Nancy')
# say_something('Hi!', *t)

# キーワード引数の辞書化
# *を二つ**にしてkwargsを続けて書く
def menu(**kwargs):
    # print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

# menu(entree = 'beef', drink = 'coffee')
# 結構使う
d = {
    'entree':'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}
menu(**d)

# *argsと**kwargsの順序が逆になるとエラーになる
def menu_2(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu_2('banana', 'apple', 'orange', entree = 'beef', drink ='coffee')

#Docstrings
# pythonではfunc内のドキュメントの書き方はクウォテーション三つで挟む
def example_func(param1, param2):
    """Example function with types documented in the docstring.

    Args:
        param1 (int) : The first parameter.
        param2 (str) : The second parameter.
    Returns:
         bool : The return value. True for success, False otherwise.
    """
    print(param1)
    print(param2)
    return True

# これで関数のドキュメントを出力できるprint(example_func.__doc__)

# 関数内関数, inner function
def outer(a, b):

    def plus(c, d):
        return c + d

    r1 = plus(a, b) #上で定義した関数に返す
    r2 = plus(b, a)
    print(r1 + r2)

outer(1, 2)

#デコレータ

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

@print_info #指定するとprint_infoにいってくれる
def add_num(a, b):
    return a + b

#二つ並べると、順序が発生する。
@print_info
@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

#名前空間とスコープ

animal = 'cat'

def f():
    #print(animal) error!　
    # ファンクション内で宣言された変数＝ローカル変数
    # を宣言する前に参照しているとないと判断されてエラーが起きる
    animal = 'dog'
    print('after', animal)

f()
print('global:', animal)

#グローバルの変数を関数内で書き換える方法
def f():
    global animal #globalを変数の前におくことでできる
    animal = 'dog'
    print('local', animal)

def f():
    animal = 'dog'
    print('local:', locals()) #locals()でローカル変数が辞書型で返される

#例外処理
l = [1, 2, 3]
i = 5
#del i

"""try:
    l[i]
except:
    print("Don't worry")
"""

try:
    l[0]

except IndexError as ex:
    print("Don't worry :{}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print('other: {}'.format(ex))
else: #上までのものがエラーなく抜けた場合におけ
    print('done')
finally:
    print('clean up')

#独自エラーの作成
#raise IndexError('text error')　自分でエラーを作る方法

#Exceptionという既存のクラスを独自のものに変更する場合
class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE','orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next')