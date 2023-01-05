import argparse

# reverse inputpath outputpath: 
# inputpath にあるファイルを受け取り、outputpath に inputpath の内容を
# 逆にした新しいファイルを作成します。
reverseComment = "inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。"

class ReverseAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        setattr(namespace, self.dest, values)
        # Namespace(copy=None, duplicate=None, replace=None, reverse=None) 
        # Namespace(copy=None, duplicate=None, replace=None, reverse=['input.txt', 'text1.txt'])
        # setattrは、オブジェクトの属性の追加 
        # --reverseはoption_string
        # reverseはself.dest
        # valuesに位置引数が入っている

        input_file, output_file = values
        try:
            with open(input_file, "r") as f:
                content = f.read()
            
            with open(output_file, "w") as f:
                f.write(content[::-1])

        except FileNotFoundError:
            print("入力ファイルが存在しません")
        
        


# copy inputpath outputpath: 
# inputpath にあるファイルのコピーを作成し、outputpath として保存します。
copyComment = "inputpath にあるファイルのコピーを作成し、outputpath として保存します。"

class CopyAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        setattr(namespace, self.dest, values)
        input_file, output_file = values
        try:
            with open(input_file, "r") as f:
                content = f.read()
            
            with open(output_file, "w") as f:
                f.write(content)

        except FileNotFoundError:
            print("入力ファイルが存在しません")
    

# duplicate-contents inputpath n:
# inputpath にあるファイルの内容を読み込み、その内容を複製し、
# 複製された内容を inputpath に n 回複製します。
duplicateComment = "inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に duplicateTimes 回複製します。"

class DuplicateAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        setattr(namespace, self.dest, values)
        input_file, duplicateTimes = values

        try:
            int(duplicateTimes)
        except ValueError:
            print("二番目の引数には整数を入力してください")
            return

        try:
            with open(input_file, "r") as f:
                content = f.read()
            
            with open(input_file, "w") as f:
                f.write(content * int(duplicateTimes))

        except FileNotFoundError:
            print("入力ファイルが存在しません")
        


# replace-string inputpath needle newstring: 
# inputpath' にあるファイルの内容から文字列 'needle' を検索し、
# 'needle' の全てを 'newstring' に置き換えます。
replaceComment = "inputpath' にあるファイルの内容から文字列 'needle' を検索し 'needle' の全てを 'newstring' に置き換えます。"

class ReplaceAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        setattr(namespace, self.dest, values)
        
        input_file, needle, newstring = values

        try:
            with open(input_file, "r") as f:
                content = f.read()

            if content.find(needle) == -1:
                print("見つかりませんでした。")
                return 

            with open(input_file, "w") as f:
                f.write(content.replace(needle, newstring))
                

        except FileNotFoundError:
            print("入力ファイルが存在しません")




# オプション引数は接頭辞 - により識別され、それ以外の引数は位置引数として扱われます:
# --をつけるのとつけないのとでは動作が異なる

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--reverse",                         # オプション引数名設定
        type=str,                            # inputType
        nargs=2,                             # 要する引数
        metavar=("inputpath", "outputpath"), # ヘルプメッセージを出力する際、各引数に対しての参照名
        action=ReverseAction,                # 処理内容
        help=reverseComment                  # ヘルプメッセージ
    )

    parser.add_argument(
        "--copy", 
        type=str, 
        nargs=2, 
        metavar=("inputpath", "outputpath"),
        action=CopyAction,
        help=copyComment)

    parser.add_argument(
        "--duplicate", 
        type=str, 
        nargs=2,
        metavar=("inputpath", "duplicateTimes"),
        action=DuplicateAction,
        help=duplicateComment
    )

    parser.add_argument(
        "--replace", 
        type=str, 
        nargs=3,
        metavar=("inputpath", "needle", "newstring"),
        action=ReplaceAction,
        help=replaceComment
    )

    args = parser.parse_args()


if __name__ == "__main__":
    main()