from setuptools import setup

setup(
    name='google_meet_xblock',
    version='0.1',
    description='Google Meet XBlock',
    packages=['google_meet_xblock'],
    install_requires=['XBlock'],
    entry_points={
        'xblock.v1': [
            'google_meet_xblock = google_meet_xblock:GoogleMeetXBlock',
        ]
    },
    package_data={
        'google_meet_xblock': [
            'templates/*.html',
            'static/css/*.css',
            'static/js/*.js',
        ],
    },
)
