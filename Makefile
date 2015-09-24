.PHONY: publish

publish:
	# Register and upload packages to PyPi, then clean up
	python setup.py register
	python setup.py sdist upload
	rm -rf dist
	rm -rf osx_trash.egg-info

update:
	# Upload the latest release to PyPi
	python setup.py sdist upload
	rm -rf dist
	rm -rf osx_trash.egg-info
