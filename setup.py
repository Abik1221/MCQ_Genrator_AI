from setuptools import setup, find_packages


setup(
    name ="multiple choice question generator",
    version = "0.1",
    author = "Nahom Keneni",
    author_email = "nahomkeneni4@gmail.com",
    description = "A package to generate multiple choice questions from a given textor file.",
    long_description = "This package uses OpenAI's GPT-3.5-turbo model to generate multiple choice questions from a given text or file. It allows users to specify the number of questions and options per question.",
    install_requires = ["openai", "langchain", "streamlit", "pyPdf2", "python-dotenv"],
    packages = find_packages()
)