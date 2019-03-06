import pandas as pd
import sys
# 패턴 / 정규 표현식을 활용한 필터링(판다스 사용)
input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame_value_matches_pattern = data_frame.ix[data_frame['Invoice Number']\
    .str.startswith("001-"), :]

data_frame_value_matches_pattern.to_csv(output_file, index=False)