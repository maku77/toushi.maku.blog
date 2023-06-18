---
title: "MetaTrader/MQL: 時刻情報を扱う (datetime, TimeLocal, TimeCurrent, TimeToString)"
linkTitle: "時刻情報を扱う (datetime, TimeLocal, TimeCurrent, TimeToString)"
url: "p/mfee8vj/"
date: "2015-10-25"
lastmod: "2023-06-18"
changes:
  - 2023-06-18: 外部リンクを更新 (mql4 → mql5)
tags: ["MetaTrader/MQL"]
---

MQL では、日付や時刻の情報を [datetime 型](https://www.mql5.com/en/docs/basis/types/integer/datetime) の値として扱います。


ローカル PC 上の現在時刻 (TimeLocal)
----

ホスト PC 上の現在時刻は [TimeLocal 関数](https://www.mql5.com/en/docs/dateandtime/timelocal)を使って取得できます（`1970-01-01 00:00:00` からの経過秒数）。
取得した `datetime` 値を [TimeToString 関数](https://www.mql5.com/en/docs/convert/timetostring)に渡すと、文字列表現の時刻に変換することができます。

{{< code lang="cpp" title="ローカル PC 上の現在日時を取得する" >}}
datetime now = TimeLocal();

string s1 = TimeToString(now, TIME_DATE);     // 2015.10.23
string s2 = TimeToString(now, TIME_MINUTES);  // 21:00
string s3 = TimeToString(now, TIME_SECONDS);  // 21:00:00
string s4 = TimeToString(now, TIME_DATE | TIME_MINUTES);  // 2015.10.23 21:00
string s5 = TimeToString(now, TIME_DATE | TIME_SECONDS);  // 2015.10.23 21:00:00
{{< /code >}}


サーバ上の現在時刻 (TimeCurrent)
----

MetaTrader を実行しているホスト PC 上の現在時刻ではなく、ブローカーのサーバーから最後に取得した現在時刻 (time of the last quote receipt) を取得するには、[TimeCurrent 関数](https://www.mql5.com/en/docs/dateandtime/timecurrent)を使用します。
使い方は `TimeLocal` 関数と同様です。

{{< code lang="cpp" title="サーバー上の現在日時を取得する" >}}
datetime serverTime = TimeCurrent();

string s1 = TimeToString(now, TIME_DATE);     // 2015.10.23
// ...
{{< /code >}}

