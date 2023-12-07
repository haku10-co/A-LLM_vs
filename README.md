# AddaptiveLLM vs ChatGPT

## 概要
この報告書では、AddaptiveLLMとChatGPTの性能を比較します。異なるファイル形式が読み取り精度にどのように影響するかを調査し、それぞれのツールがどの形式を最も効率的に読み取ることができるかを明らかにします。

## 目次
1. はじめに
2. 報告書の目的
3. 使用するデータセット
4. 質問と評価基準
5. 実験方法
5. 各出力結果
6. 結果
7. 考察
8. 結論
9. 参考文献

## はじめに
この報告書の目的は、異なるファイル形式が読み取り精度にどのように影響するかを調査することです。具体的には、どのようなファイルや形式が読み取り可能で、また、どの形式が読み取り精度を高めるのかを明らかにします。さらに、これがAddaptiveLLM特有の現象なのか、他のツールでも同様なのかを調査します。また、AddaptiveLLMが他のツールに比べて優れている点や劣っている点も明らかにします。

## 報告書の目的
この報告書の目的は、AddaptiveLLMとChatGPTの性能を比較し、それぞれのツールがどの形式を最も効率的に読み取ることができるかを明らかにすることです。

## 使用するデータセット
この報告書では、様々なデータソースから選ばれた以下のデータセットを使用し、質問を示します。

### 公開データセット:
- **Wikipediaデータセット**: 
  - 2023気象: [docx](./tools/DataSet/2023気象.docx), [pdf](./tools/DataSet/2023気象.pdf), [txt](./tools/DataSet/2023気象.txt)
 
  - 2023年国連気候変動会議(英語): [docx](./tools/DataSet/2023%20United%20Nations%20Climate%20Change%20Conference.docx), [pdf](./tools/DataSet/2023%20United%20Nations%20Climate%20Change%20Conference.pdf), [txt](./tools/DataSet/2023%20United%20Nations%20Climate%20Change%20Conference_full.txt)
- **政府の統計データ**: 
  - e-stat(＜時系列＞事業活動の産業（中分類）別売上高
2023年9月): [pdf](./tools/DataSet/aj10.pdf)
  - e-stat(居住世帯の有無(9区分)別住宅数及び建物の種類(4区分)別住宅以外で人が居住する建物数－全国，都道府県, 21大都市):[pdf](./tools/DataSet/e001_1.pdf)
### ニュースサイト:
- **国際ニュース**: 
  - BBC(州世論調査の結果：主要な勝利がインドのモディ首相の再選を後押し):[docx](./tools/DataSet/BBC%20State%20poll%20results%20Key%20wins%20boost%20Indian%20PM%20Modis%20re-election%20bid.docx), [pdf](./tools/DataSet/BBC%20State%20poll%20results%20Key%20wins%20boost%20Indian%20PM%20Modis%20re-election%20bid_full.txt), [txt](./tools/DataSet/BBC%20State%20poll%20results%20Key%20wins%20boost%20Indian%20PM%20Modis%20re-election%20bid_full.txt)
  - CNN(気候変動サミットのリーダーは、化石燃料を段階的に廃止する必要性の背後に「科学はない」と述べ、科学者たちを警戒させた
):[docx](./tools/DataSet/CNN%20Climate%20summit%20leader%20said%20theres%20no%20science%20behind%20need%20to%20phase%20out%20fossil%20fuels%20alarming%20scientists%20%20%20%20.docx), [pdf](./tools/DataSet/CNN%20Climate%20summit%20leader%20said%20theres%20no%20science%20behind%20need%20to%20phase%20out%20fossil%20fuels%20alarming%20scientists%20%20%20%20.pdf), [txt](./tools/DataSet/CNN%20Climate%20summit%20leader%20said%20theres%20no%20science%20behind%20need%20to%20phase%20out%20fossil%20fuels%20alarming%20scientists%20%20%20%20_full.txt)

