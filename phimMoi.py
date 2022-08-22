import streamlit

st = streamlit.set_page_config(page_icon="meo.ico",page_title="phimmoi")
st = streamlit.title("danh sach phim")

st = streamlit.video("ai muon nghe khong.mp4")
st = streamlit.caption("ai muon nghe khong")
f = open("ai muon nghe khong.mp4", "rb")
st = streamlit.download_button(label="tai video", data= f, file_name="ai muon nghe khong.mp4")

st = streamlit.video("di ve nha.mp4")
st = streamlit.caption("di ve nha")
f = open("di ve nha.mp4", "rb")
st = streamlit.download_button(label="tai video", data= f, file_name="di ve nha.mp4")
st = streamlit.video("loi nho.mp4")
st = streamlit.caption("loi nho")
f = open("loi nho.mp4", "rb")
st = streamlit.download_button(label="tai video", data= f, file_name="loi nho.mp4")

