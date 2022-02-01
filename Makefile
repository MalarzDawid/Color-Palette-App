streamlit_app:
	poetry run streamlit run dominant/app.py

format:
	black dominant/
	isort dominant/
