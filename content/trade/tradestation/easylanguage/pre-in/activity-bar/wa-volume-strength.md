---
title: "TradeStation/アクティビティバー/WA-Volume Strength（出来高強度）"
url: "/p/8eemvwj"
linkTitle: "出来高強度"
description: "出来高強度 (WA-Volume Strength) は、価格レベルごとの出来高比をセルの数で描画します。"
ts-use: ["C"]
---

{{< code title="WA-Volume Strength" >}}
{ Search Tag: WA-Volume Strength }

{
This study plots a modified ActivityBar, with each ActivityData bar being processed
0 or more times depending on its volume and the specified BlockSize divisor.  If
BlockSize is set to zero, each ActivityData bar is processed exactly once,
resulting in the basic ActivityBar plot of the Price Distribution ActivityBar
study.
}

inputs:
    ApproxNumRows( 10 ) [DisplayName = "ApproxNumRows", ToolTip =
     "Approximate Number of Rows.  Enter the approximate number of rows to use in the study."],
    CycleColors( true ) [DisplayName = "CycleColors", ToolTip =
     "Enter true to cycle colors from one cell group to the next."],
    DefaultColor( DarkGreen ) [DisplayName = "DefaultColor", ToolTip =
     "Enter the default color used in the ActivityBar study."],
    BlockSize( 100 ) [DisplayName = "BlockSize", ToolTip =
     "Enter the volume increment for calibrating candlestick body width."],
    MaxWeight( 5 ) [DisplayName = "MaxWeight", ToolTip =
     "Maximum Weight.  Enter the maximum number of times an ActivityData bar can be processed."];

variables:
    MinuteInterval( BarInterval of ActivityData ),
    CellGroupColor( 0 ),
    CellGroupLabel( "" ),
    RawWeight( 0 ),
    Weight( 0 ),
    AnyVol( 0 );

AB_SetRowHeight( AB_RowHeightCalc( ApproxNumRows, 3 ) );

if BarType of ActivityData >= 2 then { ie, not minute data }
    AnyVol = Volume of ActivityData
else { if minute data }
    AnyVol = Ticks of ActivityData;

if CycleColors then
    CellGroupColor = AB_NextColor( MinuteInterval ) of ActivityData
else
    CellGroupColor = DefaultColor;

if CellGroupColor = GetBackGroundColor then
    CellGroupColor = DefaultColor;

CellGroupLabel = AB_NextLabel( MinuteInterval ) of ActivityData;

if AnyVol >= BlockSize then
begin
    if BlockSize > 0 then
        RawWeight = IntPortion( AnyVol / BlockSize )
    else
        RawWeight = 1;

    Weight = MinList( RawWeight, MaxWeight );

    for Value1 = 1 to Weight
    begin
        Value2 = AB_AddCellRange( High of ActivityData, Low of ActivityData,
         RightSide, CellGroupLabel, CellGroupColor, 0 );
    end;
end;
{{< /code >}}

{{< ts-copyright >}}

