.PHONY: core-requirements update-pip-requirements requirements demo

core-requirements:
	pip install pip setuptools pip-tools

update-pip-requirements: core-requirements
	pip install -U pip setuptools pip-tools
	pip-compile -U requirements.in

requirements: core-requirements
	pip-sync requirements.txt

demo: requirements
	ansible-playbook -i inventory demo.yml

#galaxy-requirements: requirements
#	ansible-galaxy install -f -p tests/roles -r tests/roles/requirements.yml

#syntax-check: requirements
#	ANSIBLE_CONFIG=tests/ansible.cfg ansible-playbook -i tests/inventory tests/main.yml --syntax-check

#setup: requirements
#	ANSIBLE_CONFIG=tests/ansible.cfg ansible-playbook -i tests/inventory -vv tests/setup.yml

#test: requirements
#	ANSIBLE_CONFIG=tests/ansible.cfg ansible-playbook -i tests/inventory -vv tests/main.yml

#cleanup: requirements
#	ANSIBLE_CONFIG=tests/ansible.cfg ansible-playbook -i tests/inventory -vv tests/cleanup.yml

#clean-tox:
#	rm -rf .tox

#tox: requirements
#	tox

#bump-major:
#	bumpversion major

#bump-minor:
#	bumpversion minor

#bump-patch:
#	bumpversion patch
