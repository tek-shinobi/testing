from setuptools import setup


setup(
    name="TestbedSQLAlchemy",
    version="1.0",
    description="Testbed for building SQLAlchemy queries on a test database.",
    author="Anshu Singh",
    author_email="4evrsun@gmail.com",
    url="https://github.com/tek-shinobi/testing",
    install_requires=[],
    package_dir={"": "sandbox"},
    packages=["core_lib"],
    include_package_data=True,
    zip_safe=False,
)
