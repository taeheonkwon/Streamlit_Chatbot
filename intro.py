import streamlit as st

def app():
	st.write('''
	### 해당 누리집을 통해 프로그래밍에 대한 관심을 곰비임비 늘려가고
	### 무람없는 교류를 통해 서로의 지향점을 볼맞춰 나가리라 벅벅이 명토박아둡니다.
	''')
	placeholder = st.empty()

	with placeholder.container():
		st.write('One')
		st.write('Two')
