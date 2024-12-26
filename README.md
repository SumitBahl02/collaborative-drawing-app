---

```markdown
# 🎨 Collaborative Drawing App 🖌️

A **real-time collaborative drawing and chat application** built with Python and WebSockets. This project includes a **WebSocket server** and a **command-line client** for interacting with the server. Perfect for artists, teams, or anyone who wants to collaborate in real-time!

---

## ✨ Features

- **👤 User Registration and Login**: Users can register and log in with a username and password.
- **🖼️ Canvas Management**: Users can join or create canvases to collaborate in real-time.
- **🎨 Real-Time Drawing**: Users can draw on the canvas, and strokes are broadcasted to all users in the same canvas.
- **↩️ Undo/Redo**: Users can undo or redo their strokes.
- **💬 Chat**: Users can send chat messages to others in the same canvas.
- **💾 Save/Load Canvas**: Users can save and load canvases.

---

## 🛠️ Installation

### 📋 Requirements
- Python 3.x
- `websockets` library
- `nest_asyncio` library

### ⚙️ Steps to Set Up
1. Clone the repository:
   ```bash
   git clone https://github.com/SumitBahl02/collaborative-drawing-app.git
   cd collaborative-drawing-app
   ```

2. Install the required Python libraries:
   ```bash
   pip install websockets nest_asyncio
   ```

3. Start the server:
   ```bash
   python server.py
   ```

4. Run the client in a separate terminal:
   ```bash
   python client.py
   ```

---

## 🚀 How to Use

### Step 1: Register and Log In
- Enter a username and password to register.
- Log in with the same credentials.

### Step 2: Join a Canvas
- Enter a canvas name to join or create a new canvas.

### Step 3: Draw
- Use the `DRAW` command to draw strokes on the canvas.

### Step 4: Undo/Redo
- Use the `UNDO` and `REDO` commands to undo or redo strokes.

### Step 5: Chat
- Use the `CHAT` command to send messages to other users in the canvas.

### Step 6: Save/Load Canvas
- Use the `SAVE_CANVAS` command to save the canvas.
- Use the `LOAD_CANVAS` command to load a previously saved canvas.

### Step 7: Exit
- Use the `EXIT` command to disconnect from the server.

---

## 📜 Example Interaction

### Server Logs
```
2024-12-26 23:52:26,942 - Server initialized
2024-12-26 23:52:26,942 - Starting server on ws://127.0.0.1:8766
2024-12-26 23:52:29,937 - New client connected: ('127.0.0.1', 58309)
2024-12-26 23:52:36,859 - User sumit registered
2024-12-26 23:52:36,859 - User sumit logged in
2024-12-26 23:52:39,960 - User sumit joined canvas sumit
2024-12-26 23:52:44,768 - User sumit disconnected
```

### Client Interaction
```
Enter username: sumit
Enter password: sumit
{"status": "SUCCESS", "message": "Registered successfully"}
{"status": "SUCCESS", "message": "Logged in successfully"}
Enter canvas name: sumit
{"command": "CANVAS_HISTORY", "strokes": []}
Enter command (DRAW, UNDO, REDO, CHAT, SAVE_CANVAS, LOAD_CANVAS, EXIT): DRAW
Enter startX: 10
Enter startY: 10
Enter endX: 100
Enter endY: 100
Enter color (e.g., #000000): #000000
Enter brush size: 2
Received: {"status": "SUCCESS", "message": "Stroke drawn"}
Enter command (DRAW, UNDO, REDO, CHAT, SAVE_CANVAS, LOAD_CANVAS, EXIT): EXIT
```

---

## 📁 Files

- `server.py`: The WebSocket server code.
- `client.py`: The command-line client code.
- `sumit.json`, `sumithasifd.json`, `test_canvas.json`: Example canvas files saved by the server.

---

## 🚀 Future Enhancements (Frontend)

While this project currently uses a **command-line client**, it can be extended with a **frontend** for a more user-friendly experience. Here’s how:

### Frontend Ideas
1. **React Frontend**:
   - Use **React** and **React-Konva** to create a web-based drawing interface.
   - Connect to the WebSocket server for real-time updates.

2. **Features to Add**:
   - A visual canvas for drawing.
   - A chat box for real-time messaging.
   - Buttons for undo/redo, save/load, and other commands.

3. **How to Integrate**:
   - The frontend can connect to the existing WebSocket server (`ws://127.0.0.1:8766`).
   - Use the same commands (`DRAW`, `CHAT`, `UNDO`, etc.) to interact with the server.

---

## 🤝 Contributing

Contributions are welcome! Here’s how you can contribute to this project:

1. **Fork the Repository**:
   - Fork the project on GitHub.

2. **Create a New Branch**:
   - Create a new branch for your feature or bug fix:
     ```bash
     git checkout -b feature/NewFeature
     ```

3. **Commit Your Changes**:
   - Commit your changes with a descriptive message:
     ```bash
     git commit -m 'Add NewFeature'
     ```

4. **Push Your Branch**:
   - Push your branch to your forked repository:
     ```bash
     git push origin feature/NewFeature
     ```

5. **Submit a Pull Request**:
   - Open a pull request on GitHub with a detailed description of your changes.

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

```text
MIT License

Copyright (c) 2024 Sumit Bahl

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Credits
- **Sumit Bahl**: Developer of this awesome collaborative drawing app! 🚀

---

## 🚀 Get Started
Clone the repository and start collaborating in real-time:
```bash
git clone https://github.com/SumitBahl02/collaborative-drawing-app.git
cd collaborative-drawing-app
```

---

Let me know if you need further assistance! Happy coding! 🎉
```

---

### **How to Use**
1. Copy and paste this content into a file named `README.md` in your project folder.
2. Create a `LICENSE` file in the root folder and paste the MIT License text into it.
3. Push the updated files to GitHub:
   ```bash
   git add README.md LICENSE
   git commit -m "Add README and LICENSE"
   git push
   ```

---

Let me know if you need further tweaks! 🚀