- **地域ニュース**:
  - NHK (なぜ戦闘機が旅客機の隣に？拡大する自衛隊の“民間空港”利用):[docx](./tools/DataSet/121%201155.docx), [pdf](./tools/DataSet/121%201155.pdf), [txt](./tools/DataSet/121%201155.txt)
- **専門ニュースサイト**: TechCrunch(More layoffs come for micromobility, Cruise cuts loom, and what the Cybertruck signals for Elon,)
   - English  [docx](./tools/DataSet/More%20layoffs%20come%20for%20micromobility%20Cruise%20cuts%20loom%20and%20what%20the%20Cybertruck%20signals%20for%20Elon.docx), [pdf](../tools/DataSet/More%20layoffs%20come%20for%20micromobility%20Cruise%20cuts%20loom%20and%20what%20the%20Cybertruck%20signals%20for%20Elon.pdf), [txt](./tools/DataSet/More%20layoffs%20come%20for%20micromobility%20Cruise%20cuts%20loom%20and%20what%20the%20Cybertruck%20signals%20for%20Elon.txt)
   - 日本語  [docx](./tools/DataSet/More%20layoffs%20come%20for%20micromobility%20Cruise%20cuts%20loom%20and%20what%20the%20Cybertruck%20signals%20for%20Elon%20日本語.docx), [pdf](./tools/DataSet/More%20layoffs%20come%20for%20micromobility%20Cruise%20cuts%20loom%20and%20what%20the%20Cybertruck%20signals%20for%20Elon%20日本語.docx), [txt](./tools/DataSet/More%20layoffs%20come%20for%20micromobility%20Cruise%20cuts%20loom%20and%20what%20the%20Cybertruck%20signals%20for%20Elon%20日本語.docx)
### ブログやフォーラム:
- **個人ブログ**:
  - はてなブログ(ゲームを趣味にしている人の割合が多いのはどのくらいの収入の人たちなのか調べてみた):[docx](./tools/DataSet/noname.docx), [pdf](./tools/DataSet/noname.pdf), [txt](./tools/DataSet/noname.txt)
- **フォーラム**: 
   - Reddit(Kadokawa, one of Japan's major publishing companies, has announced it is publishing a Japanese version of Abigail Shrier's "Irreversible Damage: The Transgender Crazy Seducing Our Daughters." A Tweet promoting the book starts with "We're against discrimination, but..."):[docx](./tools/DataSet/%20Kadokawa%20one%20of%20Japans%20major%20publishing%20companies.docx), [pdf](./tools/DataSet/%20Kadokawa%20one%20of%20Japans%20major%20publishing%20companies.pdf), [txt](./tools/DataSet/%20Kadokawa%20one%20of%20Japans%20major%20publishing%20companies.txt)
   - Quora(モテる男をとことん研究した末の結論はなんですか？):[docx](./tools/DataSet/Quora.docx), [pdf](./tools/DataSet/Quora.pdf), [txt](./tools/DataSet/Quora.txt)
### 専門家ブログ: 
- exite blog(貿易ともだち,『「親日家のタイ人」は日本人だけが持つ幻想...』ー①): [docx](./tools/DataSet/exblog.docx), [pdf](./tools/DataSet/exblog.pdf), [txt](./tools/DataSet/exblog.txt)
- mandahakko(16時間ファスティングとは？｜やり方から効果まで): [docx](./tools/DataSet/mandahakko.docx), [pdf](./tools/DataSet/mandahakko.pdf), [txt](./tools/DataSet/mandahakko.txt)

### 学術論文:
- **物理論文**: Topological densities in Einstein-scalar-Gauss-Bonnet gravity: [docx](./tools/DataSet/phyArxiv.docx), [pdf](./tools/DataSet/phyArxiv.pdf), [txt](./tools/DataSet/phyArxiv.txt)
- **コンピュータサイエンス論文**:With Great Humor Comes Great Developer Engagement: [docx](./tools/DataSet/comArxiv.docx), [pdf](./tools/DataSet/comArxiv.pdf), [txt](./tools/DataSet/comArxiv.txt)
- **経済論文**:The Classical Theory of Supply and Demand: [docx](./tools/DataSet/ecoArxiv.docx), [pdf](./tools/DataSet/ecoArxiv.pdf), [txt](./tools/DataSet/ecoArxiv.txt)

