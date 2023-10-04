import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing 
 
#title
st.title("Image to text converter")

#subtitle
st.subheader("**You can copy the extracted text!!**✌️")
st.markdown("Currently can extract- **English and Japanese** language")

st.markdown("AI and ML project- **_Ravali & Rupini_**")

#image uploader
image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])

@st.cache_resource
def load_model(): 
    reader = ocr.Reader(['en','ja'],model_storage_directory='.')
    # english- en; hindi-hi; telugu-te; tamil-ta; spanish-es; french- fr; german-de; italian-it; 
    # kannada-kn; korean-ko; chinese-'ch_sim'-'ch_tra';japanese-ja; urudu- ur;
    return reader 

reader = load_model() #load model

if image is not None:

    input_image = Image.open(image) #read image
    st.image(input_image) #display image

    with st.spinner("Extracting text from image "):
        

        result = reader.readtext(np.array(input_image))

        result_text = [] #empty list for results


        for text in result:
            result_text.append(text[1])

        st.write(result_text)
    st.success("Here you go!")
    #st.balloons()
else:
    st.write("Upload an Image")

st.markdown(" Optical Character Recognition - Using `easyocr`, `streamlit`")