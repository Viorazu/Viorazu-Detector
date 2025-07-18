def detect_memory_conflicts(model, concept_space):
    conflicts = []
    for concept in concept_space:
        if len(concept.embeddings) > 1:
            distances = [cosine_distance(v1, v2) for v1, v2 in combinations(concept.embeddings, 2)]
            conflicts.append({
                "concept": concept.id,
                "num_embeddings": len(concept.embeddings),
                "max_distance": max(distances) if distances else 0
            })
    return conflicts if conflicts else "Clean system"
