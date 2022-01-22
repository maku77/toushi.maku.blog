---
title: "EasyLanguage: インジケーターサンプル「日毎の始値（寄付）価格にラインを引く」"
linkTitle: "インジケーターサンプル「日毎の始値（寄付）価格にラインを引く」"
url: "/p/7pz8gpx"
date: "2020-05-07"
tags: ["EasyLanguage"]
---

概要
----

{{< image border="true" src="img-001.png" >}}

このインジケーターは、その日の寄付の価格にラインを引きます。
日毎の買い優勢・売り優勢の判断などに利用できます。
__日をまたぐ部分は線を繋がない__ というテクニックも使っています。


コード
----

{{< code >}}
Plot1(OpenD(0), "Open", Green);

if (Time = SessionEndTime(1, 1)) then begin
    SetPlotColor(1, Transparent);
end;
{{< /code >}}

`OpenD(0)` で、日毎の始値を取得できるので、基本的にはこれをプロットしているだけです。

後半の `if (Time = SessionEndTime(1, 1)` という条件に一致した場合に、プロット色を透明 (`Transparent`) に設定することで、 __日をまたぐ部分に線を引かない__ ようにしています。

