---
title: "FX 時刻表"
url: "/p/9vqo9fk"
date: "2016-01-17"
tags: ["FX"]
---

為替の世界は 24 時間動いています。
現在主要なマーケットは、ロンドン市場、ニューヨーク市場、東京市場の 3 つです。
中でもロンドン市場と、ニューヨーク市場の時間帯が重なる午後 11 時前後は、取引が盛んに行われるため、為替レートが大きく動きます。
FX で一攫千金を狙おうとする人たちも、この時間帯は特に集中しています。

<center>
  <canvas id="my-canvas" style="max-width: 100%" width="680" height="800"></canvas>
</center>

下記に、世界の為替市場の取引時間、証券取引所の Web サイトへのリンクをまとめておきます。

世界の市場の取引時間 (JST) ※カッコ内は夏時間
----

### オセアニア
- ウェリントン市場（ニュージーランド）- [New Zealand Exchange](http://www.nzx.com/)
    - 為替市場: 6:00〜14:00 (5:00〜13:00)
    - 株式市場: 7:00〜13:45 (6:00〜12:45)（現地時間 10:00〜16:45）
- シドニー市場（オーストラリア）- [Australian Securities Exchange](http://www.asx.com.au/)
    - 為替市場: 6:00〜15:00 (5:00〜14:00)</li>
    - 株式市場: 9:00〜15:45 (8:00〜14:45)（現地時間 10:00〜16:45）</li>

### アジア
- 東京（日本）★ - [日本取引所グループ (JPX: Japan Exchange Group)](http://www.jpx.co.jp/)
    - 為替市場: 9:00〜17:00
    - 株式市場: 9:00〜11:30、12:30〜15:00
- 香港市場（香港）- [Hong Kong Exchanges](http://www.hkex.com.hk/)
    - 為替市場: 10:00〜18:00
    - 株式市場: 11:00～13:30、15:30〜17:00（現地時間: 10:00〜12:30、14:30〜16:00）
- 上海市場（中国）- [Shanghai Stock Exchange](http://english.sse.com.cn/)
    - 株式市場: 10:30〜18:30（現地時間: 9:30〜15:30）
- シンガポール市場（シンガポール）- [Singapore Exchange](http://www.sgx.com/)
    - 為替市場: 10:00〜18:00（現地時間: 9:00〜17:00）
- ムンバイ市場（インド）
    - 為替市場: 13:25〜19:00（現地時間: ）昼休みなし
- バーレーン（バーレーン）
    - 為替市場 (14:00〜23:00)

### ヨーロッパ
- フランクフルト市場（ドイツ）- [Frankfurt Stock Exchange](http://www.boerse-frankfurt.de/en/start)
    - 為替市場: 17:00〜1:00 (16:00〜0:00)
    - 株式市場: 17:30〜1:30 (16:30〜0:30)（現地時間: 9:30〜17:30）
- チューリッヒ（スイス）
    - 為替市場 (17:00〜3:00)
- ロンドン市場（イギリス）★ - [London Stock Exchange](http://www.londonstockexchange.com/)
    - 為替市場: 17:00〜2:00 (16:00〜0:00)
    - 株式市場: 17:30〜1:30 (16:30〜0:30) （現地時間: 8:30〜16:30）

###  アフリカ
- ヨハネスブルグ市場（南アフリカ）- [Johannesburg Stock Exchange](https://www.jse.co.za/)
    - 株式市場: 16:00〜23:30（現地時間: 9:00〜16:30）

###  アメリカ
- ニューヨーク市場（アメリカ）★ - [New York Stock Exchange](https://www.nyse.com)
    - 為替市場: 22:30〜7:00 (21:30〜6:00)
    - 株式市場: 23:30〜6:00 (22:30〜5:00) （現地時間: 9:30〜16:00）昼休みなし
- トロント市場（カナダ）- [Toronto Stock Exchange](http://www.tsx.com/)
    - 株式市場: 23:30〜6:00 (22:30〜5:00) （現地時間: 9:30〜16:00）


FX の重要時間
----

- **ロンドンフィックス: 25:00（夏: 24:00）**
    - 世界の金の値段である、スポット価格を決めます。金はドル建てで取引されるため、ドルに関連する相場が大きく動きます。
- **NY オプションカット: 24:00（夏: 23:00）**
    - オプションカットは通貨オプションの権利行使期限です。相場が大きく動きます。
- **東京仲値算定: 9:55**
    - 各銀行が仲値 (TTM) を決定する時間帯で、取引が活発化します。
    - 仲値不足により、銀行によるドル買いが起こることがあります。
    - 特に**ゴトウ日（5 の倍数の日）**は企業等の大口決済が多く、取引が活発になります。


各国の夏時間（サマータイム）
----

- <b>ニュージーランド（一部除く）</b>
    - 9月最終日曜日 2:00 〜 4月第1日曜日 3:00（現地時間）
- <b>オーストラリア</b>
    - 10月最終日曜日 2:00 〜 3月最終日曜日 3:00（現地時間）
- <b>欧州</b>
    - 3月最終日曜日 〜 10月最終日曜日
- <b>アメリカ</b>
    - 3月第2日曜日 〜 11月第1日曜日（エネルギー政策法により改定されました。2007年以前は、4月第1日曜日午前2時〜10月最終日曜日午前2時でした）


<script>
$(function() {
  'use strict';
  var Layout = new function() {
    // Base position
    this.MARGIN_TOP = 50;
    this.MARGIN_LEFT = 50;

    // Market
    this.OFFSET_MARKET_X = this.MARGIN_LEFT + 50;
    this.OFFSET_MARKET_Y = this.MARGIN_TOP;
    this.OFFSET_MARKET_LABEL_X = this.OFFSET_MARKET_X + 5;
    this.OFFSET_MARKET_LABEL_Y = this.OFFSET_MARKET_Y - 10;
    this.MARKET_WIDTH = 100;
    this.MARKET_HEIGHT = 30;

    // Time labels
    this.OFFSET_TIME_LABEL_X = this.MARGIN_LEFT;
    this.OFFSET_TIME_LABEL_Y = this.MARGIN_TOP + 5;

    // Schedules labels
    this.SCHEDULE_LABEL_FONT = '9pt sans-serif';
    this.OFFSET_SCHEDULE_LABEL_X = this.OFFSET_MARKET_X + (this.MARKET_WIDTH * 3) + 5;
    this.OFFSET_SCHEDULE_LABEL_Y = this.OFFSET_MARKET_Y + 5;

    // Colors
    this.COLOR_TIME_LABEL = '#333';
    this.COLOR_TIME_LINE = '#ccc';
    this.COLOR_MARKET_LABEL = '#333'
    this.COLOR_SCHEDULE_LABEL = 'green'
    this.COLOR_LONDON = '#fcc';
    this.COLOR_LONDON_STOCK = '#e99';
    this.COLOR_NEWYORK = '#cfc';
    this.COLOR_NEWYORK_STOCK = '#6c6';
    this.COLOR_TOKYO = '#cef';
    this.COLOR_TOKYO_STOCK = '#6cf';
  }();

  var canvas = document.getElementById('my-canvas');
  var c = canvas.getContext('2d');

  // Market Labels
  drawMarketLabel(c, 0, 'ロンドン');
  drawMarketLabel(c, 1, 'NY');
  drawMarketLabel(c, 2, '東京');

  // Market Cells
  drawMarketCells(c, 0, 0, 2, Layout.COLOR_LONDON);
  drawMarketCells(c, 0, 17, 24, Layout.COLOR_LONDON);
  drawMarketCells(c, 0, 0, 1.5, Layout.COLOR_LONDON_STOCK);
  drawMarketCells(c, 0, 17.5, 24, Layout.COLOR_LONDON_STOCK);

  drawMarketCells(c, 1, 0, 7, Layout.COLOR_NEWYORK);
  drawMarketCells(c, 1, 22.5, 24, Layout.COLOR_NEWYORK);
  drawMarketCells(c, 1, 0, 6, Layout.COLOR_NEWYORK_STOCK);
  drawMarketCells(c, 1, 23.5, 24, Layout.COLOR_NEWYORK_STOCK);

  drawMarketCells(c, 2, 8.5, 17, Layout.COLOR_TOKYO);
  drawMarketCells(c, 2, 9, 11.5, Layout.COLOR_TOKYO_STOCK);
  drawMarketCells(c, 2, 12.5, 15, Layout.COLOR_TOKYO_STOCK);

  // Schedules
  drawScheduleLabel(c, 0, ' 0:00(冬) NY オプションカット★');
  drawScheduleLabel(c, 1, ' 1:00(冬) ロンドンフィックス★');
  drawScheduleLabel(c, 1.5, ' 1:30(冬) ロンドン株式市場終了');
  drawScheduleLabel(c, 3, ' 3:00(冬) NY 株式市場お昼休み');
  drawScheduleLabel(c, 6, ' 6:00(冬) NY 株式市場終了');
  drawScheduleLabel(c, 8.5, ' 8:30 日本の指標発表の時間帯★');
  drawScheduleLabel(c, 9, ' 9:00 東京株式市場開始（寄り付き）');
  drawScheduleLabel(c, 9.9, ' 9:55 東京仲値算定★');
  drawScheduleLabel(c, 11.5, '11:30 東京株式前場終了');
  drawScheduleLabel(c, 12.5, '12:30 東京株式後場開始');
  drawScheduleLabel(c, 15, '15:00 東京株式市場終了、東京カット');
  drawScheduleLabel(c, 17.5, '17:30(冬) ロンドン株式市場開始（寄り付き）');
  drawScheduleLabel(c, 18, '18:00(冬) 欧州の指標発表の時間帯★');
  drawScheduleLabel(c, 20.5, '20:30(冬) 欧州市場お昼休み');
  drawScheduleLabel(c, 22.5, '22:30(冬) アメリカの指標発表の時間帯★');
  drawScheduleLabel(c, 23.5, '23:30(冬) NY 株式市場開始（寄り付き）');
  drawScheduleLabel(c, 24, '24:00(冬) NY オプションカット★');

  // Time-bar
  drawTimeLines(c);
  drawTimeLabels(c);

  function drawMarketCells(ctx, index, fromHour, toHour, color) {
    var x = Layout.OFFSET_MARKET_X + (Layout.MARKET_WIDTH * index);
    var y = Layout.OFFSET_MARKET_Y + (Layout.MARKET_HEIGHT * fromHour);
    var h = Layout.MARKET_HEIGHT * (toHour - fromHour);
    ctx.fillStyle = color;
    ctx.fillRect(x, y, Layout.MARKET_WIDTH, h);
  }

  function drawTimeLines(ctx) {
    ctx.beginPath();
    ctx.strokeStyle = Layout.COLOR_TIME_LINE;
    var x1 = Layout.OFFSET_MARKET_X;
    var x2 = Layout.OFFSET_MARKET_X + (Layout.MARKET_WIDTH * 3);
    for (var i = 0; i < 25; ++i) {
      var y = Layout.MARGIN_TOP + (Layout.MARKET_HEIGHT * i);
      ctx.moveTo(x1, y);
      ctx.lineTo(x2, y);
    }
    ctx.stroke();
  }

  function drawTimeLabels(ctx) {
    ctx.font = "12pt sans-serif";
    ctx.fillStyle = Layout.COLOR_TIME_LABEL;

    for (var i = 0; i <= 24; ++i) {
      ctx.fillText(i + ':00', Layout.OFFSET_TIME_LABEL_X,
          Layout.OFFSET_TIME_LABEL_Y + (Layout.MARKET_HEIGHT * i));
    }
  }

  function drawMarketLabel(ctx, index, label) {
    ctx.font = "Bold 12pt sans-serif";
    ctx.fillStyle = Layout.COLOR_MARKET_LABEL;
    ctx.fillText(label, Layout.OFFSET_MARKET_LABEL_X + (Layout.MARKET_WIDTH * index),
        Layout.OFFSET_MARKET_LABEL_Y);
  }

  function drawScheduleLabel(ctx, hour, label) {
    ctx.font = Layout.SCHEDULE_LABEL_FONT;
    ctx.fillStyle = Layout.COLOR_SCHEDULE_LABEL;
    ctx.fillText(label, Layout.OFFSET_SCHEDULE_LABEL_X,
        Layout.OFFSET_SCHEDULE_LABEL_Y + (Layout.MARKET_HEIGHT * hour));
  }
});

function TimeCell(index) {
  var WIDTH = 48, HEIGHT = 30;

  // Public properties.
  var that = {
    draw: function(ctx) {
      var x1 = (WIDTH + 2) * index + 10;
      ctx.fillStyle = '#dee';
      ctx.fillRect(x1, 10, WIDTH, HEIGHT);
      drawText(ctx);
    }
  };

  // index: 0-23
  function drawText(ctx) {
    ctx.font = "10pt sans-serif";
    ctx.fillStyle = 'black';
    ctx.fillText(index, 50 * index, 100);
  }

  // Returns public properties.
  return that;
}
</script>
