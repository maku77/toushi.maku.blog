---
title: "TradeStation/アクティビティバー/Price Distribution（プライス・ディストリビューション）"
url: "/p/fbpxvp3"
linkTitle: "プライス・ディストリビューション"
description: "プライス・ディストリビューション (Price Distribution) は、指定した時間帯の価格レンジに基づき、プライス・ディストリビューションの描画を行います。"
ts-use: ["C"]
---

{{< code title="WA-Price Distribution" >}}
{ Search Tag: WA-Price Distribution }

{ This study plots the basic ActivityBar, together with a value area zone based on
  standard deviations around the ActivityBar's mode price. }

inputs:
    ApproxNumRows( 10 ) [DisplayName = "ApproxNumRows", ToolTip =
     "Aprroximate Number of Rows.  Enter the approximate number of rows to use in the study."],
    CycleColors( true ) [DisplayName = "CycleColors", ToolTip =
     "Enter true to cycle colors from one cell group to the next;  enter false to use only a single color for all cells."],
    DefaultColor( DarkGreen ) [DisplayName = "DefaultColor", ToolTip =
     "Enter the default color used in the ActivityBar study."],
    ModeType( -1 ) [DisplayName = "ModeType", ToolTip =
     "Enter 1 for highest mode, enter -1 for lowest mode."],
    ZoneNumDevs( 1 ) [DisplayName = "ZoneNumDevs", ToolTip =
     "Zone Number of Deviations.  Enter the number of standard deviations on each side of mode price to be included in the AB Zone."] ;

variables:
    CellGroupColor( 0 ),
    MinuteInterval( BarInterval of ActivityData ),
    CellGroupLabel( "" ),
    oModeCount( 0 ),
    oModePrice( 0 ),
    SDev( 0 ),
    ZoneHi( 0 ),
    ZoneLo( 0 ) ;

AB_SetRowHeight( AB_RowHeightCalc( ApproxNumRows, 3 ) ) ;

if CycleColors then
    CellGroupColor = AB_NextColor( MinuteInterval ) of ActivityData
else
    CellGroupColor = DefaultColor ;

if CellGroupColor = GetBackGroundColor then
    CellGroupColor = DefaultColor ;

CellGroupLabel = AB_NextLabel( MinuteInterval ) of ActivityData ;

Value1 = AB_AddCellRange( High of ActivityData, Low of ActivityData, RightSide,
 CellGroupLabel, CellGroupColor, 0 ) ;

Value2 = AB_Mode( RightSide, ModeType, oModeCount, oModePrice ) ;

SDev = AB_StdDev( ZoneNumDevs, RightSide ) ;
ZoneHi = MinList( AB_High, oModePrice + SDev ) ;

if ZoneHi = 0 then { ie, if oModePrice + SDev = 0 }
    ZoneHi = AB_High ;

ZoneLo = MaxList( AB_Low, oModePrice - SDev ) ;
{ if oModePrice - SDev = 0 then ZoneLo = Low, so don't need a check here }

AB_SetZone( ZoneHi, ZoneLo, RightSide ) ;
{{< /code >}}

{{< ts-copyright >}}

