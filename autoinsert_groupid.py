import pandas as pd

# 读取CSV文件，指定编码格式为ANSI
file_path = r'D:\BaiduSyncdisk\Work_Space\KB\Projetcs\hotan\cele\2013\fanghulin\table_2.csv'
df = pd.read_csv(file_path, encoding='ANSI')

# 创建一个新的列'groupfield'并初始化为None
# df['groupfield'] = None

# 使用groupby对'A', 'B', 'C'列进行分组，并为每组分配唯一的groupfield值
group_id = 1
for _, group in df.groupby(['YMJ', 'LLZS', 'SJXMM']):
    df.loc[group.index, 'groupfield'] = group_id
    group_id += 1

# 保存处理后的CSV文件
newfile_path = file_path[:-4] + '_grouped' + file_path[-4:]
df.to_csv(newfile_path, index=False, encoding='ANSI')

print("处理完成, 结果已保存到: " + newfile_path)