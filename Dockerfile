FROM python:3.10-slim

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["bash", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 7860 & streamlit run streamlit_app/ui.py --server.port 7861 --server.enableCORS false"]
