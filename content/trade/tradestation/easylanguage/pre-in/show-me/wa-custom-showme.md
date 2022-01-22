---
title: "TradeStation/ショウミー/WA-Custom ShowMe（カスタムショウミー）"
url: "/p/fifwwmv"
linkTitle: "カスタムショウミー"
description: "カスタムショウミー (WA-Custom ShowMe) は、利用者が設定した条件式に合致した場合に描画します。"
ts-use: ["C", "R"]
---

{{< code title="WA-Custom ShowMe" >}}
{ Search Tag: WA-Custom ShowMe }

inputs:
    Criteria( High < High[1] and Low > Low[1] ) [DisplayName = "Criteria", ToolTip =
     "Enter the criteria to be evaluated on each bar.  The expression must evaluate to true or false."],
    PlotPrice( Close ) [DisplayName = "PlotPrice", ToolTip =
     "Enter the price at which the ShowMe marker is to be plotted."],
    AlertMessage( "" ) [DisplayName = "AlertMessage", ToolTip =
     "Enter the text to be displayed when the expression in the Criteria input evaluates to true."] ;

if Criteria then
    begin
    Plot1( PlotPrice, !( "CustomSM" ) ) ;
    Alert( AlertMessage ) ;
    end
else
    NoPlot( 1 ) ; { remove the marker if Criteria is no longer true, intrabar }
{{< /code >}}

{{< ts-copyright >}}

