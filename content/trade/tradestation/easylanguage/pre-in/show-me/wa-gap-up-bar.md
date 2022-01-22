---
title: "TradeStation/ショウミー/WA-Gap Up Bar（ギャップアップ足）"
url: "/p/s2utkg9"
linkTitle: "ギャップアップ足"
description: "ギャップアップ足 (WA-Gap Up Bar) は、安値が一つ前の高値よりも高い場合に描画します。"
ts-use: ["C", "R"]
---

{{< code title="WA-Gap Up Bar" >}}
{ Search Tag: WA-Gap Up Bar }

if Low > High[1] then
    begin
    Plot1( High, !( "GapUp" ) ) ;
    Alert ;
    end
else
    NoPlot( 1 ) ; { remove the marker }
{{< /code >}}

{{< ts-copyright >}}

