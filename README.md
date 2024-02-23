# Streamlit CRUD

## Architecture

![clean-architecture](docs/assets/clean_architecture.jpg)

- `DTOs` are used from external layer _if fits_, and passed to `controllers` then use cases in which the `DTOs` data will instance `entities`. those `entities` will be passed to `gateways` and persisted in the `database`.

## Usage

1. `python -m venv venv`
2. `source venv/Scripts/activate` or `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `cd app`
5. create a `.env` file as the `.env.template` example
6. `python scripts/database.py`
7. `streamlit run app/init_streamlit.py` or `python app/init_api.py` to run fastapi
8. if running fastapi go to `http://localhost:8000/api/v1`

## Tests

1. `python -m venv venv`
2. `source venv/Scripts/activate` or `source venv/bin/activate`
3. `pip install -r requirements-dev.txt`
4. `cd app`
5. `pytest .`

## Type checking

1. `python -m venv venv`
2. `source venv/Scripts/activate` or `source venv/bin/activate`
3. `pip install -r requirements-dev.txt`
4. `cd app`
5. `mypy .`

_obs: you may need to use `mypy --install-types`_

## Development

**IMPORTANT**: _Streamlit_ will watch for file changes and rerun the application, but resources cached with `@st.cache_resource` will not be updated by the reruns triggered by the file watchdog

## Streamlit Alternatives

- panel
- solara
- nicegui
- shiny for python
- reflex
- plotly dash
- h2O Wave
- gradio

## Resources

- [Design Patterns - Singleton](https://design-patterns-ebook.readthedocs.io/en/latest/creational/singleton/)
- [SQLAlchemy async examples](https://docs.sqlalchemy.org/en/20/_modules/examples/asyncio/async_orm.html)
