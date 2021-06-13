import streamlit as st
import numpy as np
import pandas as pd
# from PIL import Image

st.title('Streamlit 超入門')

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

# # st.line_chart(df)
# # st.area_chart(df)
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


st.write('Interactive Widgets')

# option = st.selectbox('test',[1,2,3] )
option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,11))
)

'あなたの好きな数日：',option


# text = st.text_input('あなたの趣味')
# 'あなたの趣味：',text

# condition = st.slider('あなたの今日の調子は',0,100,50)
# 'あなたの調子：',condition



text = st.sidebar.text_input('あなたの趣味')

condition = st.sidebar.slider('あなたの今日の調子は',0,100,50)

'あなたの趣味：',text
'あなたの調子：',condition

