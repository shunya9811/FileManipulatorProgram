# FileManipulationProgram


Recursionのプロジェクト 「File Manipulation Program」です。

## プロジェクトの概要
それぞれに応じたコマンドを入力することで、
ファイル内容を反転させたファイルの出力、
ファイルのコピー、
ファイル内容の繰り返し、
ファイル内検索
が出来ます


## 実行方法

シェルを通して、以下コマンドでそれぞれの機能を使うことができます

inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成
```
python3 --reverse inputpath outputpath

```

inputpath にあるファイルのコピーを作成し、outputpath として保存する
```
python3 --copy inputpath outputpath 
```

inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製
```
python3 --duplicate-contents inputpath n
```

inputpath' にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換え
```
python3 --replace-string inputpath needle newstring
```