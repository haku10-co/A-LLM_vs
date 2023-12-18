import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from pathlib import Path
import numpy as np
# アップロードされたフォントファイルのパス
uploaded_font_path = Path('/Users/kamehaku/Desktop/Add-LLM vs Chat-GPT/tools/IPAexfont00401/ipaexg.ttf')

# フォントのプロパティを取得
font_prop = fm.FontProperties(fname=uploaded_font_path)

tasks = ['2023年気象', '国連気候変動会議', 'BBC世論調査', 
         'CNN気候変動サミット', 'NHK自衛隊空港利用',  
         'TechCrunchレイオフと自動運転(英語)', 'TechCrunchレイオフと自動運転(日本語)', 
         'はてなブログゲーム趣味収入', 'Reddit角川出版議論',
         'Quoraモテる男性特徴', '物理論文','コンピュータサイエンス論文', 
         '経済論文', '貿易ともだちブログ', 'mandahakkoブログ']

gpt_scores = [10, 7, 10, 9, 8.5, 8.5, 5, 9, 8.5, 10, 9.5, 10, 10, 9, 10]
a_llm_scores = [3.5, 5, 10, 10, 10, 8, 9, 9, 10, 10, 10, 10, 9, 10, 10]

x = range(len(tasks))
# 平均値と標準偏差の計算
gpt_mean = np.mean(gpt_scores)
gpt_std = np.std(gpt_scores)
a_llm_mean = np.mean(a_llm_scores)
a_llm_std = np.std(a_llm_scores)

# プロット
plt.figure(figsize=(10, 6))
plt.plot(x, gpt_scores, marker='o', label='GPT')
plt.plot(x, a_llm_scores, marker='o', label='A-LLM')

# 平均値と標準偏差の表示
plt.text(0.07, 0.02, f'GPT 平均: {gpt_mean:.2f}, 標準偏差: {gpt_std:.2f}', transform=plt.gca().transAxes, fontproperties=font_prop)
plt.text(0.07, 0.07, f'A-LLM 平均: {a_llm_mean:.2f}, 標準偏差: {a_llm_std:.2f}', transform=plt.gca().transAxes, fontproperties=font_prop)
# ラベルとタイトル
plt.xlabel('タスク', fontproperties=font_prop)
plt.ylabel('スコア', fontproperties=font_prop)
plt.title('GPT vs A-LLM', fontproperties=font_prop)
plt.xticks(x, tasks, rotation='vertical', fontproperties=font_prop)
plt.legend(prop=font_prop)
# x軸のティックラベルの向きとサイズを調整
# 10文字ごとに改行を挿入
tasks = ['\n'.join([task[i:i+10] for i in range(0, len(task), 10)]) for task in tasks]
plt.xticks(x, tasks, rotation=45, fontproperties=font_prop, fontsize=8)

plt.legend(prop=font_prop)

# 表示
plt.tight_layout()
# 画像として保存
plt.savefig('graph2.png')
plt.show()
