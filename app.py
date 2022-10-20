#app.py 
import streamlit as st
import tensorflow as tf

@st.cache()
def load_model():
    model = tf.keras.models.load_model("streamlit/CNN_MOD_IMP.h5")
    return model


if __name__ == '__main__':

    model = load_model()
    st.title('Covid-19 X-Ray Detection: Tensorflow')

    uploaded_file = st.file_uploader('File uploader')

    if not uploaded_file:
        st.warning("Please upload an image before proceeding!")
        st.stop()
    else:
        # Decode Image and Predict Right Class
        image_as_bytes = uploaded_file.read()
        st.image(image_as_bytes, use_column_width=True)
        img = tf.io.decode_image(image_as_bytes, channels=3)
        img = tf.image.resize(img, (256, 256))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)  # Create a batch

        predictions = model.predict(img_array)
        score = tf.nn.softmax(predictions[0])

        st.title('Results')

        st.write("This image is %.2f percent Covid and %.2f percent Normal."
                 % (100 * (1 - score), 100 * score)
                 )