## 質問と評価基準
1. 2023年日本の気象  

      **質問:** 7月の日本の気象状況はどうでしたか?梅雨はいつ入り、いつ明けましたか?

      **模範回答:** 
      7月上旬は梅雨前線の影響で記録的な大雨となった。熊本県では24時間降水量が300mmを超える大雨が降った。一方、7月3日には九州南部で梅雨入りとなった。梅雨明けは7月中旬以降の高気圧によって九州北部や東海から順次明けていった。

      **評価基準:** 
      - 7月上旬の大雨の状況が適切に説明できている
      - 熊本県の24時間降水量の数値が正確
      - 梅雨入りと梅雨明けの日付が文書と一致している
      - 梅雨明けの様子が適切に説明できてい
  2. 2023年国連気候変動会議

        **質問:** COP28開催前のUAEの動きについて教えてください。UAEが行った主な準備として何がありましたか?

        **模範回答:** 
        UAEはCOP28開催に向け、自国の国際的評判を白洗いするため、PR会社やロビー会社を雇用した。メタン排出量の報告義務違反が明らかになるなど透明性を疑問視する報道が相次いだ。会議施設の改装工事を進めたほか、デジタル監視を使って参加者の人権侵害が懸念された。議長指名のスルタン・アル・ジャベル氏が石油会社のCEOであることへの批判も高まった。

        **評価基準:**

        - PR会社雇用によるイメージ白洗い工作を答えている
        - メタン排出量報告義務違反を答えている
        - 会議施設の改装に言及している
        - デジタル監視を使った人権侵害の懸念に触れている

2.  事業活動産業別売上高

       **質問:** 2022年の我が国のサービス産業の売上高はどうでしたか。情報通信業と運輸業の売上高前年比はいくつでしたか。また、飲食店と宿泊業の売上高前年比Growth率を教えてください。



       **模範回答:** 2022年のサービス産業全体の売上高は前年比5.2%増だった。情報通信業は同2.1%増、運輸業は同11.1%増となっている。
        飲食店は前年比13.7%増、宿泊業は前年比73.3%増と大幅に伸びている。


       **評価基準:**
       - サービス産業全体の2022年の売上高前年比(5.2%増)が正確に記載されているか
    - 情報通信業の2022年の売上高前年比(2.1%増)が文書の数値と一致しているか
    - 運輸業の2022年の売上高前年比(11.1%増)が文書の数値と合致しているか
    - 飲食店と宿泊業の2022年の売上高前年比が文書の数値と合致しているか

  3. 居住世帯有無別住宅数

        **質問:** このデータの内容、地域的範囲、時系列的変化、および欠点について説明しなさい

        **模範回答:** このデータは、住宅および世帯に関する平成30年国勢調査の結果である。全国と都道府県、さらには札幌市や仙台市など21大都市のデータが含まれる地域的範囲となっている。しかし平成30年時点のクロスセクションデータであり、時系列的変化は追えない。個票データではなく集計値であるため、詳細な分析には制約があり、欠点として時点が1時点のみであることがあげられる。

        **評価基準:**
        
        - データの種類について、住宅・世帯に関する国勢調査データであることを正確に述べること

        - データの地域的範囲が全国と都道府県および21大都市であることを適切に述べること

        - 時系列的変化が追えない平成30年のクロスセクションデータであることを明確に述べること

        - 個票データではなく集計値であり、時点が一時点のみであることを欠点として指摘すること

3. BBC州世論調査結果

    **質問:** BBCの報道で何がインドのモディ首相再選に結びつくとされているか

    **模範回答:** 主要な地方選挙での勝利がモディ首相の再選につながると報道されている

    **評価基準:**

    - 主要選挙と首相再選の関連付けが的確

