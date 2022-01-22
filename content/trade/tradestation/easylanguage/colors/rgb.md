---
title: "EasyLanguage: RGB関数（RGBの各値を合成して32ビットカラー値を作成する）"
linkTitle: "RGB関数（RGB の各値を合成して32ビットカラー値を作成する）"
url: "/p/znycoyb"
date: "2020-05-03"
tags: ["EasyLanguage"]
---

{{% private %}}
- [EasyLanguage Reserved Words & Functions: RGB (Reserved Word)](http://help.tradestation.com/09_05/eng/tsdevhelp/Subsystems/elword/word/rgb_reserved_word_.htm)
{{% /private %}}

__`RGB`__ 予約語を使用すると、RGB の各成分の色情報を合成して、32 ビット整数の RGB 値を生成することができます。

{{< code >}}
RGB(nRed, nGreen, nBlue);
{{< /code >}}

下記のサンプルコード（インジケーター）では、`RGB` 予約語の戻り値をログ出力しています。

{{< code >}}
once begin
    ClearPrintLog;
    Value1 = RGB(255, 0, 0);  // = Red (255)
    Value2 = RGB(255, 255, 0);  // = Yellow (65535)
    Value3 = RGB(255, 0, 255);  // = Magenta (16711935)
    Print(Value1:0:0);
    Print(Value2:0:0);
    Print(Value3:0:0);
end;
{{< /code >}}

{{< code title="実行結果" >}}
255
65535
16711935
{{< /code >}}

