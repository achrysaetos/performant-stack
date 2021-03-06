# Backend

Built with FastAPI and Postgres. Run `poetry install`, then `poetry run uvicorn main:app --reload`. (Don't forget to change the python interpreter in VS Code to use Poetry's version in order to avoid pylance import warnings.)

**Tools and frameworks used:** FastAPI, SQLAlchemy, Postgres, pgAdmin 4, Pydantic, Alembic, Poetry, Flake8, Black, Pre-commit

*Not implemented yet: Asyncpg, Flake8, Black, Pre-commit*

## Important files and directories

**alembic/**\
&nbsp; **data/** -- JSON examples you can use to test your migrations.\
&nbsp; **versions/** -- autogenerated change versions for each migration.\
&nbsp; **env.py** -- set up your models to work with alembic.

**api/**\
&nbsp; **utils/**\
&nbsp; &nbsp; **courses.py** -- create functions to create, read, update, and delete courses.\
&nbsp; &nbsp; **users.py** -- create functions to create, read, update, and delete users.\
&nbsp; **courses.py** -- set routes to create, read, update, and delete courses.\
&nbsp; **sections.py** -- set routes to create, read, update, and delete sections.\
&nbsp; **users.py** -- set routes to create, read, update, and delete users.

**db/**\
&nbsp; **models/**\
&nbsp; &nbsp; **course.py** -- describe the relationships between course model fields and other abstract constraints.\
&nbsp; &nbsp; **mixins.py** -- let classes from your models inherit fields from the classes in this file.\
&nbsp; &nbsp; **user.py** -- describe the relationships between user model fields and other abstract constraints.\
&nbsp; **schemas/**\
&nbsp; &nbsp; **course.py** -- define the fields and data types for your course model.\
&nbsp; &nbsp; **user.py** -- define the fields and data types for your user model.\
&nbsp; **db_setup.py** -- create the engine and db session for your api as well as the base for your models.

**alembic.ini** -- add your database url to work with alembic.

**main.py** -- entrypoint for your api. Import your routers and create your tables here.

**pyproject.toml** -- manage your backend's dependencies and scripts here.
