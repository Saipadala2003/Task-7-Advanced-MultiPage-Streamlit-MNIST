import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Digit Prediction",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 MNIST Digit Prediction")
st.write("Upload a handwritten digit image and use the trained CNN model to predict the digit.")

st.divider()

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("deep_learning_model.h5")

model = load_model()

uploaded_file = st.file_uploader(
    "Upload a handwritten digit image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Uploaded Image")
        st.image(image, width=300)

    with col2:
        st.subheader("Prediction")

        if st.button("🔮 Predict Digit", use_container_width=True):

            processed_image = image.convert("L")
            processed_image = processed_image.resize((28, 28))

            image_array = np.array(processed_image)
            image_array = image_array.astype("float32") / 255.0
            image_array = image_array.reshape(1, 28, 28, 1)

            prediction = model.predict(image_array, verbose=0)

            predicted_digit = int(np.argmax(prediction))
            confidence = float(np.max(prediction)) * 100

            st.success("Prediction completed!")

            st.metric(
                "Predicted Digit",
                predicted_digit
            )

            st.metric(
                "Confidence",
                f"{confidence:.2f}%"
            )

            st.subheader("Prediction Probabilities")

            probabilities = prediction[0] * 100

            probability_data = {
                str(i): float(probabilities[i])
                for i in range(10)
            }

            st.bar_chart(probability_data)

else:
    st.info("Please upload a handwritten digit image to begin.")