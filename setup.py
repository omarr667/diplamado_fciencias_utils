from setuptools import setup, find_packages

setup(
    name="diplomado_finpy_utils",   
    version="0.1.0",                    
    packages=find_packages(),           
    include_package_data=True,  
    package_data={
        'diplomado_finpy_utils': ['data/*.csv']
    },
    install_requires=["numpy", "pandas", "matplotlib", "scipy"],  
    description="Un paquete de utilidades para el curso de diplamado de finanzas con Python de la Facultad de Ciencias (UNAM)",  
    author="Facultad de ciencias",      
    author_email="omarr667@gmail.com",  
    url="https://github.com/omarr667/diplomado_finpy_utils",  
    
)


