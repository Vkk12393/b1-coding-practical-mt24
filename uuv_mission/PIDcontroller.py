class PIDController:
    def __init__(self, KP: float = 0.15, KD: float = 0.6, KI: float = 0.1):
        self.KP = KP
        self.KD = KD
        self.KI = KI
        self.previous_error = 0.0
        self.integral_error = 0.0

    def compute_action(self, reference: float, measurement: float) -> float:
        """Compute PID control action based on reference and measurement."""
        error = reference - measurement
        self.integral_error += error
        action = (self.KP * error + 
                 self.KD * (error - self.previous_error) + 
                 self.KI * self.integral_error)
        self.previous_error = error
        return action
