---
title: "EasyLanguage で垂直線を描画する (VerticalLine)"
linkTitle: "垂直線を描画する (VerticalLine)"
url: "/p/f3gs6gs"
date: "2020-04-18"
tags: ["トレステ", "EasyLanguage"]
image: "img-001.png"
---

{{% private %}}
- [About Drawing Ojbect Class](http://help.tradestation.com/09_01/tsdevhelp/Subsystems/elobject/topics/about_drawing_objects.htm)
{{% /private %}}


垂直線を引く方法
----

__`DrawingObjects.Add()`__ で、__`VerticalLine`__ オブジェクトを追加することで、画面上に垂直線を追加することができます。
これは、水平線 (`HorizontalLine`) を引く方法と同様です。

- 参考: [水平線を描画する (HorizontalLine)](/p/ufr2cmv)


VerticalLine オブジェクトで垂直線を表示する
----

{{< image w="600" src="img-001.png" >}}

### コード

次のサンプルコードでは、日付が変わるタイミングで垂直線を描画しています。

{{< code title="#DateLine" >}}
using elsystem.drawingobjects;

var:
    bool myIsBarTypeProper(false),
    BNPoint myPoint(null),
    VerticalLine myLine(null);

method void DrawVerticalLine() begin
    myPoint = BNPoint.Create(CurrentBar, 0);
    myLine = VerticalLine.Create(myPoint);
    myLine.Color = elsystem.drawing.Color.GreenYellow;
    myLine.Style = elsystem.drawingobjects.StyleType.Solid;
    myLine.Weight = 3;
    DrawingObjects.Add(myLine);
end;

once begin
    // ティック足(0)、分足(1)、秒足(14) のときのみ描画
    myIsBarTypeProper = (BarType = 0) or (BarType = 1) or (BarType = 14);
end;

// 日付が変わった時に垂直線を描画
if myIsBarTypeProper and (Date > Date[1]) then begin
    DrawVerticalLine();
end;
{{< /code >}}

### 解説

`VerticalLine` オブジェクトは、`VerticalLine.Create()` を使って生成するのですが、このとき、描画位置の点を示す、下記のいずれかのオブジェクトを指定します。

- `BNPoint` ... 足のインデックスと価格を指定（BN は BarNumber の略）
- `DTPoint` ... 日時と価格を指定（DT は DateTime の略）

ここでは、`BNPoint.Create()` で `BNPoint` オブジェクトを生成しています。

{{< code >}}
myPoint = BNPoint.Create(CurrentBar, 0);
{{< /code >}}

X 座標としては現在の足のインデックス (`CurrentBar`) を指定し、Y 座標としては価格 `0` 円を指定しています（垂直線を引く場合は上下位置は関係ないので価格は何でもよい）。
あとは、この `BNPoint` オブジェクトを使って `VerticalLine` を生成し、それを `DrawingObjects.Add()` で追加すれば垂直線が描画されます。

{{< code >}}
myLine = VerticalLine.Create(myPoint);
DrawingObjects.Add(myLine);
{{< /code >}}

最後のポイントは、いつ描画するかの条件分岐です。
ここでは、足種 (`BarType`) が「ティック」「分足」「秒足」のいずれかであり、かつ、現在の足で日付が変わったときのみ `DrawVerticalLine()` を呼び出して垂直線を描画しています。

{{< code >}}
// 日付が変わった時に垂直線を描画
if myIsBarTypeProper and (Date > Date[1]) then begin
    DrawVerticalLine();
end;
{{< /code >}}

仮に別の足種（日足や週足など）でも描画してしまうと、すべての足で垂直線が描画されることになり、大変なことになります。

### おまけ

`BNPoint` の代わりに、`DTPoint` を使う場合は、次のような感じになります。
足のインデックス (`CurrentBar`) で横方向の座標を指定する代わりに、時刻情報 (`BarDateTime`) を指定します。

{{< code >}}
var:
    bool myIsBarTypeProper(false),
    DTPoint myPoint(null),
    VerticalLine myLine(null);

method void DrawVerticalLine() begin
    myPoint = DTPoint.Create(BarDateTime, 0);
    myLine = VerticalLine.Create(myPoint);
    // ...
    DrawingObjects.Add(myLine);
end;
{{< /code >}}

{{< reference >}}
- [水平線を描画する (HorizontalLine)](/p/ufr2cmv)
{{< /reference >}}

