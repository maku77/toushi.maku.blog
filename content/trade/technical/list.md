---
title: "テクニカル指標の一覧"
url: "p/7y8y8yw/"
tags: ["テクニカル指標"]
date: "2017-09-24"
weight: 1
---

{{% private %}}
- 移動平均のダマシを軽減するコツ ... 終値ではなく、高値と安値の中間値 (median price) を使う。
{{% /private %}}

<script>
document.addEventListener('DOMContentLoaded', function() {
  const arr = [
    { en: "Bill William's Alligator Oscillator", jp: '', tags: ['trend'] },
    { en: "Bill William's Alligator", jp: '', tags: ['trend'] },
    { en: "Lane's Stochastic Oscillator", jp: '', tags: ['momentum'] },
    { en: "Williams’ Percent Range", jp: 'ウィリアム％Ｒ', tags: ['momentum'] },
    { en: '', jp: '株価移動平均乖離線', tags: ['momentum'] },
    { en: 'A/D (Accumulation Distribution) Ocsillator', jp: '騰落オシレーター', tags: ['momentum'] },
    { en: 'AB Ratio', jp: '強弱レシオ', tags: ['momentum'] },
    { en: 'ADX/DMI', jp: '', tags: ['trend'], url: '/p/9ju3pvu/' },
    { en: 'ADXR', jp: '', tags: ['trend'] },
    { en: 'ASI: Accumulation Swing Index', jp: '集積スイング・インデックス', tags: ['momentum'], note: '考案者: J.W.ワイルダー(Welles Wilder)' },
    { en: 'Accelerator/Decelerator', jp: 'AC オシレーター', tags: ['momentum'] },
    { en: 'Adaptive Moving Average', jp: '', tags: ['ma'] },
    { en: 'Anti-Watch Curve, Contrary Watch Curve, Counter Clock Curve', jp: '逆ウォッチ曲線', tags: ['sp'] },
    { en: 'Arnaud Legoux Moving Average', jp: '', tags: ['ma'] },
    { en: 'Aroon Oscillator', jp: '', tags: ['trend'] },
    { en: 'Aroon Up/Dn', jp: '', tags: ['trend'] },
    { en: 'Bollinger Bands', jp: 'ボリンジャーバンド', tags: ['momentum', 'ma'], url: '/p/s6djqv3/' },
    { en: 'Chaikin Money Flow', jp: 'チャイキン・マネー・フロー', tags: ['momentum'] },
    { en: 'Chaikin Oscillator', jp: 'チャイキン・オシレーター', tags: ['momentum'] },
    { en: 'Chande Momentum Oscillator', jp: '', tags: ['momentum'] },
    { en: 'Chop Zone', jp: '', tags: ['trend'] },
    { en: 'Choppiness Index', jp: '', tags: ['trend'] },
    { en: 'Connors RSI', jp: '', tags: ['trend'] },
    { en: 'Coppock Curve', jp: '', tags: ['trend'] },
    { en: 'DMI: Directional Movement Index', jp: '方向性指数', tags: ['trend'], url: '/p/9ju3pvu/' },
    { en: 'Delta', jp: 'デルタ', tags: ['momentum', 'op'], note: 'オプションプレミアムの変化率' },
    { en: 'Departure Chart', jp: '', tags: ['ma'] },
    { en: 'Detrended Price Oscillator', jp: '', tags: ['trend'] },
    { en: 'Donchian Channel Width', jp: '', tags: ['trend'] },
    { en: 'Donchian Channels', jp: '', tags: ['trend'] },
    { en: 'Double Exponential Moving Avg', jp: '', tags: ['ma'] },
    { en: 'Ease of Movement', jp: '', tags: ['ma'] },
    { en: 'Elder-Ray', jp: '', tags: ['momentum'] },
    { en: 'Elder Impulse  System', jp: '', tags: ['trend'] },
    { en: 'Envelope', jp: 'エンベロープ', tags: ['momentum'] },
    { en: 'Fast Stochastic Oscillator', jp: 'ファスト・ストキャスティクス', tags: ['momentum'], url: '/p/ibp4usz/' },
    { en: 'Fibonacci Retracement', jp: 'フィボナッチ（フィボナッチ・リトレースメント）', tags: ['sp'] },
    { en: 'Force Index', jp: '', tags: ['momentum'] },
    { en: 'GMMA', jp: '複合型移動平均線', tags: ['ma', 'trend'], url: '/p/92izet9/', note: '考案者: ダリル・グッピー。12本のEMA（指数平滑移動平均線）を使用する。' },
    { en: 'High & Low Channel', jp: 'HL バンド', tags: ['trend'] },
    { en: 'Hull Moving Average', jp: '', tags: ['ma'] },
    { en: 'IV: Implied Volatility', jp: 'インプライド・ボラティリティ', tags: ['momentum', 'op'] },
    { en: 'Ichimoku', jp: '一目均衡表', tags: ['ma', 'sp'], note: '考案者: 一目山人' },
    { en: 'Intraday Intensity %', jp: '', tags: ['momentum'] },
    { en: 'Intraday Intensity', jp: '', tags: ['momentum'] },
    { en: 'Know Sure Thing', jp: '', tags: ['ma'] },
    { en: 'MA Crossover', jp: '', tags: ['ma'] },
    { en: 'MACD: Moving Average Convergence/Divergence', jp: '移動平均収束発散法', tags: ['momentum'], url: '/p/hj7nm4h/' },
    { en: 'MFI: Money Flow Index', jp: 'マネー・フロー・インデックス', tags: ['momentum'] },
    { en: 'Mass Index', jp: '', tags: ['trend'] },
    { en: 'McGinley Dynamic', jp: '', tags: ['ma'] },
    { en: 'Momentum', jp: 'モメンタム', tags: ['momentum'], url: '/p/q7gow5c/', note: '一定期間前の価格に対して、現在の価格がどれくらいの比率（％）かを表します。同じ価格ならば 100 で、値段が倍になっているのであれば 200 となります。' },
    { en: 'Moving Standard Deviation', jp: '', tags: ['ma'] },
    { en: 'Normal Stochastic Oscillator', jp: 'ノーマル・ストキャスティクス', tags: ['momentum'], url: '/p/ibp4usz/' },
    { en: 'Parabolic SAR', jp: 'パラボリック SAR', tags: ['trend'] },
    { en: 'Percent B', jp: '', tags: ['ma'] },
    { en: 'Percentage Price Oscillator', jp: '', tags: ['momentum'] },
    { en: 'Pivot Points High/Low', jp: 'ピボットポイント', tags: ['sp'], note: '考案者：J.W.ワイルダー(Welles Wilder)' },
    { en: 'Point and Figure', jp: 'ポイント＆フィギュア', tags: ['sp', 'trend'] },
    { en: 'Price Oscillator', jp: '', tags: ['momentum'] },
    { en: 'Price Volume Trend', jp: '', tags: ['trend'] },
    { en: 'Psychological Line', jp: 'サイコロジカル・ライン', tags: ['momentum'] },
    { en: 'RCI: Rank Correlation Index', jp: '順位相関係数', tags: ['momentum'] },
    { en: 'ROC: Rate Of Change', jp: 'レート・オブ・チェンジ', tags: ['momentum'] },
    { en: 'RSI: Relative Strength Index', jp: '相対力指数', tags: ['momentum'], url: '/p/trghokn/' },
    { en: 'Ratiocator', jp: 'レシオケータ', tags: ['momentum'], note: '日経平均株価と個別銘柄株価の乖離を示します。' },
    { en: 'Relative Vigor Index', jp: '', tags: ['trend'] },
    { en: 'Slow Stochastic Oscillator', jp: 'スロー・ストキャスティクス', tags: ['momentum'], url: '/p/ibp4usz/' },
    { en: 'Stochastic Oscillator', jp: 'ストキャスティクス', tags: ['momentum'], url: '/p/ibp4usz/' },
    { en: 'Stochastic RSI', jp: 'ストキャスティック RSC', tags: ['momentum'] },
    { en: 'Swing Index', jp: '', tags: ['trend'] },
    { en: 'TRIX', jp: '', tags: ['ma'] },
    { en: 'Three Line Break', jp: '新値足（スリーラインブレイク）', tags: ['sp'] },
    { en: 'Triangular Moving Average', jp: '', tags: ['ma'] },
    { en: 'Triple Exponential Moving Avg', jp: '', tags: ['ma'] },
    { en: 'True Strength Index', jp: '', tags: ['momentum'] },
    { en: 'Typical Price', jp: '', tags: ['trend'] },
    { en: 'VAP: Volume at Price', jp: '価格帯別出来高', tags: ['sp'] },
    { en: 'VR: Volume Ratio', jp: 'ボリューム・レシオ', tags: ['momentum'], note: 'RSI の出来高版。' },
    { en: 'Variable Moving Average', jp: '', tags: ['ma'] },
    { en: 'Vertical Horizontal Filter', jp: '', tags: ['trend'] },
    { en: 'Vortex', jp: '', tags: ['trend'] },
    { en: 'Weighted Close', jp: '', tags: ['trend'] },
    { en: 'Wilder Moving Average', jp: '', tags: ['ma'] },
    { en: 'ZigZag', jp: 'ジグザグ', tags: ['trend'] },
    { en: '', jp: 'ケルトナー・チャネル', tags: ['momentum'] },
    { en: '', jp: 'コモディティー・チャネル', tags: ['momentum'] },
    { en: '', jp: 'パフォーマンス', tags: ['trend'] },
    { en: '', jp: 'パラボリック', tags: ['trend'] },
    { en: 'WMA: Weighted Moving Average', jp: '加重移動平均', tags: ['ma'] },
    { en: 'SMA: Simple Moving Average', jp: '単純移動平均', tags: ['ma'] },
    { en: 'EMA: Exponential Moving Average', jp: '指数平滑移動平均', tags: ['ma'], url: '/p/67gvggc/' },
    { en: '', jp: '究極のオシレーター', tags: ['ma'] },
  ];
  let html = '';
  for (let i = 0; i < arr.length; ++i) {
    const e = arr[i];
    html += '<tr>';
    if (e.url) {
      html += '<td><a href="' + e.url + '">' + e.en + '</td>';
      html += '<td><a href="' + e.url + '">' + e.jp + '</td>';
    } else {
      html += '<td>' + e.en + '</td>';
      html += '<td>' + e.jp + '</td>';
    }
    html += '<td style="text-align:center">' + (e.tags.indexOf('momentum') != -1 ? 'モ' : '-') + '</td>';
    html += '<td style="text-align:center">' + (e.tags.indexOf('trend') != -1 ? 'ト' : '-') + '</td>';
    html += '<td style="text-align:center">' + (e.tags.indexOf('ma') != -1 ? '移' : '-') + '</td>';
    html += '<td style="text-align:center">' + (e.tags.indexOf('sp') != -1 ? '特' : '-') + '</td>';
    html += '<td style="text-align:center">' + (e.tags.indexOf('op') != -1 ? 'Op' : '-') + '</td>';
    html += '<td>' + (e.note ? e.note : '-') + '</td>';
    html += '</tr>';
  }
  document.getElementById('placeholder').innerHTML += html;
});
</script>


