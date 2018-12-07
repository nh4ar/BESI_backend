install:
	# pyvenv env
	python3 -m venv env
	./env/bin/pip install --upgrade pip
	./env/bin/pip install -r requirements.txt

upgrade: requirements.txt
	./env/bin/pip install --upgrade -r requirements.txt

update-requirements:
	./env/bin/pip freeze > requirements.txt

uninstall:
	rm -rf env/

.PHONY: install upgrade update-requirements uninstall
