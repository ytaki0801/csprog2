class Base:
  def __init__(self, n):
    print('- Baseの引数付きコンストラクタ__init__ -')
    self.__num = n
  def __str__(self):
    print('- Baseの特殊メソッド__str__ -')
    return 'num: ' + str(self.__num)
  def setNum(self, n):
    print('- BaseのメソッドsetNum -')
    self.__num = n

class Even(Base):
  def __init__(self, n):
    print('- Evenの引数付きコンストラクタ__init__ -')


  def __str__(self):
    print('- Evenの特殊メソッド__str__ -')



    return r
  def setNum(self, n):
    print('- EvenのメソッドsetNum -')
    if n % 2 == 0:


    else:


print('===== Baseのインスタンスb作成・出力 =====')
b = Base(1); print(b)
print('===== Evenのインスタンスe作成・出力 =====')
e = Even(10); print(e)
print('==== bのsetNumの動作確認 ====')
b.setNum(15); print(b)
print('==== eのsetNumの動作確認 ====')
e.setNum(15); e.setNum(8); e.setNum(3); print(e)
