from abc import ABC, abstractmethod

# Handler（処理を行う抽象クラス）
class Animal(ABC):
    def __init__(self):
        # 次の処理を行うオブジェクト
        self.next_animal = None

    def set_next(self, next_animal):
        # 次の処理を行うオブジェクトを設定
        self.next_animal = next_animal

    @abstractmethod # 抽象メソッド
    def carry_water(self, amount):
        # 水を運ぶ処理
        pass

# 具体的なHandler
class Rabbit(Animal):
    def carry_water(self, amount):
        # 水を運ぶ処理
        if amount < 10:
            # 10リットル未満の場合水を運ぶ
            print(f"ウサギが{amount}リットルの水を運びます。")
        elif self.next_animal:
            # 次の処理を行うオブジェクトがある場合は次の処理を行う
            self.next_animal.carry_water(amount)

class Squirrel(Animal):
    def carry_water(self, amount):
        # 水を運ぶ処理
        if 10 <= amount < 20:
            # 10リットル以上20リットル未満の場合水を運ぶ
            print(f"リスが{amount}リットルの水を運びます。")
        elif self.next_animal:
            # 次の処理を行うオブジェクトがある場合は次の処理を行う
            self.next_animal.carry_water(amount)

# クライアント
rabbit = Rabbit() # ウサギ(リーダー)
squirrel = Squirrel() # リス(ウサギの次の処理を行うオブジェクト)

rabbit.set_next(squirrel) # ウサギの次の処理を行うオブジェクトをリスに設定

rabbit.carry_water(5) # ウサギが5リットルの水を運びます(10リットル未満のため)。
rabbit.carry_water(15) # リスが15リットルの水を運びます(10リットル～20リットルのため)。