import torch.nn as nn
from torch import Tensor


class MLP(nn.Module):
    """
    A simple Multi-Layer Perceptron.
    """

    def __init__(self, input_size: int, hidden_size: int, num_classes: int) -> None:
        """
        Initializes the MLP model.

        Parameters
        ----------
        input_size : int
            The size of the input features.
        hidden_size : int
            The number of neurons in the hidden layer.
        num_classes : int
            The number of output classes.
        """
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, num_classes),
        )

    def forward(self, x: Tensor) -> Tensor:
        """Defines the forward pass of the model."""
        return self.layers(x)
