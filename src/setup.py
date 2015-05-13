from distutils.core import setup	
import os.path
import sys

setup(
	name = 'Flex pipeline',
	version = '0.1',
	packages = ['flex','flex.tests','flex.tests.pipelines'],
	package_data = {'flex.tests.pipelines' : ['*'] },

	scripts = ['../scripts/fx'],

	# # dependencies

	# # testing suite
	#test_suite = 'flex.test',

	# # project metadata
	author = 'Derek Ruths',
	author_email = 'druths@networkdynamics.org',
	description = 'Flex is a framework for building and executing computing pipelines',
	license = 'BSD',
	url = 'http://flex.derekruths.com',
	download_url = 'https://github.com/druths/flex'
)
