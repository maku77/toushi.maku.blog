---
title: "テクニカル指標: Elder Impulse System"
linkTitle: "Elder Impulse System"
url: "/p/yaeh8wr"
date: "2020-01-14"
tags: ["テクニカル指標"]
---

Elder Impulse System の概要
----

- トレンドの強さを分かりやすく表示してくれる
- {{< amazon-inline id="4939103285" title="投資苑" >}} の著者であるアレキサンダー・エルダーが開発
- 13 期間の EMA でトレンドの判断、MACD ヒストグラムでモメンタム（トレンドの強さ）を判断する
- 米国ではメジャーなインジケーター


Elder Impulse System のトレンド判断方法
----

- 緑色のバー（ブル相場: 強気トレンド）
    - EMA(13) ＞ 前区間のEMA(13) かつ MACDヒストグラム ＞ 前区間のMACDヒストグラム
    - 「買いエントリー」してもよい
- 赤色のバー（ベア相場: 弱気トレンド）
    - EMA(13) ＜ 前区間のEMA(13) かつ MACDヒストグラム ＜ 前区間のMACDヒストグラム
    - 「売りエントリー」してもよい
- 青色のバー（もみ合い）
    - 上記のいずれでもない場合（EMA と MACD の方向が逆）
    - 「様子見」

例えば、緑色のバーになるときに「買いエントリー」し、緑色以外のバーに変わったときに「手仕舞い」します。


参考
----

- [Elder Impulse System - MetaTrader 5のためのインディケーター - MQL5](https://www.mql5.com/ja/code/685)

