---
title: "TradeStation/ショウミー/WA-New High for Month（1ヶ月基準の高値更新）"
url: "/p/g5cf6h5"
linkTitle: "1ヶ月基準の高値更新"
description: "1ヶ月基準の高値更新 (WA-New High for Month) は、1ヶ月の中での高値更新を描画します。"
ts-use: ["C"]
---

{{< code title="WA-New High for Month" >}}
{ Search Tag: WA-New High for Month }

variables:
    HighestHi( 0 ) ;

{ if tick, second, minute, daily or weekly bars }
if BarType < 4 or BarType = 14 then
    begin
    if Month( Date ) <> Month( Date[1] ) then
        HighestHi = High
    else if High > HighestHi then
        begin
        Plot1( High, !( "NewHi-M" ) ) ;
        Alert ;
        HighestHi = High ;
        end ;
    end ;
{{< /code >}}

{{< ts-copyright >}}

