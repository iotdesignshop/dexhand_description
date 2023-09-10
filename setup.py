from setuptools import find_packages, setup

package_name = 'dexhand_description'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Trent Shumay',
    maintainer_email='trent@iotdesignshop.com',
    description='ROS 2 description package for DexHand v1',
    license='CC BY-NC-SA 4.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
