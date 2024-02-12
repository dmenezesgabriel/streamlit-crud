# Streamlit CRUD

## Architecture

![clean-architecture](docs/assets/clean_architecture.jpg)

- `DTOs` are used from external layer _if fits_, and passed to `controllers` then use cases in which the `DTOs` data will instance `entities`. those `entities` will be passed to `gateways` and persisted in the `database`.

## Usage

1. `python -m venv venv`
2. `source venv/Scripts/activate` or `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. create a `.env` file as the `.env.template` example
5. `python scripts/database.py`
6. `streamlit run src/main.py`

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

- [SQLAlchemy async examples](https://docs.sqlalchemy.org/en/20/_modules/examples/asyncio/async_orm.html)
