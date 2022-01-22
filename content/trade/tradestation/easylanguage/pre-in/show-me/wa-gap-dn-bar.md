---
title: "TradeStation/ショウミー/WA-Gap Dn Bar（ギャップダウン足）"
url: "/p/9cpecds"
linkTitle: "ギャップダウン足"
description: "ギャップダウン足 (WA-Gap Dn Bar) は、高値が一つ前の安値よりも低い場合に描画します。"
ts-use: ["C", "R"]
---

{{< code title="WA-Gap Dn Bar" >}}
{ Search Tag: WA-Gap Dn Bar }

if High < Low[1] then
    begin
    Plot1( Low, !( "GapDn" ) ) ;
    Alert ;
    end
else
    NoPlot( 1 ) ; { remove the marker }
{{< /code >}}

{{< ts-copyright >}}

