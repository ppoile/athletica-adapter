.PHONY: all docs
all: docs

docs: doc/athletica-models.pdf

doc/athletica-models.pdf: stadion/models.py meeting/models.py main/models.py
	mkdir -p doc && \
	python manage.py graph_models stadion meeting main | \
		dot -T pdf > doc/athletica-models.pdf

clean:
	rm -rf doc