テクニカル指標の種類
----

テクニカル指標は大きく分けて、トレンド系（順張り系）とオシレーター系（逆張り系）の指標に分けることができます。

トレンド系（順張り系）
: トレンド系の指標は相場の方向性を判断するために用いられます。移動平均線などが代表的です。

オシレーター系／モメンタム系（逆張り系）
: オシレータ系の指標は、相場の勢いや、買われ過ぎや売られ過ぎなどの情報を示します。オシレータ (oscillator) とは「振動するもの」という意味を持っており、その名の通り、一定の範囲内で値が上下する性質を持っています。


テクニカル指標一覧
----

<table id="placeholder" style="font-size: smaller">
    <tr>
        <th>指標名（英語）</th>
        <th>指標名（日本語）</th>
        <th>モメンタム系</th>
        <th>トレンド系</th>
        <th>移動平均</th>
        <th>特殊</th>
        <th>オプション</th>
        <th>ノート</th>
    </tr>
</table>


その他
----

### 回帰分析
- Awesome Oscillator
- Least Squares Moving Average
- Linear Regression (Least Square)
- Linear Regression Curve
- Linear Regression Intercept
- Linear Regression R-Squared
- Linear Regression Slope
- Raff Channel
- Standard Deviation Channel

### ボラティリティ
- [ATR: Average True Range](/p/tasaq7n)
- Chaikin Volatility
- Chande Volatility Index Dynamic Average
- Historical Volatility Ratio
- Relative Volatility Index

### 出来高分析
- Klinger Volume Oscillator
- Negative Volume Index
- Percentage Volume Oscillator
- Positive Volume Index
- Volume ＊ PMO
- Volume Exponential Moving Average
- Volume Oscillator
- Volume Simple Moving Average
- Volume Weighted Moving Average
- オン・バランス・ボリューム (OBV)
- 加重平均価格

