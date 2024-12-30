from setuptools import setup

setup(
    name='google_meet_xblock',
    version='0.1',
    description='Google Meet XBlock',
    packages=['google_meet_xblock'],
    install_requires=['XBlock'],
    entry_points={
        'xblock.v1': [
            'google-meet = google_meet_xblock:GoogleMeetXBlock',
        ]
    },
)
