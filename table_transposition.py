import pandas as pd

#指定CSV文件的路径
file_path = r'D:\BaiduSyncdisk\Work_Space\KB\Projetcs\hotan\cele\2013\fanghulin\table_11X.csv'

# 读取CSV文件
df = pd.read_csv(file_path, encoding='ANSI')

# 定义要处理的列
column_to_check = 'x'

# 创建一个新的DataFrame来存储结果
new_df = pd.DataFrame(columns=df.columns)

for index, row in df.iterrows():
    # 获取该列之后的非空值单元格
    non_empty_cells = row[column_to_check:].dropna()
    n = len(non_empty_cells)
    
    if n > 0:
        # 插入新行并转置非空单元格的值
        for i in range(n):
            new_row = row.copy()
            new_row[column_to_check] = non_empty_cells.iloc[i]
            new_df = new_df.append(new_row, ignore_index=True)

# 保存处理后的CSV文件
newfile_path = file_path[:-4] + '_transposition' + file_path[-4:]
new_df.to_csv(newfile_path, index=False, encoding='ANSI')