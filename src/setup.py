from setuptools import setup


setup(
    name="mlpro-int-tensorboard",
    version="0.0.1",
    description="MLPro: Integration Tensorboard",
    author="Mochammad Rizky Diprasetya",
    author_mail="software@rizkydiprasetya.com",
    license="Apache Software License (http://www.apache.org/licenses/LICENSE-2.0)",
    packages=["mlpro_int_tensorboard"],
    # Package dependencies for full installation
    extras_require={
        "full": ["dill", "numpy", "matplotlib", "multiprocess", "mlpro"],
    },
    zip_safe=False,
)
