# ELS-Error-Logs-System-new-version
ELSのライブラリ版です
ELS Error-Logs-System

まず、ELSを使用していただきありがとうございます。
このテキストファイルではELSの使用方法とご説明させていただきます。
※このテキストファイルはPYTHONやそのほかのプログラミング言語を使用している「開発者」向けです。　なのでPYTHONのインストールなどの準備は説明を省かせていただきます。

この説明ではPythonの3.11.0を使用しています。

## 1.導入
els.pyは基本的にはmain.pyなどのディレクトリにelsフォルダしそこに配置するのがおすすめです
```bash
program
   |-main.py
   |-dir1
   |-dir2
   |-els
      |-els.py
```
このような感じです

呼び出しをするときはimport elsなどで呼び出して下さい

## 2.関数一覧
print_switchはprint(出力)をオンオフする変数です※オフの時にerror ok を受け取るには戻り値を使い
```bash
------main.py------------------------------------------
  private_ip = els.private_ip("8.8.8.8", 80, "Off")
  print(private_ip)
-------------------------------------------------------
```
のように受け取れます

error_stop_switchはエラーが起こった時にプログラムを終了するかしないかの変数です
count_elsはpingを行う回数です

```bash
check_platform(print_switch)

check_file_dir(path, error_stop_switch, print_switch)

check_ping(host, count_els, error_stop_switch, print_switch)

private_ip(host, port, print_switch)

global_ip(error_stop_switch, print_switch)
```

check_file_dirでは複数のファイルやディレクトリをチェックする場合はfor文で
```bash
------main.py--------------------------------------------------
path = ['a.txt', 'b.txt', 'c.txt']
for pathcount in path:
    file = els.check_file_dir(str(pathcount), "False", "Off")
    print(file)
---------------------------------------------------------------
```
このように書きます

## 3.終わりに
基本的な説明はここで書きましたが何かありましたらgithubのIssuesで教えてください。

ちなみにtemplateフォルダにmain.pyのテンプレートを入れときます
