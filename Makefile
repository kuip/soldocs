help:
	@echo "install - install package and dependencies"
	@echo "install-dev - install development dependencies"
	@echo "build-example - build soldocs package"
	@echo "publish - build soldocs package"

publish:
	python3 setup.py sdist bdist_wheel
	twine upload dist/*

install:
	pip install -r requirements.txt
	pip install -e .

install-dev:
	pip install -r requirements-dev.txt
	pip install -e .

build-example:
	populus -p examples compile
	soldocs --input examples/build/contracts.json --output examples/docs.md
