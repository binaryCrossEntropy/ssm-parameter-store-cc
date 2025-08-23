from setuptools import setup, find_packages


LONG_DESCRIPTION = open('README.md').read()


setup(
    name='ssm-parameter-store-cc',
    version='0.1.1',
    description='Simple Python wrapper for getting values from AWS Systems Manager Parameter Store-fork',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/binaryCrossEntropy/ssm-parameter-store-cc',
    author='Iqbal Singh',
    author_email='iqbalamo93@gmail.com',
    license='MIT',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=['boto3'],
    python_requires='>=3.10',
    zip_safe=False
)
