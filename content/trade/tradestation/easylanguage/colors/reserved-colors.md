---
title: "EasyLanguage: カラー予約語と値の対応表"
linkTitle: "カラー予約語と値の対応表"
url: "/p/f9q6kye"
date: "2020-05-02"
tags: ["EasyLanguage"]
---

カラー予約語の一覧
----

EasyLanguage には下記のような RGB 値を表す予約語が定義されています。
これらの予約語は、内部的には RGB 値を表す int 型の値（32 ビット整数値）です。
つまり、コード上で `Red` と記述するのと、`255` と記述するのは同じ意味になります。

| カラー予約語 | 10進表記 | 16進表記 | RGB値 | レガシー値 | サンプル |
| ---- | ---: | :--: | :--: | :--: | :--: |
| Black | 0 | 000000 | (0,0,0) | 1 | <span style="background: #000000">　　　　</span> |
| Blue | 16711680 | 0000ff | (0,0,255) | 2 | <span style="background: #0000ff">　　　　</span> |
| Cyan | 16776960 | 00ffff | (0,255,255) | 3 | <span style="background: #00ffff">　　　　</span> |
| Green | 65280 | 00ff00 | (0,255,0) | 4 | <span style="background: #00ff00">　　　　</span> |
| Magenta | 16711935 | ff00ff | (255,0,255) | 5 | <span style="background: #ff00ff">　　　　</span> |
| Red | 255 | ff0000 | (255,0,0) | 6 | <span style="background: #ff0000">　　　　</span> |
| Yellow | 65535 | ffff00 | (255,255,0) | 7 | <span style="background: #ffff00">　　　　</span> |
| White | 16777215 | ffffff | (255,255,255) | 8 | <span style="background: #ffffff">　　　　</span> |
| DarkBlue | 8388608 | 000080 | (0,0,128) | 9 | <span style="background: #000080">　　　　</span> |
| DarkCyan | 8421376 | 008080 | (0,128,128) | 10 | <span style="background: #008080">　　　　</span> |
| DarkGreen | 32768 | 008000 | (0,128,0) | 11 | <span style="background: #008000">　　　　</span> |
| DarkMagenta | 8388736 | 800080 | (128,0,128) | 12 | <span style="background: #800080">　　　　</span> |
| DarkRed | 128 | 800000 | (128,0,0) | 13 | <span style="background: #800000">　　　　</span> |
| DarkBrown | 32896 | 808000 | (128,128,0) | 14 | <span style="background: #808000">　　　　</span> |
| DarkGray | 8421504 | 808080 | (128,128,128) | 15 | <span style="background: #808080">　　　　</span> |
| LightGray | 12632256 | c0c0c0 | (192,192,192) | 16 | <span style="background: #c0c0c0">　　　　</span> |


おまけ: カラー予約語の値を出力するコード
----

下記の EasyLanguage コードは、すべてのカラー予約語の RGB 値を出力します。

{{< code >}}
using elsystem.drawing;  // Color class

method void printRgb(double inColor, string inName)
var:
    Color objColor;
begin
    objColor = Color.FromARGB(inColor);
    Print(string.Format("{0}: {1} ({2},{3},{4})",
        inName, objColor.Name, objColor.R, objColor.G, objColor.B));
end;

once begin
    ClearPrintLog;
    printRgb(Black, "Black");
    printRgb(Blue, "Blue");
    printRgb(Cyan, "Cyan");
    printRgb(Green, "Green");
    printRgb(Magenta, "Magenta");
    printRgb(Red, "Red");
    printRgb(Yellow, "Yellow");
    printRgb(White, "White");
    printRgb(DarkBlue, "DarkBlue");
    printRgb(DarkCyan, "DarkCyan");
    printRgb(DarkGreen, "DarkGreen");
    printRgb(DarkMagenta, "DarkMagenta");
    printRgb(DarkRed, "DarkRed");
    printRgb(DarkBrown, "DarkBrown");
    printRgb(DarkGray, "DarkGray");
    printRgb(LightGray, "LightGray");
end;
{{< /code >}}

上記のコードでは、各カラー予約語の RGB 成分を取り出すために、`Color` オブジェクトに変換してから `R` プロパティなどを参照していますが、カラー予約語から `GetRValue(Cyan)`、`GetGValue(Cyan)`、`GetBValue(Cyan)` のように直接 RGB 成分を取り出すこともできます。

`Color` オブジェクトの `Name` プロパティは、`FF808080` のような 16 進数表記の RGBA 文字列になるみたいなのでこれを利用してます。

