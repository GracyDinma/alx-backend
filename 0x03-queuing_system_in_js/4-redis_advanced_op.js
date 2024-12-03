import redis, { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Create Hash
const createHash = () => {
  client.hset('HolbertonSchools', 'Portland', '50', redis.print);
  client.hset('HolbertonSchools', 'Seattle', '80', redis.print);
  client.hset('HolbertonSchools', 'New York', '20', redis.print);
  client.hset('HolbertonSchools', 'Bogota', '20', redis.print);
  client.hset('HolbertonSchools', 'Cali', '40', redis.print);
  client.hset('HolbertonSchools', 'Paris', '2', redis.print);
};
// Display Hash
const displayHash = () => {
  client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) {
      console.error(`Error: ${err.message}`);
    } else {
      console.log(reply);
    }
  });
};

// Call the functions
createHash();
displayHash();
