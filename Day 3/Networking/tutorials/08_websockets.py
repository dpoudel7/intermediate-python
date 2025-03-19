import asyncio
import websockets
import json
import time
import datetime
import random
import signal
import sys

# Simple WebSocket Server
async def websocket_server(websocket, path):
    """Handle WebSocket connections."""
    client_id = id(websocket)
    print(f"Client {client_id} connected from {websocket.remote_address}")
    
    try:
        # Register the client
        CLIENTS[client_id] = websocket
        
        # Send welcome message
        await websocket.send(json.dumps({
            "type": "welcome",
            "message": f"Welcome! You are client #{client_id}",
            "timestamp": datetime.datetime.now().isoformat()
        }))
        
        # Broadcast new client notification
        await broadcast({
            "type": "notification",
            "message": f"Client {client_id} has joined",
            "timestamp": datetime.datetime.now().isoformat()
        }, exclude=client_id)
        
        # Handle messages from this client
        async for message in websocket:
            try:
                data = json.loads(message)
                print(f"Received from client {client_id}: {data}")
                
                # Echo the message back with a timestamp
                await websocket.send(json.dumps({
                    "type": "echo",
                    "original": data,
                    "timestamp": datetime.datetime.now().isoformat()
                }))
                
                # If it's a chat message, broadcast to other clients
                if data.get("type") == "chat":
                    await broadcast({
                        "type": "chat",
                        "sender": client_id,
                        "message": data.get("message", ""),
                        "timestamp": datetime.datetime.now().isoformat()
                    }, exclude=client_id)
            except json.JSONDecodeError:
                # Handle non-JSON messages
                await websocket.send(json.dumps({
                    "type": "error",
                    "message": "Please send valid JSON",
                    "timestamp": datetime.datetime.now().isoformat()
                }))
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Client {client_id} disconnected: {e}")
    finally:
        # Unregister the client
        if client_id in CLIENTS:
            del CLIENTS[client_id]
        
        # Broadcast disconnection
        await broadcast({
            "type": "notification",
            "message": f"Client {client_id} has left",
            "timestamp": datetime.datetime.now().isoformat()
        })

async def broadcast(message, exclude=None):
    """Broadcast a message to all connected clients except the excluded one."""
    if not isinstance(message, str):
        message = json.dumps(message)
    
    disconnected_clients = []
    for client_id, websocket in CLIENTS.items():
        if client_id != exclude:
            try:
                await websocket.send(message)
            except websockets.exceptions.ConnectionClosed:
                disconnected_clients.append(client_id)
    
    # Clean up disconnected clients
    for client_id in disconnected_clients:
        if client_id in CLIENTS:
            del CLIENTS[client_id]

# Dictionary to track connected clients
CLIENTS = {}

# Data simulation for a dashboard example
async def generate_dashboard_data():
    """Generate simulated dashboard data and broadcast to clients."""
    while True:
        # Generate random data
        data = {
            "type": "dashboard_update",
            "timestamp": datetime.datetime.now().isoformat(),
            "metrics": {
                "cpu_usage": random.uniform(0, 100),
                "memory_usage": random.uniform(0, 100),
                "active_users": random.randint(0, 500),
                "requests_per_second": random.randint(0, 200),
                "error_rate": random.uniform(0, 5)
            }
        }
        
        # Broadcast to all clients
        await broadcast(data)
        
        # Wait before sending next update
        await asyncio.sleep(5)

# Stock price simulator
async def generate_stock_prices():
    """Generate simulated stock price data and broadcast to clients."""
    # Starting prices for some stocks
    stocks = {
        "AAPL": 150.0,
        "MSFT": 300.0,
        "GOOG": 2500.0,
        "AMZN": 3000.0,
        "TSLA": 800.0
    }
    
    while True:
        # Update each stock with a small random change
        for symbol in stocks:
            # Random percentage change (-2% to +2%)
            change_pct = random.uniform(-2, 2)
            stocks[symbol] *= (1 + change_pct / 100)
        
        # Create the update message
        data = {
            "type": "stock_update",
            "timestamp": datetime.datetime.now().isoformat(),
            "stocks": {symbol: round(price, 2) for symbol, price in stocks.items()}
        }
        
        # Broadcast to all clients
        await broadcast(data)
        
        # Wait before sending next update
        await asyncio.sleep(3)

