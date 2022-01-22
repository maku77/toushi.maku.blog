---
title: "MetaTrader/MQL: チャートの足（バー）の数を取得する (Bars)"
linkTitle: "チャートの足（バー）の数を取得する (Bars)"
url: "/p/6nw7gpx"
date: "2015-06-10"
lastmod: "2021-02-12"
tags: ["MetaTrader/MQL"]
---

[Bars 関数](https://www.mql5.com/en/docs/series/bars)を使用すると、指定したシンボル、時間足のローソク足の数を調べることができます。

{{< code lang="cpp" >}}
int Bars(string symbol, ENUM_TIMEFRAMES timeframe)
{{< /code >}}

{{< code lang="cpp" title="使用例" >}}
int bars = Bars("USDJPY", PERIOD_MN1));  // 157
int bars = Bars("USDJPY", PERIOD_D1));   // 2142
int bars = Bars("USDJPY", PERIOD_H1));   // 2098
int bars = Bars("USDJPY", PERIOD_M1));   // 32051
{{< /code >}}

下記のようにすると、現在のチャートのローソク足の数を取得することができます。

{{< code lang="cpp" >}}
int bars = Bars(_Symbol, _Period);
{{< /code >}}

カスタムインジケータの `OnCalculate` 関数の第一パラメータで渡される __`rates_total`__ には、上記で求められる値と同じ値が格納されています。

