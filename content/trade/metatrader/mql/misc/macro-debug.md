---
title: "MetaTrader/MQL: デバッグ用のマクロを定義する (#define)"
linkTitle: "デバッグ用のマクロを定義する (#define)"
url: "p/8779pnk/"
date: "2023-06-18"
tags: ["MetaTrader/MQL"]
---

MQL では、C/C++ と同様に [#define](https://www.mql5.com/ja/docs/basis/preprosessor/constant) ディレクティブを使って独自のマクロを定義することができます。
現在のファイル名を示す __`__FILE__`__ や、行番号を示す __`__LINE__`__ なども同様に使用することができます。
次の例では、現在のファイル名と行番号、指定したメッセージを表示するマクロを定義しています。

{{< code lang="cpp" title="HelloEa.mq5" >}}
#define DEBUG(text) Print(__FILE__, "(", __LINE__, "): ", text)

void OnTick() {
    DEBUG("Hello, Expert Advisor");
}
{{< /code >}}

関数名を取得するための __`__FUNCTION__`__ なども便利です。

```cpp
Print(__FUNCTION__);  // => "OnTick()"
Print(__FUNCSIG__);   // => "void OnTick()"
```

