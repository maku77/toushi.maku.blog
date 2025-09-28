---
title: "yfinance ライブラリで銘柄情報を取得する"
url: "p/5dyijyb/"
date: "2025-05-05"
tags: ["yfinance"]
draft: true
---

Python の [**`yfinance`** ライブラリ](https://ranaroussi.github.io/yfinance/)を使って、Yahoo Finance から銘柄情報を取得する方法のまとめです。
このライブラリは非公式なものなのでいつ使えなくなるか分かりませんが、2025 年現在でも利用可能です。

基本的な使い方
----

下記は `yfinance` ライブラリを使って、ソニーグループ (6758) の銘柄情報を取得する例です。
`Ticker` コンストラクタにティッカーシンボル `6758.T` を渡すだけで、簡単に情報を取得できます。

```python
import yfinance as yf

t = yf.Ticker("6758.T")  # ソニーグループのティッカーシンボルを指定
info = t.info  # 銘柄の基本情報を dict 形式で取得
```

銘柄情報を出力する場合は、json ライブラリを使って整形して表示すると見やすいです。

```python
import json

print(json.dumps(t.info, indent=2, ensure_ascii=False))
```

{{< accordion title="出力結果" >}}
{{< code lang="json" >}}
{
  "address1": "7-1, Konan 1-chome",
  "address2": "Minato-ku",
  "city": "Tokyo",
  "zip": "108-0075",
  "country": "Japan",
  "phone": "81-3-6748-2111",
  "website": "https://www.sony.com",
  "industry": "Consumer Electronics",
  "industryKey": "consumer-electronics",
  "industryDisp": "Consumer Electronics",
  "sector": "Technology",
  "sectorKey": "technology",
  "sectorDisp": "Technology",
  "longBusinessSummary": "Sony Group Corporation designs, develops, produces, and sells electronic equipment, instruments, and devices for the consumer, professional, and industrial markets in Japan, the United States, Europe, China, the Asia-Pacific, and internationally. The company distributes software titles and add-on content through digital networks; network services related to game, video, and music content; and home gaming consoles, packaged and game software, and peripheral devices. It also develops, produces, markets, and distributes recorded music; publishes music; and produces and distributes animation titles, game applications, and various services for music and visual products. In addition, the company produces, acquires, and distributes live-action and animated motion pictures for theatrical release, as well as scripted and animated series, unscripted reality or light entertainment, daytime serials, game shows, television movies, and miniseries and other television programs; operation of television networks and direct-to-consumer streaming services; operates a visual effects and animation unit; and manages a studio facility. Further, it researches, develops, designs, produces, markets, distributes, sells, and services televisions, and video and sound products; interchangeable lens, as well as compact digital, and consumer and professional video cameras; projectors and medical equipment; mobile phones, accessories, and applications; and metal oxide semiconductor image sensors, charge-coupled devices, integration systems, and other semiconductors. Additionally, it offers Internet broadband network services; recording media, and storage media products; and life and non-life insurance, banking, and other services, as well as creates and distributes content for PCs and mobile phones. The company was formerly known as Sony Corporation and changed its name to Sony Group Corporation in April 2021. Sony Group Corporation was incorporated in 1946 and is headquartered in Tokyo, Japan.",
  "fullTimeEmployees": 113000,
  "companyOfficers": [
    {
      "maxAge": 1,
      "name": "Dr. Hiroaki  Kitano Ph.D.",
      "age": 63,
      "title": "Senior EVP & CTO, Corporate Executive Officer",
      "yearBorn": 1961,
      "fiscalYear": 2024,
      "totalPay": 96000000,
      "exercisedValue": 0,
      "unexercisedValue": 0
    },
    {
      "maxAge": 1,
      "name": "Mr. Shiro  Kambe",
      "age": 63,
      "title": "Senior EVP & Corporate Executive Officer",
      "yearBorn": 1961,
      "fiscalYear": 2024,
      "totalPay": 94000000,
      "exercisedValue": 0,
      "unexercisedValue": 0
    },
    {
      "maxAge": 1,
      "name": "Mr. Kazushi  Ambe",
      "age": 63,
      "title": "Senior EVP & Corporate Executive Officer",
      "yearBorn": 1961,
      "fiscalYear": 2024,
      "totalPay": 93000000,
      "exercisedValue": 0,
      "unexercisedValue": 0
    },
    {
      "maxAge": 1,
      "name": "Mr. Toshimoto  Mitomo",
      "age": 61,
      "title": "Executive Deputy President, CSO, Corporate Executive Officer & Chief Strategy Officer",
      "yearBorn": 1963,
      "fiscalYear": 2024,
      "totalPay": 111000000,
      "exercisedValue": 0,
      "unexercisedValue": 0
    },
    {
      "maxAge": 1,
      "name": "Mr. Hiroki  Totoki",
      "age": 60,
      "title": "President, CEO, Director & Representative Corporate Executive Officer",
      "yearBorn": 1964,
      "fiscalYear": 2024,
      "totalPay": 223000000,
      "exercisedValue": 0,
      "unexercisedValue": 0
    },
    {
      "maxAge": 1,
      "name": "Mr. Kenichiro  Yoshida",
      "age": 65,
      "title": "Chairman & Representative Corporate Executive Officer",
      "yearBorn": 1959,
      "fiscalYear": 2024,
      "totalPay": 651000000,
      "exercisedValue": 0,
      "unexercisedValue": 0
    },
    {
      "maxAge": 1,
      "name": "Lin  Tao",
      "title": "CFO & Corporate Executive Officer",
      "fiscalYear": 2024,
      "exercisedValue": 0,
      "unexercisedValue": 0
    },
    {
      "maxAge": 1,
      "name": "Mr. J. Justin Hill",
      "title": "Senior Vice President of Finance & Investor Relations and Head of Investor Relations",
      "fiscalYear": 2024,
      "exercisedValue": 0,
      "unexercisedValue": 0
    },
    {
      "maxAge": 1,
      "name": "Ms. Natsuko  Takei",
      "age": 63,
      "title": "Senior General Manager of Legal & Compliance Department",
      "yearBorn": 1961,
      "fiscalYear": 2024,
      "exercisedValue": 0,
      "unexercisedValue": 0
    },
    {
      "maxAge": 1,
      "name": "Yasuhiro  Ito",
      "title": "Chief People Officer, Corporate Exec Off. & Officer in charge of Human Res. & General Affairs",
      "fiscalYear": 2024,
      "exercisedValue": 0,
      "unexercisedValue": 0
    }
  ],
  "auditRisk": 1,
  "boardRisk": 1,
  "compensationRisk": 1,
  "shareHolderRightsRisk": 4,
  "overallRisk": 1,
  "governanceEpochDate": 1746057600,
  "compensationAsOfEpochDate": 1735603200,
  "executiveTeam": [],
  "maxAge": 86400,
  "priceHint": 2,
  "previousClose": 3663.0,
  "open": 3639.0,
  "dayLow": 3631.0,
  "dayHigh": 3756.0,
  "regularMarketPreviousClose": 3663.0,
  "regularMarketOpen": 3639.0,
  "regularMarketDayLow": 3631.0,
  "regularMarketDayHigh": 3756.0,
  "dividendRate": 20.0,
  "dividendYield": 0.54,
  "exDividendDate": 1743120000,
  "payoutRatio": 0.1022,
  "fiveYearAvgDividendYield": 0.57,
  "beta": 0.77,
  "trailingPE": 20.08071,
  "forwardPE": 20.37118,
  "volume": 14797500,
  "regularMarketVolume": 14797500,
  "averageVolume": 17345965,
  "averageVolume10days": 14228922,
  "averageDailyVolume10Day": 14228922,
  "bid": 3732.0,
  "ask": 3734.0,
  "bidSize": 0,
  "askSize": 0,
  "marketCap": 22459474509824,
  "fiftyTwoWeekLow": 2210.0,
  "fiftyTwoWeekHigh": 3904.0,
  "priceToSalesTrailing12Months": 1.6265804,
  "fiftyDayAverage": 3575.74,
  "twoHundredDayAverage": 3124.6924,
  "trailingAnnualDividendRate": 19.0,
  "trailingAnnualDividendYield": 0.0051870053,
  "currency": "JPY",
  "tradeable": false,
  "enterpriseValue": 25788499886080,
  "profitMargins": 0.082049996,
  "floatShares": 6021930804,
  "sharesOutstanding": 6018079744,
  "heldPercentInsiders": 0.00075999997,
  "heldPercentInstitutions": 0.4758,
  "impliedSharesOutstanding": 6232050176,
  "bookValue": 1358.498,
  "priceToBook": 2.7471516,
  "lastFiscalYearEnd": 1711843200,
  "nextFiscalYearEnd": 1743379200,
  "mostRecentQuarter": 1735603200,
  "earningsQuarterlyGrowth": 0.027,
  "netIncomeToCommon": 1132877971456,
  "trailingEps": 185.85,
  "forwardEps": 183.2,
  "lastSplitFactor": "5:1",
  "lastSplitDate": 1727395200,
  "enterpriseToRevenue": 1.868,
  "enterpriseToEbitda": 14.054,
  "52WeekChange": 0.4287902,
  "SandP52WeekChange": 0.09765589,
  "lastDividendValue": 10.0,
  "lastDividendDate": 1743120000,
  "quoteType": "EQUITY",
  "currentPrice": 3732.0,
  "targetHighPrice": 4800.0,
  "targetLowPrice": 3600.0,
  "targetMeanPrice": 4263.913,
  "targetMedianPrice": 4300.0,
  "recommendationMean": 1.5,
  "recommendationKey": "strong_buy",
  "numberOfAnalystOpinions": 23,
  "totalCash": 1415304970240,
  "totalCashPerShare": 234.898,
  "ebitda": 1835003019264,
  "totalDebt": 4378092896256,
  "quickRatio": 0.486,
  "currentRatio": 0.682,
  "totalRevenue": 13807786131456,
  "debtToEquity": 51.356,
  "revenuePerShare": 2272.571,
  "returnOnAssets": 0.02555,
  "returnOnEquity": 0.14321,
  "grossProfits": 3687152091136,
  "freeCashflow": 2171870511104,
  "operatingCashflow": 2065254973440,
  "earningsGrowth": 0.048,
  "revenueGrowth": 0.177,
  "grossMargins": 0.26703,
  "ebitdaMargins": 0.1329,
  "operatingMargins": 0.107370004,
  "financialCurrency": "JPY",
  "symbol": "6758.T",
  "language": "en-US",
  "region": "US",
  "typeDisp": "Equity",
  "quoteSourceName": "Delayed Quote",
  "triggerable": false,
  "customPriceAlertConfidence": "LOW",
  "regularMarketChange": 69.0,
  "regularMarketDayRange": "3631.0 - 3756.0",
  "fullExchangeName": "Tokyo",
  "averageDailyVolume3Month": 17345965,
  "fiftyTwoWeekLowChange": 1522.0,
  "fiftyTwoWeekLowChangePercent": 0.6886878,
  "fiftyTwoWeekRange": "2210.0 - 3904.0",
  "fiftyTwoWeekHighChange": -172.0,
  "fiftyTwoWeekHighChangePercent": -0.044057377,
  "fiftyTwoWeekChangePercent": 42.87902,
  "earningsTimestamp": 1747202400,
  "earningsTimestampStart": 1747202400,
  "earningsTimestampEnd": 1747202400,
  "earningsCallTimestampStart": 1747206000,
  "earningsCallTimestampEnd": 1747206000,
  "isEarningsDateEstimate": false,
  "epsTrailingTwelveMonths": 185.85,
  "epsForward": 183.2,
  "fiftyDayAverageChange": 156.26001,
  "fiftyDayAverageChangePercent": 0.043700047,
  "twoHundredDayAverageChange": 607.3076,
  "twoHundredDayAverageChangePercent": 0.19435757,
  "sourceInterval": 15,
  "exchangeDataDelayedBy": 20,
  "prevName": "Sony Corporation",
  "nameChangeDate": "2025-04-29",
  "averageAnalystRating": "1.5 - Strong Buy",
  "cryptoTradeable": false,
  "marketState": "CLOSED",
  "corporateActions": [],
  "regularMarketTime": 1746167400,
  "exchange": "JPX",
  "messageBoardId": "finmb_23021",
  "exchangeTimezoneName": "Asia/Tokyo",
  "exchangeTimezoneShortName": "JST",
  "gmtOffSetMilliseconds": 32400000,
  "market": "jp_market",
  "esgPopulated": false,
  "regularMarketChangePercent": 1.8837018,
  "regularMarketPrice": 3732.0,
  "hasPrePostMarketData": false,
  "firstTradeDateMilliseconds": 946944000000,
  "shortName": "SONY GROUP CORPORATION",
  "longName": "Sony Group Corporation",
  "trailingPegRatio": null
}
{{< /code >}}
{{< /accordion >}}


いろんな情報を取得する
----

| コード | 説明 | 値の例 |
| ---- | ---- | ---- |
| `t.info["shortName"]` | 企業の略称 | SONY GROUP CORPORATION |
| `t.info["longName"]` | 企業の正式名称 | Sony Group Corporation |
| `t.info["country"]` | 企業が所在する国 | Japan |
| `t.info["totalRevenue"]` | 売上高（総収益） | 13807786131456 |
| `t.info["grossProfits"]` | 売上総利益（粗利益） | 3687152091136 |
| `t.info[""]` | 営業利益 |  |
| `t.info[""]` |  |  |
| `t.info[""]` |  |  |
| `t.info["marketCap"]` | 時価総額 | 22459474509824 |
| `t.info["fullTimeEmployees"]` | 従業員数 | 113000 |


### ファンド情報

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


{{< accordion title="出力結果" >}}
{{< code >}}
                                                          2024-03-31        2023-03-31       2022-03-31       2021-03-31
Tax Effect Of Unusual Items                            21991079000.0     -2243134000.0      266500000.0    10220956000.0
Tax Rate For Calcs                                             0.227             0.206            0.205           0.3062
Normalized EBITDA                                    2357762000000.0   2316373000000.0  1966036000000.0  1666166000000.0
Total Unusual Items                                    96877000000.0    -10889000000.0     1300000000.0    33380000000.0
Total Unusual Items Excluding Goodwill                 96877000000.0    -10889000000.0     1300000000.0    33380000000.0
Net Income From Continuing Operation Net Minori...    970573000000.0   1005277000000.0   882178000000.0  1029610000000.0
Reconciled Depreciation                              1144981000000.0   1004590000000.0   835233000000.0   687373000000.0
Reconciled Cost Of Revenue                           9695687000000.0   7739284000000.0  7219841000000.0  6567553000000.0
EBITDA                                               2454639000000.0   2305484000000.0  1967336000000.0  1699546000000.0
EBIT                                                 1309658000000.0   1300894000000.0  1132103000000.0  1012173000000.0
Net Interest Income                                    -5703000000.0    -12269000000.0   -19839000000.0    -3924000000.0
Interest Expense                                       40996000000.0     26398000000.0    14600000000.0    14208000000.0
Interest Income                                        37580000000.0     22399000000.0     6996000000.0     7610000000.0
Normalized Income                                     895687079000.0   1013922866000.0   881144500000.0  1006450956000.0
Net Income From Continuing And Discontinued Ope...    970573000000.0   1005277000000.0   882178000000.0  1029610000000.0
Total Expenses                                      11853782000000.0   9701168000000.0  8809117000000.0  8041703000000.0
Total Operating Income As Reported                   1208831000000.0   1302389000000.0  1202339000000.0   955255000000.0
Diluted Average Shares                                  6176655000.0      6206885000.0     6256300000.0     6253460000.0
Basic Average Shares                                    6156210000.0      6178505000.0     6196495000.0     6152400000.0
Diluted EPS                                                  157.136            161.97          141.032           187.38
Basic EPS                                                    157.658           162.706          142.368          190.458
Diluted NI Availto Com Stockholders                   970573000000.0   1005328000000.0   882341000000.0  1029995000000.0
Average Dilution Earnings                                        0.0        51000000.0      163000000.0      385000000.0
Net Income Common Stockholders                        970573000000.0   1005277000000.0   882178000000.0  1029610000000.0
Net Income                                            970573000000.0   1005277000000.0   882178000000.0  1029610000000.0
Minority Interests                                     -9921000000.0     -6496000000.0    -6228000000.0   -14286000000.0
Net Income Including Noncontrolling Interests         980494000000.0   1011773000000.0   888406000000.0  1043896000000.0
Net Income Continuous Operations                      980494000000.0   1011773000000.0   888406000000.0  1043896000000.0
Tax Provision                                         288168000000.0    262723000000.0   229097000000.0   -45931000000.0
Pretax Income                                        1268662000000.0   1274496000000.0  1117503000000.0   997965000000.0
Other Income Expense                                  107379000000.0     13560000000.0    24946000000.0    44931000000.0
Other Non Operating Income Expenses                              NaN               NaN    69217000000.0    -8737000000.0
Special Income Charges                                 31343000000.0      4735000000.0    66297000000.0   -13254000000.0
Gain On Sale Of Ppe                                     4675000000.0       417000000.0    -8316000000.0   -32122000000.0
Gain On Sale Of Business                               26668000000.0      4318000000.0    74613000000.0    18868000000.0
Restructuring And Mergern Acquisition                            NaN               NaN              NaN              0.0
Earnings From Equity Interest                          10502000000.0     24449000000.0    23646000000.0    11551000000.0
Gain On Sale Of Security                               65534000000.0    -15624000000.0   -64997000000.0    46634000000.0
Net Non Operating Interest Income Expense              -5703000000.0    -12269000000.0   -19839000000.0    -3924000000.0
Total Other Finance Cost                                2287000000.0      8270000000.0    12235000000.0    -2674000000.0
Interest Expense Non Operating                         40996000000.0     26398000000.0    14600000000.0    14208000000.0
Interest Income Non Operating                          37580000000.0     22399000000.0     6996000000.0     7610000000.0
Operating Income                                     1166986000000.0   1273205000000.0  1112396000000.0   956958000000.0
Operating Expense                                    2158095000000.0   1961884000000.0  1589276000000.0  1474150000000.0
Other Operating Expenses                                1939000000.0     -7286000000.0      803000000.0      996000000.0
Selling General And Administration                   2156156000000.0   1969170000000.0  1588473000000.0  1473154000000.0
Gross Profit                                         3325081000000.0   3235089000000.0  2701672000000.0  2431108000000.0
Cost Of Revenue                                      9695687000000.0   7739284000000.0  7219841000000.0  6567553000000.0
Total Revenue                                       13020768000000.0  10974373000000.0  9921513000000.0  8998661000000.0
Operating Revenue                                   13020768000000.0  10974373000000.0  9921513000000.0  8998661000000.0
{{< /code >}}
{{< /accordion >}}

