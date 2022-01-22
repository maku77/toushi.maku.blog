---
title: "TradeStation/ショウミー/WA-New Low for Week（1週間基準の安値更新）"
url: "/p/oim95k9"
linkTitle: "1週間基準の安値更新"
description: "1週間基準の安値更新 (WA-New Low for Week) は、1週間の中での安値更新を描画します。"
ts-use: ["C"]
---

{{< code title="WA-New Low for Week" >}}
{ Search Tag: WA-New Low for Week }

variables:
    LowestLo( 0 ) ;

if BarType < 3 or BarType = 14 then { tick, second, minute or daily bars }
    begin
    if DayOfWeek( Date ) < DayOfWeek( Date[1] ) then
        LowestLo = Low
    else if Low < LowestLo then
        begin
        Plot1( Low, !( "NewLo-W" ) ) ;
        Alert ;
        LowestLo = Low ;
        end ;
    end ;
{{< /code >}}

{{< ts-copyright >}}

