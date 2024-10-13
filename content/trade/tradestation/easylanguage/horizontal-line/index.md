---
title: "EasyLanguage で水平線を描画する (HorizontalLine)"
linkTitle: "水平線を描画する (HorizontalLine)"
url: "/p/ufr2cmv"
date: "2020-04-18"
tags: ["トレステ", "EasyLanguage"]
image: "img-001.png"
---

{{% private %}}
- [About Drawing Ojbect Class](http://help.tradestation.com/09_01/tsdevhelp/Subsystems/elobject/topics/about_drawing_objects.htm)
{{% /private %}}


水平線を引く方法
----

インジケーターで水平線を引くには下記のような方法があります。

- Drawing Object の一種である **HorizontalLine** を追加する
- `Plot1` 関数などで固定 Price の線を引く

後者の方法は、`Plot1(100)` のように、固定価格でライン描画してしまう方法ですが、この値がインジケーターで求められた値として使われてしまうので、あまり望ましい方法ではないでしょう。
チャート上でローソク足が存在する部分しかラインが引かれないという欠点もあります。

そこで、ここでは前者の `HorizontalLine` を使った方法を採用することにします。


HorizontalLine オブジェクトで水平線を表示する
----

{{< image w="600" src="img-001.png" >}}

__`DrawingObjects.Add()`__ で、__`HorizontalLine`__ オブジェクトを追加することで、画面上に水平線を追加することができます。
次のサンプルコードでは、各足の高値 (High) と安値 (Low) の位置に水平線を描画しています。

{{< code >}}
using elsystem.drawingobjects;

// HorizontalLine オブジェクト用の変数
vars:
    HorizontalLine myLine1(null),
    HorizontalLine myLine2(null);

// チャート上に水平線を追加
myLine1 = HorizontalLine.Create(High);
myLine2 = HorizontalLine.Create(Low);
DrawingObjects.Add(myLine1);
DrawingObjects.Add(myLine2);

// 水平線のスタイルや色、太さを変更可能
myLine1.Style = elsystem.drawingobjects.StyleType.Solid;
myLine2.Style = elsystem.drawingobjects.StyleType.Dotted;
myLine1.Color = elsystem.drawing.Color.Crimson;
myLine2.Color = elsystem.drawing.Color.DeepSkyBlue;
myLine1.Weight = 2;
myLine2.Weight = 1;
{{< /code >}}

- （参考）[垂直線を描画する (VerticalLine)](/p/f3gs6gs)
- （参考）[インジケーターサンプル「本日のOHLCラインを表示する」](/p/h4fr3dn)

