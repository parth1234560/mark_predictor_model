import streamlit as st
import pandas
from sklearn.linear_model import LinearRegression

st.header("🚀 Do you want to increase your study hours?")
st.title("📘 Then come to our website!")

uploaded_file = st.file_uploader("📂 Upload a CSV file with 'hrs' and 'mark' columns", type=["csv"])

if uploaded_file is not None:
	dataset = pandas.read_csv(uploaded_file)
	st.subheader("🧾 Dataset Preview")
	st.dataframe(dataset, use_container_width=True)
	mark = dataset["Scores"].values.reshape(-1, 1)
	hr = dataset["Hours"].values.reshape(-1, 1)
	x = st.number_input("🕒 Enter number of hours studied", min_value=0.0, step=0.5)

	if x > 0:
		brain = LinearRegression()
		brain.fit(hr, mark)
		predicted = brain.predict([[x]])[0][0]
		coefficient = brain.coef_[0][0]
		if predicted < 50:
			st.markdown("<h3 style='color:red>:WorkHard💪</h3>",unsafe_allow_html=True)
		elif predicted <80:
			st.markdown("<h3 style='color:orange'>A little more effort🧐</h3>",unsafe_allow_html=True)
		else:
			st.markdown("<h3 style='color:green'>Excellent keep it up!👌</h3>",unsafe_allow_html=True)
		st.markdown("### 🧠 Predicted Score")
		if predicted<100:
			st.markdown(f"<div style='font-size: 38px; color: #4CAF50; font-weight: bold;'>{predicted:.2f} marks</div>", unsafe_allow_html=True)
		else:
			st.markdown(f"<div style='font-size: 38px; color: #4CAF50; font-weight: bold;'>{100} marks</div>", unsafe_allow_html=True)
			st.markdown("You are going to be next topper")
		st.markdown("---")
		st.markdown("### 📐 Model Coefficient")
		st.markdown(f"<div style='font-size: 24px; color: #2196F3;'>{coefficient:.4f}</div>", unsafe_allow_html=True)
else:
	st.warning("⚠️ Please upload a valid CSV file to continue.")