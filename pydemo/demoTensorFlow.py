import numpy as np
import Dense
import Sequential

# 输入数据
x = np.array([[200.0, 17.0]])

# 定义模型
model = Sequential()
model.add(Dense(units=3, activation='sigmoid', input_dim=2))  # input_dim=2 是输入特征的数量

# 前向传播
a1 = model(x)

# 输出结果
print(a1)
