# Generated by ariadne-codegen
# Source: graphql/central-data

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetAvailableGames(BaseModel):
    all_series: "GetAvailableGamesAllSeries" = Field(alias="allSeries")


class GetAvailableGamesAllSeries(BaseModel):
    edges: List["GetAvailableGamesAllSeriesEdges"]
    page_info: "GetAvailableGamesAllSeriesPageInfo" = Field(alias="pageInfo")
    total_count: int = Field(alias="totalCount")


class GetAvailableGamesAllSeriesEdges(BaseModel):
    node: "GetAvailableGamesAllSeriesEdgesNode"


class GetAvailableGamesAllSeriesEdgesNode(BaseModel):
    id: str


class GetAvailableGamesAllSeriesPageInfo(BaseModel):
    end_cursor: Optional[Any] = Field(alias="endCursor")
    has_next_page: bool = Field(alias="hasNextPage")


GetAvailableGames.model_rebuild()
GetAvailableGamesAllSeries.model_rebuild()
GetAvailableGamesAllSeriesEdges.model_rebuild()
