all: clean
	./anonymize.py *.odt
	libreoffice --headless --convert-to pdf *.odt

clean:
	rm -f *.pdf *_anon.odt
