from distutils.core import setup
import athumb


setup(
    name='django-athumb',
    version=athumb.VERSION,
    packages=['athumb', 'athumb.backends', 'athumb.management',
              'athumb.pial', 'athumb.pial.engines',
              'athumb.management.commands', 'athumb.templatetags',
              'athumb.upload_handlers'],
    description='A simple, S3-backed thumbnailer field.',
    author='Gregory Taylor',
    author_email='gtaylor@gc-taylor.com',
    license='BSD License',
    url='http://github.com/gtaylor/django-athumb',
    platforms=["any"],
    requires=['django', 'boto', 'pillow'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Web Environment',
    ],
)
