---
title: "TradeStation/ショウミー/WA-C_BullHar_BearHar（はらみ線）"
url: "/p/qawfte2"
linkTitle: "はらみ線"
description: "はらみ線 (WA-C_BullHar_BearHar) は、ローソク足パターン「陰の陽はらみまたは陽の陰はらみ」を特定します。"
ts-use: ["C", "R"]
---

{{< code title="WA-C_BullHar_BearHar" >}}
{ Search Tag: WA-C_BullHar_BearHar }

{ Candlestick ShowMe }

inputs:
    Length( 14 ) [DisplayName = "Length", ToolTip =
     "Enter the number of bars to use in the moving averages used to determine trend and average body size."] ;

variables:
    ReturnValue( 0 ),
    oBullishHarami( 0 ),
    oBearishHarami( 0 ) ;

ReturnValue = C_BullHar_BearHar( Length, oBullishHarami, oBearishHarami ) ;

if oBullishHarami = 1 then
    begin
    Plot1( High, !( "BullHar" ) ) ;
    Alert( !( "BullishHarami" ) ) ;
    end
else if oBearishHarami = 1 then
    begin
    Plot2( Low, !( "BearHar" ) ) ;
    Alert( !( "BearishHarami" ) ) ;
    end ;
{{< /code >}}

{{< ts-copyright >}}

