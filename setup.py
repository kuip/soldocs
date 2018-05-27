from setuptools import setup, find_packages

with open('requirements.txt') as fd:
    requires = fd.read().splitlines()

setup(name='soldocs',
        author='Loredana Cirstea',
        author_email='loredana.cirstea@gmail.com',
        url='https://github.com/kuip/soldocs',
        version='0.1.1',
        license='MIT',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4'
        ],
        keywords='populus solidity natspec documentation',
        packages=find_packages(exclude=['test']),
        install_requires=requires,
        entry_points={'console_scripts': ['soldocs=soldocs.main:main']}
)
