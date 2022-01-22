---
title: "TradeStation/ショウミー/WA-New High for Year（1年間基準の高値更新）"
url: "/p/feg7f8k"
linkTitle: "1年間基準の高値更新"
description: "1年間基準の高値更新 (WA-New High for Year) は、1年間の中での高値更新を描画します。"
ts-use: ["C"]
---

{{< code title="WA-New High for Year" >}}
{ Search Tag: WA-New High for Year }

variables:
    HighestHi( 0 ) ;

{ tick, second, minute, daily, weekly or monthly bars }
if BarType < 5 or BarType = 14 then
    begin
    if Year( Date ) <> Year( Date[1] ) then
        HighestHi = High
    else if High > HighestHi then
        begin
        Plot1( High, !( "NewHi-Y" ) ) ;
        Alert ;
        HighestHi = High ;
        end ;
    end ;
{{< /code >}}

{{< ts-copyright >}}

