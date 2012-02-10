from setuptools import setup, find_packages

version = '0.9.2'

setup(name='rt.zps',
      version=version,
      description="A zope processes inspector",
      long_description=( file('README.txt').read() + '\n\n' +
                         file('docs/HISTORY.txt').read()
                         ),
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='alert',
      author_email='alessandro.pisa@redturtle.net',
      url='http://www.redturtle.net',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      scripts=['rt/zps/zps'],
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'psutil'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
