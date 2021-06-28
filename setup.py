from setuptools import setup, find_packages

setup(
    name = "sierra",
    version = "v1.1.1",
    author = "Pranav and Siddhesh",
    author_email = "BrainStormYourWayIn@gmail.com",
    description = "Sierra is a skeletal micro templating library for web frameworks in Python.",
    long_description = open("README.md").read(),
    long_description_content_type = "text/markdown",
    license = "Apache Software License",
    url = "http://github.com/BrainStormYourWayIn/sierra",
    project_urls = {
        "Bug Tracker": "https://github.com/BrainStormYourWayIn/sierra/issues",
        "Documentation": "https://brainstormyourwayin.github.io/sierra.github.io/",
    },
    packages = find_packages(where="src"),
    keywords = ["CSS", "HTML", "Web Development", "Templating", "Web Framework", "Python to HTML", "Python to CSS"],
    install_requires = ['pandas', 'bs4'],
    zip_safe = True,
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    package_dir = {"":"src"},
    python_requires = ">=3.4",
)
