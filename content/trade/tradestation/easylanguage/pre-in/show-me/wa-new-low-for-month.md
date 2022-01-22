---
title: "TradeStation/ショウミー/WA-New Low for Month（1ヶ月基準の安値更新）"
url: "/p/hv33tqx"
linkTitle: "1ヶ月基準の安値更新"
description: "1ヶ月基準の安値更新 (WA-New Low for Month) は、1ヶ月の中での安値更新を描画します。"
ts-use: ["C"]
---

{{< code title="WA-New Low for Month" >}}
{ Search Tag: WA-New Low for Month }

variables:
    LowestLo( 0 ) ;

{ tick, second, minute, daily or weekly bars }
if BarType < 4 or BarType = 14 then
    begin
    if Month( Date ) <> Month( Date[1] ) then
        LowestLo = Low
    else if Low < LowestLo then
        begin
        Plot1( Low, !( "NewLo-M" ) ) ;
        Alert ;
        LowestLo = Low ;
        end ;
    end ;
{{< /code >}}

{{< ts-copyright >}}

