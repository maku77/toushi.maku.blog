---
title: "TradeStation/アクティビティバー/WA-Volume Distribution（ボリューム・ディストリビューション）"
url: "/p/c2qkjx3"
linkTitle: "ボリューム・ディストリビューション"
description: "ボリューム・ディストリビューション (WA-Volume Distribution) は、設定した出来高以上のバーに基づき、ボリュームディストリギューションを描画します。"
ts-use: ["C"]
---

{{< code title="WA-Volume Distribution" >}}
{ Search Tag: WA-Volume Distribution }

{
This study plots a modified ActivityBar, with each ActivityData bar being processed
either once or not at all depending on whether its volume is above or below the
specified BlockSize.  If BlockSize is set to zero, each ActivityData bar is
processed, resulting in the basic ActivityBar plot of the Price Distribution
ActivityBar study.
}

inputs:
	ApproxNumRows( 10 ) [DisplayName = "ApproxNumRows", ToolTip =
	 "Aprroximate Number of Rows.  Enter the approximate number of rows to use in the study."],
	CycleColors( true ) [DisplayName = "CycleColors", ToolTip =
	 "Enter true to cycle colors from one cell group to the next."],
	DefaultColor( DarkGreen ) [DisplayName = "DefaultColor", ToolTip =
	 "Enter the default color used in the ActivityBar study."],
	BlockSize( 100 ) [DisplayName = "BlockSize", ToolTip =
	 "Enter the volume increment for calibrating candlestick body width."] ;

variables:
	MinuteInterval( BarInterval of ActivityData ),
	CellGroupColor( 0 ),
	CellGroupLabel( "" ),
	AnyVol( 0 ) ;

AB_SetRowHeight( AB_RowHeightCalc( ApproxNumRows, 3 ) ) ;

if BarType of ActivityData >= 2 then { ie, not minute data }
	AnyVol = Volume of ActivityData
else { if minute data }
	AnyVol = Ticks of ActivityData ;

if CycleColors then
	CellGroupColor = AB_NextColor( MinuteInterval ) of ActivityData
else
	CellGroupColor = DefaultColor ;

if CellGroupColor = GetBackGroundColor then
	CellGroupColor = DefaultColor ;

CellGroupLabel = AB_NextLabel( MinuteInterval ) of ActivityData ;

if AnyVol >= BlockSize then
	Value1 = AB_AddCellRange( High of ActivityData, Low of ActivityData, RightSide,
	 CellGroupLabel, CellGroupColor, 0 ) ;
{{< /code >}}

{{< ts-copyright >}}
