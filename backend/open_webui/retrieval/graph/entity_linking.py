@router.get("/api/v1/graph/{topic_entity_id}")
async def get_subgraph(topic_entity_id: str):
    return {
        "nodes": [{"id": "...", "label": "...", "type": "..."}],
        "edges": [{"source": "...", "target": "...", "label": "defines"}]
    }
