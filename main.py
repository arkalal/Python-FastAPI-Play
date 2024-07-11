import asyncio
from fastapi import FastAPI
from routes.topic import router as TopicRouter
import uvicorn
from dotenv import load_dotenv

# Ensure the event loop is running
loop = asyncio.get_event_loop()
if loop.is_closed():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

# Load environment variables
load_dotenv()

app = FastAPI()

app.include_router(TopicRouter, prefix="/topics", tags=["topics"])


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
