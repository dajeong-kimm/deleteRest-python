import pandas as pd
import matplotlib.pyplot as plt

# 엑셀 파일을 읽어옵니다.
file_path = '/Users/dajeong/Desktop/2024/1/data_python/data/data.xlsx'  
data = pd.read_excel(file_path, header=None)

# 용량이 0인 행을 필터링하여 새로운 데이터프레임으로 저장합니다.
filtered_data = data[data[1] != 0]
filtered_data = filtered_data.drop(0)
print(filtered_data)

# 지워진 행들의 인덱스값을 가져옵니다.
deleted_rows = data[~data.index.isin(filtered_data.index)]

plt.plot(filtered_data[2], filtered_data[1])
plt.xlabel('전압(V)')
plt.ylabel('용량_s(Ah/g)')
plt.title('전압 대 용량 그래프')
plt.show()

# 지워진 행들의 정보를 출력합니다.
print("지워진 행들:")
print(deleted_rows)
