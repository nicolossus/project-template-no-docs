import torch

from package_name import MLP


def test_mlp_forward_pass():
    """
    Test that the MLP accepts the correct input shape
    and produces the expected output shape.
    """
    # Setup parameters
    input_size = 10
    hidden_size = 20
    num_classes = 5
    batch_size = 8

    # Initialize model
    model = MLP(input_size, hidden_size, num_classes)

    # Create dummy data
    x = torch.randn(batch_size, input_size)

    # Run forward pass
    output = model(x)

    # Assertions
    assert output.shape == (batch_size, num_classes), f"Expected shape {(batch_size, num_classes)}, got {output.shape}"
    assert not torch.isnan(output).any(), "Model produced NaN values!"


def test_mlp_parameter_count():
    """Ensure the model has parameters (it's not empty)."""
    model = MLP(10, 20, 5)
    params = list(model.parameters())
    assert len(params) > 0, "Model has no parameters!"
