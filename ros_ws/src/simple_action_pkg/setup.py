from setuptools import find_packages, setup

package_name = 'simple_action_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yash',
    maintainer_email='yash@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'fibonacci_action_server = simple_action_pkg.fibonacci_action_server:main',
            'fibonacci_action_client = simple_action_pkg.fibonacci_action_client:main',
        ],
    },
)
