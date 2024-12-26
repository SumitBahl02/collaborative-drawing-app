import asyncio
import websockets
import json
from datetime import datetime
import logging
import nest_asyncio

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

class DrawingServer:
    def __init__(self):
        self.clients = {}        # username: set of connections
        self.canvases = {}       # canvas_name: {users: set of usernames, strokes: list of strokes}
        self.history = {}        # canvas_name: {undo: list of strokes, redo: list of strokes}
        self.users = {}          # username: password
        logging.info("Server initialized")

    async def register_user(self, websocket, data):
        username = data['username']
        password = data['password']
        if username in self.users:
            await websocket.send(json.dumps({"status": "ERROR", "message": "Username already taken"}))
        else:
            self.users[username] = password
            await websocket.send(json.dumps({"status": "SUCCESS", "message": "Registered successfully"}))
            logging.info(f"User {username} registered")

    async def login_user(self, websocket, data):
        username = data['username']
        password = data['password']
        if username not in self.users:
            await websocket.send(json.dumps({"status": "ERROR", "message": "Username does not exist"}))
        elif self.users[username] != password:
            await websocket.send(json.dumps({"status": "ERROR", "message": "Incorrect password"}))
        else:
            self.clients.setdefault(username, set()).add(websocket)
            await websocket.send(json.dumps({"status": "SUCCESS", "message": "Logged in successfully"}))
            logging.info(f"User {username} logged in")

    async def handle_message(self, websocket, message):
        try:
            data = json.loads(message)
            command = data.get('command')
            logging.info(f"Received command: {command}")

            if command == "REGISTER":
                await self.register_user(websocket, data)

            elif command == "LOGIN":
                await self.login_user(websocket, data)

            elif command == "JOIN_CANVAS":
                username = data['username']
                canvas_name = data['canvas_name']
                if canvas_name not in self.canvases:
                    self.canvases[canvas_name] = {'users': set(), 'strokes': []}
                self.canvases[canvas_name]['users'].add(username)
                self.clients.setdefault(username, set()).add(websocket)
                # Send canvas history to the new user
                strokes = self.canvases[canvas_name]['strokes']
                await websocket.send(json.dumps({"command": "CANVAS_HISTORY", "strokes": strokes}))
                await websocket.send(json.dumps({"status": "SUCCESS", "message": "Joined canvas successfully"}))
                # Broadcast updated user list
                await self.broadcast_user_list(canvas_name)
                logging.info(f"User {username} joined canvas {canvas_name}")

            elif command == "DRAW":
                username = data['username']
                canvas_name = data['canvas_name']
                stroke = data['stroke']
                if canvas_name in self.canvases and username in self.canvases[canvas_name]['users']:
                    self.canvases[canvas_name]['strokes'].append(stroke)
                    # Store the stroke in history
                    self.history.setdefault(canvas_name, {'undo': [], 'redo': []})['undo'].append(stroke)
                    # Broadcast the stroke to all users in the canvas
                    await self.broadcast_draw(canvas_name, stroke)
                    logging.info(f"User {username} drew on canvas {canvas_name}")

            elif command == "UNDO":
                canvas_name = data['canvas_name']
                if canvas_name in self.history and self.history[canvas_name]['undo']:
                    last_stroke = self.history[canvas_name]['undo'].pop()
                    self.history[canvas_name]['redo'].append(last_stroke)
                    # Broadcast the undo action to all users in the canvas
                    await self.broadcast_undo(canvas_name, last_stroke)
                    logging.info(f"Undo action performed on canvas {canvas_name}")

            elif command == "REDO":
                canvas_name = data['canvas_name']
                if canvas_name in self.history and self.history[canvas_name]['redo']:
                    redo_stroke = self.history[canvas_name]['redo'].pop()
                    self.history[canvas_name]['undo'].append(redo_stroke)
                    # Broadcast the redo action to all users in the canvas
                    await self.broadcast_redo(canvas_name, redo_stroke)
                    logging.info(f"Redo action performed on canvas {canvas_name}")

            elif command == "CHAT":
                username = data['username']
                canvas_name = data['canvas_name']
                message = data['message']
                if canvas_name in self.canvases and username in self.canvases[canvas_name]['users']:
                    # Broadcast the chat message to all users in the canvas
                    chat_data = {
                        "command": "CHAT",
                        "username": username,
                        "message": message,
                        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                    await self.broadcast_chat(canvas_name, chat_data)
                    logging.info(f"User {username} sent a chat message on canvas {canvas_name}")

            elif command == "SAVE_CANVAS":
                canvas_name = data['canvas_name']
                if canvas_name in self.canvases:
                    strokes = self.canvases[canvas_name]['strokes']
                    with open(f"{canvas_name}.json", "w") as f:
                        json.dump(strokes, f)
                    await websocket.send(json.dumps({"status": "SUCCESS", "message": "Canvas saved successfully"}))
                    logging.info(f"Canvas {canvas_name} saved")

            elif command == "LOAD_CANVAS":
                canvas_name = data['canvas_name']
                try:
                    with open(f"{canvas_name}.json", "r") as f:
                        strokes = json.load(f)
                    self.canvases[canvas_name]['strokes'] = strokes
                    await websocket.send(json.dumps({"command": "CANVAS_HISTORY", "strokes": strokes}))
                    logging.info(f"Canvas {canvas_name} loaded")
                except FileNotFoundError:
                    await websocket.send(json.dumps({"status": "ERROR", "message": "Canvas not found"}))
                    logging.error(f"Canvas {canvas_name} not found")

        except Exception as e:
            logging.error(f"Error handling message: {e}")

    async def broadcast_draw(self, canvas_name, stroke):
        for user in self.canvases[canvas_name]['users']:
            for ws in self.clients.get(user, set()):
                await ws.send(json.dumps({"command": "DRAW", "stroke": stroke}))

    async def broadcast_undo(self, canvas_name, stroke):
        for user in self.canvases[canvas_name]['users']:
            for ws in self.clients.get(user, set()):
                await ws.send(json.dumps({"command": "UNDO", "stroke": stroke}))

    async def broadcast_redo(self, canvas_name, stroke):
        for user in self.canvases[canvas_name]['users']:
            for ws in self.clients.get(user, set()):
                await ws.send(json.dumps({"command": "REDO", "stroke": stroke}))

    async def broadcast_chat(self, canvas_name, chat_data):
        for user in self.canvases[canvas_name]['users']:
            for ws in self.clients.get(user, set()):
                await ws.send(json.dumps(chat_data))

    async def broadcast_user_list(self, canvas_name):
        user_list = list(self.canvases[canvas_name]['users'])
        for user in self.canvases[canvas_name]['users']:
            for ws in self.clients.get(user, set()):
                await ws.send(json.dumps({"command": "USER_LIST", "users": user_list}))

    async def handle_client(self, websocket, path):
        logging.info(f"New client connected: {websocket.remote_address}")
        async for message in websocket:
            await self.handle_message(websocket, message)
            
        # Handle disconnection
        username = None
        for user, connections in self.clients.items():
            if websocket in connections:
                username = user
                connections.remove(websocket)
                if not connections:
                    del self.clients[username]
                break
        if username:
            for canvas_name, canvas_data in self.canvases.items():
                if username in canvas_data['users']:
                    canvas_data['users'].remove(username)
                    await self.broadcast_user_list(canvas_name)
            logging.info(f"User {username} disconnected")
                       
    async def run(self):
        logging.info("Starting server on ws://127.0.0.1:8766")
        async with websockets.serve(
            self.handle_client, 
            '127.0.0.1', 
            8766,
            ping_interval=60,  # Send a ping every 60 seconds
            ping_timeout=120   # Wait 120 seconds for a pong response
        ):
            await asyncio.Future()  # Keep the server running indefinitely

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

# Create and run the server
server = DrawingServer()
asyncio.run(server.run())