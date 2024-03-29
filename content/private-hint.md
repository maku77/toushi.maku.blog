---
title: "（個人的）投資ヒント"
url: "p/ojrrxj4/"
date: "2024-01-05"
draft: true
---

- 大切なこと・信念
  - シストレには試行回数が必要（再現性が重要なので 1000 回以上のトレードは必要）
  - 机上の理論だけではなく、繰り返しのトレードによる技術向上が必要

- 買いから入るときも、売りから入るときも __2 分割で入る__。決済は一括で OK。これは波に乗るための経験則。 <!-- 2024-01-27 相場師スクリーニングを参考 -->

- ローリング ... 定期市場で順ザヤの先物を売り続ける <!-- 2024-01-27 相場師スクリーニングを参考 -->

- 相場師スクリーニング（林輝太郎）
  - 先物の順ザヤを売り続ける
    1. 順ざやの先 3 本ないし 4 本が一代の高値を更新してから売り始める。
    2. ひと単位の売り建て玉数を定めておき、新甫で売るのはそのうちの最小の 1 単位または 2 単位。
    3. 残りは、さらに高値が出たときか、サヤにより、値動きにより、10日、20日と日を決めて、のどれかを決めて売る。
    4. 乗り換えは、建て玉のあるいちばん近い限月から、いちばん遠い限月へ。また 3 あるいは 4 の限月に玉が建ってから。
    5. 納会でサヤすべりしない限月が 4 つ出るまで続ける（『脱アマ相場師列伝』）
  - 金は偶数限月の新甫発会でとにかく売ってみる。
    - 1 年後の納会で手仕舞うの原則だが、途中の手仕舞い可。
    - 一代の前半（6 か月）は __売り建て玉を維持して値動きを実感__ してみる。
  - 小豆は発会毎に、同ザヤか順ザヤならば売る。
    - 6 か月後の納会で手仕舞うのが原則だが、途中の手仕舞いは可。
    - 発会が逆ザヤならば売らないが、一代の前半（3 か月）以内に順ザヤに変化したら、その限月を売る。
    - 一代の後半（4 か月目以降）に順ザヤに変化しても売らない。
  - 自分の相場観を捨てて、一年は新甫毎に売る。

- テンバガーを狙うには、__時価総額 300 億円以下__ の銘柄を狙う。
  - メモ: 小型株は時価総額が 100 億円以下の銘柄のこと

- 利確のタイミング <!-- 2016-03-22 -->
  - 日足で見ているのであれば、__月足を見て、過去の高値あたりを目安__ とする。
    - 高値更新の銘柄に関しては、N 字計算法、E 字計算法で目標値を決める。

- 「リスク」をコントロールする
  - 「リターン」はコントロールできないが、「リスク」はコントロールできる。
    - __利確ラインと損切りラインを決めて、利確ラインを超えた時点でそこからトレーリングストップを置いてみよう__ 
  - ポートフォリオを組むときは、相関係数が低い（βが -1 に近い）ものを組み合わせることで収益のブレを抑えることができる。例えば、季節変動の激しい銘柄は、それぞれ夏と冬に売り上げが伸びやすい 2 つの銘柄を組み合わせることでシーズンリスクを下げることができる。これが正しい「分散」。

- 税グループの考慮
  - 似たような商品を選ぶ場合は、同じ税グループに入るように組み合わせると損益通算できて有利。
    - (NG) 預金 ＋ 株式
      - 預金の利息は源泉課税で完結してしまい戻ってこない。
    - (Good) MMF・公社債投信・債権 ＋ 株式
      - 同じ株式グループなので損益通算できる。

- 税金
  - 通勤費の支給（通勤手当）は、__月15万円までは非課税__。

- 短期トレードにおける資金管理（リスクマネジメント）
  - 資金管理こそが、長期的に利益を生み出すための聖杯
  - まず最初に、何回損失を出しても生き残れるか（口座を維持できるか）を考える
  - 10 回連続で負けることは普通にあることなので、その場合でも傷口は浅いと言える範囲内でトレードする

- リスクリワード比（Risk-Reward Ratio）を考える
  - ポジションをとるときは、例えば、1% のリスクで 3% の利益（リスクリワード比 1:3）を得られるようなタイミングを狙う。これなら、4 回中 1 回以上勝てるストラテジーであればよい。

- 法人設立のメリット
  - 消費税の免除
    - 資本金が 1,000 万円未満の場合、最初の 2 年間（2 期）は消費税の納税が免除されます。
    - 3 期目からは、1 期目（基準期間とされている 2 期前）の課税売上高が 1,000 万円を超えていたら課税事業者になります。
    - ちなみに、原則として年間の課税売上高が 1,000 万円以下であれば __免税事業者__ となるのは、個人でも法人でも変わりありません。その場合、お客様から受け取った消費税は納める必要がありません。
    - 個人事業を開業した場合も、消費税の 2 年間免除があるので、「個人事業（2年）→ 法人化（2年）」とすることで、合計 4 年間の消費税が免除されます。

- 東証 33 業種の分類は古い
  - 通信 ... 固定電話とスマホは全然別物
  - 商社はメーカーになったりする

- ポートフォリオの分散の軸
  - __業種__、__規模__、__国__、__タイミング__

- OnTick 内の処理の流れ
  1. 対象チャートかどうか念の為チェック
     - 通貨（シンボル）は想定しているものか？
     - 時間足は想定しているものか？
  1. 売買シグナルの確認
     - `return SIGNAL_BUY;`
     - `return SIGNAL_SELL;`
  1. ロット数の計算
  1. ポジションを追加 or 手仕舞い

- 資金管理 (Position control)
  - Factor
    - 総余剰資金
    - 1 トレードあたりのリスク（何％までなくしてもよいか）
      - 例えば、100 万円あって 1 トレードあたり 1% のリスクに晒してもよいのであれば、ロスカットは最大でも 1 万円までに抑える。
  - ポジションサイズは金額変動にもとづいて正規化する（タートルの手法）。
    多くの市場で取引したときに、すべての取引の変動が同じになるようにするということ。

