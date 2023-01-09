import streamlit as st
import graphviz
import Mongo
from Node import *
import copy
from Mongo import *

if 'count' not in st.session_state:
    st.session_state[0] = Node(0, parentId=None)
    st.session_state['count'] = 0
    st.session_state['current'] = 0

node = st.session_state[st.session_state['current']]
if node.parentId is not None:
    st.title(st.session_state['mainTitle'])
    backButton = st.button('Natrag', key='b'+str(node.parentId))
    if backButton:
        node = st.session_state[node.parentId]
        st.session_state['current'] = node.id
else:
    st.session_state['mainTitle'] = st.text_input('Naslov ekspertnog sustava: ', value=st.session_state['mainTitle'])
    st.session_state['mainDescription'] = st.text_area('Kratki opis sustava: ', value=st.session_state['mainDescription'])
node.setTitle(st.text_input('Naslov opcije: ', value=node.title))
node.setText(st.text_area('Detaljniji opis: ', value=node.text))
st.session_state['img'] = st.file_uploader('Slika: ', type=['png', 'jpg', 'jpeg'])
if 'img' in st.session_state and st.session_state['img'] is not None:
    node.setImage(st.session_state['img'].read())

if st.button('Dodaj'):
    con = int(st.session_state['count']) + 1
    st.session_state['count'] = con
    node.addChild(con)
    ch = Node(con)
    ch.parentId = st.session_state['current']
    ch.text = ''
    ch.image = ''
    st.session_state[con] = ch

i = 0
for c in node.children:
    child = st.session_state[c]
    key = copy.copy(c)
    inp = st.text_input('Naziv opcije: ', key='c'+str(i), value=child.title)
    child.setTitle(inp)
    col1, col2 = st.columns(2)
    i += 1
    with col1:
        b = st.button('Uredi', key='b' + str(child.id))
        if b:
            st.session_state['current'] = child.id
    with col2:
        b1 = st.button('Izbriši', key='d'+str(child.id))
        if b1:
            node.children.remove(child.id)


col1, col2 = st.columns(2)
with col1:
    if st.button('Pregled stabla odluke', type='primary'):
        graph = graphviz.Digraph()
        d = st.session_state[0].toDict({}, st.session_state)
        for d1 in d:
            for c in d[d1]['children']:
                graph.edge(d[d1]['title'], d[c]['title'])
        st.graphviz_chart(graph)
        st.write(d)
with col2:
    if st.button('Spremi'):
        l = st.session_state[0].toList([], st.session_state)
        st.write(l)
        st.write(st.session_state['mainTitle'])
        st.write(st.session_state['mainDescription'])
        Mongo.insertDiv(l, st.session_state['mainTitle'], st.session_state['mainDescription'])
