from fastapi import APIRouter, HTTPException
from typing import List
from bson import ObjectId
from models.topic import TopicModel, UpdateTopicModel
from utils.mongodb import database

router = APIRouter()


@router.post("/", response_description="Add new topic", response_model=TopicModel)
async def create_topic(topic: TopicModel):
    topic = topic.dict()
    topic["_id"] = str(ObjectId())
    result = await database["topics"].insert_one(topic)
    if result.inserted_id:
        return topic
    raise HTTPException(status_code=400, detail="Topic could not be created")


@router.get(
    "/", response_description="List all topics", response_model=List[TopicModel]
)
async def list_topics():
    topics = await database["topics"].find().to_list(1000)
    return topics


@router.get(
    "/{id}", response_description="Get a single topic", response_model=TopicModel
)
async def get_topic(id: str):
    if (topic := await database["topics"].find_one({"_id": id})) is not None:
        return topic
    raise HTTPException(status_code=404, detail=f"Topic with id {id} not found")


@router.put("/{id}", response_description="Update a topic", response_model=TopicModel)
async def update_topic(id: str, topic: UpdateTopicModel):
    topic = {k: v for k, v in topic.dict().items() if v is not None}
    result = await database["topics"].update_one({"_id": id}, {"$set": topic})
    if result.modified_count == 1:
        if (
            updated_topic := await database["topics"].find_one({"_id": id})
        ) is not None:
            return updated_topic
    raise HTTPException(status_code=404, detail=f"Topic with id {id} not found")


@router.delete("/{id}", response_description="Delete a topic")
async def delete_topic(id: str):
    result = await database["topics"].delete_one({"_id": id})
    if result.deleted_count == 1:
        return {"message": "Topic deleted"}
    raise HTTPException(status_code=404, detail=f"Topic with id {id} not found")
