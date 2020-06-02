from setuptools import setup

setup(name='mlutils',
      version='0.0.1',
      description='A simple library with frequntly used methods in ML pipelines.',
      url='https://github.com/depitropov/mlutils',
      author='Dimitar Epitropov',
      author_email='depitropov@gmail.com',
      license='MIT',
      packages=['mlutils'],
      zip_safe=False,
      install_requires=[
          'numpy',
      ])
