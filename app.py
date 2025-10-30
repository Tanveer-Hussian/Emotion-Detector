import pickle
import streamlit as st

st.title('Emotion Predictor')
st.write("")

st.subheader("Let us predict emotion behind your sentence")

tfidf = pickle.load(open('tfidf_vectorizer1.pkl', 'rb'))
model = pickle.load(open('logistic_model3.pkl', 'rb'))


label_map = {
    0: 'sadness',
    1: 'anger',
    2: 'love',
    3: 'surprise',
    4: 'fear',
    5: 'joy'
}


input = st.text_input("Enter an emotional Sentence")
st.write("")


if st.button("Predict Emotion"):
    if(input.strip()!=""):
        input_vector = tfidf.transform([input])
        prediction = model.predict(input_vector)[0]
        emotion = label_map.get(prediction, "Unkown")
        st.success(f"Predicted emotion is: {emotion}")
    else:
        st.warning('Kindly enter sentence before prediction')     

