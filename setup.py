from setuptools import setup, find_packages

setup(
    name="NetGuard",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'scapy',
        'sqlite3',
    ],
    entry_points={
        'console_scripts': [
            'netguard=netguard:main',
        ],
    },
)