# WebSocket client example
async def websocket_client(uri):
    """Example WebSocket client implementation."""
    print(f"Connecting to {uri}...")
    
    try:
        async with websockets.connect(uri) as websocket:
            print("Connected!")
            
            # Start a task to receive messages
            receive_task = asyncio.create_task(receive_messages(websocket))
            
            # Send messages periodically
            try:
                for i in range(5):
                    message = {
                        "type": "chat",
                        "message": f"Hello from client, message #{i+1}"
                    }
                    
                    print(f"Sending: {message}")
                    await websocket.send(json.dumps(message))
                    await asyncio.sleep(2)
                
                # Send a message and wait for the response
                await websocket.send(json.dumps({
                    "type": "query",
                    "query": "status"
                }))
                
                # Wait for a while to receive any final messages
                await asyncio.sleep(5)
                
            except asyncio.CancelledError:
                print("Send task cancelled")
            
            # Cancel the receive task
            receive_task.cancel()
            try:
                await receive_task
            except asyncio.CancelledError:
                pass
            
    except Exception as e:
        print(f"Error: {e}")

async def receive_messages(websocket):
    """Receive and display messages from the WebSocket server."""
    try:
        async for message in websocket:
            try:
                data = json.loads(message)
                print(f"Received: {data}")
            except json.JSONDecodeError:
                print(f"Received non-JSON message: {message}")
    except asyncio.CancelledError:
        print("Receive task cancelled")
        raise
    except Exception as e:
        print(f"Error in receive_messages: {e}")

# Create a simple browser client using HTML
HTML_CLIENT = """
<!DOCTYPE html>
<html>
<head>
    <title>WebSocket Demo</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }
        #messages { border: 1px solid #ccc; height: 300px; padding: 10px; overflow-y: auto; margin-bottom: 10px; }
        #dashboard { border: 1px solid #ccc; padding: 10px; margin-bottom: 10px; }
        #stocks { border: 1px solid #ccc; padding: 10px; margin-bottom: 10px; }
        .message { margin-bottom: 5px; }
        .system { color: #888; }
        .error { color: red; }
        .chat { color: blue; }
        input[type="text"] { width: 80%; padding: 5px; }
        button { padding: 5px 10px; }
    </style>
</head>
<body>
    <h1>WebSocket Demo</h1>
    
    <h2>Chat</h2>
    <div id="messages"></div>
    <input type="text" id="messageInput" placeholder="Type a message...">
    <button onclick="sendMessage()">Send</button>
    
    <h2>Dashboard Metrics</h2>
    <div id="dashboard">
        <p>CPU Usage: <span id="cpu_usage">-</span>%</p>
        <p>Memory Usage: <span id="memory_usage">-</span>%</p>
        <p>Active Users: <span id="active_users">-</span></p>
        <p>Requests per Second: <span id="requests_per_second">-</span></p>
        <p>Error Rate: <span id="error_rate">-</span>%</p>
    </div>
    
    <h2>Stock Prices</h2>
    <div id="stocks">
        <p>Loading stock data...</p>
    </div>
    
    <script>
        // Connection status
        let connectionOpen = false;
        
        // Create WebSocket connection
        const socket = new WebSocket('ws://localhost:8765');
        
        // Connection opened
        socket.addEventListener('open', function (event) {
            connectionOpen = true;
            addMessage('Connected to server', 'system');
        });
        
        // Connection closed
        socket.addEventListener('close', function (event) {
            connectionOpen = false;
            addMessage('Disconnected from server', 'system');
        });
        
        // Listen for messages
        socket.addEventListener('message', function (event) {
            try {
                const data = JSON.parse(event.data);
                
                // Handle different message types
                switch(data.type) {
                    case 'welcome':
                    case 'notification':
                        addMessage(data.message, 'system');
                        break;
                    case 'chat':
                        addMessage(`Client ${data.sender}: ${data.message}`, 'chat');
                        break;
                    case 'echo':
                        addMessage(`Echo: ${JSON.stringify(data.original)}`, 'system');
                        break;
                    case 'error':
                        addMessage(`Error: ${data.message}`, 'error');
                        break;
                    case 'dashboard_update':
                        updateDashboard(data.metrics);
                        break;
                    case 'stock_update':
                        updateStocks(data.stocks);
                        break;
                    default:
                        addMessage(`Received: ${JSON.stringify(data)}`, 'system');
                }
            } catch (e) {
                addMessage(`Error processing message: ${e}`, 'error');
            }
        });
        
        // Handle errors
        socket.addEventListener('error', function (event) {
            addMessage('WebSocket error', 'error');
        });
        
        function sendMessage() {
            const input = document.getElementById('messageInput');
            const message = input.value.trim();
            
            if (message && connectionOpen) {
                const data = {
                    type: 'chat',
                    message: message
                };
                
                socket.send(JSON.stringify(data));
                addMessage(`You: ${message}`, 'chat');
                input.value = '';
            }
        }
        
        function addMessage(message, type) {
            const messagesDiv = document.getElementById('messages');
            const messageElement = document.createElement('div');
            messageElement.className = `message ${type}`;
            messageElement.textContent = message;
            messagesDiv.appendChild(messageElement);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        }
        
        function updateDashboard(metrics) {
            document.getElementById('cpu_usage').textContent = metrics.cpu_usage.toFixed(1);
            document.getElementById('memory_usage').textContent = metrics.memory_usage.toFixed(1);
            document.getElementById('active_users').textContent = metrics.active_users;
            document.getElementById('requests_per_second').textContent = metrics.requests_per_second;
            document.getElementById('error_rate').textContent = metrics.error_rate.toFixed(2);
        }
        
        function updateStocks(stocks) {
            const stocksDiv = document.getElementById('stocks');
            stocksDiv.innerHTML = '';
            
            for (const [symbol, price] of Object.entries(stocks)) {
                const stockElement = document.createElement('p');
                stockElement.textContent = `${symbol}: $${price}`;
                stocksDiv.appendChild(stockElement);
            }
        }
        
        // Allow sending by pressing Enter
        document.getElementById('messageInput').addEventListener('keyup', function(event) {
            if (event.key === 'Enter') {
                sendMessage();
            }
        });
    </script>
</body>
</html>
"""

