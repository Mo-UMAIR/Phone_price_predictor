import streamlit as st
import pickle
import numpy as np
#python -m streamlit run app.py

# import the model
model=pickle.load(open('model.pkl','rb'))
phone=pickle.load(open('phone_orignal.pkl','rb'))

st.title(":rainbow[Phone price predictor]")

st.markdown("*  **This table is used for choose the ram_rate with the help of company name and ram in gb.**")

col1, col2, col3 = st.columns(3)

with col1:
   st.markdown("**(Company)**     **(RAM)**    **(ram_rate)**")
   st.text('Apple       2        140')
   st.text('Apple       3        109')
   st.text('Apple       4        139')
   st.text('Apple       6        174')
   st.text('Xiaomi       2        30')
   st.text('Xiaomi       3        32')
   st.text('Xiaomi       4        34')
   st.text('Xiaomi       6        40')
   st.text('Xiaomi       8        46')
   st.text('Xiaomi       12       54')
   st.text('Xiaomi       16       57')
   st.text('Vivo         2        62')
   st.text('Vivo         4        49')
   st.text('Vivo         6        45')
   st.text('Vivo         8        42')
   st.text('LG           2        36')
   st.text('LG           4        31')
   st.text('LG           6        26')
   st.text('LG           8        23')

with col2:
   st.markdown("**(Company)**     **(RAM)**    **(ram_rate)**")
   st.text('Realme       2        47')
   st.text('Realme       4        38')
   st.text('Realme       6        43')
   st.text('Realme       8        36')
   st.text('Oppo         2        61')
   st.text('Oppo         4        33')
   st.text('Oppo         6        28')
   st.text('Oppo         8        38')
   st.text('Huawei       2        45')
   st.text('Huawei       4        40')
   st.text('Huawei       6        38')
   st.text('Huawei       8        35')
   st.text('Google       4       39')
   st.text('Google       6       34')
   st.text('Google       8       31')
   
with col3:
   st.markdown("**(Company)**     **(RAM)**    **(ram_rate)**")
   st.text('OnePlus         4     52')
   st.text('OnePlus         6     46')
   st.text('OnePlus         8     44')
   st.text('Sumsung         2     57')
   st.text('Sumsung         4     40')
   st.text('Sumsung         6     34')
   st.text('Sumsung         8     32')
   st.text('Sumsung         12    28')
   st.text('Lenovo         2      46')
   st.text('Lenovo         4      39')
   st.text('Lenovo         6      37')
   st.text('Lenovo         8      35')
   st.text('Sony           2      32') 
   st.text('Sony           4      42') 
   st.text('Sony           6      45') 
   st.text('Sony           8      48')   
   
   
st.header(':green[Fill All the Columns.]', divider='rainbow')

# brand
brand=st.selectbox('Brand',phone['brand'].unique())

# type of os
type=st.selectbox('operating system(os)',phone['os'].unique())


# screen size
size= st.selectbox('screen(in inches)',phone['inches'].unique())

# resolution
resolution= st.selectbox('resolution',phone['resolution'].unique())

# battery
battery= st.selectbox('Battery',phone['battery'].unique())

#battery_t_code(Li-po = 0, Li-ion = 1)
battery_type= st.selectbox('Battery Type',['Li-po','Li-ion'])

# RAM
ram = st.selectbox('RAM(GB)',phone['ram(GB)'].unique())

# Weight
weight= st.selectbox('Weight(gram)',phone['weight(g)'].unique())

# Storage
storage= st.selectbox('Storage(GB)',phone['storage(GB)'].unique())

# N_video_720p
video_720p= st.selectbox('video_720p',['NO','YES'])

# N_video_1080p
video_1080p= st.selectbox('video_1080p',['NO','YES'])

# N_video_4K
video_4K= st.selectbox('video_4K',['NO','YES'])

# N_video_8K
video_8K= st.selectbox('video_8K',['NO','YES'])

# N_video_30fps
video_30fps= st.selectbox('video_30fps',['NO','YES'])

# N_video_60fps
video_60fps= st.selectbox('video_60fps',['NO','YES'])

# N_video_120fps
video_120fps= st.selectbox('video_120fps',['NO','YES'])

# N_video_240fps
video_240fps= st.selectbox('video_240fps',['NO','YES'])

# N_video_480fps
video_480fps= st.selectbox('video_480fps',['NO','YES'])

# N_video_960fps
video_960fps= st.selectbox('video_960fps',['NO','YES'])

# ram(GB)_rate
ram_rate= st.number_input('ram_rate')

# storage_ram (storage /ram*10)
storage_ram= st.selectbox('storage_ram(storage /ram*10)',['0.4','0.8','1','1.6','2.1','3.2'])

# storage_ram2 (storage*ram)
storage_ram2= st.selectbox('storage_ram2(storage*ram)',['16','32','48','64','96','128','196','256','384','512','768','1024','2048'])


if st.button('Predict Price'):
    # query
    if battery_type == 'Li-ion':
        battery_type = 1
    else:
        battery_type = 0
    
    if video_720p == 'Yes':
        video_720p = 1
    else:
        video_720p = 0
    
    if video_1080p == 'Yes':
        video_1080p = 1
    else:
        video_1080p = 0
        
    if video_4K == 'Yes':
        video_4K = 1
    else:
        video_4K = 0
        
    if video_8K == 'Yes':
        video_8K = 1
    else:
        video_8K = 0
        
    if video_30fps == 'Yes':
        video_30fps = 1
    else:
        video_30fps = 0
        
    if video_60fps == 'Yes':
        video_60fps = 1
    else:
        video_60fps = 0
        
    if video_120fps == 'Yes':
        video_120fps = 1
    else:
        video_120fps = 0
        
    if video_240fps == 'Yes':
        video_240fps = 1
    else:
        video_240fps = 0
        
    if video_480fps == 'Yes':
        video_480fps = 1
    else:
        video_480fps = 0

    if video_960fps == 'Yes':
        video_960fps = 1
    else:
        video_960fps = 0


    query = np.array([brand,type,size,resolution,battery,battery_type,ram,weight,storage,video_720p,video_1080p,video_4K,video_8K,video_30fps,video_60fps,video_120fps,video_240fps,video_480fps,video_960fps,ram_rate,storage_ram,storage_ram2])

    query = query.reshape(1,22)
    st.header(":green[The predicted price of this configuration is  ] " + str(model.predict(query)) +":green[in USD.]")
    
    
    
    st.markdown('''
        :rainbow[THIS MODEL MADE BY MOHD UMAIR].''')
