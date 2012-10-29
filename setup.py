from setuptools import setup, find_packages

version = '0.9.4'

setup(name='rt.zps',
      version=version,
      description="A zope processes inspector",
      long_description=(file('README.rst').read() +
                        '\n\n' +
                        file('docs/HISTORY.txt').read()
                        ),
      classifiers=[],
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
