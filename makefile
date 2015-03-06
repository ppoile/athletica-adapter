.PHONY: all docs
all: docs

docs: doc/athletica-models.pdf

doc/athletica-models.pdf: main/models.py
	mkdir -p doc && \
	python manage.py graph_models main | \
		dot -T pdf > doc/athletica-models.pdf

clean:
	rm -rf doc
