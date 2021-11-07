import streamlit as st
import pickle
from datetime import datetime
startTime = datetime.now()
# import znanych nam bibliotek

filename = "model.sv"
model = pickle.load(open(filename,'rb'))
# otwieramy wcześniej wytrenowany model
#objawy - jest
# ;wiek - jest
# ;choroby - jest
# ;wzrost - jest
# o ile wcześniej kodowaliśmy nasze zmienne, to teraz wprowadzamy etykiety z ich nazewnictwem
def main():

	st.set_page_config(page_title="Czy osoba wyzdrowieje w ciągu tygodnia?")
	overview = st.container()
	left, right = st.columns(2)
	prediction = st.container()

	st.image("https://previews.123rf.com/images/katalinks/katalinks2003/katalinks200300294/142810876-a-man-in-a-suit-and-tie-holds-in-his-hands-an-electronic-thermometer-with-temperature-37-5-human-is-.jpg")

	with overview:
		st.title("Czy osoba wyzdrowieje w ciągu tygodnia?")

	with left:
		age_slider = st.slider( "Wiek", value=20, min_value=1, max_value=100 )
		height_slider = st.slider( "Wzrost", value=180, min_value=50, max_value=250)

	with right:
		symptoms_slider = st.slider("Objawy", min_value=0, max_value=6)
		disease_slider = st.slider("Choroby", min_value=0, max_value=5)

	data = [[symptoms_slider, age_slider, disease_slider, height_slider]]
	cure = model.predict(data)
	s_confidence = model.predict_proba(data)

	with prediction:
		st.header("Czy osoba wyzdrowieje w ciągu tygodnia? {0}".format("Tak" if cure[0] == 1 else "Nie"))
		st.subheader("Pewność predykcji {0:.2f} %".format(s_confidence[0][cure][0] * 100))

if __name__ == "__main__":
    main()

## Źródło danych [https://www.kaggle.com/c/titanic/](https://www.kaggle.com/c/titanic), zastosowanie przez Adama Ramblinga