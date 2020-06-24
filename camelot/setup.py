from setuptools import setup

package_name = 'camelot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Eric Boehlke',
    maintainer_email='eric.p.boehlke@gmail.com',
    description='A package for Camelot',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = camelot.publisher_member_function:main',
            'listener = camelot.subscriber_member_function:main',
            'motor_node = camelot.motor_node:main',
            'tank_drive_node = camelot.tank_drive_node:main',
        ],
    },
)
