## ライブラリのインストール

> MeCab

```
$ brew install mecab mecab-ipadic git curl xz
$ git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
$ cd /mecab-ipadic-neologd
$ sudo ./bin/install-mecab-ipadic-neologd -n -a
$ echo `mecab-config --dicdir`"/mecab-ipadic-neologd" （階層確認コマンド）
```



## 実行手順

> mecab_judge.py

レビューごとのネガポジ点数を算出する。

```
8行目 text_paths = glob.glob('./review/star1-/**.txt')
```

star1-，star2-，star3，star4+，star5+ それぞれ⭐︎1から⭐︎5のレビューが格納されている。8行目のパスを書き換えて，それぞれ実行する。

```
49行目 dic = get_dic('./dic/dictionary.csv')
```

dicディレクトリ に" dictionary.csv(自作辞書)"と"dictionary_gene.csv(一般的な辞書)"が格納されている。それぞれ実行して，レビューごとの点数を算出する。

> accuracy.py

レビューの⭐︎1, 2をマイナス。⭐︎3を0。⭐︎4, 5をプラスとして，精度を測る。

18行目から34行目のif文について，以下のパターンでコードを書き換える。

- ⭐︎1, 2
- ⭐︎3
- ⭐︎4, 5

