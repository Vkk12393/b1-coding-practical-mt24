class PDController:
    def __init__(self, KP: float = 0.15, KD: float = 0.6):
        self.KP = KP
        self.KD = KD
        self.previous_error = 0.0

    def compute_action(self, reference: float, measurement: float) -> float:
        """Compute PD control action based on reference and measurement."""
        error = reference - measurement
        action = self.KP * error + self.KD * (error - self.previous_error)
        self.previous_error = error
        return action
