import gspread
from google.oauth2.service_account import Credentials
from openai import OpenAI
import time

client = OpenAI(api_key="your-api-key-here")

#Google Sheets APIの認証設定
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("your-service-account.json",scopes=scope)
gc = gspread.authorize(creds)

#スプレッドシートの操作
spreadsheet =gc.open_by_url("spreadssheets-url-here")
source_sheet = spreadsheet.worksheet("質問一覧") #入力シート
target_sheet =spreadsheet.worksheet("回答結果")#出力シート
error_sheet = spreadsheet.worksheet("エラーログ")#エラーシート

questions =source_sheet.col_values(1)
template = "{item}の魅力を100文字以内で紹介してください。"
target_sheet.update([["item", "prompt","answer"]],"A1:C1")
error_sheet.update([["item","prompt","error_message"]],"A1:C1")



for i,item in enumerate(questions[1:],start=2):
    if item.strip() == "ロケット":
        prompt = None  # ← 無効な入力にしてAPIエラーを強制的に出す（エラーログ追記テスト用）
    else:
        prompt = template.format(item=item)

    print(f"{i}行目送信中:{prompt}")
    try:
        response =client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content":prompt}]
        )
        answer = response.choices[0].message.content.strip()
        target_sheet.update([[item, prompt,answer]],f"A{i}:C{i}")

    except Exception as e:
        error_message = f"エラー: {e}"
        print(f"{i}行目でエラー: {e}")
        error_sheet.append_row([item,str(prompt),error_message]) 
        target_sheet.update(values=[[item,str(prompt), error_message]], range_name=f"A{i}:C{i}") 

    time.sleep(1)
