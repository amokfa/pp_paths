from setuptools import (setup,find_packages)

def main():
    setup(
            name='pp_paths',
            version='1.0.0',
            packages=find_packages(),
            scripts=['scripts/pp_paths']
            )

if __name__ == '__main__':
    main()
# __magic__
