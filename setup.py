from distutils.core import setup
setup(
  name = 'smax',
  packages = ['smax'],
  version = '0.1',
  license='MIT',
  description = 'API wrapper for Microfocus SMAX application',
  author = 'Harvey Dumancic',
  author_email = 'dez.osk@gmail.com',
  url = 'https://github.com/Armitage87/smax',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['SMAX', 'Service management automation x', 'micro focus', 'automation'],
  install_requires=[
          'requests'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: API wrapper',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
  ],
)