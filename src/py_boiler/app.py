import click
from pathlib import Path
from templates import README_CODE, MAIN_CODE, GITIGNORE_CODE

@click.group()
def main():
    """Py-Boiler: Generate boilerplate Python apps."""
    pass


@main.group()
def new():
    """Scaffold new boilerplate projects."""
    pass


@new.command("basic")
def basic():
    """Generate a Hello World app.py file."""
    target_files = [
        "README1.md", "app1.py", ".gitignore1", "__init__1.py"
    ]
    for file in target_files:
        target_file = Path(f"./{file}")
        
        if target_file.exists():
            click.echo(f"⚠️  {file} already exists, not overwriting.")
            continue

        match file:
            case "README1.md":
                app_code = README_CODE
            case "app1.py":
                app_code = MAIN_CODE
            case ".gitignore1":
                app_code = GITIGNORE_CODE
            case _:
                app_code = ""
        target_file.write_text(app_code)
        click.echo("✅ Created {file} with Hello World template.")

if __name__ == "__main__":
    main()
