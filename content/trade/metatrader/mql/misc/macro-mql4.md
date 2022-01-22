---
title: "MQLマクロ: MQL4 と MQL5 のどちらでコンパイルされているか調べる"
linkTitle: "MQL4 と MQL5 のどちらでコンパイルされているか調べる"
url: "/p/43cgihf"
date: "2020-10-27"
tags: ["MetaTrader/MQL"]
---

MQL のプログラムが MQL4 コンパイラでビルドされるとき、__`__MQL4__`__ マクロが定義されます。
これを利用すると、MQL4 用と MQL5 用のコードを分けて記述することができます。

{{< code lang="cpp" >}}
#ifdef __MQL4__
    MessageBox("MQL4でコンパイルされています");
#else
    MessageBox("MQL5でコンパイルされています");
#endif
{{< /code >}}

