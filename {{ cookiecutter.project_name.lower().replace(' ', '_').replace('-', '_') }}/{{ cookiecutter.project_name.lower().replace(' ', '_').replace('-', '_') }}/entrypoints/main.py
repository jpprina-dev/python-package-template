# type: ignore[attr-defined]
from {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }} import author
from {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }} import example

def main():
    greeting: str = example.hello(author)
    print(f"{greeting}")



if __name__ == '__main__':
    main()
