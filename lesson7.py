#object and class

#78　クラスの定義
# class Person(object): #継承のときに'object'が必要になってくる
#     def say_something(self):
#         print('hello')
#
#
# person = Person()
# person.say_something()
#'hello'が出力される

#79  クラスの初期化
# class Person(object):
# #下のものをコンストラクタと呼ぶ
#     def __init__(self):#初期化
#         print('First')
#
#     def say_something(self):
#         print('hello')
#
# person = Person()
# #person.say_something()
# #'First'が出力される

# class Person(object):
#     #selfは保持される
#     def __init__(self, name):
#         self.name = name #引数'name'をself.nameに自分自身の名前を出力
#         print(self.name)
#
#     def say_something(self):
#         print('I am {}.hello'.format(self.name))
#
# person = Person('Mike') #()に人名がないとエラー
# person.say_something()

#80  コンストラクタとデストラクタ
# class Person(object):
#     #selfは保持される
#     #コンストラクタ
#     def __init__(self, name):
#         self.name = name #引数'name'をself.nameに自分自身の名前を出力
#         print(self.name)
#
#     def say_something(self):
#         print('I am {}.hello'.format(self.name))
#
#     def run(self, num):
#         print('run' * 10)
#
#     #デストラクタ　オブジェクトが最後の時に使用される
#     def __del__(self):
#         print('good bye')
#
# person = Person('Mike')
# person.say_something()
#
# #自分で設定するには del オブジェクト名　で可能
# del person
#
# #del personをしない場合には下のものの次にdel personが実行される
# print('##########')

#81 クラスの継承

class Car(object):
    #method run
    def run(self):
        print('run')

#クラスの継承をする 上のclass Carが持ってるオブジェクトの機能をToyotaCarが引き継ぐ
#その際には()にクラス名
class ToyotaCar(Car):
    pass #なにもしない

class TeslaCar(Car):
    def auto_run(self):
        print('auto run')

#carという変数にCarというオブジェクトを作った
car = Car()
#Carのメソッドを作る
car.run()

toyota_car = ToyotaCar()
#メソッドが継承できている
print('##########')
toyota_car.run()
print('##########')

tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()

#82　メソッドのオーバーライドとsuperによる親のメソッドの呼び出し
