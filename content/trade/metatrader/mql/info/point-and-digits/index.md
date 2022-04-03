---
title: "MetaTrader/MQL: 通貨（シンボル）のポイントサイズ、Digit 数を調べる (Point, Digits, SymbolInfoDouble)"
linkTitle: "通貨のポイントサイズ、Digit 数を調べる (Point, Digits, SymbolInfoDouble)"
url: "/p/gkcxsb2"
date: "2020-11-08"
lastmod: "2022-04-03"
tags: ["MetaTrader/MQL"]
---

Point と Digits とは（Pips とは違う？）
----

__ポイントサイズ (Point)__ は具体的には 0.001 や 0.0001 などの数値であり、ブローカーが各通貨ごとに提示 (quote) する価格表示の最小単位を示しています。
ポイントの単位は決済通貨です。
下記はあるブローカーを使用した場合の、MetaTrader の取引パネルの表示例（ドル円とユーロドル）です。

{{< image w="700" src="img-001.png" >}}

USDJPY は 0.001（円）の単位まで表示されているので、1 point = 0.001 です。
EURUSD は 0.00001（ドル）の単位まで表示されているので、1 point = 0.00001 です。
同様の概念として __桁数 (Digits)__ がありますが、これは小数点以下何桁まで提示するかであり、本質的には Point と同じ情報を示しています。
これらの値は、通貨ごとに異なるだけでなく、__ブローカーによって異なること__ に注意してください。
提示パターンは大きく下記の 2 通りに分かれるようです。

- 3/5 digit broker ... USDJPY が `x.xxX`、EURUSD が `x.xxxxX` と提示される。
- 4/6 digit broker ... USDJPY が `x.xxxX`、EURUSD が `x.xxxxxX` と提示される。

[OrderSend 関数や CTrade クラスで注文を出す](/p/qboyakv) 場合、最大許容スリッページ (Deviation) などをポイント数で指定する必要があります。
例えば、USDJPY のポイントサイズが 0.001 のときに、最大許容スリッページを 0.005 円 (0.5 pips) にしたければ、5 ポイントと指定する必要があります。

ちなみに、FX の世界では __Pips (percentage in point)__ という単位もよく使われており、取引の成績を表現するときに利用されています（例:「ドル円で 10 ピップとった！」）。
ある通貨の 1 pip がいくらかは世界共通で決められていて、USDJPY の 1 pip = 0.01 円（1 銭）、EURUSD の 1 pip は 0.0001 ドルです。
上の取引パネルの図で、大きく表示されている数値が Pips を表しています。
つまり、このブローカーの場合、1 pip = 10 points です。


カレントチャートの通貨のポイントサイズを取得する (Point, Digits)
----

カレントチャートで表示している通貨のポイントサイズを調べるには、[Point 関数](https://www.mql5.com/en/docs/check/point)、桁数を調べるには [Digits 関数](https://www.mql5.com/en/docs/check/digits) を使用します。

{{< code lang="cpp" title="Scripts/ShowPointAndDigits.mq5" >}}
void OnStart() {
    const string symbol = Symbol();  // カレントチャートのシンボル（例: "USDJPY）
    double point = Point();  // ポイントサイズ（例: USDJPY なら 0.001 や 0.0001）
    int digits = Digits();   // 小数点以下桁数（例: USDJPY なら 3 や 4）

    MessageBox(StringFormat("Symbol=%s, Point=%f, Digits=%d", symbol, point, digits));
}
{{< /code >}}

{{< code title="表示例" >}}
Symbol=EURUSD, Point=0.000010, Digits=5
{{< /code >}}


指定した通貨のポイントサイズを取得する (CSymbolInfo クラス、SymbolInfoXXX 関数)
----

### CSymbolInfo クラスを使う方法

[取引クラス](https://www.mql5.com/ja/docs/standardlibrary/tradeclasses) のひとつである [CSymbolInfo クラス](https://www.mql5.com/ja/docs/standardlibrary/tradeclasses/csymbolinfo) を使用すると、指定したシンボル（通貨）の情報を取得することができます。
例えば、通貨ペア "USDJPY" のポイントサイズや桁数を知らべるには次のようにします。

{{< code lang="cpp" title="CSymbolInfo クラスで USDJPY のポイントサイズを調べる" >}}
#include <Trade\SymbolInfo.mqh>

void OnStart() {
    CSymbolInfo sym;
    if (!sym.Name("USDJPY")) {  // 扱う通貨を指定
        Alert(StringFormat("Symbol name [%s] is invalid", sym.Name()));
        return;
    }

    MessageBox(StringFormat(
        "Symbol=%s, Point=%f, Digits=%d",
        sym.Name(), sym.Point(), sym.Digits()
    ));
}
{{< /code >}}

### SymbolInfoXXX 関数をつかう方法

シンボル情報は、[SymbolInfoDouble 関数](https://www.mql5.com/en/docs/marketinformation/symbolinfodouble) や [SymbolInfoInteger 関数](https://www.mql5.com/en/docs/marketinformation/symbolinfointeger) で取得することもできます。
こちらは、毎回対象のシンボル名を指定する必要があります。
1 つのシンボルからいろいろな情報を取得したい場合は、`CSymbolInfo` クラスを使った方がコードがすっきりします。

{{< code lang="cpp" title="SymbolInfoXXX 関数で USDJPY のポイントサイズを調べる" >}}
void OnStart() {
    const string symbol = "USDJPY";
    double point = SymbolInfoDouble(symbol, SYMBOL_POINT);
    long digits = SymbolInfoInteger(symbol, SYMBOL_DIGITS);
    if (digits == 0) {
        Alert(StringFormat("%s の情報を取得できません", symbol));
        return;
    }

    MessageBox(StringFormat("Symbol=%s, Point=%f, Digits=%d", symbol, point, digits));
}
{{< /code >}}

`SymbolInfoDouble(Symbol(), SYMBOL_POINT)` とした場合は、`Point()` と同じ意味になります。
不正なシンボル名などを指定して情報が取れない場合は、`SymbolInfoInteger` が 0 を返すことを利用してある程度のエラー処理を行えますが、ちゃんとエラー処理を行いたい場合は、3 つの引数を取るバージョンの `SymbolInfoDouble/Integer` 関数を使用します。

{{< code lang="cpp" >}}
void OnStart() {
    const string symbol = "USDJPY";
    double point;
    long digits;

    bool isOk = SymbolInfoDouble(symbol, SYMBOL_POINT, point);
    isOk &= SymbolInfoInteger(symbol, SYMBOL_DIGITS, digits);
    if (!isOk) {
        Alert(StringFormat("%s の情報を取得できません", symbol));
        return;
    }

    MessageBox(StringFormat("Symbol=%s, Point=%f, Digits=%d", symbol, point, digits));
}
{{< /code >}}

### MarketInfo 関数をつかう方法（MT4 のみ）

MQL4 では次のように `MarketInfo` 関数を使っても同様にポイントサイズを取得することができますが、MQL4/5 共通で `SymbolInfoDouble` 関数が使えるので、そちらを使っておけばよいでしょう。

{{< code lang="cpp" title="MarketInfo を使う方法 (MT4)" >}}
void OnStart() {
    const string symbol = "USDJPY";
    double point = MarketInfo(symbol, MODE_POINT);
    MessageBox(StringFormat("%s のポイントサイズは %f です", symbol, point));
}
{{< /code >}}

