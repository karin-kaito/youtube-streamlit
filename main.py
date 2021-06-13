import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# st.title('Streamlit 超入門')

# st.write('DataFrame')

# df = pd.DataFrame({
#     '1列目':[1,2,3,4],
#     '2列目':[10,20,30,40]
# })

# # st.write(df)
# # st.dataframe(df.style.highlight_max(axis=0),width=100,height=100)

# st.table(df.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ###　項

# ```
# import streamlit as st
# import numpy as nu
# import pandas as pd
# ```


# """


# df = pd.DataFrame(
#     np.random.rand(20,3),
#     columns={'a','b','c'}
# )

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69,139.70],
#     columns={'lat','lon'}
# )

# st.map(df)

# if st.checkbox('Show Image'):
#     st.write('Display Image')
#     img = Image.open('MyPhoto.jpg')
#     st.image(img, caption='Kimihiro Nishiyama',use_column_width=True)

st.write('Streamlit 超入門')

import time

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右からカラムに文字を表示')
if button:
    right_column.write('ココは右カラム')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ回答1')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ回答2')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ回答3')



# option = st.selectbox('test',[1,2,3] )
# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,11))
# )
# 'あなたの好きな数日：',option


# text = st.sidebar.text_input('あなたの趣味')
# condition = st.sidebar.slider('あなたの今日の調子は',0,100,50)

# 'あなたの趣味：',text
# 'あなたの調子：',condition

text = st.text_input('あなたの趣味')
condition = st.slider('あなたの今日の調子は',0,100,50)

'あなたの趣味：',text
'あなたの調子：',condition

