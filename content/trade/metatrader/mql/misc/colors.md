---
title: "MetaTrader/MQL: MQL での色の表現方法 (color)"
linkTitle: "MQL での色の表現方法 (color)"
url: "p/rn6kw8j/"
date: "2015-10-10"
lastmod: "2021-02-12"
tags: ["MetaTrader/MQL"]
---

MQL コード内で色情報を表現する場合、[color 型](https://www.mql5.com/en/docs/basis/types/integer/color)（[日本語](https://www.mql5.com/ja/docs/basis/types/integer/color)）の変数を使います。

`color` 変数は 4 バイトの数値で、後ろ 3 バイトでそれぞれ RGB の色情報 (0~255) を保持しています。
コード内で色を表すときは、下記のいずれかのリテラル形式で表現します。

- __`C'r,g,b'`__ 形式リテラル
- 定義済みのカラー名
- 4 バイト数値

{{< code lang="cpp" >}}
// RGB 形式
C'128,128,128'     // Gray
C'0x00,0x00,0xFF'  // Blue

// 定義済みカラー値
clrRed             // Red
clrYellow          // Yellow
clrBlack           // Black

// 4 バイト整数
0xFFFFFF           // White
16777215           // White
0x008000           // Green
32768              // Green
{{< /code >}}

`clrRed` のような定義済みのカラー値として何が用意されているかは、下記を参照してください。

- （参考）[MQL5 - Web Colors](https://www.mql5.com/en/docs/constants/objectconstants/webcolors)（[日本語](https://www.mql5.com/ja/docs/constants/objectconstants/webcolors)）

