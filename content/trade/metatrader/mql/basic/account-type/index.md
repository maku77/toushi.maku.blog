---
title: "MetaTrader/MQL: ヘッジアカウントとネットアカウントの違いを理解する"
linkTitle: "ヘッジアカウントとネットアカウントの違いを理解する"
url: "/p/xmseugr"
date: "2021-02-02"
tags: ["MetaTrader/MQL"]
weight: 201
---

{{% private %}}
- [MetaTrader 5にポジション計算のヘッジシステムが追加されました - MQL5記事](https://www.mql5.com/ja/articles/2299)
{{% /private %}}

MT5 のアカウント（口座）には、__ヘッジアカウント__ と __ネットアカウント__ の 2 種類があり、それぞれポジションの取り方が異なります。
どちらを使用できるかは、FX 会社によって異なります。

ヘッジカウント
: 同一シンボル（通貨）でも、注文ごとにポジションが作られるため __両建てが可能です__。ポジションを決済するときは、ポジションを特定するチケット番号 ([MqlTradeRequest 構造体](https://www.mql5.com/en/docs/constants/structures/mqltraderequest) の `position` フィールド) の指定が必要です。

ネットアカウント
: シンボル（通貨）ごとに 1 つにマージされたポジションになるため、__両建てができません__。例えば、USDJPY を 0.1 ロット買い、次に 0.5 ロット売ると、USDJPY の 0.4 ロットのショートポジションが残ります。2 つのロングポジションを取ると、加重平均のオープン価格でポジションを取ったのと同じ扱いになります。注文時のパラメータ指定は、基本的にシンボル情報＋売買タイプだけの指定になります。

以前はネットアカウントの FX 会社が多かったのですが、現在は多くの FX 会社がヘッジアカウントを採用しています。
MT4 で両建てが可能だったのに、MT5 でできなくなったことに対して不満が出たためでしょう。
{{< amazon-inline id="4534053479" title="くるくるワイド" >}} みたいな両建て手法は、基本的にはヘッジアカウントでなければ実行できません。


MQL でアカウントのタイプを調べる方法
----

### MT5 のタイトルバーで確認する

MetaTrader アプリケーションのタイトルバーに、次のような感じで __Headge__ と表示されていれば、ヘッジアカウントであることが分かります。

{{< image border="true" src="img-001.png" >}}

### MQL プログラムで確認する

`AccountInfoInteger` 関数を使って、ヘッジアカウントとネットアカウントのどちらを使っているかを調べることができます。

{{< code lang="cpp" title="Scripts/ShowAccountType.mq5" >}}
void OnStart() {
    ENUM_ACCOUNT_MARGIN_MODE marginMode =
        (ENUM_ACCOUNT_MARGIN_MODE) AccountInfoInteger(ACCOUNT_MARGIN_MODE);

    switch (marginMode) {
        case ACCOUNT_MARGIN_MODE_RETAIL_HEDGING:
            MessageBox("ヘッジアカウントを使用しています。両建て可能です。");
            break;
        case ACCOUNT_MARGIN_MODE_RETAIL_NETTING:
            MessageBox("ネットアカウントを使用しています。両建てできません。");
            break;
        case ACCOUNT_MARGIN_MODE_EXCHANGE:
            MessageBox("株式取引用のアカウントを使用しています。");
            break;
    }
}
{{< /code >}}

- 参考: [アカウント情報（口座情報）を取得する (AccountXxx) (MT5)](/p/nb7h9vg)

