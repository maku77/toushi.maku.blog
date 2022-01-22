---
title: "TradeStation/アクティビティバー/WA-Candlestick VolAccum（ローソク足出来高アキュムレーション）"
url: "/p/p3omdnr"
linkTitle: "ローソク足出来高アキュムレーション"
description: "ローソク足出来高アキュムレーション (WA-Candlestick VolAccum) は、出来高の大きさに従い、ローソク足の幅を描画します。"
ts-use: ["C"]
---

{{< code title="WA-Candlestick VolAccum" >}}
{ Search Tag: WA-Candlestick VolAccum }

{ This study plots an ActivityBar that simulates a candlestick, with the width of the
  candlestick body varying in proportion to the volume of the ActivityBar. }

using elsystem.drawing;
using elsystem.drawingobjects;

inputs:
    BlockSize( 100 ) [DisplayName = "BlockSize", ToolTip =
     "Enter the amount of volume that will cause the width of the candlestick to be increased."],
    MaxNumCells( 100 ) [DisplayName = "MaxNumCells", ToolTip =
     "Maximum Number of Cells.  Enter the maximum number of cells that can be added to each side of the bar."],
    UpColor( Magenta ) [DisplayName = "UpColor", ToolTip =
     "Enter the color to use when the close is greater than the open."],
    DnColor( Yellow ) [DisplayName = "DnColor", ToolTip =
     "Down Color.  Enter the color to use when the close is less than the open."];

variables:
    TrendLine varTrendLine( NULL ),
    Counter( 0 ),
    BStatus1Prev( 0 ),
    BStatus1( 0 ),
    Remainder( 0 ),
    FirstOpen( 0 ),
    UnprocessedVol( 0 ),
    RawNumCells( 0 ),
    NumCells( 0 ),
    TLRef( 0 ),
    AnyVol( 0 );

method Trendline CreateTrendline()
variables: TrendLine tempTL;
begin
    tempTL = Trendline.Create( DTPoint.Create( BarDateTime, Open ),
     DTPoint.Create( BarDateTime, Close ) );

    {
    Setting 'Persist' to false causes the text label to be deleted on an intrabar
    tick.  When set to false, a text label that is created on the closing tick of
    the bar is saved/retained.
    }
    tempTL.Persist = false;
    tempTL.Lock = true; { prevent inadvertant moving }
    tempTL.ExtLeft = false;
    tempTL.ExtRight = false;
    tempTL.Weight = 2;

    if Close > Open then
        tempTL.Color = GetColorFromInteger( 255, UpColor )
    else if Close < Open then
        tempTL.Color = GetColorFromInteger( 255, DnColor );

    {
    this is how the Trendline is "shown"; the Trendline is added to the
    DrawingObjects collection; if you want to remove the Trendline, you can
    use the Delete method of the DrawingObjects class
    }
    DrawingObjects.Add( tempTL );

    return tempTL;
end;

{ convert integer color to a color object and return the color object }
method Color GetColorFromInteger( int Alpha, int ColorInteger )
begin
    return Color.FromARGB( Alpha, GetRValue( ColorInteger ),
     GetGValue( ColorInteger ), GetBValue( ColorInteger ) );
end;

BStatus1Prev = BStatus1;
BStatus1 = BarStatus( 1 );

if BarType of ActivityData >= 2 then { not minute data }
    AnyVol = Volume of ActivityData
else { minute data }
    AnyVol = Ticks of ActivityData;

{ initialize ActivityBar }
{
ie, if beginning of act data stream (can't check if ActivityData's CB  = 1
because act data stream does not start at CB = 1) or if first act data bar of
new act bar
}
if ( CurrentBar of Data1 = 1 and BStatus1 = 2 )
    or BStatus1Prev = 2 then
begin
    Remainder = 0;
    FirstOpen = Open of ActivityData;
    AB_SetRowHeight( .5 ); { arbitrary; cells not displayed, see note below }
end;

{ add "hidden" cells corresponding to additional volume }
UnprocessedVol = Remainder + AnyVol;
RawNumCells = IntPortion( UnprocessedVol / BlockSize );
Remainder = Mod( UnprocessedVol, BlockSize );
NumCells = MinList( RawNumCells, MaxNumCells );

for Counter = 1 to NumCells
begin
    {
    these cells are arbitrarily added at FirstOpen; they can be added at any price
    as long as it stays constant for the entire ActivityBar; the cells and labels
    are not meant to be displayed (see study properties), but are used to control
    the width of the zone - or candlestick body - that will be plotted and
    displayed.
    }
    AB_AddCell( FirstOpen, RightSide, "*", Yellow, 0 );
    AB_AddCell( FirstOpen, LeftSide, "*", Yellow, 0 );
end;

{ set/update zone representing candlestick body }
AB_SetZone( FirstOpen, Close of ActivityData, RightSide );
AB_SetZone( FirstOpen, Close of ActivityData, LeftSide );

{ if at last ActivityData bar of ActivityBar, paint the ActivityBar }
if BStatus1 = 2 then
begin
    varTrendLine = CreateTrendline();
end;
{{< /code >}}

{{< ts-copyright >}}

