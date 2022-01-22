---
title: "TradeStation/アクティビティバー/WA-Up vs Down Strength（上昇・下落ストレングス）"
url: "/p/4wnw4rp"
linkTitle: "上昇・下落ストレングス"
description: "上昇・下落ストレングス (WA-Up vs Down Strength) は、上昇出来高と下落出来高の強さをバーの左右に積み上げます。"
ts-use: ["C"]
---

{{< code title="WA-Up vs Down Strength" >}}
{ Search Tag: WA-Up vs Down Strength }

{
This study is somewhat similar to the Volume Strength ActivityBar study.  As in that
study, it plots an ActivityBar in which each ActivityData bar is processed 0 or more
times depending on its volume and the specified BlockSize divisor.  If BlockSize
is set to zero, each ActivityData bar is processed exactly once.

The difference is that each time an ActivityData bar is processed, at most one cell
is added instead of a range of cells:
  - if the ActivityData bar was an up bar, one cell is added to the right
  - if the ActivityData bar was a down bar, one cell is added to the left
  - if the ActivityData bar was unchanged, no cells are added
}

inputs:
    ApproxNumRows( 10 ) [DisplayName = "ApproxNumRows", ToolTip =
     "Aprroximate Number of Rows.  Enter the approximate number of rows to use in the study. "],
    BlockSize( 100 ) [DisplayName = "BlockSize", ToolTip =
     "Enter the volume divisor to determine the number of times to process an ActivityData bar."],
    MaxWeight( 15 ) [DisplayName = "MaxWeight", ToolTip =
     "Maximum Weight.  Enter the maximum number of times an ActivityData bar can be processed."],
    UpColor( Cyan ) [DisplayName = "UpColor", ToolTip =
     "Enter the plot color to be used when the Close is greater than the Open."],
    DnColor( Red ) [DisplayName = "DnColor", ToolTip =
     "Down Color.  Enter the plot color for the ActivityBar used when the Close is less than the Open."] ;

variables:
    Counter( 0 ),
    MinuteInterval( BarInterval of ActivityData ),
    CellGroupLabel( "" ),
    RawWeight( 0 ),
    Weight( 0 ),
    Side( 0 ),
    Color( 0 ),
    AnyVol( 0 ) ;

AB_SetRowHeight( AB_RowHeightCalc( ApproxNumRows, 3 ) ) ;

if BarType of ActivityData >= 2 then { ie, not minute data }
    AnyVol = Volume of ActivityData
else { if minute data }
    AnyVol = Ticks of ActivityData ;

CellGroupLabel = AB_NextLabel( MinuteInterval ) of ActivityData ;

if Close of ActivityData <> Close[1] of ActivityData and AnyVol >= BlockSize then
    begin

    if BlockSize > 0 then
        RawWeight = IntPortion( AnyVol / BlockSize )
    else
        RawWeight = 1 ;

    Weight = MinList( RawWeight, MaxWeight ) ;

    if Close of ActivityData > Close[1] of ActivityData then
        begin
        Side = RightSide ;
        Color = UpColor ;
        end
    else
        begin
        Side = LeftSide ;
        Color = DnColor ;
        end ;

    for Counter = 1 to Weight
        begin
        AB_AddCell( Close of ActivityData, Side, CellGroupLabel, Color, 0 ) ;
        end ;

    end ;
{{< /code >}}

{{< ts-copyright >}}

