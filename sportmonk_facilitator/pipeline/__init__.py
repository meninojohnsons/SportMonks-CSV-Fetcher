"""
Pacote de orquestração do pipeline de ETL e API.
"""
from .controller import Controller
from .steps import (
    step_compile_raw,
    step_treat_compiled,
    step_add_country_season,
    step_compile_treated,
    step_merge_with_season_ids,
    step_filter_data,
    step_generate_urls,
    step_fetch_api
)
from .checkpoints import Checkpoint
