---
title: "TradeStation/インジケーター/移動平均線1本 (WA-Mov Avg 1 Line)"
linkTitle: "移動平均線1本 (WA-Mov Avg 1 Line)"
url: "/p/kkipwgp"
date: "2019-04-12"
tags: ["トレステ", "インジケーター"]
description: "移動平均線1本 (Mov Avg 1 Line) は、1本の移動平均線を描画します。"
ts-use: ["C", "R", "A"]
---

{{< code title="WA-Mov Avg 1 Line" >}}
{ Search Tag: WA-Mov Avg 1 Line }

inputs:
    Price( Close ) [DisplayName = "Price", ToolTip =
     "Enter an EasyLanguage expression to use in the moving average calculation."],
    Length( 9 ) [DisplayName = "Length", ToolTip =
     "Enter number of bars over which to calculate the simple moving average."],
    Displace( 0 ) [DisplayName = "Displace", ToolTip =
     "Displacement.  Enter the number of bars by which plots will be displaced.  Displacement may be positive (left) or negative (right)."] ;

variables:
    Avg( 0 ) ;

Avg = AverageFC( Price, Length ) ;

if Displace >= 0 or CurrentBar > AbsValue( Displace ) then
    begin
    Plot1[Displace]( Avg, !( "Avg" ) ) ;

    { alert criteria }
    if AlertEnabled and Displace <= 0 then
        begin
        if Price crosses over Avg then
            Alert( !( "Price crossing over average" ) )
        else if Price crosses under Avg then
            Alert( !( "Price crossing under average" ) ) ;
        end ;
    end ;
{{< /code >}}

{{< ts-copyright >}}

