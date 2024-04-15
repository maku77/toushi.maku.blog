---
title: "トレステの設定: シンボルリンクとインターバルリンクでウィンドウ間の表示を連携させる"
linkTitle: "シンボルリンクとインターバルリンクでウィンドウ間の表示を連携させる"
url: "/p/yhr2aiq"
date: "2020-01-12"
tags: ["トレステ"]
---

ウィンドウリンクとは
----

TradeStation の「ウィンドウリンク」の仕組みを使用すると、ウィンドウ間（トレーディングアプリ間）で選択している銘柄や、足のインターバル（分足や時間足）の設定を同期させることができます。
ウィンドウリンクの機能には、次の 2 種類があります。

* **シンボルリンク** ... 銘柄をリンクして切り替える
* **インターバルリンク（足種リンク）** ... 足のインターバルをリンクして切り替える


シンボルリンク
----

シンボルリンクを有効にするには、各ウィンドウのタイトルバー右上に表示されている「S」マークをクリックし、ハイライトされた状態にします。

{{< image w="600" border="true" src="001.png" >}}

ここでは、「レーダースクリーン」と「チャート分析」のウィンドウのシンボルリンクを有効にしています。
レーダースクリーンの銘柄コードをクリックすると、チャート分析のウィンドウで表示している銘柄が連動して切り替わるようになります。


インターバルリンク（足種リンク）
----

インターバルリンクを有効にするには、各ウィンドウのタイトルバー右上に表示されている「I」マークをクリックし、ハイライトされた状態にします（シンボルリンクのボタンの右にあります）。

{{< image w="150" border="true" src="002.png" >}}

インターバルリンクを複数のウィンドウで有効にしておくと、5分足や、1時間足などのインターバル設定を同期させることができます。


リンクカラーとグローバル設定
----

シンボルリンクやインターバルリンクのボタンの隅にあるプルダウンマークを押すと、下記のようにリンクの種類を選択することができます。

{{< image w="250" border="true" src="003.png" >}}

ここでは、リンクの色を設定することができ、等しい色を選択したウィンドウ同士でリンク機能が働くようになります。

また、ここで、**グローバルリンク**と記述されたものを選択すると、ワークスペースをまたがったウィンドウ間でもリンク機能が働くようになります（デフォルトはローカルリンクになっています）。
ローカルリンクとグローバルリンクはボタンの形が若干違うので、タイトルバーを見るだけで現在どちらが設定されているかを判別できます。

{{< image border="true" src="004.png" >}}

上のボタンがローカルリンク時の形状で、下のボタンがグローバルリンク時の形状です。
