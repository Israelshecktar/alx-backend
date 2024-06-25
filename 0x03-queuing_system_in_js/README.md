# Queuing System in JS

## Requirements

- Node.js 12.x
- Redis 5.0.7 or higher

## Installation

1. Install Redis:
   

sh wget http://download.redis.io/releases/redis-6.0.10.tar.gz tar xzf redis-6.0.10.tar.gz cd redis-6.0.10 make src/redis-server &

Replit Logo

2. Clone the repository and install dependencies:
   

sh git clone https://github.com/yourusername/alx-backend.git cd alx-backend/0x03-queuing_system_in_js npm install

Replit Logo

3. Start the server:
   

sh npm run dev

Replit Logo

## Usage

- Set a value in Redis:
  

sh curl -X POST -H "Content-Type: application/json" -d '{"key":"Holberton","value":"School"}' http://localhost:3000/set

Replit Logo

- Get a value from Redis:
  

sh curl http://localhost:3000/get/Holberton

Replit Logo

- Create a job in the queue:
  

sh curl -X POST -H "Content-Type: application/json" -d '{"title":"My Job"}' http://localhost:3000/job

Replit Logo

## License

This project is licensed under the ISC License.