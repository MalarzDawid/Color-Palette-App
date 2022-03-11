streamlit_app:
	poetry run streamlit run dominant/app.py

format:
	black dominant/
	isort dominant/

install:
	pip install -r requirements.txt
