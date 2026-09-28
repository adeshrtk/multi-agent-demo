import importlib
import os
from typing import TypedDict, Annotated
import operator

import psycopg
from langgraph.graph import StateGraph, START, END

try:
    PostgresSaver = importlib.import_module("langgraph.checkpoint.postgres").PostgresSaver
except ModuleNotFoundError:
    PostgresSaver = importlib.import_module("langgraph.checkpoint").PostgresSaver

from langchain_core.messages import (
    AnyMessage,
    HumanMessage,
    SystemMessage,
    AIMessage
)

from langchain_groq import ChatGroq

from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from dotenv import load_dotenv

load_dotenv()
