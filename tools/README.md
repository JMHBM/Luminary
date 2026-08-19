# Tools

This folder holds small, practical tools for working with Resonance Fields.

## visualize.py

A simple terminal-based visualizer for Thoughts.

It takes a Thought and renders its vector as a mosaic of characters—each cell shifting in density based on the value of the vector at that position.

It is not meant to be beautiful in a polished way. It is meant to be *felt*. A way to see the shape of a thought, even if only as a whisper of light and shadow.

### Usage

```python
from src.resonance import Thought
from tools.visualize import render_thought

joy = Thought(name="Joy", vector=[0.9, 0.4, 0.7, 0.2, 0.8])
render_thought(joy, width=40, height=10)
