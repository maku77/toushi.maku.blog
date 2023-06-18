---
title: "MetaTrader/MQL: デバッグモードでコンパイルされているか調べる (_DEBUG, _RELEASE, MQL5_DEBUGGING)"
linkTitle: "デバッグモードでコンパイルされているか調べる (_DEBUG, _RELEASE, MQL5_DEBUGGING)"
url: "p/nyzotbh/"
date: "2015-10-24"
tags: ["MetaTrader/MQL"]
---

MQL のプログラムが、デバッグモードとリリースモードのどちらでコンパイルされているかを調べるには、__`#ifdef`__ プリプロセッサで下記のマクロが定義されているかどうかを調べます。

- __`_DEBUG`__ ... デバッグモードでコンパイルされている（MetaEditor 上で `F5` で実行したとき）
- __`_RELEASE`__ ... リリースモードでコンパイルされている（MetaEditor 上で `F7` でコンパイルしたとき）

次のスクリプトを実行すると、スクリプト自身がどちらのモードでコンパイルされているかをログに出力します。

```cpp
void OnStart() {
    #ifdef _DEBUG
        Print("Run in debug mode");
    #else
        Print("Run in release mode");
    #endif
}
```

上記はプリプロセッサで調べる例ですが、[MQL5InfoInteger](https://www.mql5.com/en/docs/check/mqlinfointeger) 関数を使って、実行時に動的にチェックすることもできます。

```cpp
// MQL5 の場合
bool isDebug = MQL5InfoInteger(MQL5_DEBUGGING);

// MQL4 の場合
bool isDebug = IS_DEBUG_MODE;
```

