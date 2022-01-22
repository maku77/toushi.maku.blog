---
title: "FX（外国為替証拠金取引）"
url: "/p/xbskchu"
linkTitle: "FX"
weight: 1000
---

<!-- 以下 FX Clock 実装 -->
<center>
  <canvas id="canvas" width="300" height="90"></canvas>
  <div>FX Clock</div>
</center>

<script>
var ZONES = [
  { label: 'TK', tz: 'Asia/Tokyo' },  // 東京（日本）
  { label: 'GB', tz: 'Europe/London' },  // ロンドン（イギリス）
  { label: 'NY', tz: 'America/New_York' },  // ニューヨーク（アメリカ）
];

function convertDateByTimeZone(date, tz) {
  var str = date.toLocaleString('ja-JP', { timeZone: tz });
  return new Date(str);
}

// 0時からの経過秒数を計算
function getElapsedSeconds(date) {
  return (date.getHours() * 60 * 60) +
    (date.getMinutes() * 60) + date.getSeconds();
}

window.onload = function() {
  var INTERVAL = 1000;  // ms
  var FONT = '16pt monospace';
  var BAR_OFFSET_X = 40;
  var BAR_HEIGHT = 30;
  var canvas = document.getElementById('canvas');  // HTMLCanvasElement
  var ctx = canvas.getContext('2d');  // CanvasRenderingContext2D

  function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  }

  function drawTimeBar(index, label, date) {
    var maxBarWidth = canvas.width - BAR_OFFSET_X;

    // 時刻バー（背景）
    ctx.fillStyle = "#aaa";
    ctx.fillRect(BAR_OFFSET_X, BAR_HEIGHT * index, maxBarWidth, BAR_HEIGHT);

    // 時刻バー（前景）
    var barWidth = maxBarWidth * getElapsedSeconds(date) / (24 * 60 * 60);
    ctx.fillStyle = "rgba(255, 0, 0, 0.5)";
    ctx.fillRect(BAR_OFFSET_X, BAR_HEIGHT * index, barWidth, BAR_HEIGHT);


    // ラベル
    ctx.font = FONT;
    ctx.fillStyle = '#333';
    ctx.fillText(label, 5, BAR_HEIGHT * index + 25);

    // 時刻文字列
    var hh = ('0' + date.getHours()).slice(-2);
    var mm = ('0' + date.getMinutes()).slice(-2);
    var ss = ('0' + date.getSeconds()).slice(-2);
    var timeStr = hh + ':' + mm + ':' + ss;
    ctx.fillStyle = 'white';
    var drawWidth = ctx.measureText(timeStr).width;
    ctx.fillText(timeStr, BAR_OFFSET_X + ((maxBarWidth - drawWidth) / 2),
      (BAR_HEIGHT * index) + BAR_HEIGHT * 0.8);
  }

  function start() {
    setTimeout(function() {
      clearCanvas();
      var date = new Date();
      for (var i = 0; i < ZONES.length; ++i) {
        var d = convertDateByTimeZone(date, ZONES[i].tz);
        drawTimeBar(i, ZONES[i].label, d)
      }
      start();
    }, INTERVAL);
  }
  start();
};
</script>


- 外部リンク: [MetaTrader によるシステムトレード](http://maku77.github.io/mt/)

### FX のファーストステップ

規律のある FX 取引を始めるためのファーストステップは、ルールを決めることです。まずはここから始めよう。

* 1回の取引あたりの最大損失は？
    * 1回の取引通貨量を決める
    * 最大損切 pips を決める
    * 最小利食い pips を決める

