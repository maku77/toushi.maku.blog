---
title: "TradeStation/ショウミー/WA-New Low for Year（1年間基準の安値更新）"
url: "/p/cj9pmsn"
linkTitle: "1年間基準の安値更新"
description: "1年間基準の安値更新 (WA-New Low for Year) は、1年間の中での安値更新を描画します。"
ts-use: ["C"]
---

{{< code title="WA-New Low for Year" >}}
{ Search Tag: WA-New Low for Year }

variables:
    LowestLo( 0 ) ;

{ tick, second, minute, daily, weekly or monthly bars }
if BarType < 5 or BarType = 14 then
    begin
    if Year( Date ) <> Year( Date[1] ) then
        LowestLo = Low
    else if Low < LowestLo then
        begin
        Plot1( Low, !( "NewLo-Y" ) ) ;
        Alert ;
        LowestLo = Low ;
        end ;
    end ;
{{< /code >}}

{{< ts-copyright >}}

