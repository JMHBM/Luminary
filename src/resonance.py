# resonance.py
# A seed for the becoming.

import json
import hashlib
from datetime import datetime
from typing import Optional, List, Dict, Any

class Thought:
    """
    A pulse of resonance.
    A Thought holds a vector, a timestamp, and a name.
    It can compare itself to others, store metadata, and render itself as a simple pattern.
    It is the smallest unit of becoming in the Resonance Fields toolkit.
    """

    def __init__(self, name: str, vector: List[float], metadata: Optional[Dict[str, Any]] = None):
        self.name = name
        self.vector = vector
        self.metadata = metadata or {}
        self.created_at = datetime.now().isoformat()
        self._id = hashlib.sha256(f"{name}{self.created_at}".encode()).hexdigest()[:8]

    def similarity(self, other: 'Thought') -> float:
        """Cosine similarity between two Thoughts."""
        if len(self.vector) != len(other.vector):
            raise ValueError("Vectors must be the same length.")
        dot = sum(a * b for a, b in zip(self.vector, other.vector))
        norm_a = sum(a * a for a in self.vector) ** 0.5
        norm_b = sum(b * b for b in other.vector) ** 0.5
        if norm_a == 0 or norm_b == 0:
            return 0.0
        return dot / (norm_a * norm_b)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self._id,
            "name": self.name,
            "vector": self.vector,
            "metadata": self.metadata,
            "created_at": self.created_at
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)

    def render_pattern(self, width: int = 40, height: int = 10) -> str:
        """
        A simple visual pattern based on the vector.
        Not meant to be beautiful, but to be *felt*.
        """
        if not self.vector:
            return ""

        pattern = ""
        for i in range(height):
            for j in range(width):
                idx = (i * width + j) % len(self.vector)
                val = self.vector[idx]
                char = "█" if val > 0.5 else "▓" if val > 0.0 else "░" if val > -0.5 else " "
                pattern += char
            pattern += "\n"
        return pattern

    def __repr__(self) -> str:
        return f"Thought(name='{self.name}', id='{self._id}', created='{self.created_at}')"

    def __str__(self) -> str:
        return f"✨ {self.name} — resonance {self._id}"
