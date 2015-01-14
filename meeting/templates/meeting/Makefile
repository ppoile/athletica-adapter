.PHONY: rangliste.odt unzip-rangliste.odt

rangliste.odt:
	@echo "creating rangliste.odt..."
	@cd rangliste.odt-unzipped/ && \
	rm -f ./*~ && \
	rm -f ../rangliste.odt && \
	zip -r ../rangliste.odt * > /dev/null

unzip-rangliste.odt:
	@echo "unzipping rangliste.odt..."
	@mkdir -p rangliste.odt-unzipped && \
	cd rangliste.odt-unzipped/ && \
	rm -rf ./* && \
	unzip ../rangliste.odt > /dev/null && \
	tidy -modify -xml -utf8 -indent ./content.xml 2> /dev/null && \
	tidy -modify -xml -utf8 -indent ./styles.xml  2> /dev/null
