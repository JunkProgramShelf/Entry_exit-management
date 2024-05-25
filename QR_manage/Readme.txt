*main.pyについて*

以下のパッケージをインストールすると動きます。(Python 3.7.4で確認)
・pyzbar
・numpy
・OpenCV

上記以外のパッケージはデフォルトで入っているので追加のインストール花王です。
インストールの際はコマンドプロンプトでpipコマンドを使えば入ります(ディレクトリは適宜変更して入力すること)。
[コマンド例]
C:\Test>pip install pyzbar
C:\Test>pip install python-opencv

読み取りの際にメッセージが出るかと思いますが特に問題なく動いているなら無視しても構いません。
また、ESCキーを押すと停止します。その際のWARNメッセージは停止に関することなので無視してください。


*meibo.csvについて*
IDの列にあるのがIDです。QRコードにはこのIDを用いてください。
作れない場合はQR_codeディレクトリ内にあります。

*QRコードについて
デフォルトではQR_Codeディレクトリ内にあるものが使えるようになっています。
適宜変更してご使用ください。
以下のwebサイトなどで作成することが可能ですので参考にどうぞ
RQコード作成サイト
https://qr.quel.jp/

*エラーについて(Windowsの場合)
FileNotFound...みたいなエラーが出た場合、以下のサイトから
「Visual Studio 2013 の Visual C++ 再頒布可能パッケージ 」の
[vredist_x64.exe]をダウンロードし、手順に従ってインストールしてください
'https://www.microsoft.com/ja-JP/download/details.aspx?id=40784'
