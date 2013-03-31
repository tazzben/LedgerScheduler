try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

long_desc = """
	This application moves transactions from a scheduled transaction file to a main ledger file. A very common task would be to use this app as part of a cron job after using Depreciate for Ledger.
"""


setup(name="LedgerScheduler",
      version=1.0,
      description="Tool to auto populate Ledger with enteries when the time comes",
      author="Ben Smith",
      author_email="ben@wbpsystems.com",
      url="https://github.com/tazzben/LedgerScheduler",
      license="MIT",
      packages=[],
      scripts=['scheduler'],
      package_dir={},
      long_description=long_desc,
      classifiers=[
          'Topic :: Text Processing',
          'Environment :: Console',
          'Development Status :: 5 - Production/Stable',
          'Operating System :: POSIX',
          'Intended Audience :: Developers',
          'Intended Audience :: End Users/Desktop'
      ]
     )