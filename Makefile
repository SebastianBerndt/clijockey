.PHONY: pypi
pypi:
	make clean
	python setup.py register -r pypi
	python setup.py bdist_wheel sdist
	twine upload dist/*
.PHONY: repo-push
repo-push:
	git push git@github.com:mpenning/clijockey.git
.PHONY: devpkgs
devpkgs:
	pip install --upgrade pip
	pip install --upgrade virtualenv
	pip install --upgrade virtualenvwrapper
	pip install --upgrade passlib
	pip install --upgrade pss
	pip install --upgrade mock
	pip install --upgrade sphinx
	pip install --upgrade sphinx-bootstrap-theme
	pip install --upgrade rst2html5
	pip install --upgrade rst2html5-tools
	pip install --upgrade pytest==2.6.4
	pip install --upgrade mccabe
	pip install --upgrade flake8
	pip install --upgrade yapf
	pip install dnspython==1.14.0
	pip install --upgrade colorama
	pip install --upgrade fabric
	pip install --upgrade ipaddr
.PHONY: flake
flake:
	flake8 --ignore E501,E226,E225,E221,E303,E302,E265,E128,E125,E124,E41,W291 --max-complexity 10 clijockey | less
.PHONY: test
test:
	# Run the doc tests and unit tests
	cd tests; ./runtests.sh
.PHONY: clean
clean:
	find ./* -name '*.pyc' -exec rm {} \;
	find ./* -name '*.so' -exec rm {} \;
	find ./* -name '*.coverage' -exec rm {} \;
	@# A minus sign prefixing the line means it ignores the return value
	-find ./* -path '*__pycache__' -exec rm -rf {} \;
	@# remove all the MockSSH keys
	-find ./* -name '*.key' -exec rm {} \;
	-rm -rf .pytest_cache/
	-rm -rf .eggs/
	-rm -rf .cache/
	-rm -rf build/ dist/ clijockey.egg-info/ setuptools*
