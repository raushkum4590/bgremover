import streamlit as st
from PIL import Image
from rembg import remove
import io, time

# Sidebar controls
st.sidebar.title("⚙️ Settings")
threshold = st.sidebar.slider("Alpha threshold", 0.0, 1.0, 0.5)
st.sidebar.markdown("Upload an image and click Remove.")

# Main UI
st.title("🖼️ Background Remover")
uploaded = st.file_uploader("", type=["png","jpg","jpeg"])
if uploaded:
    img = Image.open(uploaded).convert("RGB")
    col1, col2 = st.columns(2)
    with col1: st.image(img, caption="Original", use_column_width=True)
    if st.button("Remove Background"):
        with st.spinner("Processing..."):
            prog = st.progress(0)
            for i in range(5):
                time.sleep(0.1); prog.progress((i+1)*20)
            out = remove(img, alpha_matting=True, alpha_matting_foreground_threshold=int(threshold*255))
        with col2: st.image(out, caption="Result", use_column_width=True)
        buf = io.BytesIO(); out.save(buf, format="PNG")
        st.download_button("Download", buf.getvalue(), "no_bg.png", "image/png")
