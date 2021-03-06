.PHONY: all docs
all: docs

docs: doc/athletica-models.pdf

doc/athletica-models.pdf: main/models.py
	mkdir -p doc && \
	python manage.py graph_models main | \
		dot -T pdf > doc/athletica-models.pdf

clean:
	rm -rf doc

jsondump-without-base:
	python manage.py dumpdata main --exclude main.BaseAccount \
--exclude main.BaseAthlete --exclude main.BaseLog \
--exclude main.BasePerformance --exclude main.BaseRelay \
--exclude main.BaseSvm --indent 2 > data.json

jsondump-all:
	python manage.py dumpdata main --indent 2 > data.json
