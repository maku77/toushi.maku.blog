---
title: "MetaTrader/MQL: 実行中のプログラムの種類（スクリプト/インジケーター/EA）を判別する (MQL5_PROGRAM_TYPE)"
linkTitle: "実行中のプログラムの種類（スクリプト/インジケーター/EA）を判別する (MQL5_PROGRAM_TYPE)"
url: "p/dct2372/"
date: "2015-10-08"
tags: ["MetaTrader/MQL"]
---

__`MQL5InfoInteger`__ 関数の引数に __`MQL5_PROGRAM_TYPE`__ を指定すると、その関数の呼び出し元がスクリプトなのか、EA なのか、インジケーターなのかを調べることができます。

```cpp
// 実行中のプログラムが「スクリプト」かどうかを調べます
bool isCalledFromScript() {
    return MQL5InfoInteger(MQL5_PROGRAM_TYPE) == PROGRAM_SCRIPT;
}

// 実行中のプログラムが「EA」かどうかを調べます
bool isCalledFromEa() {
    return MQL5InfoInteger(MQL5_PROGRAM_TYPE) == PROGRAM_EXPERT;
}

// 実行中のプログラムが「インジケーター」かどうかを調べます
bool isCalledFromIndicator() {
    return MQL5InfoInteger(MQL5_PROGRAM_TYPE) == PROGRAM_INDICATOR;
}
```