# Function to start the WebSocket server
async def start_server(host='localhost', port=8765):
    """Start the WebSocket server and data generators."""
    # Create the server
    server = await websockets.serve(websocket_server, host, port)
    print(f"WebSocket server started at ws://{host}:{port}")
    
    # Start data generators
    dashboard_task = asyncio.create_task(generate_dashboard_data())
    stocks_task = asyncio.create_task(generate_stock_prices())
    
    # Handle graceful shutdown
    loop = asyncio.get_running_loop()
    
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, lambda: asyncio.create_task(shutdown(server, dashboard_task, stocks_task)))
    
    # Keep the server running
    await server.wait_closed()

async def shutdown(server, *tasks):
    """Shutdown the server and cancel tasks gracefully."""
    print("Shutting down...")
    
    # Cancel all background tasks
    for task in tasks:
        task.cancel()
    
    # Close the server
    server.close()
    await server.wait_closed()
    
    # Stop the event loop
    asyncio.get_event_loop().stop()

# Save the HTML client to a file
def save_html_client(filename="websocket_client.html"):
    """Save the HTML client to a file."""
    with open(filename, "w") as f:
        f.write(HTML_CLIENT)
    print(f"HTML client saved to {filename}")

# Function to demonstrate WebSocket functionality
def demonstrate_websockets():
    """Demonstrate WebSocket functionality."""
    print("WEBSOCKET DEMONSTRATION")
    print("----------------------")
    print("WebSockets provide full-duplex communication channels over a single TCP connection.")
    
    # Save HTML client
    save_html_client()
    
    print("\nDemonstration options:")
    print("1. Start WebSocket server")
    print("2. Run WebSocket client")
    print("3. Open HTML client in browser")
    print("\nTo start the WebSocket server, run:")
    print("    asyncio.run(start_server())")
    print("\nTo run a WebSocket client, run:")
    print("    asyncio.run(websocket_client('ws://localhost:8765'))")
    print("\nTo use the HTML client, open the 'websocket_client.html' file in a browser")
    print("after starting the server.")

# Main function
def main():
    """Main function."""
    demonstrate_websockets()
    
    # Uncomment one of these to run the demonstration
    # asyncio.run(start_server())
    # asyncio.run(websocket_client('ws://localhost:8765'))

if __name__ == "__main__":
    main()