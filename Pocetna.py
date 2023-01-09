import streamlit as st

import Mongo

if 'dic' in st.session_state:
    dic = st.session_state['dic']
    position = st.session_state['position']
    dic1 = dic[position]
    if dic1['parentId'] is not None:
        if st.button('Natrag', key='n'+str(dic1['parentId'])):
            st.session_state['position'] = str(dic1['parentId'])
    st.title(dic1['question'])
    st.text(dic1['text'])
    if dic1['image'] is not None and dic1['image'] != "":
        st.image(dic1['image'])

    for c in dic1['children']:
        if st.button(dic[str(c)]['title'], key='b'+str(c)):
            st.session_state['position'] = str(c)
else:
    lis = Mongo.getNames()
    i = 0
    for l in lis:
        with st.expander(l['title']):
            st.write(l['description'])
            if st.button('Pregledaj', key='b'+str(i)):
                st.session_state['id'] = l['title']
                st.session_state['list'] = l['ids']
                st.session_state['dic'] = Mongo.listToDict(lis=Mongo.getSysem(st.session_state['list']))
                st.session_state['position'] = "0"
            i += 1
