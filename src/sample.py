class Sample:
    """Sampleクラス"""

    def add_and_double(self, x, y):
        """
        xとyを足して2倍した値を返却する

        Args:
            x: 入力値1
            y: 入力値2
        """
        # intでない場合は、ValueErrorとする
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError

        # 計算処理
        result = x + y
        result *= 2

        return result