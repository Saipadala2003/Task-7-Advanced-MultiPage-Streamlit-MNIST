import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Model Performance",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Model Performance")
st.write("Evaluation and performance analysis of the MNIST CNN classification model.")

st.divider()

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("deep_learning_model.h5")

@st.cache_data
def load_test_data():
    (_, _), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

    x_test = x_test.astype("float32") / 255.0
    x_test = x_test.reshape(-1, 28, 28, 1)

    return x_test, y_test


model = load_model()

st.subheader("📊 Model Evaluation")

with st.spinner("Evaluating model on MNIST test dataset..."):

    x_test, y_test = load_test_data()

    loss, accuracy = model.evaluate(
        x_test,
        y_test,
        verbose=0
    )

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Test Accuracy",
        f"{accuracy * 100:.2f}%"
    )

with col2:
    st.metric(
        "Test Loss",
        f"{loss:.4f}"
    )

with col3:
    st.metric(
        "Test Samples",
        f"{len(y_test):,}"
    )

st.divider()

st.subheader("🏗️ Model Architecture")

architecture = []

for layer in model.layers:

    architecture.append({
        "Layer": layer.name,
        "Type": layer.__class__.__name__,
        "Output Shape": str(layer.output.shape),
        "Parameters": layer.count_params()
    })

architecture_df = pd.DataFrame(architecture)

st.dataframe(
    architecture_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.subheader("🔢 Sample Prediction Analysis")

sample_predictions = model.predict(
    x_test[:20],
    verbose=0
)

predicted_labels = np.argmax(
    sample_predictions,
    axis=1
)

comparison_df = pd.DataFrame({
    "Sample": range(1, 21),
    "Actual Digit": y_test[:20],
    "Predicted Digit": predicted_labels,
    "Correct": y_test[:20] == predicted_labels
})

st.dataframe(
    comparison_df,
    use_container_width=True,
    hide_index=True
)

correct_predictions = np.sum(
    y_test[:20] == predicted_labels
)

st.info(
    f"Correct predictions among first 20 samples: "
    f"{correct_predictions}/20"
)