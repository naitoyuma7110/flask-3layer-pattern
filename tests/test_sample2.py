from src import sample 
import pytest

# スキップ用フラグ
SKIP_FLAG = True

class TestSample:
    """Sampleクラスのテスト用クラス"""
    
    
    # @classmethod:インスタンス化したオブジェクトではなくクラスの変更を行う

    # setup_class:クラス生成時に実行される。引数は生成されるクラス自身
    @classmethod
    def setup_class(cls):
        print("\nStart TestSample")
        # sampleクラスをインスタンス化してTestSampleクラス変数に保持
        cls.temp = sample.Sample()

    # teardown_class:クラス破壊時に実行される
    @classmethod
    def teardown_class(cls):
        print("\nEnd of TestSample")
        del cls.temp

    # setup_method：メソッドの呼び出し時に実行される。引数は実行されるメソッド自身
    def setup_method(self, method):
        print(f"\nStart method name: {method.__name__}")

    # teardown_method：メソッドの終了時に実行される
    def teardown_method(self, method):
        print(f"\nEnd method name: {method.__name__}")
        

    def test_add_and_double(self):
        """テストケース1: 正常計算"""
        assert self.temp.add_and_double(1, 1) == 4
        assert self.temp.add_and_double(2, 2) == 8

    def test_add_and_double_raise(self):
        """テストケース2: 例外処理"""
        
        # 例外処理をテストする場合 with句とpytest.raise(例外クラス)を宣言する
        with pytest.raises(ValueError):
            self.temp.add_and_double("1", 1)
        with pytest.raises(ValueError):
            self.temp.add_and_double(1, "1")
        with pytest.raises(ValueError):
            self.temp.add_and_double("1", "1")

    # 明示的にスキップ(特定の条件に応じてスキップするなどのユースケース)
    @pytest.mark.skip(reason="skip理由:xxxxxxxxxx")
    def test_add_and_double_skip(self):
        """スキップ確認用"""
        assert self.temp.add_and_double(1, 1) == 4

    # 単純な条件であればskipifで判定
    @pytest.mark.skipif(SKIP_FLAG is True, reason="条件付きskip理由:xxxxxxxxx")
    def test_add_and_double_skipif(self):
        """条件付きスキップ確認用"""
        assert self.temp.add_and_double(1, 1) == 4

    def test_add_and_double_option(self, request):
        """フィクスチャの使用
        requestはpytestで定義されたフィクスチャで引数として受け取る事で使用できる

        Args:
            request: フィクスチャ
        """
        os_name = request.config.getoption("--os-name")
        if os_name == "windows":
            print("dir")
        elif os_name == "linux" or os_name == "mac":
            print("ls")
        assert self.temp.add_and_double(1, 1) == 4


    def test_add_and_double_original(self, target_numbers):
        """独自フィクスチャを使ってテストする場合

        Args:
            target_numbers: テスト対象数値リストを返す独自フィクスチャ
        """
        print(target_numbers)
        a, b = target_numbers
        assert self.temp.add_and_double(a, b) == 12

    def test_add_and_double_original_csv(self, open_csv_file):
        """独自フィクスチャを使ってテストする場合
        csvファイルなどのオープン/クローズをフィクスチャ側で実行

        Args:
            open_csv_file: csvファイルを開く独自フィクスチャ
        """
        
        print(open_csv_file)
        open_csv_file.write("test1,test2,test3")
        assert self.temp.add_and_double(1, 1) == 4