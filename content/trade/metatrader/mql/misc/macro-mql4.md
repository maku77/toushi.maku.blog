---
title: "MetaTrader/MQL: MQL4 と MQL5 のどちらでコンパイルされているか調べる"
linkTitle: "MQL4 と MQL5 のどちらでコンパイルされているか調べる"
url: "/p/43cgihf"
date: "2020-10-27"
tags: ["MetaTrader/MQL"]
---

MQL コード内で下記のマクロが定義されているかどうかを調べることによって、MQL プログラムが MQL4 としてコンパイルされているのか、MQL5 としてコンパイルされているのかを判別することができます。

- __`MQL4`__ ... MQL4 としてコンパイルされているときに定義される
- __`MQL5`__ ... MQL5 としてコンパイルされているときに定義される

これを利用すると、MQL4 用と MQL5 用のコードを単一のファイルで記述することができます。

{{< code lang="cpp" title="MQL4/5 コードを混在させる" >}}
void OnStart() {
#ifdef __MQL5__
    MessageBox("MQL5 でコンパイルされています");
#else
    MessageBox("MQL4 でコンパイルされています");
#endif
}
{{< /code >}}

