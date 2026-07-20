from fastapi import APIRouter

router = APIRouter()

@router.get("/{topic_entity_id}")
async def get_subgraph(topic_entity_id: str):
    return {
        "nodes": [{"id": "...", "label": "...", "type": "..."}],
        "edges": [{"source": "...", "target": "...", "label": "defines"}]
    }
