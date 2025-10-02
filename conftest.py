import pytest
from src import logger

@pytest.fixture
def sample_text_data():
    logger.info("Setting up sample fixture")
    text = "sample data"
    yield text
    logger.info("Tearing down sample fixture")
