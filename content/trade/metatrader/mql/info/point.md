---
title: "MetaTrader/MQL: 現在の通貨／シンボルのポイントサイズを調べる (Point, SymbolInfoDouble)"
linkTitle: "現在の通貨／シンボルのポイントサイズを調べる (Point, SymbolInfoDouble)"
url: "/p/gkcxsb2"
date: "2020-11-08"
tags: ["MetaTrader/MQL"]
---

[OrderSend などで注文を出す](/p/bw6tgck) 場合、最大許容スリッページなどをポイント数で指定する必要があります。
1 ポイントが実際の決済通貨でいくらかを示すものが、__ポイントサイズ__ です。
ポイントサイズが 0.001 であれば、1 ポイントが決済通貨で 0.001 の価格であることを示しています。

例えば、USDJPY でポイントサイズが 0.001 であれば、__1ポイント ＝ 0.001円__ です。
EURUSD でポイントサイズが 0.00001 であれば、__1ポイント ＝ 0.00001ドル__ です。


カレントチャートの通貨のポイントサイズを取得する (Point)
----

カレントチャートで表示している通貨のポイントサイズを調べるには、[Point 関数](https://www.mql5.com/en/docs/check/point) を使用します。

{{< code lang="cpp" title="Scripts/ShowPointSize.mq4" >}}
#property strict

void OnStart() {
  string symbol = Symbol();
  double point = Point();

  MessageBox(StringFormat("%s のポイントサイズは %f です", symbol, point));
}
{{< /code >}}

上記のスクリプトを実行すると、次のように表示されます。

{{< code >}}
USDJPY のポイントサイズは 0.001000 です
{{< /code >}}


指定した通貨のポイントサイズを取得する (SymbolInfoDouble)
----

カレントチャートの通貨に関係なく、指定した通貨ペアのポイントサイズを調べるには、[SymbolInfoDouble 関数](https://www.mql5.com/en/docs/marketinformation/symbolinfodouble) の引数に [SYMBOL_POINT](https://www.mql5.com/en/docs/constants/environment_state/marketinfoconstants#enum_symbol_info_double) を指定して呼び出します。

{{< code lang="cpp" title="SymbolInfoDouble を使う方法" >}}
void OnStart() {
    const string symbol = "USDJPY";
    double point = SymbolInfoDouble(symbol, SYMBOL_POINT);
    MessageBox(StringFormat("%s のポイントサイズは %f です", symbol, point));
}
{{< /code >}}

`SymbolInfoDouble(Symbol(), SYMBOL_POINT)` とすれば、`Point()` と同じ値を取得できます。
3 引数バージョンの `SymbolInfoDouble` 関数を使用すれば、呼び出しに成功したかどうかを戻り値で判断できます。
シンボル名の間違いなどをケアするときは、こちらのバージョンを使用します。

{{< code lang="cpp" >}}
void OnStart() {
    const string symbol = "USDJPY";
    double point;
    if (SymbolInfoDouble(symbol, SYMBOL_POINT, point)) {
        MessageBox(StringFormat("%s のポイントサイズは %f です", symbol, point));
    } else {
        MessageBox(StringFormat("%s のポイントサイズを取得できません", symbol))
    }
}
{{< /code >}}

ちなみに、MQL4 では次のように `MarketInfo` 関数を使っても同様にポイントサイズを取得することができますが、MQL4/5 共通で `SymbolInfoDouble` 関数が使えるので、そちらを使っておけばよいでしょう。

{{< code lang="cpp" title="MarketInfo を使う方法" >}}
void OnStart() {
    const string symbol = "USDJPY";
    double point = MarketInfo(symbol, MODE_POINT);
    MessageBox(StringFormat("%s のポイントサイズは %f です", symbol, point));
}
{{< /code >}}

