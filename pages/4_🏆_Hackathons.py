import streamlit as st

st.title('Hackathons')



tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["HackSVIT", "Hackout'22", "Hackthisfall 3.0", "DotSlash 6.0", "HackVengers", "WittyHacks 3.0"])

with tab1:
   st.header("HackSVIT")
   st.image("data:image/jpeg;base64,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")

   st.write("My first hackthon and started journey that never ends, to attending such hackathon we can up to date with latest technology advancemnets, thier in hackthon we creted sort of feedback form that calculates the Happiness index of school students. ")
   
   st.markdown('Skills: `React` , `Node.js`, `Mysql`, `Tailwind CSS`' )

   st.button("Github")
  


with tab2:
   st.header("Hackout'22")
   st.image("data:image/png;base64,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")

with tab3:
   st.header("Hackthisfall 3.0")
   st.image("https://d112y698adiu2z.cloudfront.net/photos/production/challenge_thumbnails/002/336/697/datas/original.png")

with tab4:
   st.header("DotSlash 6.0")
   st.image("data:image/png;base64,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")

with tab5:
   st.header("HackVengers")
   st.image("https://devfolio-prod.s3.ap-south-1.amazonaws.com/hackathons/2cf7715148724d268e9e4b31d46c30ea/assets/favicon/512.jpeg")

with tab6:
   st.header("WittyHacks 3.0")
   st.image("https://wittyhacks.in/assets/img/fb-og.png")
