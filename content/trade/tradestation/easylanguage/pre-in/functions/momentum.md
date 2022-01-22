---
title: "トレステ/関数/Momentum 関数 - 現在の足のモメンタムを求める"
linkTitle: "Momentum 関数 - 現在の足のモメンタムを求める"
url: "/p/xrap6ky"
date: "2020-04-13"
tags: ["トレステ"]
---

Momentum 関数の使い方
----

`Momentum` 関数は、現在の足のモメンタム（n 本前の足との価格差）を返します。
第1引数に使用する価格の種類 (OHLC)、第2引数に何本前の足と比べるかを指定します。

{{< code title="14 本前の終値との差分を求める" >}}
Value1 = Momentum(Close, 14);
{{< /code >}}

`Momentum` 関数は単純に価格差を返しますが、比率（パーセンテージ）で求めるには次のように __`RateOfChange`__ 関数を使用します。
`RateOfChange` が返す値は、価格に変化がないときは 0、価格が 50％ 上がっているときは 50 になります。

{{< code title="14 本前の終値からの変化率（騰落率％）を求める" >}}
Value1 = RateOfChange(Close, 14);
{{< /code >}}



Momentum 関数の実装
----

`Momentum` 関数の実装はとてもシンプルです。

{{< code title="Momentum 関数の実装" >}}
inputs: Price(numericseries), Length(numericsimple);

Momentum = Price - Price[Length];
{{< /code >}}

`RateOfChange` 関数の実装は次のようになっています。

{{< code title="RateOfChange 関数の実装" >}}
inputs: Price(numericseries), Length(numericsimple) ;

if Price[Length] <> 0 then
    RateOfChange = (Price / Price[Length] - 1) * 100
else
    RateOfChange = 0;
{{< /code >}}

