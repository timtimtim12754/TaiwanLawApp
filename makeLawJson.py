import os
import json

# 定義要掃描的目錄和GitHub repository的URL前綴
directory = "Law"  # 替換為你的實際目錄
base_url = "https://raw.githubusercontent.com/timtimtim12754/TaiwanLawApp/main/"

# 初始化一個空的lawList
law_list = []

# 遍歷目錄樹
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".json"):
            # 取得分類名稱
            class_name = os.path.basename(root)
            # 取得檔案名稱（去掉.json副檔名）
            file_name = os.path.splitext(file)[0]
            # 生成文件的完整URL
            file_link = os.path.join(base_url, root, file).replace("\\", "/")
            # 將信息添加到law_list中
            law_list.append({
                "class": class_name,
                "fileName": file_name,
                "fileLink": file_link
            })

# 將law_list寫入到一個JSON文件中
output = {
    "lawList": law_list
}

# 將結果輸出到指定的json文件
with open("Law/Law.json", "w", encoding="utf-8") as json_file:
    json.dump(output, json_file, ensure_ascii=False, indent=4)

print("JSON文件已成功生成！")
