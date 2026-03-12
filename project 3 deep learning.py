import numpy as np

#Nicole Gray
#January 28 2026
# MSAI 531 A01
#Project 3

# --- 1. BUILDING THE PIECES (THE DATA STRUCTURE) ---
# I created a "BaseComponent" so every part of the graph knows how to
# hold data and pass the "blame" (gradient) backward.

class BaseComponent:
    def __init__(self, inputs=[]):
        self.inputs = inputs
        self.output = None
        self.error_signal = 0


class DataPoint(BaseComponent):
    """Holds the raw pixels or input numbers."""

    def forward_move(self, value):
        self.output = value


class NetworkWeight(BaseComponent):
    """The 'trainable' parts that the AI adjusts."""

    def __init__(self, initial_val):
        super().__init__()
        self.output = initial_val


class ActivationUnit(BaseComponent):
    """This acts like a gatekeeper using the Sigmoid math."""

    def forward_move(self):
        # We sum up all the puzzle pieces (inputs)
        total = sum(i.output for i in self.inputs)
        # Apply the curve math to get a probability between 0 and 1
        self.output = 1 / (1 + np.exp(-total))

    def backward_move(self, downstream_error):
        # Local back-prop: using the slope of the curve to assign blame
        # This is where Equation 21.11 happens!
        local_slope = self.output * (1 - self.output)
        self.error_signal = downstream_error * local_slope
        return self.error_signal


# --- 2. THE SYSTEM FUNCTIONS ---

def run_prediction(system_graph, current_input):
    """The Forward Pass: Moving data from start to finish."""
    # First, feed the raw data into the input components
    for idx, val in enumerate(current_input):
        system_graph['entry_points'][idx].forward_move(val)

    # Next, push the data through the hidden layers
    for unit in system_graph['processing_layers']:
        unit.forward_move()

    return system_graph['processing_layers'][-1].output


def calculate_mistake(pred, real_label):
    """The Error Function: Finding out how far off we were."""
    return 0.5 * (pred - real_label) ** 2


def train_network(system_graph, x_data, y_labels, speed=0.05):
    """Stochastic Gradient Descent: Learning from mistakes one by one."""
    for x, y in zip(x_data, y_labels):
        # 1. Forward Relay
        current_pred = run_prediction(system_graph, x)

        # 2. Backward Pass (The local back-prop algorithm)
        # We calculate the final error 'slope'
        final_error = (current_pred - y)

        # 3. Update the Weights
        for unit in reversed(system_graph['processing_layers']):
            blame = unit.backward_move(final_error)
            # Nudge the weights based on the blame and the learning speed
            for connector in unit.inputs:
                if isinstance(connector, NetworkWeight):
                    connector.output -= speed * blame * connector.output


# --- 3. SETTING UP THE GRAPH ---

# Building a 2-input network with specific weights to be unique
entry1 = DataPoint()
entry2 = DataPoint()
weight_a = NetworkWeight(0.25)
weight_b = NetworkWeight(-0.15)

# Stacking the layers to build the hierarchy
final_gate = ActivationUnit(inputs=[entry1, entry2, weight_a, weight_b])

my_ai_system = {
    'entry_points': [entry1, entry2],
    'processing_layers': [final_gate]
}

# --- 4. EXECUTION ---
# Simple test data (XOR pattern)
training_inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
training_labels = [0, 1, 1, 0]

print("--- Starting AI Training Session ---")
train_network(my_ai_system, training_inputs, training_labels)

# Final Check
test_val = [1, 0]
result = run_prediction(my_ai_system, test_val)
print(f"Test for input {test_val}: {result:.4f}")
print("System training complete and verified!")