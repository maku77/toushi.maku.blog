---
title: "TradeStation/ショウミー/WA-Inside Bar（インサイドバー）"
url: "/p/bgcy4nq"
linkTitle: "インサイドバー"
description: "インサイドバー (WA-Inside Bar) は、高値と安値が 1 つ前のバーの高値と安値の範囲にすっぽりと収まるときに描画します。"
ts-use: ["C", "R"]
---

{{< code title="WA-Inside Bar" >}}
{ Search Tag: WA-Inside Bar }

{
This ShowMe study identifies bars that meet the following conditions:

    1. the PriceH of 1 bar ago is greater than the PriceH of the current bar,AND
    2. the PriceL of 1 bar ago is less than the PriceL of the current bar.

The NoPlot statement in the code is used to remove the ShowMe marker in the case
where the update intrabar setting is checked and the Inside Bar condition is no
longer true.
}

inputs:
    double PriceH( High ) [DisplayName = "PriceH", ToolTip =
     "Price High.  Enter an EasyLanguage expression.  The value of this expression will be used to determine whether the high criteria for an inside bar is met."],
    double PriceL( Low ) [DisplayName = "PriceL", ToolTip =
     "Price Low.  Enter an EasyLanguage expression.  The value of this expression will be used to determine whether the low criteria for an inside bar is met."],
    double PlotPrice( Close ) [DisplayName = "PlotPrice", ToolTip =
     "Enter the value at which the ShowMe marker is to be plotted."] ;

if InsideBar( PriceH, PriceL ) then
    begin
    Plot1( PlotPrice, !( "Inside" ) ) ;
    Alert( !( "Inside Bar" ) ) ;
    end
else
    { if update intrabar is selected and the Inside Bar condition is no longer
      true, remove the marker }
    NoPlot( 1 ) ;
{{< /code >}}

{{< ts-copyright >}}

