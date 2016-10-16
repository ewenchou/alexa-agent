from setuptools import setup, find_packages

setup(name='alexa-agent',
    version='0.1',
    description="Agent for interacting with Alexa Voice Service using text",
    url='',
    author='Ewen Chou',
    author_email='ewenchou@gmail.com',
    license='Apache 2.0',
    packages=find_packages(),
    package_data={
        'alexa_agent': ['audio/*'],
        '': ['*.mp3']
    },
    install_requires=[
        'alexa_client',
        'simple_tts'
    ],
    zip_safe=False)
