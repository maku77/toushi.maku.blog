---
title: "Python の yfinance ライブラリで銘柄情報を取得する"
url: "p/5dyijyb/"
date: "2025-05-05"
lastmod: "2026-02-28"
tags: ["yfinance"]
---

Python の [**`yfinance`** ライブラリ](https://ranaroussi.github.io/yfinance/)を使って、Yahoo Finance から銘柄情報を取得する方法のまとめです。
このライブラリは非公式なものなのでいつ使えなくなるかわかりませんが、2026 年現在でも利用可能です。


パッケージのインストール
----

`yfinance` パッケージは `pip install yfinance` でインストールできますが、ローカル環境を汚さないために [uv パッケージマネージャを使ってインストールする](https://maku77.github.io/p/fjsfjpw/)ことをおすすめします。

{{< code lang="console" title="yfinance のインストール（uv を使う方法）" >}}
$ uv init yfinance-study  # プロジェクトディレクトリを作成
$ cd yfinance-study       # プロジェクトディレクトリに移動
$ uv add yfinance         # yfinance ライブラリをインストール

$ uv run main.py          # main.py を実行できるか確認
Hello from yfinance-study!
{{< /code >}}


基本的な使い方
----

下記は `yfinance` ライブラリを使って、ソニーグループ (6758) の銘柄情報を取得する例です。
**`Ticker`** コンストラクタにティッカーシンボル **`6758.T`** を渡し、各種プロパティにアクセスするだけで簡単に情報を取得できます（東証銘柄のシンボルには `.T` サフィックスを付けます）。

{{< code lang="python" title="main.py" >}}
import json
import yfinance as yf

t = yf.Ticker("6758.T")  # ソニーグループのティッカーシンボルを指定
info = t.info  # 銘柄の基本情報を dict 形式で取得

# 取得結果を json ライブラリで整形して表示
print(json.dumps(info, indent=2, ensure_ascii=False))
{{< /code >}}

実際に Web 経由でのデータ取得が発生するのは、`Ticker.info` などのプロパティにアクセスしたときです。
`Ticker` オブジェクトの生成時には Web アクセスは発生しません。

- {{< file src="ticker-info.json" caption="出力結果の例 (ticker-info.json)" >}}


リクエストをキャッシュできるようにする
----

Yahoo サーバーへ頻繁にアクセスするのは望ましくないので、サーバーから取得した情報はローカルにキャッシュしておくようにしましょう。
次の例では、`diskcache` ライブラリを使って `.cache` ディレクトリにキャッシュデータを保存しています。

{{< code lang="python" title="Ticker.info の取得結果をディスクにキャッシュ" >}}
import diskcache
import yfinance as yf

cache = diskcache.Cache(directory=".cache")

@cache.memoize()
def fetch_ticker_info(symbol: str) -> dict:
    return yf.Ticker(symbol).info

if __name__ == "__main__":
    info = fetch_ticker_info("6758.T")  # 2回目以降はキャッシュから取得される
    print(info["country"])  # Japan
    print(info["ebitda"])  # 2036071006208
{{< /code >}}

- 参考: [関数実行結果をファイル（不揮発）にキャッシュする (`diskcache`) - まくまく Python ノート](https://maku77.github.io/p/msu6xd9/)


Ticker.info の内容
----

`Ticker.info` プロパティからは例えば次のような情報を取得できます。

### 基本情報

| キー | 日本語名 | 概要 | 値の例 |
| ---- | ---- | ---- | ---- |
| `shortName` | 会社名 | 会社の短い名称 | SONY GROUP CORPORATION |
| `symbol` | ティッカー | 取引所での銘柄コード | 6758.T |
| `exchange` | 取引所 | 上場している取引所 | JPX |
| `sector` | セクター | 事業分野の大分類 | Technology |
| `industry` | 業種 | より具体的な業種区分 | Consumer Electronics |
| `country` | 国 | 本社所在地の国 | Japan |
| `website` | 公式サイト | 企業の公式 Web サイト | https://www.sony.com |

### 株価・評価

| キー | 日本語名 | 概要 | 値の例 |
| ---- | ---- | ---- | ---- |
| `currentPrice` | 現在株価 | 最新の取引価格 | 3336.0 |
| `marketCap` | 時価総額 | 発行済株式数×株価 | 19893707603968 |
| `enterpriseValue` | 企業価値 (EV) | 時価総額+純有利子負債 | 19835845083136 |
| `trailingPE` | PER(実績) | 株価÷直近EPS | 16.154964 |
| `forwardPE` | PER(予想) | 株価÷予想EPS | 18.209608 |
| `priceToSalesTrailing12Months` | PSR(TTM) | 株価÷直近売上 | 1.5104991 |
| `priceToBook` | PBR | 株価÷1株純資産 | 2.438962 |

### 収益性

| キー | 日本語名 | 概要 | 値の例 |
| ---- | ---- | ---- | ---- |
| `profitMargins` | 利益率 | 売上に対する純利益率 | -0.0161 |
| `grossMargins` | 粗利率 | 売上に対する粗利益率 | 0.29479 |
| `operatingMargins` | 営業利益率 | 売上に対する営業利益率 | 0.13736 |
| `returnOnAssets` | ROA | 総資産利益率 | 0.0396 |
| `returnOnEquity` | ROE | 自己資本利益率 | 0.14917 |

### 財務

| キー | 日本語名 | 概要 | 値の例 |
| ---- | ---- | ---- | ---- |
| `totalRevenue` | 売上高(TTM) | 直近12か月の売上 | 13170287575040 |
| `ebitda` | EBITDA | 利払い・税引き・償却前利益 | 2036071006208 |
| `totalCash` | 現金等 | 手元資金 | 2086500040704 |
| `totalDebt` | 有利子負債 | 借入や社債など | 1656855986176 |
| `freeCashflow` | フリーCF | 営業CF−投資CF | -79850749952 |

### 配当

| キー | 日本語名 | 概要 | 値の例 |
| ---- | ---- | ---- | ---- |
| `dividendRate` | 配当額 | 1株あたり配当 | 25.0 |
| `dividendYield` | 配当利回り | 配当÷株価 | 0.75 |
| `payoutRatio` | 配当性向 | 利益のうち配当の割合 | 0.109 |

### 取引情報

| キー | 日本語名 | 概要 | 値の例 |
| ---- | ---- | ---- | ---- |
| `volume` | 出来高 | 直近の売買高 | 26683400 |
| `averageVolume` | 平均出来高 | 平均の売買高 | 17558655 |
| `fiftyTwoWeekHigh` | 52週高値 | 過去52週の最高値 | 4776.0 |
| `fiftyTwoWeekLow` | 52週安値 | 過去52週の最安値 | 2980.5 |

上記のテーブル出力に使ったコード: {{< file src="yfutils.py" >}} + `main.py`

{{< code lang="python" title="main.py" >}}
from libs import yfutils

if __name__ == "__main__":
    info = yfutils.fetch_ticker_info("6758.T")
    yfutils.print_info_tables(info)
{{< /code >}}


Ticker.funds_data（ファンド情報）
----

```python
fund = yf.Ticker("SPY").funds_data
print(fund.description)  # ファンドの説明
print(fund.asset_classes)  # 資産クラスごとの保有割合
print(fund.sector_weightings)  # セクターごとの保有割合
print(fund.top_holdings)  # 上位保有銘柄
```

{{< code title="出力結果" >}}
The trust seeks to achieve its investment objective by holding a portfolio ...(省略)...

{'cashPosition': 0.0008, 'stockPosition': 0.9993, 'bondPosition': 0.0,
 'preferredPosition': 0.0, 'convertiblePosition': 0.0, 'otherPosition': 0.0}

{'realestate': 0.0225, 'consumer_cyclical': 0.1038, 'basic_materials': 0.0177,
 'consumer_defensive': 0.0615, 'technology': 0.3168, 'communication_services': 0.0946,
 'financial_services': 0.14039999, 'utilities': 0.0256, 'industrials': 0.0766,
 'energy': 0.0318, 'healthcare': 0.108500004}

                                  Name  Holding Percent
Symbol
AAPL                         Apple Inc         0.067592
MSFT                    Microsoft Corp         0.062217
NVDA                       NVIDIA Corp         0.056481
AMZN                    Amazon.com Inc         0.036831
META        Meta Platforms Inc Class A         0.025457
BRK-B   Berkshire Hathaway Inc Class B         0.020696
GOOGL             Alphabet Inc Class A         0.019613
AVGO                      Broadcom Inc         0.019103
TSLA                         Tesla Inc         0.016719
GOOG              Alphabet Inc Class C         0.016105
{{< /code >}}

