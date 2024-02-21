from src import sample 
import pytest

class TestSample:
    """Sampleクラスのテスト用クラス"""
    
    # @classmethod:インスタンス化したオブジェクトではなくクラスへの変更を行う
    # setup_class:クラス生成時に実行される。引数は生成されるクラス自身
    @classmethod
    def setup_class(cls):
        # テスト対象のsampleクラスをインスタンス化してTestSampleクラス変数に保持
        cls.temp = sample.Sample()

    def test_add_and_double(self):
        """テストケース1: 正常計算のテスト成功"""
        # selfから@classmethodで自分自身のクラス変数としてSampleクラスのadd_and_doubleを実行する
        assert self.temp.add_and_double(1, 1) == 4
        assert self.temp.add_and_double(2, 2) == 8
        
    def test_add_and_double2(self):
      """テストケース2: 正常計算のテスト失敗"""

      assert self.temp.add_and_double(1, 1) == 5
      assert self.temp.add_and_double(2, 2) == 9
      
    def test_add_and_double3(self):
        """テストケース3: 正常計算のテスト成功"""
        # selfから@classmethodで自分自身のクラス変数としてSampleクラスのadd_and_doubleを実行する
        assert self.temp.add_and_double(1, 2) == 6
        assert self.temp.add_and_double(2, 4) == 12