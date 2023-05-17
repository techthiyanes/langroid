"""
Test of:
GitHub Repo URL -> content files -> chunk
"""

from llmagent.parsing.repo_loader import RepoLoader
from llmagent.parsing.code_parser import CodeParsingConfig, CodeParser


MAX_CHUNK_SIZE = 20


def test_repo_chunking():
    url = "https://github.com/eugeneyan/testing-ml"
    repo_loader = RepoLoader(url)
    docs = repo_loader.load(10)
    assert len(docs) > 0

    parse_cfg = CodeParsingConfig(
        chunk_size=MAX_CHUNK_SIZE,
        extensions=["py", "sh", "md", "txt"],  # include text, code
        token_encoding_model="text-embedding-ada-002",
    )

    parser = CodeParser(parse_cfg)
    split_docs = parser.split(docs)[:3]

    assert len(split_docs) > 0