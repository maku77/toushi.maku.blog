---
title: "EasyLanguage のコーディングルール（スタイル）"
linkTitle: "コーディングルール（スタイル）"
url: "/p/5wet9n3"
date: "2020-04-18"
tags: ["トレステ", "EasyLanguage"]
weight: 1
description: "EasyLanguage はこれといったコーディングルールがなくて、みんながいろいろなスタイルで書いているみたいです。ここでは、できるだけモダンな言語のルールに似たコーディングルールを定義してみます。"
---

スペース
----

- インデントは半角スペース x4 で行う（タブは使用しない）。


大文字・小文字
----

- 小文字で始める
    - 制御構文: `if`、`begin`、`and` など
    - プリミティブ型名: `bool`、`double`、`null`、スキップワード（`a`、`at` など）
    - 変数定義: `input:` で宣言する入力変数や `var:` で宣言するローカル変数
- 大文字で始める
    - 関数: `AverageFC`、`StdDev` など（ユーザー定義関数を含む）
    - 売買命令: `Buy`、`SellShort` など（関数名っぽいので大文字で）
    - 組み込み変数: `Open`、`Close`、`CurrentBar`、`Date`、`Time` など
- すべて大文字
    - 定数: `const:` で宣言するもの


変数宣言のセクション名
----

入力変数は __`input:`__、定数は __`const:`__、変数は __`var:`__ を使う（一番短い記述のものを採用）。

{{< code title="記述例" >}}
input:
    iPrice(Close) [DisplayName = "Price",
        ToolTip = "Enter an EasyLanguage expression."];

const:
    BASELINE_COLOR("Green");

var:
    double myAvg(0),
    HorizontalLine myLine1(null),
    HorizontalLine myLine2(null);

// ここから本文
{{< /code >}}

上記では、入力変数のプレフィックスに __`i`__、ローカル変数のプレフィックスに `my` を付けていますが、付けなくても OK（`myAvg` の代わりに `avg` とかでよい）。
ただし、定義済みの変数名や関数名と被るのを避けるために、プレフィックスを付けるのをオススメします。


改行位置
----

- `then` や `begin` は基本的に同じ行に続けて記述、`end;` は単独行に記述。

{{< code >}}
if AlertEnabled and alertCondition then begin
    if alertCond1 then
        Alert("Close crossed under high retrace")
    else
        Alert("Close crossed over low retrace");
end;
{{< /code >}}

ただし、関数（メソッド）定義の場合は、`begin` の前に `var` 定義が挟まるので、その場合は `begin` は単独行に記述します。

{{< code >}}
method void printRgb(double inColor, string inName)
var:
    Color objColor;
begin
    objColor = Color.FromARGB(inColor);
    Print(string.Format("{0}: {1} ({2},{3},{4})",
        inName, objColor.Name, objColor.R, objColor.G, objColor.B));
end;
{{< /code >}}

