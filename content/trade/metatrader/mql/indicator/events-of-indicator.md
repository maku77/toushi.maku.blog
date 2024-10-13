---
title: "MetaTrader/MQL: カスタムインジケーターで使用できるイベント"
linkTitle: "カスタムインジケーターで使用できるイベント"
url: "p/ugs5fq2/"
date: "2015-06-10"
tags: ["MetaTrader/MQL"]
weight: 100
---

{{% private %}}
- [Event Handling Functions - MQL5 Reference](https://www.mql5.com/en/docs/basis/function/events)
{{% /private %}}

カスタムインジケーターのプログラム内で、決まったシグネチャ（関数名やパラメーター構成）で関数を定義しておくと、特定のイベント発生時に自動的にその関数を呼び出してくれるようになります。

- （参考）[アプリの種類ごとに扱えるイベントハンドラーの一覧](/p/um6bbep/)
- （参考）[EA で使用できるイベント](/p/aamwkiu/)
- （参考）[スクリプトで使用できるイベント](/p/fvh3d6r/)

カスタムインジケーターでは次のようなイベントハンドラーを定義することができます。


OnInit 関数
----

```cpp
int OnInit(void);
```

インジケーターの [OnInit()](https://www.mql5.com/en/docs/event_handlers/oninit) 関数は、__Init__ イベントが発生したときに呼び出されます。
Init イベントは次のようなタイミングで発生します。

- インジケーターが最初にチャートにアタッチされたとき
- チャートのシンボル（`USDJPY` など）やタイムフレーム（時間足）が変更されたとき
- MetaEditor 上でインジケーターが再コンパイルされたとき
- インジケーターの入力パラメータがダイアログから変更されたとき

このハンドラー関数内では、描画用バッファーの初期化などを行います。
戻り値が `void` のバージョンもありますが、互換性のために残されているだけなので、`int` を返すバージョンを使ってください。


OnDeinit 関数
----

```cpp
void OnDeinit(const int reason);
```

インジケーターの [`OnDeinit`](https://www.mql5.com/en/docs/event_handlers/ondeinit) 関数は、次のようなタイミングで呼び出されます（参考: [Uninitialization Reason Codes](https://www.mql5.com/en/docs/constants/namedconstants/uninit)）。
パラメータ部分の `const` を省略して `int reason` と記述したりすると、ちゃんと呼び出されないので注意してください。

| 説明 | 定数 |
|---|---|
| チャートからインジケーターをデタッチしたとき | `REASON_REMOVE (1)` |
| MetaEditor 上でインジケーターが再コンパイルされたとき | `REASON_RECOMPILE (2)` |
| チャートのシンボル（`USDJPY` など）やタイムフレーム（時間足）が変更されたとき | `REASON_CHARTCHANGE (3)` |
| チャートを閉じたとき | `REASON_CHARTCLOSE (4)` |
| インジケーターの入力パラメータがダイアログから変更されたとき | `REASON_PARAMETERS (5)` |
| 別のアカウントで接続されたとき | `REASON_ACCOUNT (6)` |
| テンプレートが適用されて、インジケーターが設定されたチャートが開くとき | `REASON_TEMPLATE (7)` |
| `OnInit()` 処理が失敗して `0` 以外の値を返したとき | `REASON_INITFAILED (8)` |
| ターミナル (MetaTrader) を閉じたとき | `REASON_CLOSE (9)` |


OnCalculate 関数
----

```cpp
int  OnCalculate(
   const int rates_total,      // price[] array size
   const int prev_calculated,  // number of handled bars at the previous call
   const int begin,            // index number in the price[] array meaningful data starts from
   const double& price[]       // array of values for calculation
);

int OnCalculate(
    const int rates_total,      // size of input time series
    const int prev_calculated,  // bars handled in previous call
    const datetime& time[],     // Time
    const double& open[],       // Open
    const double& high[],       // High
    const double& low[],        // Low
    const double& close[],      // Close
    const long& tick_volume[],  // Tick Volume
    const long& volume[],       // Real Volume
    const int& spread[]         // Spread
);
```

インジケーターの [OnCalculate()](https://www.mql5.com/en/docs/event_handlers/oncalculate) 関数は、__Calculate__ イベントが発生したとき（最新の価格が変化したとき）に呼び出されます。
インジケーターを最初にチャートにアタッチしたときにも呼び出されます。


OnTimer 関数
----

```cpp
void OnTimer(void);
```

インジケーターの [`OnTimer()`](https://www.mql5.com/en/docs/event_handlers/ontimer) 関数は、__Timer__ イベントが発生したときに呼び出されます。
[`EventSetTimer()`](https://www.mql5.com/en/docs/eventfunctions/eventsettimer) 関数でセットした秒数ごとに Timer イベントが発生します。タイマーのセットは、通常 `OnInit()` 関数で行います。


OnChartEvent 関数
----

```cpp
void OnChartEvent()
    const int id,          // event ID
    const long& lparam,    // long type event parameter
    const double& dparam,  // double type event parameter
    const string& sparam   // string type event parameter
);
```

インジケーターの [`OnChartEvent()`](https://www.mql5.com/en/docs/event_handlers/onchartevent) 関数は、__ChartEvent__ イベントが発生したときに呼び出されます。
[`EventChartCustom()`](https://www.mql5.com/en/docs/eventfunctions/eventchartcustom) 関数を使うと、独自の ChartEvent イベントを発生させることができます。


OnBookEvent 関数
----

```cpp
void OnBookEvent(const string& symbol);
```

インジケーターの [`OnBookEvent()`](https://www.mql5.com/en/docs/event_handlers/onbookevent) 関数は、__BookEvent__ イベントが発生したときに呼び出されます。


（おまけ）インジケーターのイベントをすべて表示するインジケーター
----

- https://github.com/maku77/metatrader/blob/main/MQL5/Indicators/maku77/IndicatorEvents.mq5