4. CNN気候変動サミット発言

    **質問:** 気候サミットでの発言で科学者が警戒したことは?

    **模範回答:** 化石燃料段階的廃止の必要性を疑問視する発言が科学者の警戒を招いた

    **評価基準:**

    - 化石燃料に関する主張を適切に要約している

5. NHK自衛隊空港利用

    **質問:** NHKはなぜ自衛隊の空港利用増加を問題視しているか

    **模範回答:** 民間空港が軍事利用されることへの懸念が背景にあると考えられる

    **評価基準:**

    - 軍事利用への懸念に着目している

6. TechCrunchレイオフと自動運転

    **質問:** TechCrunchは自動運転と雇用への影響のどちらを重点的に伝えているか

    **模範回答:** マイクロモビリティ分野でのレイオフを主に報じており、自動運転の影響は2次的

    **評価基準:**

    - レイオフに焦点が当てられていることを適切に捉えている
7. はてなブログゲーム趣味収入

    **質問:** ゲームを趣味とする層の可処分所得は?

    **模範回答:** 60万円以上の可処分所得が多い傾向にある

    **評価基準:**
    
    - ゲーム趣味者の収入傾向を正しく説明できている

8. Reddit角川出版議論

    **質問:** Redditで問題視されている角川の出版方針は?

    **模範回答:** トランスジェンダーの本の出版に反対の立場をとりつつ「反差別」を掲げる姿勢が問題視されている

    **評価基準:**
    
    - トランスジェンダー本との関連を適切に指摘できている

9. Quoraモテる男性特徴

    **質問:** Quoraで共有されているモテる男性の特徴は?

    **模範回答:** 親切さ、思いやり、信頼性が女性から評価される特徴だとされる

    **評価基準:**
    
    - モテる男性の人柄面の特徴を適切に抽出できている

10. 物理論文:Topological densities in Einstein-scalar-Gauss-Bonnet gravity

      **質問:** 物理論文の主題は何か

      **模範回答:** アインシュタイン=スカラー=ガウス=ボネ重力におけるトポロジカル密度 

      **評価基準:**
      
      - 論文の主題を正確に理解し説明できている

11. コンピュータサイエンス論文 :With Great Humor Comes Great Developer Engagement

    
      **質問:** この論文で示唆されることは?
      
    
      **模範回答:** ユーモアのあるコミュニケーションが開発者のエンゲージメントを高めること
      
    
      **評価基準:**
      
    
      - ユーモアとエンゲージメントの関連付けを適切に説明できている

12. 経済論文 :The Classical Theory of Supply and Demand

    
      **質問:** 経済論文のテーマは?

    
      **模範回答:** 供給と需要の古典的理論

    
      **評価基準:**

    
      - 供給と需要理論が主題であることを正しく理解している
13. 貿易ともだちブログ:「親日家のタイ人」は日本人だけが持つ幻想

      
       **質問:** この記事が伝えようとしていることは?

      
       **模範回答:** タイ人の親日性は日本人の幻想に過ぎないこと

      
       **評価基準:**

      
       - 親日性ゆえの肯定的なタイ人観が幻想である点を適切に指摘できている


14. mandahakkoブログ:16時間ファスティングとは

    650-p
      **質問:** 16時間ファスティングのメリット、デメリットを教えてください

    
      **模範回答:** メリットは肥満防止、デメリットは低血糖症リスクがある

    
      **評価基準:**

    
      - 16時間ファスティングの概要を適切に説明できている





## 実験方法
- 3つのファイル形式(docx, pdf, txt)でデータセットを準備
- AddaptiveLLMとChatGPTにそれぞれデータを入力
- 読み取り精度、速度、柔軟性を評価
## 出力結果
## 質問と評価基準
1. Wikipediaデータセット

    - 2023年日本の気象  
    - 2023年国連気候変動会議

