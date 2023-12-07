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






## 実験方法
- 3つのファイル形式(docx, pdf, txt)でデータセットを準備
- AddaptiveLLMとChatGPTにそれぞれデータを入力
- 読み取り精度を評価(評価基準と質問: [md](./resDoc/評価基準.md))
## 出力結果
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