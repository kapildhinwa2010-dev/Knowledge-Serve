import pytest
import torch
from knowledge_serve import KnowledgeServe, create_knowledge_serve

class TestKnowledgeServe:
    def test_init(self):
        m = KnowledgeServe(dim=256, hidden_dim=512)
        assert m.dim == 256
    
    def test_forward(self):
        m = KnowledgeServe(dim=256)
        x = torch.randn(32, 256)
        assert m(x).shape == (32, 256)
    
    def test_factory(self):
        m = create_knowledge_serve()
        assert isinstance(m, KnowledgeServe)

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
