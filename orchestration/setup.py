import setuptools

setuptools.setup(
    name="orchestration",
    packages=setuptools.find_packages(exclude=["orchestration_tests"]),
    install_requires=[
        "dagster==0.13.12",
        "dagit==0.13.12",
        "pytest",
        "gcloud",
    ],
)
