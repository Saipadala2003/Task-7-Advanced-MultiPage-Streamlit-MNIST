import streamlit as st
import tensorflow as tf
import numpy as np

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="MNIST AI Dashboard",
    page_icon="🔢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------------

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("deep_learning_model.h5")


try:
    model = load_model()
    model_loaded = True
except Exception as e:
    model = None
    model_loaded = False
    model_error = str(e)

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.title("🔢 MNIST AI System")

st.sidebar.markdown("""
### Navigation

Use the pages on the left to explore:

- 🏠 Dashboard
- 🔮 Digit Prediction
- 🧠 Model Performance
- 📊 Data Visualization
- 📄 Project Report
""")

st.sidebar.divider()

st.sidebar.info(
    "This application is developed as part of "
    "L&T Edutech Task 7 – Advanced Multi-Page Streamlit Application."
)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.title("🔢 MNIST AI Classification Dashboard")

st.subheader(
    "Advanced Multi-Page Streamlit Application for "
    "Handwritten Digit Classification"
)

st.markdown("""
This professional dashboard provides an interactive interface
for exploring a trained Convolutional Neural Network (CNN)
model for MNIST handwritten digit classification.
""")

st.divider()

# ---------------------------------------------------------
# SYSTEM STATUS
# ---------------------------------------------------------

st.header("⚙️ System Status")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Dataset",
        "MNIST"
    )

with col2:
    st.metric(
        "Classes",
        "10"
    )

with col3:
    st.metric(
        "Image Size",
        "28 × 28"
    )

with col4:
    if model_loaded:
        st.metric(
            "Model Status",
            "Loaded"
        )
    else:
        st.metric(
            "Model Status",
            "Error"
        )

# ---------------------------------------------------------
# MODEL INFORMATION
# ---------------------------------------------------------

st.divider()

st.header("🧠 Model Information")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Dataset

    **MNIST Handwritten Digit Dataset**

    - Image type: Grayscale
    - Image dimensions: 28 × 28 pixels
    - Number of classes: 10
    - Classes: 0–9
    - Task: Image Classification
    """)

with col2:
    st.markdown("""
    ### Deep Learning Model

    **Convolutional Neural Network (CNN)**

    The model processes handwritten digit images
    and predicts the corresponding digit class.

    The trained model is stored in:

    `deep_learning_model.h5`
    """)

# ---------------------------------------------------------
# WORKFLOW
# ---------------------------------------------------------

st.divider()

st.header("🔄 Application Workflow")

step1, step2, step3, step4 = st.columns(4)

with step1:
    st.markdown("""
    ### 1️⃣ Input

    Upload a handwritten
    digit image.
    """)

with step2:
    st.markdown("""
    ### 2️⃣ Processing

    Convert to grayscale,
    resize and normalize.
    """)

with step3:
    st.markdown("""
    ### 3️⃣ Prediction

    CNN analyzes the
    processed image.
    """)

with step4:
    st.markdown("""
    ### 4️⃣ Output

    Display digit,
    confidence and probabilities.
    """)

# ---------------------------------------------------------
# QUICK MODEL SUMMARY
# ---------------------------------------------------------

st.divider()

st.header("📋 Model Architecture Summary")

if model_loaded:

    architecture_data = []

    for layer in model.layers:
        output_shape = "Available"
        try:
            output_shape = str(layer.output.shape)
        except Exception:
            pass

        architecture_data.append({
            "Layer": layer.name,
            "Type": layer.__class__.__name__,
            "Output Shape": output_shape,
            "Parameters": layer.count_params()
        })

    st.dataframe(
        architecture_data,
        use_container_width=True,
        hide_index=True
    )

else:

    st.error("Model could not be loaded.")

    st.code(model_error)

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.divider()

st.caption(
    "L&T Edutech – Task 7 | Advanced Multi-Page Streamlit Application | MSc AI"
)