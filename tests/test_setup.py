import torch

def test_torch_anda():
    a = torch.tensor([
        1.0, 2.0, 3.0
    ])

    b = torch.tensor([
        4.0, 5.0, 6.0
    ])

    assert torch.allclose(
        a+b, torch.tensor([5.0, 7.0, 9.0])
    )

def test_torch_esta_en_cpu():
    a = torch.zeros(3,3)

    assert a.device.type == "cpu"

def test_versiones():
    import tokenizers
    import requests
    assert torch.__version__ is not None
    assert tokenizers.__version__ is not None
    assert requests.__version__ is not None