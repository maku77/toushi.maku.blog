---
title: "テクニカル指標: ATR (Average True Range)"
linkTitle: "ATR (Average True Range)"
url: "/p/tasaq7n"
date: "2022-03-30"
tags: ["ATR", "テクニカル指標"]
description: "ATR は真の値幅 (TR: True Range) の平均値です。直近の価格がどのくらいの変動幅で推移しているかを調べるために使います。"
---

ATR の概要
----

{{< tech-info
    name="ATR"
    long-name="Average True Range"
    jp-name="アベレージ・トゥルー・レンジ"
    inventor="J・W・ワイルダー"
    year=""
>}}

ATR は、TR（True Range、真のレンジ）の平均をとったものです。
日足の場合、14 日間の平均値を用いることが多いようです。


計算方法
----

ATR は TR の平均値なので、TR を求めることができれば簡単に計算できます。
TR は以下のレンジの中の最大値です。
ひとことで言うと、通常の当日レンジを拡張して、前日の終値からの変化を考慮したものです。

- 当日の高値 〜 当日の安値（これは通常のレンジ）
- __前日の終値__ 〜 当日の高音
- __前日の終値__ 〜 当日の安値

{{< image src="img-001.svg" title="TR (True Range)" >}}

通常の当日レンジ (High - Low) の計算では、その日にストップ高になったとしても、朝から天井に張り付いていたら、レンジは 0 になってしまいます。
これはレンジとしておかしいということで、TR (True Range) という概念が生まれました。
TR であれば、前日の終値からの変化を表現できるので、夜間取引のない株式などが朝にギャップアップして寄り付いた場合に、大きな変化が起こったものとして捉えることができます。


おまけ
----

TradingView (Pine Script) で終値 ± ATR(10) の範囲を色付けするコードです。
ローソク足がこの範囲をはみ出しているということは、最近の平均的な変動幅 (ATR) よりも大きく動いたことを示しています。

{{< image w="400" src="img-002.png" title="Close ± ATR(10)" >}}

```
//@version=5
indicator("Example of ATR", overlay=true)
myAtr = ta.atr(10)
plot1 = plot(close + myAtr, offset=1)
plot2 = plot(close - myAtr, offset=1)
fill(plot1, plot2, color=#0033ff66)
```

1 バーだけ右シフトしてプロットしていることに注意してください。
シフトしないと、自分自身のバーが ATR の計算に反映されてしまいます。


関連指標
----

- [DMI（方向性指数）](/p/9ju3pvu)
  - 同じく、J・W・ワイルダー氏の考案。TR (True Range) の概念は DMI の計算過程でも出てきます。

