"""Tests for Knowledge-Serve KnowledgeService."""

import pytest

from knowledge_serve import KnowledgeService, ServeRegistry


def test_query_direct_and_alias():
    service = KnowledgeService()
    service.add_fact("alice", "knows", "bob")
    service.add_alias("ali", "alice")
    assert service.query("alice", "knows") == ["bob"]
    assert service.query("ali", "knows") == ["bob"]


def test_serve_returns_answers_and_latency():
    service = KnowledgeService()
    service.add_fact("a", "p", "o1")
    service.add_fact("a", "p", "o2")
    out = service.serve("r1", "a", "p")
    assert out["answers"] == ["o1", "o2"]
    assert out["latency_ms"] >= 0.0


def test_serve_stats_track_answered():
    service = KnowledgeService()
    service.add_fact("a", "p", "o")
    service.serve("r1", "a", "p")
    service.serve("r2", "a", "missing")
    assert service.stats["queries"] == 2
    assert service.stats["answered"] == 1


def test_summary_counts():
    service = KnowledgeService()
    service.add_fact("a", "p", "o")
    service.add_alias("x", "a")
    summary = service.summary()
    assert summary["facts"] == 1 and summary["aliases"] == 1


def test_validation():
    service = KnowledgeService()
    with pytest.raises(ValueError):
        service.add_fact("", "p", "o")
    with pytest.raises(ValueError):
        service.add_alias("", "a")
    with pytest.raises(ValueError):
        service.serve("", "a", "p")


def test_base_registry_still_works():
    assert ServeRegistry().summary()["models"] == 0
