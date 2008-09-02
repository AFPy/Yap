version = '0.1.0'

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='Yap',
    version=version,
    description='Yet Another Planet.',
    author='Tarek Ziadé',
    author_email='tarek@ziade.org',
    url='http://atomisator.ziade.org',
    install_requires=["Pylons>=0.9.6.2", "lxml", "atomisator.main"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'yap': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors = {'yap': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', None),
    #        ('public/**', 'ignore', None)]},
    entry_points="""
    [paste.app_factory]
    main = yap.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
