---
title: "MetaTrader/MQL: チャートのタイムフレーム（H1 や M15）を取得する (Period, PeriodSeconds)"
linkTitle: "チャートのタイムフレーム（H1 や M15）を取得する (Period, PeriodSeconds)"
url: "/p/p7gpx7f"
date: "2016-03-21"
lastmod: "2021-02-12"
tags: ["MetaTrader/MQL"]
---

現在のタイムフレーム設定を取得する (Period)
----

カレントチャートのタイムフレーム（ローソク足 1 本あたりの時間）を調べるには、組み込みの [_Period 変数](https://www.mql5.com/ja/docs/predefined/_period) か [Period 関数](https://www.mql5.com/ja/docs/check/period) を使用します。

{{< code lang="cpp" >}}
ENUM_TIMEFRAMES timeframe = _Period;  // Period() でも同じ
{{< /code >}}

結果として、下記のような `ENUM_TIMEFRAMES` 型の値を得ることができます。

<table>
  <thead>
    <tr><th>値</th><th>意味</th><th>値</th><th>意味</th></tr>
  </thead>
  <tbody>
    <tr><th><code>PERIOD_M1</code></th><td>1 分</td><th><code>PERIOD_H1</code></th><td>1 時間</td></tr>
    <tr><th><code>PERIOD_M2</code></th><td>2 分</td><th><code>PERIOD_H2</code></th><td>2 時間</td></tr>
    <tr><th><code>PERIOD_M3</code></th><td>3 分</td><th><code>PERIOD_H3</code></th><td>3 時間</td></tr>
    <tr><th><code>PERIOD_M4</code></th><td>4 分</td><th><code>PERIOD_H4</code></th><td>4 時間</td></tr>
    <tr><th><code>PERIOD_M5</code></th><td>5 分</td><th><code>PERIOD_H6</code></th><td>6 時間</td></tr>
    <tr><th><code>PERIOD_M6</code></th><td>6 分</td><th><code>PERIOD_H8</code></th><td>8 時間</td></tr>
    <tr><th><code>PERIOD_M10</code></th><td>10 分</td><th><code>PERIOD_H12</code></th><td>12 時間</td></tr>
    <tr><th><code>PERIOD_M12</code></th><td>12 分</td><th><code>PERIOD_D1</code></th><td>1 日</td></tr>
    <tr><th><code>PERIOD_M15</code></th><td>15 分</td><th><code>PERIOD_W1</code></th><td>1 週間</td></tr>
    <tr><th><code>PERIOD_M20</code></th><td>20 分</td><th><code>PERIOD_MN1</code></th><td>1 カ月</td></tr>
    <tr><th><code>PERIOD_M30</code></th><td>30 分</td><th></th><td></td></tr>
  </tbody>
</table>


現在のタイムフレームの秒数を取得する (PeriodSeconds)
---

ローソク足 1 本あたりが、何秒であるかを取得するには、[PeriodSeconds 関数](https://www.mql5.com/ja/docs/common/periodseconds) を使用します。

引数を省略するか、`PERIOD_CURRENT` を指定すると、現在のチャートの足 1 本あたりの秒数を返します。
特定のタイムフレームの足 1 本あたりの秒数を調べたいときは、`ENUM_TIMEFRAMES` 型のいずれかの値を指定します。

{{< code lang="cpp" >}}
int seconds1 = PeriodSeconds();  // カレントチャートのタイムフレームの秒数
int seconds2 = PeriodSeconds(PERIOD_M1);  // 60
int seconds3 = PeriodSeconds(PERIOD_H1);  // 3600
{{< /code >}}


現在のタイムフレームのテキスト表現を取得する
----

`_Period`  で取得した `ENUM_TIMEFRAMES` 値を `EnumToString` 関数に渡すと、その enum 値の文字列表現を取得することができます。

{{< code lang="cpp" title="Scripts/Hello.mq5" >}}
void OnStart() {
    Print(EnumToString(_Period));  //=> "PERIOD_M30" など
}
{{< /code >}}

`PERIOD_M30` といった文字列ではなく、後ろの `M30` といった部分だけを取得したい場合は、次のように `StringSubstr` 関数を使って部分文字列を取得すればよいでしょう。

{{< code lang="cpp" title="Scripts/Hello.mq5" >}}
/**
 * ENUM_TIMEFRAMES 値に対応する "M30" や "H1" などの文字列を取得します。
 */
string TimeframeToStr(ENUM_TIMEFRAMES timeframe) {
    string s = EnumToString(timeframe);  // "PERIOD_XXX" のような文字列
    return StringSubstr(s, 7);  // "PERIOD_" 以降の部分文字列を取得する
}

void OnStart() {
    Print(TimeframeToStr(_Period));  // => "M30" など
}
{{< /code >}}

