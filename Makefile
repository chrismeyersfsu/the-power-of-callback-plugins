.PHONY: core-requirements update-pip-requirements requirements demo offline \
	offline-edit offline-clean

core-requirements:
	pip install pip setuptools pip-tools

update-pip-requirements: core-requirements
	pip install -U pip setuptools pip-tools
	pip-compile -U requirements.in

requirements: core-requirements
	pip-sync requirements.txt

demo: requirements
	ansible-playbook -i inventory demo.yml

PITCHME.zip:
	wget https://gitpitch.com/pitchme/offline/github/cchurch/the-power-of-callback-plugins/`git rev-parse --abbrev-ref HEAD`/white/PITCHME.zip

PITCHME/index.html: PITCHME.zip
	test -f PITCHME/index.html || unzip -o PITCHME.zip

PITCHME/assets/md/README.md: PITCHME/index.html
	test -L PITCHME/assets/md || (rm -rf PITCHME/assets/md && ln -s ../.. PITCHME/assets/md)	

offline: PITCHME/index.html
	cd PITCHME && python -m SimpleHTTPServer 8059

offline-edit: PITCHME/assets/md/README.md
	cd PITCHME && python -m SimpleHTTPServer 8059

offline-clean:
	@rm -rf PITCHME PITCHME.zip

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
