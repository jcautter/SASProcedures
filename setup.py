from setuptools import setup, find_packages

VERSION = '0.1.0' 
DESCRIPTION = 'SAS Procedures'
LONG_DESCRIPTION = 'SAS Procedures'

# Setting up
setup(
       # 'name' deve corresponder ao nome da pasta 'verysimplemodule'
        name="SASProcedures", 
        version=VERSION,
        author="João Paulo Cautter",
        author_email="jcautter@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['SASExport'], # adicione outros pacotes que 
        # precisem ser instalados com o seu pacote. Ex: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)