import streamlit as st
import pandas as pd
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

html_title = """
    <h1 style='color: #00FF00;'>Restaurants123</h1>
"""
st.markdown(html_title, unsafe_allow_html=True)




st.markdown("<p style='color: red;'>ร้านอาหารและเครื่องดื่ม </p>", unsafe_allow_html=True)
st.markdown("""
<h1 style='font-size: 18px; border: 4px solid #4CAF50; padding: 10px; border-radius: 5px;'>
คาเฟ่เล็กๆสไตล์แคมป์ปิ้งสามารถมาตั้งแคมป์พักผ่อนใจรับบรรยากาศชิวๆสบายๆ ฟังเพลงเบาๆทานอาหารอร่อยได้ครับ
</h1>
""", unsafe_allow_html=True)
st.markdown("""
    **เวลาเปิด-ปิด:**
    
    - จันทร์ - อาทิตย์: 08:00 - 23:00 น.
""")
st.markdown("<p style='color: Red;'>ร้านปิดทุกวันพุธ </p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.markdown("<h1 style='font-size: 20px;'>หมวดหมู่</h1>", unsafe_allow_html=True)
    with st.expander("คลิกที่นี่เพื่อดูรายละเอียด"):
        if st.button("เมนูอาหาร"):
            # เปลี่ยนสถานะ page เป็น 'อาหาร'
            st.session_state['page'] = 'food'
        if st.button("เมนูเครื่องดื่ม"):
            # เปลี่ยนสถานะ page เป็น 'เครื่องดื่ม'
            st.session_state['page'] = 'drink'

with col2:
    # ใช้ HTML ใน st.markdown เพื่อกำหนดขนาดตัวอักษร
    st.markdown("<h1 style='font-size: 20px;'>ช่องทางการติดต่อ</h1>", unsafe_allow_html=True)
    with st.expander("คลิกที่นี่เพื่อดูรายละเอียด"):
        st.write("""
        - [เว็บไซต์](http://localhost:8501/#restaurants123)
        - [Facebook](https://www.facebook.com/profile.php?id=100067916860892&locale=th_TH)
        - โทร: +66 81 646 9695
        """)

with col3:
    st.markdown("<h1 style='font-size: 20px;'>สถานที่ตั้งของร้าน</h1>"
                , unsafe_allow_html=True)
    with st.expander("คลิกที่นี่เพื่อดูรายละเอียด"):
        #ที่ตั้งร้านด้วย latitude และ longitude
        location = pd.DataFrame({
            'lat': [15.1925741], 
            'lon': [104.8218491]
        })

        # แสดงแผนที่พร้อมตำแหน่งที่ระบุใน DataFrame
        st.map(location)

        # รายละเอียดเพิ่มเติมที่คุณต้องการแสดง
        st.write("123 ตำบล คำน้ำแซบ อำเภอวารินชำราบ อุบลราชธานี 34190")




st.markdown("""
    <img src="https://scontent-bkk1-2.xx.fbcdn.net/v/t39.30808-6/423006223_703455085261714_1045212839573483821_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeFdFx4MMkT-DjvCppb-EI-tNisvPvoHE6o2Ky8--gcTqpcLyU55EBkA0Gf-x0lxV1HV8KZ2T8EaUgXOeUssO2a-&_nc_ohc=uBBMgL3uPKUAX9Xl_3Y&_nc_ht=scontent-bkk1-2.xx&oh=00_AfBZ23BkKBW5Qz39YmcT-63OxUwOonxP454mmetZ3Frj4w&oe=65F72861" alt="Alt Text" style="width: 909px; height: 600px; border: 5px solid #555;"/>
""", unsafe_allow_html=True)


st.markdown("<h1 style='font-size: 20px;'>บรรยากาศภายในร้าน</h1>", unsafe_allow_html=True)
st.image('D:/123/New folder/บรรยากาศภายในร้าน/1.jpg')
st.image('D:/123/New folder/บรรยากาศภายในร้าน/2.jpg')
st.image('D:/123/New folder/บรรยากาศภายในร้าน/3.jpg')
st.image('D:/123/New folder/บรรยากาศภายในร้าน/4.jpg')
st.image('D:/123/New folder/บรรยากาศภายในร้าน/5.jpg')
    


st.markdown("<h1 style='font-size: 30px;'>เมนูอาหาร</h1>"
                , unsafe_allow_html=True)
menu_items = {
    "อาหาร 1": {"description": "หน้า1", "image": "D:/123/New folder/อาหาร/1.png"},
    "อาหาร 2": {"description": "หน้า2", "image": "D:/123/New folder/อาหาร/2.png"},
    "อาหาร 3": {"description": "หน้า3", "image": "D:/123/New folder/อาหาร/3.png"},
    "อาหาร 4": {"description": "หน้า4", "image": "D:/123/New folder/อาหาร/4.png"},
    "อาหาร 5": {"description": "หน้า5", "image": "D:/123/New folder/อาหาร/5.png"},
    "อาหาร 6": {"description": "หน้า6", "image": "D:/123/New folder/อาหาร/6.png"},
}

with st.expander("คลิกที่นี่เพื่อดูรายละเอียด"):
    for item, info in menu_items.items():
        st.markdown(f"**{item}**")
        st.image(info["image"], caption=item, width=500)  # ปรับ width ตามต้องการ
        st.markdown(f"*{info['description']}*")


st.markdown("<h1 style='font-size: 30px;'>เมนูเครื่องดื่ม</h1>", unsafe_allow_html=True)

drinks = [
    ("เครื่องดื่ม 1", "D:/123/New folder/เครื่องดื่ม/1.png"),
    ("เครื่องดื่ม 2", "D:/123/New folder/เครื่องดื่ม/2.png"),
    ("เครื่องดื่ม 3", "D:/123/New folder/เครื่องดื่ม/3.png"),
    ("เครื่องดื่ม 4", "D:/123/New folder/เครื่องดื่ม/4.png"),
    ("เครื่องดื่ม 5", "D:/123/New folder/เครื่องดื่ม/5.png"),
    ("เครื่องดื่ม 6", "D:/123/New folder/เครื่องดื่ม/6.png"),
    ("เครื่องดื่ม 7", "D:/123/New folder/เครื่องดื่ม/7.png"),
    ("เครื่องดื่ม 8", "D:/123/New folder/เครื่องดื่ม/8.png"),
    ("เครื่องดื่ม 9", "D:/123/New folder/เครื่องดื่ม/9.png"),
    ("เครื่องดื่ม 10", "D:/123/New folder/เครื่องดื่ม/10.png"),

]

with st.expander("คลิกที่นี่เพื่อดูรายละเอียด"):
    for drink_name, img_path in drinks:
        st.image(img_path, caption=drink_name, width=500)



audio_file_path = 'C:/Users/HP/Downloads/the-beat-of-nature-122841.mp3'

# อ่านไฟล์เสียง
audio_file = open(audio_file_path, 'rb')
audio_bytes = audio_file.read()

# แสดงไฟล์เสียงใน Streamlit
st.audio(audio_bytes, format='audio/mp3')
