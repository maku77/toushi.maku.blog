---
title: "トレステ EashLanguage 入門"
linkTitle: "EasyLanguage"
url: "/p/peu9myd"
tags: ["トレステ", "EasyLanguage"]
---

{{% private %}}
- 価格情報を取得する
    - Open ... 現在の足の始値
    - High ... 現在の足の高値
    - Low ... 現在の足の安値
    - Close ... 現在の足の終値
    - OpenD(0) ... 本日の始値
    - HighD(0)  ... 本日の高値（ザラ場ではティックごとに変化します）
    - LowD(0) ... 本日の安値（ザラ場ではティックごとに変化します）
    - CloseD(0) ... 本日の終値（ザラ場ではティックごとに変化します）
    - OpenD(1) ... 前日の始値
    - HighD(1)  ... 前日の高値
    - LowD(1) ... 前日の安値
    - CloseD(1) ... 前日の終値
- EasyLanguage のちょいテク
    - 日をまたぐ部分に線を引かないようにする（サンプルで使ってる）
        - `If (Time = SessionEndTime(1, 1)) then SetPlotColor(1, Transparent);`
- 処理タイミングの制御
    - `if BarStatus(1) = 2 then` ... 各バーの終値が決まったときに処理
    - `if LastBarOnChart then` ... 最後のバーでティック毎に処理
    - `if LastBarOnChart and BarStatus(1) = 2 then` ... 最後のバーの終値が決まったときに処理
    - `once (LastBarOnChart) begin ... end;` ... ?
- 文字列、数値
    - [NumToStr](http://help.tradestation.com/09_05/Monex/jpn/tsdevhelp/Subsystems/elword/word/numtostr_reserved_word_.htm) 数値 → 文字列の変換
    - [StrToNum](http://help.tradestation.com/09_05/Monex/jpn/tsdevhelp/Subsystems/elword/word/strtonum_reserved_word_.htm) 文字列 → 数値の変換
{{% /private %}}

