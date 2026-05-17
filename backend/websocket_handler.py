from fastapi import WebSocket


async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        data = await websocket.receive_text()

        response = {
            "message": f"Processed: {data}"
        }

        await websocket.send_json(response)
