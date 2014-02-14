from setuptools import setup, find_packages

version = '0.9.5'

setup(name='rt.zps',
      version=version,
      description="A zope processes inspector",
      long_description=(open('README.rst').read() +
                        '\n\n' +
                        open('docs/HISTORY.txt').read()
                        ),
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],
      keywords='',
      author='alert',
      author_email='alessandro.pisa@redturtle.it',
      url='http://github.com/RedTurtle/rt.zps',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples']),
      include_package_data=True,
      scripts=['rt/zps/zps'],
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'psutil'
      ],
      test_suite="rt.zps.tests",
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
