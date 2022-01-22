---
title: "TradeStation/インジケーター/モメンタム (WA-Momentum)"
linkTitle: "モメンタム (WA-Momentum)"
url: "/p/rbnx8hr"
date: "2020-04-12"
tags: ["トレステ", "インジケーター"]
description: "モメンタム (WA-Momentum) は、N バー遡ったモメンタムを描画します。"
---

{{< code title="WA-Momentum" >}}
{ Search Tag: WA-Momentum }

inputs:
    Price( Close ) [DisplayName = "Price", ToolTip = 
     "Enter an EasyLanguage expression to use in the momentum calculation."],
    Length( 12 ) [DisplayName = "Length", ToolTip = 
     "Enter number of bars over which to calculate momentum."],
    ColorNormLength( 14 ) [DisplayName = "ColorNormLength", ToolTip = 
     "Color Normalization Length.  Enter the number of bars over which to determine high and low values of the indicator for use in creating gradient colors."],
    UseGradientColoring( true ) [DisplayName = "UseGradientColoring", ToolTip = 
     "Enter true for gradient (blended) coloring;  enter false for no gradient coloring."],
    UpColor( Yellow ) [DisplayName = "UpColor", ToolTip = 
     "Enter the color to use for indicator values that are relatively high over ColorNormLength bars."],
    DnColor( Red ) [DisplayName = "DnColor", ToolTip = 
     "Down Color.  Enter the color to use for indicator values that are relatively low over ColorNormLength bars."],
    GridForegroundColor( Black ) [DisplayName = "GridForegroundColor", ToolTip = 
     "Enter the plot color to be used in RadarScreen.  Select a color that will contrast with both UpColor and DnColor.  "];

variables:
    intrabarpersist InAChart( false ),
    Mom( 0 ),
    Accel( 0 ),
    ColorLevel( 0 );

once
begin
    InAChart = GetAppInfo( aiApplicationType ) = cChart;
end;

Mom = Momentum( Price, Length );
Accel = Momentum( Mom, 1 ); { 1 bar acceleration }

Plot1( Mom, !( "Momentum" ) );
Plot2( 0, !( "ZeroLine" ) );

{ gradient coloring }
if UseGradientColoring then
begin
    ColorLevel = NormGradientColor( Mom, true, ColorNormLength, UpColor, DnColor );

    if InAChart then { study is applied to a chart }
    begin
        SetPlotColor( 1, ColorLevel );
    end
    else { study is applied to grid app }
    begin
        SetPlotColor( 1, GridForegroundColor );
        SetPlotBGColor( 1, ColorLevel );
    end;
end;

{ alert criteria }
if AlertEnabled then
begin
    if Mom > 0 and Accel > 0 then
        Alert( !( "Indicator positive and increasing" ) )
    else if Mom < 0 and Accel < 0 then
        Alert( !( "Indicator negative and decreasing" ) );
end;
{{< /code >}}

{{< ts-copyright >}}

- 参考: [トレステ/関数/Momentum 関数 - 現在の足のモメンタムを求める](/p/xrap6ky)

