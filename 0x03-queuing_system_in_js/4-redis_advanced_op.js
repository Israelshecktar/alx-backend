const redis = require('redis');
const client = redis.createClient();

// When the client connects to the Redis server
client.on('connect', function() {
  console.log('Redis client connected to the server');
});

// Function to set hash values
function setHashValues() {
  const schools = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2
  };

  for (const [key, value] of Object.entries(schools)) {
    client.hset('HolbertonSchools', key, value, redis.print);
  }
}

// Function to display hash values
function displayHashValues() {
  client.hgetall('HolbertonSchools', function(err, values) {
    console.log(values);
  });
}

// Run the functions to set and display hash values
setHashValues();
displayHashValues();

// To properly close the connection
process.on('SIGINT', function() {
  client.quit();
});
