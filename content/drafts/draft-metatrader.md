---
title: "ドラフト: MetaTrader（メタトレーダー）"
url: "/p/6ptt3f8"
date: "2020-10-27"
tags: ["MetaTrader"]
draft: true
---

- [MetaTrader トップページ](/p/etedykx)
- [Conversion Functions](https://docs.mql4.com/mql5_language/mql5_functions/mql5_convert)


メタエディタの初期設定
----

- インデントの設定
  1. `F4` キーでメタエディタを開く
  2. `ツール` → `オプション`
     - 「一般」タブの「タブサイズ」を __4 文字__ に設定
     - 「スタイラー」タブの「スタイル」で __Java__ を選択（デフォルトは MetaQuotes になっている）


バックテストを起動する (MT4?) <!-- 2020-01-06 -->
----

MetaTrader でのバックテストは次のように起動できます。

1. メニューから `表示` → `ストラテジーテスター` を選択
1. 各設定項目を入力
1. `スタート` ボタンで実行開始

結果は複数のタブに分割されて表示されます。

- __結果__ タブ ... 各トレードの売買記録（取引時刻や結果）
- __グラフ__ タブ ... 資産曲線グラフ
- __レポート__ タブ ... 取引回数、利益や損失などの統計データ
- __操作履歴__ タブ ... EA のエラーメッセージなど


EA を実行する (MT4?) <!-- 2020-01-06 -->
----

1. ナビゲーターウィンドウから EA をチャートにドラッグ＆ドロップ（あるいは、右クリック → `チャートに表示`）
    - EA は 1 つのチャートに対して 1 つだけアタッチできます。
1. 設定ダイアログが開くので、`全般` タブで `自動売買を許可する` にチェック
1. `OK` ボタンを押して、チャートの右上に EA 名が表示されれば OK

MT4 全体の設定で自動売買を許可するには次のようにします。

1. メニューから `ツール` → `オプション` を選択
1. `エキスパートアドバイザー` タブで `自動売買を許可する` にチェック
1. `OK` ボタンを押して反映

### MQL コードから自動トレードが有効になっているか調べる方法

```cpp
// 自動トレード (AutoTrade) が無効になっている場合は警告表示する
if (!TerminalInfoInteger(TERMINAL_TRADE_ALLOWED)) {
    Alert("Check if automated trading is allowed"
        " in the terminal settings!");
}
```


EA のテンプレートコード for MT4? （メタトレーダーではじめるFXシステムトレードプログラミングを参考） <!-- 2020-01-07 -->
----

基本的な EA の処理の流れは次のような感じになります。

1. 買い or 売りのシグナルを検出
1. 手仕舞い条件に一致したらポジションクローズ
1. フィルタ条件のチェック（フィルタされたら何もしない）
1. ロット数を決めて注文を出す

```cpp
// ティック時実行関数
void OnTick() {
    // ポジションを更新して仕掛けシグナルを検出
    UpdatePosition();
    int sig = EntrySignal();  // +1:買い、-1:売り

    // 手仕舞いシグナルが出たらポジションを全決済しておく
    if (ShouldExit(sig)) MyOrderClose();

    // フィルタ条件に一致するなら何もしない
    if (IsFiltered(sig)) return;

    double lots = CalculateLots();  // 売買ロット数 (例:0.01、0.1)
    if (sig > 0) MyOrderSend(OP_BUY, lots);  // 買い注文
    else (sig < 0) MyOrderSend(OP_SELL, lots);  // 売り注文
}
```


チャートの情報を取得する
----

{{< code lang="cpp" >}}
string symbol = Symbol();  //=> "USDJPY"
//string symbol = ChartSymbol(0);
//MessageBox(symbol);

// カレントチャートの ID を取得する
long id = ChartID();  //=> 132482722507401307
//MessageBox(id);

// カレントチャートのタイムフレーム（分）を取得する
//ENUM_TIMEFRAMES period = Period();  //=> 5分足なら5 / 1時間足なら60 / 日足なら1440 / 週足なら10080 / 月足なら 43200
ENUM_TIMEFRAMES period = ChartPeriod(0);
MessageBox(period);
{{< /code >}}


MT5 に関するメモ <!-- 2019-12-12 -->
----

- MT5 では、取引情報に「約定」の概念が加わりました。
- MT5 では、「成行注文」「指値注文」「注文変更」「ポジション決済」「注文キャンセル」はすべて `OrderSend` 関数ひとつで行います。注文の「種類」が異なるという考え方です。
- 価格「market」は成行注文を表します。
- `MqlTraderRequest.type` の値
    - `ORDER_TYPE_BUY` ... 買い
    - `ORDER_TYPE_SELL` ... 売り
- タイプ「in」は新規ポジションオープン、タイプ「out」は決済を表します。
- 「青」アイコンは買い、「赤」アイコンは売りを表します。
- 「注文一覧」には成行注文などのリストが表示され、「取引一覧」にはそれによる約定のリストが表示されます。「注文ID」で両者を結びつけることができます。
- 「ポジション一覧」には、決済まで完了したポジションの履歴が表示されます。


MQL5 の処理の流れ <!-- 2019-12-12 -->
----

### カスタム指標（インジケーター）の場合

1. プリプロセッサで表示設定などを行います。
1. OnInit()
    - 初期化関数。指標バッファの割り当てなどを行います。テクニカル指標関数を使うのであれば、ここでハンドルを取得しておきます。
1. OnCalculate()
    - チャートにアタッチしたときと、ティックが発生したときに毎回呼び出される関数です。ここで指標バッファに値をセットすることで、インジケーターの表示が更新されます。
1. OnDeinit()
    - テクニカル指標ハンドルの削除を行います (`IndicatorRelease`)。


時刻に関する処理
----

### 時刻を取得する（MT4/5 共通）

```cpp
void OnTick() {
    datetime currentTime = TimeCurrent();  // 最終ティックの受信時刻
    datetime localTime = TimeLocal();  // ローカルPC時刻
    datetime serverTime = TimeTradeServer();  // 取引サーバーの時刻
    Print(
        "最終ティック:", currentTime,
        ", クライアント時刻:", localTime,
        ", サーバー時刻:", serverTime);
}
```

### 時刻 (datetime) を文字列に変換する（MT4/5 共通）

```cpp
void OnTick() {
    // ...
    datetime time = iTime(Symbol(), Period(), 0);
    string timeStr = TimeToString(time, TIME_DATE | TIME_SECONDS);
    // ...
}
```


メッセージ表示方法いろいろ
----

```cpp
MessageBox("Hello World"); // メッセージボックスでメッセージ表示
Alert("Hello World");  // アラートダイアログでメッセージ表示
Print("Hello World");  // ターミナルのエキスパートタブにメッセージ表示
```

今回は `Print()` 関数でも `Hello World` と出力しているので、画面下部の「ターミナル」内の「エキスパート」タブの中にも `Hello World` と表示されます。
「ターミナル」が表示されていない場合は、`Ctrl + T` で表示することができます（メニューから、`ボックス・バー表示` → `ツールボックス` と選択しても OK）。


その他
----

- DoubleToStr allows up to 8 digits
- DoubleToString allows up to 16 decimal digits

- `_Symbol` / `Symbol()` ... 通貨ペア（例: `USDJPY`）。`_Symbol` は互換性のために残されている。
- `_Point` ... 最小値幅（例: 0.001）
- `_Digit` ... 小数点以下の桁数（例: 3）
- `_Period` ... 分単位のタイムフレーム（例: 60）

互換性のために残されている `_Symbol` を使わないようにしたいのであれば、次のような定義をしてしまってコンパイル時に強引にエラーにしちゃうという手もあり。

{{< code lang="cpp" title="deprecated.mqh" >}}
#define _Symbol DEPRECATED
{{< /code >}}

- EA の OnTick 関数（NewTick イベント）に関して
    - 価格が変化したときに `OnTick` 関数が呼び出される。
    - `OnTick` 関数内の処理が完了する前に、次の NewTick イベントが発生した場合は、そのイベントは捨てられてしまう。
    - AutoTrade 設定（有効／無効）に関係なく、チャートに EA がアタッチされていれば `OnTick` 関数は呼ばれ続ける。

