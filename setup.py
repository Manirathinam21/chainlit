from setuptools import setup, find_packages

setup(
    name= 'zomato-bot',
    version= '0.0.1',
    author= 'manirathinam',
    author_email= 'manirathinam21@gmail.com',
    packages= find_packages(),
    install_requires= ["chainlit","notebook","ipywidgets","tqdm","python-dotenv","langchain-google-genai"] 
)