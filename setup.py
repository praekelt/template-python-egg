from setuptools import setup, find_packages

setup(
    name='<full package name, i.e. django-sharing>',
    version='0.0.1',
    description='<short package description, i.e. Django row level object sharing app.',
    long_description = open('README.rst', 'r').read(),
    author='<author name, i.e. Praekelt Foundation>',
    author_email='<author email address, i.e. dev@praekelt.com',
    license='<package license, i.e. BSD>',
    url='<package homepage url, i.e. http://github.com/praekelt/django-sharing>',
    packages = find_packages(),
    install_requires = [
        '<optional package dependencies, i.e. django-snippetscream>',
    ],
    include_package_data=True,
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
