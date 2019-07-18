from distutlis.core import setup

if __name__=="__main__":
    setup(
        name='allspark_portal',
        package_dir = {
            'manager': 'manager',
            'server':'server'},
        packages=['manager','server'],
    )