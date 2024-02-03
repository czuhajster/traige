import httpx
import asyncio
from fastapi import FastAPI, WebSocket

# Import Factory and WebSocket Manager
from app import Factory, WebSocketManager

app = FastAPI()
factory = Factory()
socket_manager = WebSocketManager()

# Global variables
# PRODUCER_ENDPOINT = 'http://traige_demo_producer:8080/v2/body'
PRODUCER_ENDPOINT = "https://traige-demo.saajan.net/v2/body"
# Adjust this list to include all user IDs you need to manage
PRODUCER_USER_IDS = ['user_a', 'user_b', 'user_c']
FETCH_INTERVALS = 5  # Fetch every five seconds


async def fetch_data_for_user(user_id: str):
    headers = {
        'accept': 'application/json',
        'dev-id': 'testingTerra',
        # Replace with your actual API key
        'x-api-key': 'ussv5SAQ53a1nNTxsMr9G41zj2KUhYMk5eDU1hjG',
    }
    params = {
        'start_date': '2022-10-01',
        'to_webhook': 'true',
        'with_samples': 'true',
        'user_id': user_id  # Ensure user_id is included in the request parameters
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(PRODUCER_ENDPOINT, headers=headers, params=params)
        if response.status_code == 200:
            try:
                return factory.process_data(response.json())
            except Exception as e:
                print(f"Error processing response for user {user_id}: {e}")
                return None
        else:
            print(
                f"Failed to fetch data for user {user_id}. Status code: {response.status_code}")
            return None


async def schedule_fetches(interval: int):
    while True:
        for user_id in PRODUCER_USER_IDS:
            result = await fetch_data_for_user(user_id)
            if result is not None:
                # Convert the result to a JSON string or similar for WebSocket transmission
                await socket_manager.broadcast(str(result))
        await asyncio.sleep(interval)


@app.on_event("startup")
async def start_periodic_fetch():
    asyncio.create_task(schedule_fetches(FETCH_INTERVALS))


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await socket_manager.connect(websocket)
    try:
        while True:
            # This loop keeps the connection alive
            await websocket.receive_text()  # No action taken on messages for now
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        socket_manager.disconnect(websocket)


@app.get("/")
def read_root():
    return {"Hello": "TrAIge V2"}
