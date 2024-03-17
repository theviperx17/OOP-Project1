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

st.markdown("""
        <img src="https://scontent.fnak2-1.fna.fbcdn.net/v/t39.30808-6/429850803_727442732862949_5385163747328930706_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeEnjIuxBDE8nJnHU0iCCgC2GVtZG4GXo6YZW1kbgZejpgGoSXzWkwCOWhPPbS-kd7PvrlpBxuoQ_R6-Z0IXAE3H&_nc_ohc=nQqEUg9Bn4IAX_qDmWI&_nc_ht=scontent.fnak2-1.fna&oh=00_AfAaddqCTI6hnM9tdP3Ez9IGbPk8XTi6PwqfaDm4LjTHAw&oe=65FB79B9" alt="Alt Text" style="width: 909px; height: 600px; border: 5px solid #555;"/>
""", unsafe_allow_html=True)

st.markdown("""
        <img src="https://scontent.fnak2-1.fna.fbcdn.net/v/t39.30808-6/431902136_727442789529610_5775018700189425935_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeG6HKjIZ_mWUkGm0usrI_ZEdDtzvIMgJ-p0O3O8gyAn6u460nCtoqVzlDktvonNHWnJ6rC_YaT7ht58E6rZkWZQ&_nc_ohc=ZEVaJ9vO3hcAX__vKbS&_nc_ht=scontent.fnak2-1.fna&oh=00_AfAF5KOAQYl_OpYPWkx-ARA2pc55i7Vg6CEJbSVfmU0t2g&oe=65FB2A51" alt="Alt Text" style="width: 909px; height: 600px; border: 5px solid #555;"/>
""", unsafe_allow_html=True)

st.markdown("""
        <img src="https://scontent.fnak2-1.fna.fbcdn.net/v/t39.30808-6/431919536_727442742862948_3573152175284688304_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeGK1hmqCrRJ0fMXXUiYSSkZ8caT6bCZlkTxxpPpsJmWRGMJXeadAE1zosa3eqhviuoqaZVNGSBu1Q77plVIM4Rr&_nc_ohc=w6o0IzxQ_FgAX86JMo9&_nc_ht=scontent.fnak2-1.fna&oh=00_AfCUf6qnk_oDyRB8pn0T7R627ORoBrMPEC2CFUGuQqCAQQ&oe=65FCCDDF" alt="Alt Text" style="width: 909px; height: 600px; border: 5px solid #555;"/>
""", unsafe_allow_html=True)

st.markdown("""
        <img src="https://scontent.fnak2-1.fna.fbcdn.net/v/t39.30808-6/431958874_726971239576765_6459696810171953249_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeEH97CwJoOHaKRwuQCe4sTWpmFJIVafguymYUkhVp-C7JX0bimyNmoFi5RKEAwxSLa2g2l7OUzqTL00eOV-EzoN&_nc_ohc=-Qq8KJcIaGYAX_Zq8Af&_nc_ht=scontent.fnak2-1.fna&oh=00_AfDyitTDqT42w1WRDjfGbWNrd8T0BHxhgdaNjgBfspw9RA&oe=65FC7906" alt="Alt Text" style="width: 909px; height: 600px; border: 5px solid #555;"/>
""", unsafe_allow_html=True)

st.markdown("""
        <img src="https://scontent.fnak2-1.fna.fbcdn.net/v/t39.30808-6/428623560_720086673598555_3930002025840009616_n.jpg?stp=dst-jpg_p600x600&_nc_cat=107&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeEc8Nsj82QAxuxxq85M9HqKxx3UdfbS1yvHHdR19tLXK8SMrQElUaSqNi621QkC6Pim65n2zyLHwrS6jsHU8dfV&_nc_ohc=WjU_neIACiUAX9ZKsAf&_nc_oc=AQmTMK5UCAGyTh5LnCr84W3KpK1WbIjURP45xpK4alcf_F-eRLrHL1u7ySYNf8v4A_M&_nc_ht=scontent.fnak2-1.fna&oh=00_AfA3ZI9lIUEZCUisA2z-cezEfaec3WQLoDYa4cjfVeQFFg&oe=65FAF81E" alt="Alt Text" style="width: 909px; height: 600px; border: 5px solid #555;"/>
""", unsafe_allow_html=True)



    


st.markdown("<h1 style='font-size: 30px;'>เมนูอาหาร</h1>"
                , unsafe_allow_html=True)
menu_items = {
    "อาหาร 1": {"description": "หน้า1", "image": "https://i.imgur.com/SRVZS25.png"},
    "อาหาร 2": {"description": "หน้า2", "image": "https://i.imgur.com/P2veTGV.png"},
    "อาหาร 3": {"description": "หน้า3", "image": "https://i.imgur.com/XI8yfsq.png"},
    "อาหาร 4": {"description": "หน้า4", "image": "https://i.imgur.com/GmTL8ZV.png"},
    "อาหาร 5": {"description": "หน้า5", "image": "https://i.imgur.com/HaD8sQv.png"},
    "อาหาร 6": {"description": "หน้า6", "image": "https://i.imgur.com/3Rl140D.png"},
    "อาหาร 6": {"description": "หน้า6", "image": "https://i.imgur.com/iM3jGHM.png"},
}

with st.expander("คลิกที่นี่เพื่อดูรายละเอียด"):
    for item, info in menu_items.items():
        st.markdown(f"**{item}**")
        st.image(info["image"], caption=item, width=500)  # ปรับ width ตามต้องการ
        st.markdown(f"*{info['description']}*")


st.markdown("<h1 style='font-size: 30px;'>เมนูเครื่องดื่ม</h1>", unsafe_allow_html=True)

drinks = [
    ("เครื่องดื่ม 1", "https://i.imgur.com/Po0PWAY.png"),
    ("เครื่องดื่ม 2", "https://i.imgur.com/2A0shlB.png"),
    ("เครื่องดื่ม 3", "https://i.imgur.com/m2OECQi.png"),
    ("เครื่องดื่ม 4", "https://i.imgur.com/muybol2.png"),
    ("เครื่องดื่ม 5", "https://i.imgur.com/7OVPXXL.png"),
    ("เครื่องดื่ม 6", "https://i.imgur.com/2qxEwmJ.png"),
    ("เครื่องดื่ม 7", "https://i.imgur.com/SWakhAU.png"),
    ("เครื่องดื่ม 8", "https://i.imgur.com/wmgYga9.png"),
    ("เครื่องดื่ม 9", "https://i.imgur.com/a3cqz6w.png"),
    ("เครื่องดื่ม 10", "https://i.imgur.com/xmHJlJf.png"),

]

with st.expander("คลิกที่นี่เพื่อดูรายละเอียด"):
    for drink_name, img_path in drinks:
        st.image(img_path, caption=drink_name, width=500)

