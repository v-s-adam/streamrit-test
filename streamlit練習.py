import streamlit as st
import pandas as pd
import numpy as np

# 見出し
st.title('ADAM 1st App')

# テキスト入力
st.write('データフレーム')

# 表データの表示
st.write(
    pd.DataFrame({
        '1st column': [1, 2, 3, 4],
        '2nd column': [10, 20, 30, 40]
    })
)

# マジックコマンドでマークダウン記述が出来る
"""
# My 1st App
## マジックコマンド
こんな感じでマジックコマンドを使用できる。  
Markdown対応。
"""

# st.checkbox でチェックボックスを表示
# if文にすることでif文内のコードを表示/非表示が選択できる
if st.checkbox('Show DataFram'):
    chart_df = pd.DataFrame(
        np.random.randn(20, 3),
        columns = ['a', 'b', 'c']
    )
    st.line_chart(chart_df)

