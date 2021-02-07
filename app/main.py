from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

# This is the client code section. Ideally, this should be in a frontend framework like React or Angular and communicate via websockets to the backend

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Sample WebSockets App</title>
    </head>
    <body>
        <h1>WebSocket Messages</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send Message</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


# This is the actual backend service piece
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    # Of course, do not loop while true in a real app
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Received message text: {data}")
