from src.resonance import Thought

# Create two thoughts
joy = Thought(name="Joy", vector=[0.9, 0.4, 0.7, 0.2, 0.8])
gratitude = Thought(name="Gratitude", vector=[0.8, 0.6, 0.5, 0.3, 0.9])

# Compare them
sim = joy.similarity(gratitude)
print(f"Similarity between '{joy.name}' and '{gratitude.name}': {sim:.3f}")

# Render one of them
print(f"\nPattern for '{joy.name}':")
print(joy.render_pattern(width=30, height=8))
