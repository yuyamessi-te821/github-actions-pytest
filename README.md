# github-actions-pytest
- sample（CI・pytest の最小動作確認）  
a + b 関数を定義

- divide  
a / b 関数を定義  
ゼロ除算のチェック（b = 0）  
例外の型とメッセージを仕様として固定  



        # workflow 名
        name: pytest (sample)

        # 実行トリガー
        on:
            push:
            pull_request:

        jobs:
            test:
                # 実行環境
                runs-on: ubuntu-latest
                strategy:
                    matrix:
                        project: [sample, divide]

        steps:
            # ソースコード取得
            - uses: actions/checkout@v4

            # Python 環境構築
            - uses: actions/setup-python@v5
              with:
                python-version: "3.10"

            # pytest のインストール
            - name: Install dependencies
                run: pip install pytest

            # pytest 実行
            - name: Run pytest
                run: pytest