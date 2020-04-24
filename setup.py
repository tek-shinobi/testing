from setuptools import setup

setup(
    name="Anshu Testing Ground",
    version="1.0",
    description="Try out SQLAlchemy queries on a test database",
    author="Anshu",
    author_email="himanshu.p.singh@gmail.com",
    url="https://github.com/tek-shinobi/testing",
    install_requires=[
        "faker",
        "psycopg2",
        "sqlalchemy",
        "tabulate",
    ],
    package_dir={"": "code"},
    packages=["testing"],
    include_package_data=True,
    zip_safe=False,
)