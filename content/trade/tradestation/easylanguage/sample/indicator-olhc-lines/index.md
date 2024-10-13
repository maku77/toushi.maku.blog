---
title: "EasyLanguage: インジケーターサンプル「本日のOHLCラインを表示する」"
linkTitle: "インジケーターサンプル「本日のOHLCラインを表示する」"
url: "/p/h4fr3dn"
date: "2020-05-03"
tags: ["EasyLanguage"]
---

{{< image border="true" src="img-001.png" >}}

概要
----

このインジケーターは、本日の OHLC（始値、高値、安値、終値）にラインを描画します。
デイトレードで、上昇基調／下降基調などを判断するときなどに利用できます。


コード
----

{{< code title="#OHLC_Lines" >}}
{ Author: Maku }
using elsystem.drawing;
using elsystem.drawingobjects;

input:
    ColorOpen(DarkRed) [DisplayName = "本日の始値の色"],
    ColorHigh(LightGray) [DisplayName = "本日の高値の色"],
    ColorLow(LightGray) [DisplayName = "本日の安値の色"],
    ColorClose(Green) [DisplayName = "本日の終値の色"];

var:
    // HorizontalLine オブジェクト用の変数
    HorizontalLine myLineOpen(null),
    HorizontalLine myLineHigh(null),
    HorizontalLine myLineLow(null),
    HorizontalLine myLineClose(null);

once (LastBarOnChart) begin
    // チャート上に水平線を追加
    myLineOpen = HorizontalLine.Create(OpenD(0));
    myLineHigh = HorizontalLine.Create(HighD(0));
    myLineLow = HorizontalLine.Create(LowD(0));
    myLineClose = HorizontalLine.Create(CloseD(0));

    // 線のスタイル
    myLineOpen.Style = elsystem.drawingobjects.StyleType.Solid;
    myLineHigh.Style = elsystem.drawingobjects.StyleType.Solid;
    myLineLow.Style = elsystem.drawingobjects.StyleType.Solid;
    myLineClose.Style = elsystem.drawingobjects.StyleType.Solid;

    // 線の色
    myLineOpen.Color = Color.FromARGB(ColorOpen);
    myLineHigh.Color = Color.FromARGB(ColorHigh);
    myLineLow.Color = Color.FromARGB(ColorLow);
    myLineClose.Color = Color.FromARGB(ColorClose);

    // 線の太さ
    myLineOpen.Weight = 1;
    myLineHigh.Weight = 1;
    myLineLow.Weight = 1;
    myLineClose.Weight = 1;

    //　ユーザーによる線の移動を禁止
    myLineOpen.Lock = true;
    myLineHigh.Lock = true;
    myLineLow.Lock = true;
    myLineClose.Lock = true;

    // 線を追加
    DrawingObjects.Add(myLineOpen);
    DrawingObjects.Add(myLineHigh);
    DrawingObjects.Add(myLineLow);
    DrawingObjects.Add(myLineClose);
end;
{{< /code >}}

- （参考）[水平線を描画する (HorizontalLine)](/p/ufr2cmv/)

