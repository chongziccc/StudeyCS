name='zhang'
age=17.655
No=3

print(f'姓名：{name},年龄：{age:.2f},学号:{No:03d}')
import pandas as pd

df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五"],
    "成绩": [88, 92, 76],
    "是否及格": [True, True, False]
})

df  # 直接输出，不要用 print(df)
