---
title: "TradeStation/ショウミー/WA-New High for Week（1週間基準の高値更新）"
url: "/p/v54vmgz"
linkTitle: "1週間基準の高値更新"
description: "1週間基準の高値更新 (WA-New High for Week) は、1週間の中での高値更新を描画します。"
ts-use: ["C"]
---

{{< code title="WA-New High for Week" >}}
{ Search Tag: WA-New High for Week }

variables:
    HighestHi( 0 ) ;

if BarType < 3 or BarType = 14 then { if tick, second, minute or daily bars }
    begin
    if DayOfWeek( Date ) < DayOfWeek( Date[1] ) then
        HighestHi = High
    else if High > HighestHi then
        begin
        Plot1( High, !( "NewHi-W" ) ) ;
        Alert ;
        HighestHi = High ;
        end ;
    end ;
{{< /code >}}

{{< ts-copyright >}}

