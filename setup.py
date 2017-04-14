import os
from setuptools import find_packages, setup

# Read version information
# Taken from https://github.com/kennethreitz/pipenv/blob/master/setup.py
about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "promgen", "version.py")) as f:
    exec(f.read(), about)

setup(
    name='Promgen',
    author='Paul Traylor',
    packages=find_packages(exclude=['test']),
    version=about['__version__'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        'atomicwrites',
        'celery[redis]==4.0.2',
        'dj_database_url',
        'Django >= 1.10, < 1.11',
        'envdir',
        'pyyaml',
        'raven',
        'requests',
    ],
    extras_require={
        'dev': [
            'django-nose',
            'nose-cov',
        ]
    },
    entry_points={
        'console_scripts': [
            'promgen = promgen.manage:main',
        ],
        'promgen.server': [
            'default = promgen.remote',
        ],
        'promgen.notification': [
            'ikasan = promgen.notification.ikasan:NotificationIkasan',
            'email = promgen.notification.email:NotificationEmail',
            'linenotify = promgen.notification.linenotify:NotificationLineNotify',
            'webhook = promgen.notification.webhook:NotificationWebhook',
        ],
    }
)
