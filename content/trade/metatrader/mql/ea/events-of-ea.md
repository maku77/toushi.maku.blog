---
title: "MetaTrader/MQL: EA で使用できるイベント"
linkTitle: "EA で使用できるイベント"
url: "p/aamwkiu/"
date: "2023-07-17"
tags: ["MetaTrader/MQL"]
---

{{% private %}}
- [Event Handling Functions - MQL5 Reference](https://www.mql5.com/en/docs/basis/function/events)
{{% /private %}}

EA（エキスパートアドバイザー）のプログラム内で、決まったシグネチャ（関数名やパラメーター構成）で関数を定義しておくと、特定のイベント発生時に自動的にその関数を呼び出してくれるようになります。

{{% reference %}}
- [アプリの種類ごとに扱えるイベントハンドラーの一覧](/p/um6bbep/)
- [カスタムインジケーターで使用できるイベント](/p/ugs5fq2/)
- [スクリプトで使用できるイベント](/p/fvh3d6r/)
{{% /reference %}}

EA では次のようなイベントハンドラーを定義することができます。


OnInit 関数
----

```cpp
int OnInit(void);
```

EA の [OnInit()](https://www.mql5.com/en/docs/event_handlers/oninit) 関数は、__Init__ イベントが発生したときに呼び出されます。
戻り値が `void` のバージョンもありますが、互換性のために残されているだけなので、`int` を返すバージョンを使ってください。


OnDeinit 関数
----

```cpp
void OnDeinit(const int reason);
```

EA の [`OnDeinit()`](https://www.mql5.com/en/docs/event_handlers/ondeinit) 関数は、__Deinit__ イベントが発生したときに呼び出されます。


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

EA の [OnCalculate()](https://www.mql5.com/en/docs/event_handlers/oncalculate) 関数は、__Calculate__ イベントが発生したとき（最新の価格が変化したとき）に呼び出されます。
EA を最初にチャートにアタッチしたときにも呼び出されます。


OnTimer 関数
----

```cpp
void OnTimer(void);
```

EA の [`OnTimer()`](https://www.mql5.com/en/docs/event_handlers/ontimer) 関数は、__Timer__ イベントが発生したときに呼び出されます。
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

EA の [`OnChartEvent()`](https://www.mql5.com/en/docs/event_handlers/onchartevent) 関数は、__ChartEvent__ イベントが発生したときに呼び出されます。
[`EventChartCustom()`](https://www.mql5.com/en/docs/eventfunctions/eventchartcustom) 関数を使うと、独自の ChartEvent イベントを発生させることができます。


OnBookEvent 関数
----

```cpp
void OnBookEvent(const string& symbol);
```

EA の [`OnBookEvent()`](https://www.mql5.com/en/docs/event_handlers/onbookevent) 関数は、__BookEvent__ イベントが発生したときに呼び出されます。


OnTick 関数
----

```cpp
void OnTick(void);
```

EA の [`OnTick()`](https://www.mql5.com/en/docs/event_handlers/ontick) 関数は、__NewTick__ イベントが発生したときに呼び出されます。
`OnTick()` は EA 専用のイベントハンドラです（インジケーターやスクリプトでは使用できません）。

NewTick イベントを `OnTick()` 関数で処理している最中に次の NewTick イベントが発生した場合、そのイベントはイベントキューに積まれないことに注意してください。
`OnTick()` 内の処理は短時間で終える必要があるため、`Sleep()` 関数や `MessageBox()` 関数の呼び出しは禁止されています。

EA による自動売買が許可されていない場合でも、`OnTick()` 関数は呼び出されます。


OnTrade 関数
----

```cpp
void OnTrade(void);
```

EA の [`OnTrade()`](https://www.mql5.com/en/docs/event_handlers/ontrade) 関数は、__Trade__ イベントが発生したときに呼び出されます。
`OnTrade()` は EA 専用のイベントハンドラです（インジケーターやスクリプトでは使用できません）。


OnTester 関数
----

```cpp
double OnTester(void);
```

EA の [`OnTester()`](https://www.mql5.com/en/docs/event_handlers/ontester) 関数は、__Tester__ イベントが発生したときに呼び出されます。
`OnTester()` は EA 専用のイベントハンドラです（インジケーターやスクリプトでは使用できません）。

