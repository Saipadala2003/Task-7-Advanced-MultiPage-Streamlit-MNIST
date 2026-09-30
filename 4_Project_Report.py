import streamlit as st

st.set_page_config(
    page_title="Project Report",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Project Report")

st.write(
    "Project documentation for the Advanced Multi-Page "
    "Streamlit Application."
)

st.divider()

st.header("🎯 1. Project Objective")

st.write("""
The objective of this project is to develop a professional,
interactive and user-friendly multi-page Streamlit application
for MNIST handwritten digit classification using a trained
Convolutional Neural Network (CNN).
""")

st.header("📚 2. Dataset")

st.write("""
The MNIST dataset contains grayscale images of handwritten
digits from 0 to 9.

Each image has a resolution of 28 × 28 pixels and belongs
to one of ten digit classes.
""")

st.markdown("""
- Dataset: MNIST
- Image Type: Grayscale
- Image Size: 28 × 28 pixels
- Number of Classes: 10
- Classes: 0–9
- Task: Image Classification
""")

st.header("🧠 3. Deep Learning Model")

st.write("""
A Convolutional Neural Network (CNN) is used for handwritten
digit classification. The model processes the input image,
extracts important visual features and produces probabilities
for the ten digit classes.
""")

st.header("⚙️ 4. Application Workflow")

st.markdown("""
**Step 1 – Input**

Upload a handwritten digit image.

**Step 2 – Preprocessing**

Convert the image to grayscale, resize it to 28 × 28 pixels
and normalize pixel values.

**Step 3 – Prediction**

The processed image is passed to the trained CNN model.

**Step 4 – Output**

The application displays the predicted digit, confidence
and prediction probabilities.
""")

st.header("🖥️ 5. Application Pages")

pages = {
    "🏠 Dashboard":
        "Provides system status, model information, workflow and architecture.",
    
    "🔮 Digit Prediction":
        "Allows users to upload a handwritten digit and obtain a prediction.",
    
    "🧠 Model Performance":
        "Displays model evaluation metrics and architecture information.",
    
    "📊 Data Visualization":
        "Provides MNIST dataset statistics, digit distribution and sample images.",
    
    "📄 Project Report":
        "Provides complete project documentation inside the application."
}

for page, description in pages.items():

    st.subheader(page)
    st.write(description)

st.header("🛠️ 6. Technologies Used")

st.markdown("""
- Python
- Streamlit
- TensorFlow
- Keras
- NumPy
- Pandas
- Matplotlib
- Pillow
""")

st.header("📈 7. Results")

st.write("""
The application provides an interactive environment for
MNIST handwritten digit classification. Users can navigate
between multiple pages, upload digit images, inspect model
performance and visualize the dataset.
""")

st.header("🔎 8. Observations")

st.markdown("""
- The application provides structured multi-page navigation.
- The CNN model performs handwritten digit classification.
- Uploaded images are converted into the required input format.
- Prediction probabilities can be visualized.
- Dataset characteristics can be explored interactively.
- Model architecture and evaluation information are available.
""")

st.header("✅ 9. Conclusion")

st.write("""
The Advanced Multi-Page Streamlit Application demonstrates
how a trained deep learning model can be converted into a
professional interactive application. The project integrates
prediction, model evaluation, data visualization and project
documentation into a single Streamlit interface.
""")