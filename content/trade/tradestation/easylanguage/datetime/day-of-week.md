---
title: "EasyLanguage: 指定した日付の曜日を調べる (DayOfWeek)"
linkTitle: "指定した日付の曜日を調べる (DayOfWeek)"
url: "/p/6pybku5"
date: "2020-05-06"
tags: ["EasyLanguage"]
---

DayOfWeek の概要
----

{{< code >}}
DayOfWeek(cDate);
{{< /code >}}

__`DayOfWeek`__ は指定した日付の曜日を返します（`0` (Sunday) 〜 `6` (Saturday)）。
不正な日付が指定された場合は、`-1` を返します。

パラメータ `cDate` には、年月日を表す `YYYMMDD` 形式の整数値 (`ELDate`) を指定します。
`YYY` は年から 1900 を引いた値で、例えば2020年10月5日であれば、引数として `1201005` という値を渡します。
指定できる値の範囲は、`0` 〜 `2501231`（1899年12月31日 〜 2150年12月31日）のようです。

戻り値は 0（日曜日）〜 6（土曜日）の整数値ですが、これらの数字は下記のような予約語で定義されています。
戻り値を使って条件分岐するときは、これらの予約後を使って値を比較すると分かりやすいコードになります。

- `Sunday` = 0
- `Monday` = 1
- `Tuesday` = 2
- `Wednesday` = 3
- `Thursday` = 4
- `Friday` = 5
- `Saturday` = 6


DayOfWeek の使用例
----

`DayOfWeek` の引数は、下記のような感じで指定します。

- `DayOfWeek(Date)` ... 現在の足の曜日
- `DayOfWeek(CurrentDate)` ... 本日の曜日
- `DayOfWeek(1200507)` ... 2020年5月7日の曜日 → 4 (Thursday)

次のコードは、現在処理中のローソク足が月曜日かどうかを調べています。

{{< code >}}
if DayOfWeek(Date) = Monday then begin
     // 月曜日の場合の処理
end;
{{< /code >}}

