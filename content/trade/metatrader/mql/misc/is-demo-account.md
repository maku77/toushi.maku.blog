---
title: "MetaTrader/MQL: プログラムがデモ口座で実行されている調べる"
linkTitle: "プログラムがデモ口座で実行されているか調べる"
url: "/p/e7gjidc"
date: "2021-01-26"
tags: ["MetaTrader/MQL"]
---

MetaTrader で取引を行うスクリプトや EA をデバッグしているときに、間違えて実際の口座で実行してしまうと、不本意なポジションをとってしまい危険です。
下記のユーティリティ関数を使うと、実行中のプログラムがデモ口座上で実行されているかを調べることができます。

{{< code lang="cpp" title="Include/maku77/Util.mqh" >}}
namespace Util {
    /**
     * プログラムがデモ口座で実行されているか調べ、そうでなければ警告を表示します。
     *
     * @return デモ口座で実行されているなら true、そうでないなら false
     */
    bool IsDemoAccount() {
        if (AccountInfoInteger(ACCOUNT_TRADE_MODE) == ACCOUNT_TRADE_MODE_DEMO) {
            return true;
        }
        Alert("Operation is not allowed on a live account!");
        return false;
    }
}
{{< /code >}}

例えば、スクリプトのエントリポイント (`OnStart` 関数) の先頭で次のようにしておけば、スクリプトがデモ口座以外で実行されたときに実行を中止できます。

{{< code lang="cpp" title="Scripts/Test.mq5" >}}
#include <maku77/Util.mqh>

void OnStart() {
    if (!Util::IsDemoAccount()) return;

    // ... 残りの処理 ...
}
{{< /code >}}

