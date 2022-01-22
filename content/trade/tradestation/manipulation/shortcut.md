---
title: "トレステの便利なショートカットキーとコマンド"
linkTitle: "便利なショートカットキーとコマンド"
url: "/p/2mx9jt4"
date: "2020-04-17"
tags: ["トレステ"]
description: "トレードステーションにはキーボードから入力できる様々なショートカットキーやコマンドが用意されており、マウスで GUI 操作を行わなくてもいろいろな画面操作を行えるようになっています。"
---

{{% private %}}
- [About the Command Line](http://help.tradestation.com/09_01/tradestationhelp/desktop/about_command_line.htm)
    - [Command Line Reference](http://help.tradestation.com/09_01/tradestationhelp/cl/command_line_ref_all.htm)
    - [コマンドラインリファレンス (全コマンド)](http://help.tradestation.com/09_05/Monex/jpn/TradeStationHelp/cl/command_line_ref_all.htm)
{{% /private %}}

トレステ内のウィンドウは、ショートカットキーやコマンドで操作することができます。
ショートカットキーは、`Ctrl + N` などでおなじみのいわゆるホットキーですが、トレステで特徴的なのは、コマンド (Command Line) です。

コマンドは、 __ドット (.) で始まるコマンド名__ として定義されており、キーボードからコマンドを入力して `Enter` キーを押すことで、アクティブなウィンドウを素早く操作することができるようになっています。
例えば、チャート分析ウィンドウをアクティブにした状態で、`.iat` と入力して `Enter` キーを押すと、「分析テクニックの挿入」のダイアログを素早く開くことができます。


全般的なショートカットキー＆コマンド
----

ショートカットキー、あるいはコマンドのどちらかを覚えておけば OK です。

| ショートカットキー | コマンド | 説明 |
| ---- | ---- | ---- |
| __`Alt + →`__ / __`Ctrl + Tab`__ | | 次のウィンドウをアクティブにする |
| __`Alt + ←`__ / __`Ctrl + Shift + Tab`__ | | 前のウィンドウをアクティブにする |
| `Ctrl + O` | | 「ワークスペース」を開く |
| `Ctrl + W` | | 「ワークスペース」を閉じる |
| `Ctrl + P` | `.p` `.print` | チャートの印刷（チャートを開いている場合のみ） |
| `Ctrl + N` | `.nw` `.newwindow` | 「トレーディングアプリ」の起動ダイアログを開く |
| __`Alt + F4`__ | | 「トレーディングアプリ」を閉じる |
| __`Ctrl + Alt + C`__ | `.nc` `.newchart` | 「チャート分析」のウィンドウを開く |
| `Ctrl + Alt + H` | `.nhl` `.newhotlist` | 「ホットリスト」のウィンドウを開く |
| `Ctrl + Alt + N` | `.nn` `.newnews` | 「ニュース」のウィンドウを開く |
| `Ctrl + Alt + Q` | `.nrs` `.newraderscreen` | 「レーダースクリーン」のウィンドウを開く |
| `Ctrl + Alt + T` | `.nts` `.newtimeandsales` | 「タイム＆セールス」のウィンドウを開く |
| `Ctrl + Alt + X` | `.nm` `.newmatrix` | 「マトリックス」のウィンドウを開く |
|  | `.nscn` `.newscanner` | 「スキャナー」のウィンドウを開く |
| __`Ctrl + Shift + C`__ | | ウィンドウをコピー |
| __`Ctrl + Shift + V`__ | | ウィンドウを貼り付け |
| `Ctrl + Shift + O` | `.ob` `.orderbar` | オーダーバーを表示・非表示 |


チャート分析関連のコマンド
----

### 新しいチャート分析ウィンドウを開く (.NewChart)

- `.nc`

{{< code title="例: 新しいチャート分析を開き、トヨタ自動車の 5 分足チャートを 10 日間分表示" >}}
.nc ;; 7203-ts 5 min 10 days
{{< /code >}}

### 分析テクニックを挿入 (.InsertAnalysisTechnique)

- `.iat` ... 分析テクニックの選択ダイアログを表示
- `.ist <分析テクニック名>` ... 指定した分析テクニックを挿入

### ストラテジーを挿入 (.InsertAnalysisTechnique)

- `.ist` ... ストラテジーの選択ダイアログを表示
- `.ist <ストラテジー名>` ... 指定したストラテジーを挿入

### スクロールバーを表示／非表示 (.ScrollBar)

- `.scroll` ... スクロールバーをトグル

### 最新のバーの右側のマージンを指定 (.Right)

- `.bar 3` ... 最新バーの右側に 3 本分のマージンができるように表示位置を調整

このコマンドは、最新のバーが画面内に表示されているときしか効果がないようです。
パラメータの数値を省略すると、0 が指定されたのと同じ意味になります（右マージンなし）。

### データウィンドウの表示／非表示 (.DataWindow)

- `.dw`


