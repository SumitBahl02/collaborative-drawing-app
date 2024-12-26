# 🎨 Collaborative Drawing App

A real-time collaborative drawing and chat application that brings artists and teams together. Built with Python and WebSockets, this application enables seamless real-time collaboration through an intuitive command-line interface.

## 🌟 Key Features

- **Real-time Collaboration**: Draw together with multiple users simultaneously
- **User Authentication**: Secure registration and login system
- **Canvas Management**: Create or join existing canvases
- **Drawing Tools**: Draw with customizable colors and brush sizes
- **History Management**: Undo/Redo support for drawing actions
- **Built-in Chat**: Communicate with other users in real-time
- **Data Persistence**: Save and load canvas states

## 🛠️ Technical Stack

- **Backend**: Python with WebSockets
- **Protocol**: WebSocket (ws://)
- **Storage**: JSON-based file system
- **Dependencies**: 
  - websockets
  - nest_asyncio

## 📦 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/SumitBahl02/collaborative-drawing-app.git
   cd collaborative-drawing-app
   ```

2. **Install Dependencies**
   ```bash
   pip install websockets nest_asyncio
   ```

3. **Start the Server**
   ```bash
   python server.py
   ```

4. **Launch the Client**
   ```bash
   python client.py
   ```

## 💡 Usage Guide

### Basic Commands

- `DRAW`: Create strokes on the canvas
  ```
  Command: DRAW
  startX: 10
  startY: 10
  endX: 100
  endY: 100
  color: #000000
  brush size: 2
  ```

- `UNDO`/`REDO`: Manage your drawing history
- `CHAT`: Send messages to other users
- `SAVE_CANVAS`/`LOAD_CANVAS`: Persist your work
- `EXIT`: Disconnect from the server

### Quick Start

1. **Register/Login**
   - Launch the client
   - Enter username and password when prompted

2. **Join a Canvas**
   - Specify a canvas name (creates new if doesn't exist)

3. **Start Drawing**
   - Use the DRAW command with coordinates and properties
   - Collaborate with other users in real-time

## 🔄 Real-time Collaboration

The app uses WebSocket connections to enable:
- Instant stroke synchronization
- Real-time chat messages
- Canvas state updates
- User presence tracking

## 🚀 Future Development

### Planned Features
- Graphical user interface using React
- Additional drawing tools and shapes
- Layer support
- Export/Import in various formats
- Room management system

### Frontend Integration
The existing WebSocket server is ready for frontend integration with:
- React + React-Konva for the drawing interface
- Real-time WebSocket communication
- Modern UI/UX design

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Credits

Developed with ❤️ by [Sumit Bahl](https://github.com/SumitBahl02)

## 📞 Support

- GitHub Issues: [Report bugs or request features](https://github.com/SumitBahl02/collaborative-drawing-app/issues)
- Email: 2022eeb1217@iitrpr.ac.in

---

**Note**: This is an active project under development. Contributions and feedback are welcome!
