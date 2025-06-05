import gspread
from google.oauth2.service_account import Credentials
from openai import OpenAI
import time

# OpenAI APIキー
client = OpenAI(api_key="your-api-key-here")

# Google Sheets API認証
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("your-service-account.json", scopes=scope)
gc = gspread.authorize(creds)

# スプレッドシートの操作
spreadsheet = gc.open_by_url("spreadssheets-url-here")
sheet =spreadsheet.worksheet("回答結果")

#回答列の取得（C列）
answers = sheet.col_values(3)

#E列にヘッダーを記入
header = sheet.row_values(1)
if len(header) < 5:
    sheet.update(range_name="E1",values=[["keywords"]])

#回答からキーワードを抽出してE列に記入
for i,answer in enumerate(answers[1:], start=2):
    if not answer or "エラー" in answer:
        continue
    
    prompt = f"次の文章から重要なキーワードを必ず1~3個の範囲で抽出してください。出力は読点「、」で区切ってください。\n\n{answer}"
    print(f"{i}行目キーワード抽出中: {prompt}")
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content":prompt}]
        )
        keywords = response.choices[0].message.content.strip()
        sheet.update(range_name=f"E{i}",values=[[keywords]])
    
    except Exception as e:
            print(f"{i}行目でキーワード抽出エラー: {e}")
        
    time.sleep(1)