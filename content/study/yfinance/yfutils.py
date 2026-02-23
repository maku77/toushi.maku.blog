import diskcache
import yfinance as yf

cache = diskcache.Cache(directory=".cache")


@cache.memoize()
def fetch_ticker_info(symbol: str) -> dict:
    return yf.Ticker(symbol).info


def print_info_tables(info: dict) -> None:
    categories = {
        "基本情報": [
            ("shortName", "会社名", "会社の短い名称"),
            ("symbol", "ティッカー", "取引所での銘柄コード"),
            ("exchange", "取引所", "上場している取引所"),
            ("sector", "セクター", "事業分野の大分類"),
            ("industry", "業種", "より具体的な業種区分"),
            ("country", "国", "本社所在地の国"),
            ("website", "公式サイト", "企業の公式Webサイト"),
        ],
        "株価・評価": [
            ("currentPrice", "現在株価", "最新の取引価格"),
            ("marketCap", "時価総額", "発行済株式数×株価"),
            ("enterpriseValue", "企業価値 (EV)", "時価総額+純有利子負債"),
            ("trailingPE", "PER(実績)", "株価÷直近EPS"),
            ("forwardPE", "PER(予想)", "株価÷予想EPS"),
            ("priceToSalesTrailing12Months", "PSR(TTM)", "株価÷直近売上"),
            ("priceToBook", "PBR", "株価÷1株純資産"),
        ],
        "収益性": [
            ("profitMargins", "利益率", "売上に対する純利益率"),
            ("grossMargins", "粗利率", "売上に対する粗利益率"),
            ("operatingMargins", "営業利益率", "売上に対する営業利益率"),
            ("returnOnAssets", "ROA", "総資産利益率"),
            ("returnOnEquity", "ROE", "自己資本利益率"),
        ],
        "財務": [
            ("totalRevenue", "売上高(TTM)", "直近12か月の売上"),
            ("ebitda", "EBITDA", "利払い・税引き前利益"),
            ("totalCash", "現金等", "手元資金"),
            ("totalDebt", "有利子負債", "借入や社債など"),
            ("freeCashflow", "フリーCF", "営業CF−投資CF"),
        ],
        "配当": [
            ("dividendRate", "配当額", "1株あたり配当"),
            ("dividendYield", "配当利回り", "配当÷株価"),
            ("payoutRatio", "配当性向", "利益のうち配当の割合"),
        ],
        "取引情報": [
            ("volume", "出来高", "直近の売買高"),
            ("averageVolume", "平均出来高", "平均の売買高"),
            ("fiftyTwoWeekHigh", "52週高値", "過去52週の最高値"),
            ("fiftyTwoWeekLow", "52週安値", "過去52週の最安値"),
        ],
    }

    for category, items in categories.items():
        print(f"\n### {category}\n")
        print("| キー | 日本語名 | 概要 | 値の例 |")
        print("| ---- | ---- | ---- | ---- |")
        for key, label, summary in items:
            value = info.get(key, "-")
            print(f"| `{key}` | {label} | {summary} | {value} |")

