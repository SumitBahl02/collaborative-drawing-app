import asyncio
import websockets
import json

async def client():
    uri = "ws://127.0.0.1:8766"
    while True:
        try:
            async with websockets.connect(uri) as websocket:
                # Register a user
                while True:
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    await websocket.send(json.dumps({
                        "command": "REGISTER",
                        "username": username,
                        "password": password
                    }))
                    response = await websocket.recv()
                    print(response)
                    if "SUCCESS" in response:
                        break
                    else:
                        print("Registration failed. Try again.")

                # Login
                await websocket.send(json.dumps({
                    "command": "LOGIN",
                    "username": username,
                    "password": password
                }))
                print(await websocket.recv())  # Receive login response

                # Join a canvas
                canvas_name = input("Enter canvas name: ")
                await websocket.send(json.dumps({
                    "command": "JOIN_CANVAS",
                    "username": username,
                    "canvas_name": canvas_name
                }))
                print(await websocket.recv())  # Receive join response

                while True:
                    # Send commands
                    command = input("Enter command (DRAW, UNDO, REDO, CHAT, SAVE_CANVAS, LOAD_CANVAS, EXIT): ").upper()
                    if command == "EXIT":
                        break
                    elif command == "DRAW":
                        try:
                            stroke = {
                                "startX": int(input("Enter startX: ")),
                                "startY": int(input("Enter startY: ")),
                                "endX": int(input("Enter endX: ")),
                                "endY": int(input("Enter endY: ")),
                                "color": input("Enter color (e.g., #000000): "),
                                "size": int(input("Enter brush size: "))
                            }
                            await websocket.send(json.dumps({
                                "command": "DRAW",
                                "username": username,
                                "canvas_name": canvas_name,
                                "stroke": stroke
                            }))
                        except ValueError:
                            print("Invalid input. Please enter numbers for coordinates and brush size.")
                    elif command in ["UNDO", "REDO"]:
                        await websocket.send(json.dumps({
                            "command": command,
                            "canvas_name": canvas_name
                        }))
                    elif command == "CHAT":
                        message = input("Enter message: ")
                        await websocket.send(json.dumps({
                            "command": "CHAT",
                            "username": username,
                            "canvas_name": canvas_name,
                            "message": message
                        }))
                    elif command in ["SAVE_CANVAS", "LOAD_CANVAS"]:
                        await websocket.send(json.dumps({
                            "command": command,
                            "canvas_name": canvas_name
                        }))
                    else:
                        print("Invalid command. Please try again.")

                    # Listen for messages
                    response = await websocket.recv()
                    print(f"Received: {response}")
        except websockets.exceptions.ConnectionClosedError:
            print("Connection to the server was closed unexpectedly. Reconnecting...")
        except Exception as e:
            print(f"An error occurred: {e}")
            break

# Run the client
asyncio.run(client())