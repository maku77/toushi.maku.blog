---
title: "TradeStation/ショウミー/WA-New N-Day HiLo（N日間高値・安値）"
url: "/p/bwzvvd9"
linkTitle: "N日間高値・安値"
ts-use: ["C", "R"]
---

{{< code title="WA-New N-Day HiLo" >}}
{ Search Tag: WA-New N-Day HiLo }

{
1. DESIGNED FOR USE WITH INTRADAY CHARTS ONLY.
2. NOT DESIGNED TO UPDATE AT EVERY TICK.
3. CAN BE USED AS A VALIDATION TOOL FOR THE RADARSCREEN INDICATORS:
        NEW N-DAY HIGH
        NEW N-DAY LOW

This ShowMe will plot the N-day high-low channel as lines and also plot any new highs/
lows as ShowMe's.  Only the first new highs/lows of the day are recognized and
plotted.

The QualDays inputs can be used to "disqualify" N-day highs/lows - or extremes - that
are too close to the ends of their N-day periods.  The disqualification is for a day
at a time, and may be temporary, i.e., the same extreme, if it holds for another day,
may qualify for that day.  This ShowMe plots qualified segments of the high-low
channel lines in a wider width, and new highs/lows across "disqualified" segments are
not recognized and not plotted as ShowMe's.

Qualification example - If NumDays = 21, NewQualDays = 5 and OldQualDays = 3, it
means you are looking for the first new 21-day high (low) in at least 5 days, where
the previous 21-day high (low) was also the highest high (lowest low) in at least 3
days when it occurred.  In other words, not only are you looking for a new extreme,
you are comparing it a previous extreme that clearly stands out on the chart.
}

inputs:
    NumDays( 7 ) [DisplayName = "NumDays", ToolTip =
     "Number of Days.  Enter the number of preceding days used to determine a new High and Low."],
    NewQualDays( 0 ) [DisplayName = "NewQualDays", ToolTip =
     "New Qualification Days.  Enter the number of days used to disqualify N-day highs and lows, or extremes, that are too close to the ends of their N-day periods."],
    OldQualDays( 0 ) [DisplayName = "OldQualDays", ToolTip =
     "Old Qualification Days.  Enter the number of days used to disqualify N-day highs and lows, or extremes, that are too close to the ends of their N-day periods."] ;

variables:
    { ReturnValue is used for calling both RS_DailyDataArray and RS_Extremes because
      the value requires no further checking and both functions always return 1 }
    ReturnValue( 0 ),
    Index( 0 ),
    oPrevHighest( 0 ),
    oPrevHighestDay( 0 ),
    oPrevLowest( 0 ),
    oPrevLowestDay( 0 ),
    StartDay( 0 ),
    QualHi( false ),
    QualLo( false ),
    PrevNewHiDate( 0 ),
    PrevNewLoDate( 0 ) ;

arrays:
    DataArray[ 12, 100 ]( 0 ),
    SubArray[3]( 0 ) ;

ReturnValue = RS_DailyDataArray( NumDays, DataArray, Index, SubArray ) ;

if CurrentBar = 1 or Date <> Date[1] then
    begin
    ReturnValue = RS_Extremes( NumDays, DataArray, Index, oPrevHighest, oPrevHighestDay,
     oPrevLowest, oPrevLowestDay ) ;
    StartDay = NumDays - OldQualDays ;
    QualHi = oPrevHighestDay <= StartDay and oPrevHighestDay > NewQualDays ;
    QualLo = oPrevLowestDay <= StartDay and oPrevLowestDay > NewQualDays ;
    end ;

{
IffLogic in following code tests to make sure that any new N-day high or low
identified during the post buffer portion of the day straddling CurrentBar = 1 is
the first new high/low for the day
}
if QualHi and High > oPrevHighest and IffLogic( DataArray[ 12, Index ] =
 SubArray[3], SubArray[1] <= oPrevHighest, true ) then
    begin
    if Date <> PrevNewHiDate then
        Plot1( High, !( "NewNDayHi" ) ) ;
    PrevNewHiDate = Date ;
    end
else if QualLo and Low < oPrevLowest and IffLogic( DataArray[ 12, Index ] =
 SubArray[3], SubArray[2] >= oPrevLowest, true ) then
    begin
    if Date <> PrevNewLoDate then
        Plot2( Low, !( "NewNDayLo" ) ) ;
    PrevNewLoDate = Date ;
    end ;

Plot3( oPrevHighest, !( "HiLine" ) ) ;
Plot4( oPrevLowest, !( "LoLine" ) ) ;

if QualHi then
    SetPlotWidth( 3, 2 ) ;
if QualLo then
    SetPlotWidth( 4, 2 ) ;
{{< /code >}}

{{< ts-copyright >}}

