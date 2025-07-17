from setuptools import setup, find_packages

setup(
    name="genai_site_afrsv",  # Name of your package
    version="1.0.0",  # Version number
    description="A GenAI site with image processing and text AI capabilities.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Arthur Frei Souza",
    author_email="arthurfreisouza@gmail.com",
    url="https://github.com/arthurfreisouza/genai-site",  # Your repository URL
    packages=find_packages(where="src"),  # Automatically finds packages in the project
    package_dir={"": "src"},  # Tells setuptools to look for packages in the src directory
    include_package_data=True,  # Includes non-Python files (e.g., images) in the package
    install_requires=[
        "opencv-python==4.11.0.86",       # Image processing
        "scikit-image==0.25.2",        # Image processing tools
        "crewai==0.108.0",              # CrewAI for LLM-based workflows
        "openai==1.69.0",              # OpenAI API
        "fpdf==1.7.2",                # PDF generation
        "langchain==0.3.21",           # LangChain framework
        "langchain-community==0.3.20", # LangChain community modules
        "google-genai==1.2.0",            # Google API client
        "PyPDF2==3.0.1",             # PDF reading
        "easyocr==1.7.2",            # OCR for text extraction
        "PyMuPDF==1.25.4",              # PyMuPDF for PDF handling
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
)
