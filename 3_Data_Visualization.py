import streamlit as st
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Data Visualization",
    page_icon="📊",
    layout="wide"
)

st.title("📊 MNIST Data Visualization")
st.write(
    "Explore handwritten digit samples and class distribution "
    "from the MNIST dataset."
)

st.divider()

@st.cache_data
def load_data():

    (x_train, y_train), (x_test, y_test) = (
        tf.keras.datasets.mnist.load_data()
    )

    return x_train, y_train, x_test, y_test


x_train, y_train, x_test, y_test = load_data()

# Dataset statistics
st.subheader("📌 Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Training Images",
        f"{len(x_train):,}"
    )

with col2:
    st.metric(
        "Testing Images",
        f"{len(x_test):,}"
    )

with col3:
    st.metric(
        "Image Size",
        "28 × 28"
    )

with col4:
    st.metric(
        "Classes",
        "10"
    )

st.divider()

# Digit distribution
st.subheader("📈 Digit Class Distribution")

unique, counts = np.unique(
    y_train,
    return_counts=True
)

distribution = {
    str(int(label)): int(count)
    for label, count in zip(unique, counts)
}

st.bar_chart(distribution)

st.divider()

# Select digit
st.subheader("🔍 Explore Digit Classes")

selected_digit = st.selectbox(
    "Select a digit",
    list(range(10))
)

indices = np.where(
    y_train == selected_digit
)[0][:12]

st.write(
    f"Showing sample images of digit **{selected_digit}**"
)

fig, axes = plt.subplots(3, 4, figsize=(8, 6))

for ax, index in zip(
    axes.flatten(),
    indices
):

    ax.imshow(
        x_train[index],
        cmap="gray"
    )

    ax.set_title(
        f"Digit: {selected_digit}"
    )

    ax.axis("off")

plt.tight_layout()

st.pyplot(fig)

st.divider()

# Random samples
st.subheader("🖼️ MNIST Sample Images")

random_indices = np.random.choice(
    len(x_train),
    12,
    replace=False
)

fig2, axes2 = plt.subplots(
    3,
    4,
    figsize=(8, 6)
)

for ax, index in zip(
    axes2.flatten(),
    random_indices
):

    ax.imshow(
        x_train[index],
        cmap="gray"
    )

    ax.set_title(
        f"Label: {y_train[index]}"
    )

    ax.axis("off")

plt.tight_layout()

st.pyplot(fig2)