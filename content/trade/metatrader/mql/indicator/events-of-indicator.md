---
title: "MetaTrader/MQL: カスタムインジケーターで使用できるイベント"
linkTitle: "カスタムインジケーターで使用できるイベント"
url: "/p/ugs5fq2"
date: "2015-06-10"
tags: ["MetaTrader/MQL"]
weight: 100
---

カスタムインジケーターのプログラム内で、決まったシグネチャで関数を定義しておくと、特定のイベント発生時に自動的にその関数を呼び出してくれるようになります。


OnInit 関数
----

[int OnInit()](https://www.mql5.com/en/docs/basis/function/events#oninit)

- インジケーターが最初にチャートにアタッチされたとき
- チャートのシンボル（USDJPY など）やタイムフレーム（時間足）が変更されたとき
- MetaEditor 上でインジケーターが再コンパイルされたとき
- インジケーターの入力パラメータがダイアログから変更されたとき


OnDeinit 関数
----

[void OnDeinit(const int reason)](https://www.mql5.com/en/docs/basis/function/events#ondeinit)

- チャートからインジケーターをデタッチしたとき (REASON_REMOVE (1))
- MetaEditor 上でインジケーターが再コンパイルされたとき (REASON_RECOMPILE (2))
- チャートのシンボル（USDJPY など）やタイムフレーム（時間足）が変更されたとき (REASON_CHARTCHANGE (3))
- チャートを閉じたとき (REASON_CHARTCLOSE (4))
- インジケーターの入力パラメータがダイアログから変更されたとき (REASON_PARAMETERS (5))
- OnInit() が 0 以外の値を返して失敗したとき (REASON_INITFAILED (8))
- MetaTrader（ターミナル）を閉じたとき (REASON_CLOSE (9))

パラメータの `reason` にどのような値が渡されるかは、下記にまとめられています。

- [Uninitialization Reason Codes](https://www.mql5.com/en/docs/constants/namedconstants/uninit)

パラメータの `const` を省略して `int reason` と記述したりすると、ちゃんと呼び出されないので注意してください。


OnCalculate 関数
----

[void OnCalculate(...)](https://www.mql5.com/en/docs/basis/function/events#oncalculate)

`OnCalculate()` は Tick ごと（最新の価格が変化するごと）に呼び出されます。
インジケーターを最初にチャートにアタッチしたときにも呼び出されます。

