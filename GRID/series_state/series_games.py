# Generated by ariadne-codegen
# Source: queries/series-state

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class SeriesGames(BaseModel):
    series_state: Optional["SeriesGamesSeriesState"] = Field(alias="seriesState")


class SeriesGamesSeriesState(BaseModel):
    id: str
    finished: bool
    valid: bool
    games: List["SeriesGamesSeriesStateGames"]


class SeriesGamesSeriesStateGames(BaseModel):
    id: str


SeriesGames.model_rebuild()
SeriesGamesSeriesState.model_rebuild()
