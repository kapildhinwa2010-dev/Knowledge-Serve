# Knowledge-Serve

[![CI](https://github.com/kapildhinwa2010-dev/Knowledge-Serve/actions/workflows/ci.yml/badge.svg)](https://github.com/kapildhinwa2010-dev/Knowledge-Serve/actions/workflows/ci.yml)
[![CodeQL](https://github.com/kapildhinwa2010-dev/Knowledge-Serve/actions/workflows/codeql.yml/badge.svg)](https://github.com/kapildhinwa2010-dev/Knowledge-Serve/actions/workflows/codeql.yml)

Serve fact queries with alias resolution: triples in, answers and latency out.

## What it does

KnowledgeService stores (subject, predicate, object) triples plus
aliases and serves queries: each query resolves the subject alias, then
returns matching objects with latency. Query and answered counts
accumulate in stats.

    from knowledge_serve import KnowledgeService

    service = KnowledgeService()
    service.add_fact("alice", "knows", "bob")
    service.add_alias("ali", "alice")
    out = service.serve("req-1", "ali", "knows")
    print(out["answers"], out["latency_ms"])

## API

- KnowledgeService.add_fact / add_alias / query / serve / summary
- ServeRegistry - the generic base registry (unchanged from DNA-Serve)

## Honest results and limitations

- Facts are asserted, not learned; nothing validates that a triple is
  true, only that it was added.
- Queries scan the triple list linearly; large stores get slow.
- No transitive chaining here (see KnowledgeBench / ChainReasoner for
  chain queries).

## Status

Part of the kapildhinwa2010-dev toolkit experiments. CI and CodeQL run on
every push to main. License: MIT.
