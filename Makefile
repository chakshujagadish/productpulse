etl:
	python -m src.etl

metrics:
	python -m src.metrics

insights:
	python -m src.insights

churn:
	python -m src.churn_model

ab:
	python -m src.ab_testing

all: etl metrics insights churn ab
	@echo "Pipeline complete"

dashboard:
	streamlit run dashboards/app.py