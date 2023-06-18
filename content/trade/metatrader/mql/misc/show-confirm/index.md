---
title: "MetaTrader/MQL: プログラムの実行前に確認ダイアログを表示する (#property show_confirm)"
linkTitle: "プログラムの実行前に確認ダイアログを表示する (#property show_confirm)"
url: "/p/6s6iu7i"
date: "2014-12-07"
tags: ["MetaTrader/MQL"]
---

プログラムの先頭で、次のように __`show_confirm` プロパティを設定しておくと、プログラムの実行前（チャートにアタッチしたとき）に、 __本当に実行してよいかの確認ダイアログ__ が表示されるようになります。

{{< code >}}
#property show_confirm
{{< /code >}}

{{< image src="img-001.png" border="true" >}}

この確認ダイアログは、スクリプト、カスタム指標、EA のどの種類のプログラムでも有効です。
新規注文や決済を行うようなプログラグムは、誤って実行してしまわないように、このプロパティを設定しておくと安心です。

