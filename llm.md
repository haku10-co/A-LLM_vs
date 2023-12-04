# AddaptiveLLM vs ChatGPT

## 概要
この報告書では、AddaptiveLLMとChatGPTの性能を比較します。異なるファイル形式が読み取り精度にどのように影響するかを調査し、それぞれのツールがどの形式を最も効率的に読み取ることができるかを明らかにします。

## 目次
1. はじめに
2. 報告書の目的
3. 使用するデータセットと質問
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
この報告書では、様々なデータソースから選ばれた以下のデータセットを使用します。

### 公開データセット:
- **Wikipediaデータセット**: 
  - 気象(日本語): [docx](./tools/DataSet/2023気象.docx), [pdf](./tools/DataSet/2023気象.pdf), [txt](./tools/DataSet/2023気象.txt)
  - 2023年国連気候変動会議(英語): [docx](./tools/DataSet/2023%20United%20Nations%20Climate%20Change%20Conference.docx), [pdf](./tools/DataSet/2023%20United%20Nations%20Climate%20Change%20Conference.pdf), [txt](./tools/DataSet/2023%20United%20Nations%20Climate%20Change%20Conference_full.txt)
- **政府の統計データ**: 

### ニュースサイト:
- **国際ニュース**: BBCやCNNなどの国際的なニュースサイトから、最近の重要なニュース記事を選びます。
- **地域ニュース**: 地元の新聞社やオンラインメディアから、地域に特化したニュース記事を選びます。
- **専門ニュースサイト**: 例えばテクノロジー（TechCrunchなど）、経済（Bloombergなど）、スポーツ（ESPNなど）など、特定のジャンルに特化したニュースサイトから記事を選びます。

### ブログやフォーラム:
- **個人ブログ**: 特定の趣味や専門分野に関する個人ブログから記事を選びます。
- **フォーラム**: RedditやQuoraなど、特定のトピックに関するディスカッションスレッドを選びます。
- **専門家ブログ**: 特定の分野（例: テクノロジー、医学、法律）の専門家によるブログから記事を選びます。

### 学術論文:
- **医学論文**: PubMedやその他の医学ジャーナルから最新の研究論文を選びます。
- **工学論文**: IEEE Xploreや他の工学関連のジャーナルから論文を選びます。
- **社会科学論文**: JSTORや他の社会科学ジャーナルから関連する研究論文を選びます。



## 実験方法
- 3つのファイル形式(docx, pdf, txt)でデータセットを準備
- AddaptiveLLMとChatGPTにそれぞれデータを入力
- 読み取り精度、速度、柔軟性を評価

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

- Wikipedia contributors. (2023). 2023年の気象・地象・天象. In _Wikipedia, The Free Encyclopedia_. Retrieved from [https://ja.wikipedia.org/wiki/2023年の気象・地象・天象](https://ja.wikipedia.org/wiki/2023年の気象・地象・天象)

- Wikipedia contributors. (2023). 2023 United Nations Climate Change Conference. In _Wikipedia, The Free Encyclopedia_. Retrieved from [https://en.wikipedia.org/wiki/2023_United_Nations_Climate_Change_Conference](https://en.wikipedia.org/wiki/2023_United_Nations_Climate_Change_Conference)
