*main.pyについて*

以下のパッケージをインストールすると動きます。(Python 3.10.6で確認)
・pyzbar-0.1.9
・numpy-1.26.4
・opencv-python-4.6.0.66

追加のインストールが必要になる可能性があります。
インストールの際はコマンドプロンプトでpipコマンドを使えば入ります(ディレクトリは適宜変更して入力すること)。
[コマンド例]
C:\Test>pip install pyzbar
C:\Test>pip install python-opencv

読み取りの際にメッセージが出るかと思いますが特に問題なく動いているなら無視しても構いません。
また、ESCキーを押すと停止します。その際のWARNメッセージは停止に関することなので無視してください。


*meibo.csvについて*
IDの列にあるのがIDです。QRコードにはこのIDを用いてください。
必要な場合は変更してください
作れない場合はQR_codeディレクトリ内にいくつかあります。

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
