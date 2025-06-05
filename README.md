# 🧠 GPT × Google Sheets 自動化ツール集

このリポジトリは、**OpenAI GPT API** と **Google Sheets API** を連携し、スプレッドシート上での作業を自動化する Python スクリプト群です。  
質問に対してAIが自動で回答し、それを要約・キーワード抽出・カテゴリ分類まで行います。

---

## 🔧 各スクリプトの役割

| スクリプト名                  | 機能内容                                                 |
|------------------------------|----------------------------------------------------------|
| `gpt_generate_answers.py`    | 質問一覧からGPTで回答を生成し、「回答結果」シートに記入 |
| `gpt_summarize_answers.py`   | 回答を簡潔な1文に要約してD列に記入                      |
| `gpt_extract_keywords.py`    | 回答から1〜3個のキーワードを抽出し、E列に記入           |
| `gpt_classify_categories.py` | キーワードに応じてカテゴリ分類し、F列に記入             |

---

## 📊 サンプルファイル

このリポジトリには、実行結果の一例を保存した Excel ファイル  
**`gpt_sheet_automation.xlsx`** が含まれています。

このファイルを開くと、以下のような構造になっています：

| A列（item） | B列（prompt） | C列（answer） | D列（summary） | E列（keywords） | F列（category） |
|-------------|---------------|---------------|----------------|------------------|------------------|
| 商品名       | 質問文         | GPTの回答       | 要約             | キーワード         | 自動分類カテゴリ     |

---

## 🗂️ ファイル構成

```
gpt_sheet_automation/
├── gpt_generate_answers.py
├── gpt_summarize_answers.py
├── gpt_extract_keywords.py
├── gpt_classify_categories.py
├── gpt_sheet_automation.xlsx     ← 実行結果サンプル（Excel）
├── gspread_key.json              ← Google認証キー（※公開しないこと）
├── .env（任意）                  ← APIキーなどの環境変数用
└── README.md
```

---

## ✅ 実行手順（推奨順）

1. `gpt_generate_answers.py` を実行 → 回答を生成して記入  
2. `gpt_summarize_answers.py` を実行 → 回答を要約して記入  
3. `gpt_extract_keywords.py` を実行 → キーワードを抽出して記入  
4. `gpt_classify_categories.py` を実行 → カテゴリを分類して記入

---

## ⚙️ 前提条件

### 🔑 必要ファイル

- `gspread_key.json`  
　Google Cloud Console で発行したサービスアカウントキー  
　（※`.gitignore`推奨）

- OpenAIのAPIキー  
　→ `.env` またはスクリプト内で直接指定

### 📝 使用するシート構成

- `質問一覧`シート：質問文をA列に記入  
- `回答結果`シート：出力先。スクリプトにより自動的に記入・更新

---

## ⚠️ セキュリティ注意

- `gspread_key.json` は**絶対に公開しない**でください  
- `api_key` は `.env` ファイル等で安全に管理することを推奨します

```env
# .envの例
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 💡 活用例

- 商品説明の自動生成
- SNS投稿文の要約
- キーワード抽出によるSEO最適化
- データのカテゴリ分けや集計補助

---

## 👤 作者について

Python学習中の個人開発者によるポートフォリオ兼ツール集です。  
実用性と実装力の証明として公開しています。

---

## 📄 ライセンス

このプロジェクトは [MIT License](./LICENSE) のもとで公開されています。
---
