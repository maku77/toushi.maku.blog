---
title: "TradeStation/ショウミー/WA-C_Harami Cross（はらみ寄せ線）"
url: "/p/rksopqr"
linkTitle: "はらみ寄せ線"
description: "はらみ寄せ線 (WA-C_Harami Cross) は、大陰線および大陽線のはらみ寄せを特定します。"
ts-use: ["C", "R"]
---

{{< code title="WA-C_Harami Cross" >}}
{ Search Tag: WA-C_Harami Cross }

{
Reference:  Gregory L. Morris, "CandlePower" (Probus Publishing Company, 1992)

This study identifies the bullish and bearish Harami Cross (harami yose sen)
candlestick patterns.
}

inputs:
    double Price( Close ) [DisplayName = "Price", ToolTip =
     "Enter an EasyLanguage expression.  This value is used to determine trend."],
    double TrendAvgLength( 14 ) [DisplayName = "TrendAvgLength", ToolTip =
     "Trend Average Length.  Enter the number of bars to use in the moving average that is used to determine trend."],
    double BodyAvgLength( 14 ) [DisplayName = "BodyAvgLength", ToolTip =
     "Body Average Length.  Enter the number of bars to use in the moving average that is used to determine average body size."],
    double DojiPercent( 5 ) [DisplayName = "DojiPercent", ToolTip =
     "Doji Percent.  Enter the maximum percentage of the bar's range that the body may be."],
    double BearishPlotPrice( Low ) [DisplayName = "BearishPlotPrice", ToolTip =
     "Enter the price at which to plot a dot when a bearish harami cross pattern is found."],
    double BullishPlotPrice( High ) [DisplayName = "BullishPlotPrice", ToolTip =
     "Enter the price at which to plot a dot when a bullish harami cross pattern is found."],
    bool ColorCellBGOnAlert( true ) [DisplayName = "ColorCellBGOnAlert", ToolTip =
     "Color Cell Background On Alert.  Enter true to color RadarScreen cell background when alert occurs;  enter false to not color cell background."],
    int BackgroundColorAlertCell( DarkGray )
     [DisplayName = "BackgroundColorAlertCell", ToolTip =
     "Enter the color to use for RadarScreen cell background when alert occurs."] ;

variables:
    intrabarpersist bool InAChart( false ),
    int HaramiCrossValue( 0 ),
    intrabarpersist bool OkToCountTop( false ),
    intrabarpersist bool OkToCountBot( false ),
    { variable to hold the count of the number of bars ago that the most recent
      bearish Harami Cross candlestick pattern was detected }
    int NumBarsSinceBearish( 0 ),
    { variable to hold the count of the number of bars ago that the most recent
      bullish Harami Cross candlestick pattern was detected }
    int NumBarsSinceBullish( 0 ) ;

once
    begin
    InAChart = GetAppInfo( aiApplicationType ) = cChart ;
    end ;

HaramiCrossValue = C_HaramiCross( Price, TrendAvgLength, BodyAvgLength,
 DojiPercent ) ;

if HaramiCrossValue <> 0 then { Harami Cross pattern detected }
    begin

    if HaramiCrossValue = 1 then { bullish Harami Cross pattern }
        begin
        { once the pattern is detected, set OkToCountBot variable to true to start
          counting bars since the pattern was detected }
        once OkToCountBot = true ;
        { reset the counter that counts the number of bars since the most recent
          bullish Harami Cross pattern was detected }
        NumBarsSinceBullish = 0 ;
        if InAChart then { if not in a Chart, plots are created below }
            Plot1( BullishPlotPrice, !( "HCBull" ) ) ;
        if ColorCellBGOnAlert then
            SetPlotBGColor( 1, BackgroundColorAlertCell ) ;
        Alert( !( "Bullish Harami Cross pattern." ) ) ;
        end
    else if HaramiCrossValue = -1 then { bearish Harami Cross pattern }
        begin
        { once the pattern is detected, set OkToCountTop variable to true to start
          counting bars since the pattern was detected }
        once OkToCountTop = true ;
        { reset the counter that counts the number of bars since the most recent
          bearish Harami Cross pattern was detected }
        NumBarsSinceBearish = 0 ;
        if InAChart then { if not in a Chart, plots are created below }
            Plot2( BearishPlotPrice, !( "HCBear" ) ) ;
        if ColorCellBGOnAlert then
            SetPlotBGColor( 2, BackgroundColorAlertCell ) ;
        Alert( !( "Bearish Harami Cross pattern." ) ) ;
        end ;

    end
else { no Harami Cross pattern }
    begin
    if OkToCountTop then
        NumBarsSinceBearish += 1 ; { increment the count }
    if OkToCountBot then
        NumBarsSinceBullish += 1 ; { increment the count }
    end ;

if InAChart = false then { in grid application }
    begin
    if OkToCountBot then
        Plot1( NumBarsSinceBullish, !( "HCBull" ) ) ;
    if OkToCountTop then
        Plot2( NumBarsSinceBearish, !( "HCBear" ) ) ;
    end ;
{{< /code >}}

{{< ts-copyright >}}

