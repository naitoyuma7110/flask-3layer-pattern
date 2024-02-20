import pytest
import os

# conftest.pyファイル内に定義された関数やクラスはテストファイル内で自動的にimportされる

# pytest_addoption：コマンドライン引数(フィクスチャ)を設定
# コマンドラインから設定する場合 "pytest --os-name linux"など
def pytest_addoption(parser):
    """テストオプション用の関数"""
    parser.addoption("--os-name", default="windows", help="os name")


# @pytest.fixture：独自フィクスチャの設定
@pytest.fixture()
def target_numbers():
    """テスト対象数値リストを返却する

    Returns:
        テスト対象数値リスト
    """
    # 関数名:フィクスチャ名
    # returnの値：フィクスチャの値
    return [1, 5]


@pytest.fixture()
def open_csv_file():
    """csvファイルをオープンして渡す
    yieldを使用することで終了時にファイルクローズする

    Yields:
        csvファイルオブジェクト
    """
    
    CSV_DIR = "output"
    
    # CSVファイルの保存先ディレクトリが存在しない場合は作成する
    if not os.path.exists(CSV_DIR):
        os.makedirs(CSV_DIR)
        
    print("before open")
    # open時に出力パスやファイル名の指定が必要
    with open(os.path.join(CSV_DIR, "test.csv"), "w+", encoding="utf-8") as csv_file:
        yield csv_file
    print("\nafter")