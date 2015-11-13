from setuptools import setup, find_packages

version = '1.0.0rc1'

setup(
    name='rt.zps',
    version=version,
    description="A zope processes inspector",
    long_description='\n\n'.join((
        open('README.rst').read(),
        open('docs/HISTORY.rst').read(),
    )),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords='',
    author='ale-rt',
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
