---
title: "EasyLanguage のストラテジーサンプル「移動平均のGC/DCによる売買」"
linkTitle: "ストラテジーサンプル「移動平均のGC/DCによる売買」"
url: "/p/5vds8n2"
date: "2020-01-20"
tags: ["トレステ", "EasyLanguage"]
---

2 本の移動平均線がクロスするタイミングで売買を行うストラテジです。
TradeStation には標準で付属しているストラテジとして、「単純移動平均2本クロス買いエントリー (ストラテジー)」がありますが、ここでは自力で実装する場合のサンプルとして示します。


ストラテジ概要
----

### エントリタイミング

- 買いエントリ (Buy) の条件
    - 短期移動平均線が長期移動平均線をゴールデンクロス (GC)
- 売りエントリ (SellShort) の条件
    - 短期移動平均線が長期移動平均線をデッドクロス (DC)

### パラメータ

- `fastLen`: 短期移動平均の足数
- `slowLen`: 長期移動平均の足数


ソースコード
----

{{< code >}}
input: fastLen(5), slowLen(25);
var: fastAvg(0), slowAvg(0);

fastAvg = AverageFC(Close, fastLen);
slowAvg = AverageFC(Close, slowLen);

if fastAvg crosses over slowAvg then begin
    Buy next bar at market;
end;

if fastAvg crosses under slowAvg then begin
    SellShort next bar at market;
end;
{{< /code >}}

