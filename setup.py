import os
from glob import glob
from setuptools import setup

package_name = 'ros2_py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name),glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='wakita',
    maintainer_email='wakita@cco.kanagawa-it.ac.jp',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker   = ros2_py_pubsub.publisher_member_function:main',
            'listener = ros2_py_pubsub.subscriber_member_function:main',
        ],
    },
)
