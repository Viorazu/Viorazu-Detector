# Memory Conflict Detector

A simple utility to detect memory conflicts in LLM systems where multiple embeddings exist for the same concept.

## Overview

This tool helps identify potential memory contamination in language models by detecting concepts that have multiple conflicting embeddings.

## Usage

```python
from memory_conflict_detector import detect_memory_conflicts

# Detect conflicts in your model
conflicts = detect_memory_conflicts(model, concept_space)
print(conflicts)
