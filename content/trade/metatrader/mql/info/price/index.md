---
title: "MetaTrader/MQL: 価格情報を取得する (SymbolInfoTick, CopyRates)"
linkTitle: "価格情報を取得する (SymbolInfoTick, CopyRates)"
url: "/p/uhv9mx9"
date: "2021-02-13"
tags: ["MetaTrader/MQL"]
---

あるシンボル（銘柄）の価格情報を取得する方法はいろいろ用意されています。

- `SymbolInfoTick` ... 最新のティック情報を取得する
- `CopyRates` ... 各バーの四本値を取得する
- `SymbolInfoDouble/Integer` ... 最新の価格情報を個別に取得する（`SymbolInfoTick` の方を使えば OK）

似たような関数があって混乱するかもしれませんが、ティック情報（Bid/Ask などの値動き）を取得する手段と、各バーの情報（OHLC 四本値情報）を取得する手段の 2 種類が用意されていると考えると理解しやすいです。


SymbolInfoTick ... 最新のティック情報を取得する
----

[SymbolInfoTick 関数](https://www.mql5.com/en/docs/marketinformation/symbolinfotick)（[日本語](https://www.mql5.com/ja/docs/marketinformation/symbolinfotick)）を使用すると、指定したシンボルの最後の値動き（ティック）における Bid/Ask 値やボリュームの情報を取得することができます。

{{< code lang="cpp" >}}
bool SymbolInfoTick(string symbol, MqlTick& tick);
{{< /code >}}

得られる情報の [MqlTick 構造体](https://www.mql5.com/en/docs/constants/structures/mqltick)（[日本語](https://www.mql5.com/ja/docs/constants/structures/mqltick)） は次のようになっています。

{{< code lang="cpp" title="MqlTick 構造体" >}}
struct MqlTick {
    datetime time;      // 価格更新時間（datetime 値）
    double bid;         // Bid 価格（売値）
    double ask;         // Ask 価格（買値）
    double last;        // 取引価格（注: ターミナル起動直後は 0.0 になる）
    ulong volume;       // 取引ボリューム
    long time_msc;      // 取引時間時間（ミリ秒）
    uint flags;         // 変化理由（TICK_FLAG_BID など）
    double volume_real; // より正確な取引ボリューム（取得できれば）
};
{{< /code >}}

この構造体は、あくまで 1 ティックの情報だけを含むため、ローソク足のような四本値 (OHLC) 情報は含まれていないことに注意してください。

次のスクリプトを実行すると、カレントチャートのシンボルにおける最新価格情報を出力します。

{{< code lang="cpp" title="Scripts/Test.mq5" >}}
void OnStart() {
    MqlTick tick;
    if (!SymbolInfoTick(_Symbol, tick)) {
        Print("Error SymbolInfoTick: ", GetLastError());
        return;
    }

    Print("time=", tick.time, ", ask=", tick.ask,
        ", bid=", tick.bid, ", volume=", tick.volume);
}
{{< /code >}}

EA（エキスパートアドバイザー）であれば、`OnTick` 関数の中で `SymbolInfoTick` を呼び出せば、ティックが発生するごとに最新の価格を取得できます。

{{< code lang="cpp" title="Experts/Test.mq5" >}}
void OnTick() {
    // 同上
}
{{< /code >}}

{{< note title="MT4 の Ask/Bid 変数" >}}
MT4 環境では `Ask`、`Bid` といった組み込み変数でカレントシンボルの現在価格を参照できました。
MT5 にはこのような組み込み変数は用意されていないので、`SymbolInfoTick` 関数などを使って価格情報を取得する必要があります。
{{< /note >}}


CopyRates ... 各バーの四本値 (OHLC) を取得する
----

[CopyRates 関数](https://www.mql5.com/en/docs/series/copyrates)（[日本語](https://www.mql5.com/ja/docs/series/copyrates)）を使うと、各バーの四本値 (OHLC) 情報を取得することができます。
`CopyRates` 関数にはいくつかのバリエーションがあり、取得するデータの位置を、ポジション（`start_pos = 0` は最新のバー）で指定するか、時刻（datetime 値）で指定するかによって使い分けます。

{{< code lang="cpp" title="CopyRates 関数" >}}
int CopyRates(
        string symbol_name, ENUM_TIMEFRAMES timeframe,
        int start_pos, int count, MqlRates rates_array[]);
int CopyRates(
        string symbol_name, ENUM_TIMEFRAMES timeframe,
        datetime start_time, int count, MqlRates rates_array[]);
int CopyRates(
        string symbol_name, ENUM_TIMEFRAMES timeframe,
        datetime start_time, datetime stop_time, MqlRates rates_array[]);
{{< /code >}}

取得結果は次のような [MqlRates 構造体](https://www.mql5.com/en/docs/constants/structures/mqlrates)（[日本語](https://www.mql5.com/ja/docs/constants/structures/mqlrates)）の配列です。

{{< code lang="cpp" title="MqlRates 構造体" >}}
struct MqlRates {
    datetime time;     // 期間開始時間
    double open;       // 始値
    double high;       // 期間中の最高値
    double low;        // 期間中の最安値
    double close;      // 終値
    long tick_volume;  // ティックボリューム
    int spread;        // スプレッド
    long real_volume;  // 取引高
};
{{< /code >}}

スプレッドの情報も取得できるのが面白いですね。

次のスクリプトでは、最新のバーから 3 本分の四本値 (OHLC) 情報を取得しています。
データ格納先の配列を [ArraySetAsSeries 関数](https://www.mql5.com/en/docs/array/arraysetasseries)（[日本語](https://www.mql5.com/ja/docs/array/arraysetasseries)）でシリーズ化（時系列化）すると、配列の先頭要素が最新のバーの情報を表すようになります（デフォルトでは、配列の先頭要素は一番過去のバー情報）。

{{< code lang="cpp" title="Scripts/Test.mq5（例: 最新の 3 本のバーの OHLC を取得する）" >}}
void OnStart() {
    MqlRates rates[];
    ArraySetAsSeries(rates, true);  // 先頭要素を最新バーとする
    int copiedCount = CopyRates(_Symbol, PERIOD_CURRENT, 0, 3, rates);
    for (int i = 0; i < copiedCount; i++) {
        Print(i, ": time=", rates[i].time,
            ", O=", rates[i].open, ", H=", rates[i].high,
            ", L=", rates[i].low, ", C=", rates[i].close,
            ", tick_volume=", rates[i].tick_volume, ", spread=", rates[i].spread);
    }
}
{{< /code >}}

{{< code lang="cpp" title="実行結果" >}}
0: time=2021.02.12 19:00:00, O=1.07397, H=1.07435, L=1.0736, C=1.07428, tick_volume=4880, spread=11
1: time=2021.02.12 20:00:00, O=1.0743, H=1.07461, L=1.07408, C=1.07448, tick_volume=3688, spread=11
2: time=2021.02.12 21:00:00, O=1.07447, H=1.07452, L=1.07412, C=1.07445, tick_volume=3043, spread=11
{{< /code >}}

上記のように、`CopyRates` 関数を使うと各バーの四本値 (OHLC) 情報を `MqlRates` の形でまとめて取得できますが、始値 (Open) や終値 (Close) だけが欲しい場合は、代わりに以下のような関数を使って取得することができます。

- [CopyTime](https://www.mql5.com/en/docs/series/copytime)（[日本語](https://www.mql5.com/ja/docs/series/copytime)）... 各バーの開始時刻 (`datetime[]`) を取得
- [CopyOpen](https://www.mql5.com/en/docs/series/copyopen)（[日本語](https://www.mql5.com/ja/docs/series/copyopen)）... 各バーの始値 (`double[]`) を取得
- [CopyHigh](https://www.mql5.com/en/docs/series/copyhigh)（[日本語](https://www.mql5.com/ja/docs/series/copyhigh)）... 各バーの高値 (`double[]`) を取得
- [CopyLow](https://www.mql5.com/en/docs/series/copylow)（[日本語](https://www.mql5.com/ja/docs/series/copylow)）... 各バーの安値 (`double[]`) を取得
- [CopyClose](https://www.mql5.com/en/docs/series/copyclose)（[日本語](https://www.mql5.com/ja/docs/series/copyclose)）... 各バーの終値 (`double[]`) を取得
- [CopySpread](https://www.mql5.com/en/docs/series/copyspread)（[日本語](https://www.mql5.com/ja/docs/series/copyspread)）... 各バーのスプレッド（ポイント数）(`int[]`) を取得

{{< code lang="cpp" title="例: 最新の 3 本のバーの「終値」を取得する" >}}
void OnStart() {
    double closes[];
    ArraySetAsSeries(closes, true);
    int copiedCount = CopyClose(_Symbol, PERIOD_CURRENT, 0, 3, closes);
    for (int i = 0; i < copiedCount; i++) {
        Print(i, ": ", closes[i]);
    }
    // 配列の内容は次のように出力しても OK
    // ArrayPrint(closes);
}
{{< /code >}}


SymbolInfoDouble/Integer ... 最新の価格情報を個別に取得する
----

[SymbolInfoDouble 関数](https://www.mql5.com/en/docs/marketinformation/symbolinfodouble)（[日本語](https://www.mql5.com/ja/docs/marketinformation/symbolinfodouble)）などの数値プロパティ取得用の関数を使うと、あるシンボルの Ask/Bid 値などを個別に取得することができます。

{{< code lang="cpp" title="Scripts/Test.mq5" >}}
void OnStart() {
    datetime time = (datetime) SymbolInfoInteger(_Symbol, SYMBOL_TIME);
    double bid = SymbolInfoDouble(_Symbol, SYMBOL_BID);
    double ask = SymbolInfoDouble(_Symbol, SYMBOL_ASK);
    long volume = SymbolInfoInteger(_Symbol, SYMBOL_VOLUME);
    Print("time=", time, ", ask=", ask, ", bid=", bid, ", volume=", volume);
}
{{< /code >}}

`SymbolInfoTick` 関数で最新のティック情報 (`MqlTick`) を一度に取得するのと同じかと思うかもしれませんが、まさに同じ値が取得できます（＾＾；

### SymbolInfoTick と SymbolInfoDouble のどちらで Bid/Ask 値を取得すべきか？

結論から言うと、__`SymbolInfoTick` 関数の方を使えばよさそう__ です。

Bid/Ask 値を取得するのであれば、どちらの関数でも同じ値が取得できるので、違いはコードの可読性と、実行時のパフォーマンスだけです。
可読性はどちらもそんなに変わらないので、パフォーマンスを調べて速い方を使うのがよさそうです。
予想では、取得できる情報量の少ない `SymbolInfoDouble` の方が速いと思いましたが、プロファイリングを取ってみると、わずかに `SymbolInfoTick` 関数の方が速そうです。

{{< image border="true" src="img-001.png" >}}