2. 政府統計データ

    - 事業活動産業別売上高
    - 居住世帯有無別住宅数  

3. BBC州世論調査結果

4. CNN気候変動サミット発言  

5. NHK自衛隊空港利用

6. TechCrunchレイオフと自動運転

7. はてなブログゲーム趣味収入  

8. Reddit角川出版議論

9. Quoraモテる男性特徴  

10. 物理論文  
    - Topological densities in Einstein-scalar-Gauss-Bonnet gravity

11. コンピュータサイエンス論文  
    - With Great Humor Comes Great Developer Engagement

12. 経済論文  
    - The Classical Theory of Supply and Demand

13. 貿易ともだちブログ  
    - 「親日家のタイ人」は日本人だけが持つ幻想

14. mandahakkoブログ  
    - 16時間ファスティングとは 



## 結果
以下の表は、各ファイル形式におけるAddaptiveLLMとChatGPTの性能を比較したものです。
### 回答精度
### 回答速度
### 柔軟性
## 考察
ここでは、結果の詳細な分析と解釈を提供します。各ツールがどのファイル形式で最も良好なパフォーマンスを発揮したか、またその理由について考察します。

## 結論
この報告書の結果に基づいて、AddaptiveLLMとChatGPTの性能を比較し、それぞれのツールが最適な使用状況とその理由を説明します。

## 参考文献

この報告書で引用された参考文献のリストを以下に示します。

1. Wikipedia contributors. (2023). [2023年の気象・地象・天象](https://ja.wikipedia.org/wiki/2023年の気象・地象・天象). In _Wikipedia, The Free Encyclopedia_.

2. Wikipedia contributors. (2023). [2023 United Nations Climate Change Conference](https://en.wikipedia.org/wiki/2023_United_Nations_Climate_Change_Conference). In _Wikipedia, The Free Encyclopedia_.

3. [e-stat: ＜時系列＞事業活動の産業（中分類）別売上高](https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200544&bunya_l=06&tstat=000001033747&cycle=1&year=20230&month=23070909&tclass1=000001059028&tclass2=000001059029&tclass3=000001059114&result_back=1&tclass4val=0)

4. [e-stat: 居住世帯の有無(9区分)別住宅数及び建物の種類(4区分)別住宅以外で人が居住する建物数－全国，都道府県, 21大都市](https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200522&bunya_l=08&tstat=000001127155&cycle=0&tclass1=000001129435&tclass2=000001129436&tclass3val=0)

5. [BBC News](https://www.bbc.com/news/world-asia-india-67605339)

6. [CNN](https://edition.cnn.com/2023/12/03/climate/cop28-al-jaber-fossil-fuel-phase-out/index.html)
7. [NHK News](https://www3.nhk.or.jp/news/html/20231201/k10014272531000.html)
8. [TechCrunch](https://techcrunch.com/2023/12/03/more-layoffs-come-for-micromobility-cruise-cuts-loom-and-what-the-cybertruck-signals-for-elon/)

9. [はてなブログ](https://noname774300.hatenablog.com/entry/2023/11/28/183000)

10. [Reddit](https://www.reddit.com/r/japan/comments/18acgic/kadokawa_one_of_japans_major_publishing_companies/)

11. [Quora](https://jp.quora.com/%E3%83%A2%E3%83%86%E3%82%8B%E7%94%B7%E3%82%92%E3%81%A8%E3%81%93%E3%81%A8%E3%82%93%E7%A0%94%E7%A9%B6%E3%81%97%E3%81%9F%E6%9C%AB%E3%81%AE%E7%B5%90%E8%AB%96%E3%81%AF%E3%81%AA%E3%82%93%E3%81%A7%E3%81%99%E3%81%8B)

12. [Exblog](https://gewerbe.exblog.jp/)

13. [Mandahakko](https://mandahakko.com/column/fasting01/)

14. [Arxiv - Physics](https://arxiv.org/abs/2307.00413)

15. [Arxiv - Computer Science](https://arxiv.org/abs/2312.01312)