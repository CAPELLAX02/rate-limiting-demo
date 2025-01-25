# Rate Limiting Demonstration

This project demonstrates a simple **rate limiting mechanism** implemented using **Spring Boot** and **Bucket4j**, accompanied by a Python script (`ddos.py`) to simulate client requests and test the rate limiting functionality.

## Features
- **Rate Limiting**: Limits each client to 10 requests per second using `Bucket4j` in-memory.
- **Spring Boot**: Provides a RESTful API endpoint protected by rate limiting.
- **Python Client Simulation**: Bombards the API with requests to test rate limiting behavior.

## How It Works

1. **Spring Boot Application**:
    - A `Filter` intercepts each request.
    - Uses `Bucket4j` to track and limit client requests based on their IP address.
    - Returns `429 Too Many Requests` when the limit is exceeded.

2. **Python Script**:
    - Sends 20 requests to the Spring Boot API.
    - Simulates a client sending requests in rapid succession.
    - Outputs success or rate limiting responses to the console.

## Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/CAPELLAX02/rate-limiting-demo
   ```

    ```bash
   cd rate-limiting-demo
    ```

2. **Monitor the Output**:
    - The Python script (`ddos.py`) will send 20 requests to the API endpoint.
        - First 15 requests: Success (`200 OK`)
        - Remaining requests: Rate Limited (`429 Too Many Requests`)

   Example output where the rate limit is 15:
   ```
    Request 1: Success (200) - Welcome to the rate-limited API endpoint!
    Request 2: Success (200) - Welcome to the rate-limited API endpoint!
    Request 3: Success (200) - Welcome to the rate-limited API endpoint!
    Request 4: Success (200) - Welcome to the rate-limited API endpoint!
    Request 5: Success (200) - Welcome to the rate-limited API endpoint!
    Request 6: Success (200) - Welcome to the rate-limited API endpoint!
    Request 7: Success (200) - Welcome to the rate-limited API endpoint!
    Request 8: Success (200) - Welcome to the rate-limited API endpoint!
    Request 9: Success (200) - Welcome to the rate-limited API endpoint!
    Request 10: Success (200) - Welcome to the rate-limited API endpoint!
    Request 11: Success (200) - Welcome to the rate-limited API endpoint!
    Request 12: Success (200) - Welcome to the rate-limited API endpoint!
    Request 13: Success (200) - Welcome to the rate-limited API endpoint!
    Request 14: Success (200) - Welcome to the rate-limited API endpoint!
    Request 15: Success (200) - Welcome to the rate-limited API endpoint!
    Request 16: Rate Limited (429) - {'error': 'Too many requests. Please try again later.'}
    Request 17: Rate Limited (429) - {'error': 'Too many requests. Please try again later.'}
    Request 18: Rate Limited (429) - {'error': 'Too many requests. Please try again later.'}
    Request 19: Rate Limited (429) - {'error': 'Too many requests. Please try again later.'}
    Request 20: Rate Limited (429) - {'error': 'Too many requests. Please try again later.'}
   ```

3. **Test Manually (Optional)**:
   Use Postman or a tool like `cURL` to manually send requests:
   ```bash
   curl -X GET http://localhost:8080/api/test
   ```

## Configuration

- **Rate Limiting Rules**:
    - Configured in `RateLimitingFilter.java`:
      ```java
      private Bucket createNewBucket(String clientIp) {
          return Bucket4j.builder()
              .addLimit(Bandwidth.classic(15, Refill.intervally(10, Duration.ofSeconds(1))))
              .build();
      }
      ```
        - **15 requests/second**: Modify these values to customize the rate limit.

    - You can also customize the `ddos.py` file to increase or decrease the number of requests:
        ```bash
          url = "http://localhost:8080/api/test"
          for i in range(20):
            try:
              response = requests.get(url)
                if response.status_code == 200:
                  print(f"Request {i + 1}: Success - {response.text}")
                elif response.status_code == 429:
                  print(f"Request {i + 1}: Rate Limited - {response.json()}")
                else:
                  print(f"Request {i + 1}: Unexpected Status - {response.status_code}")
            except requests.exceptions.RequestException as e:
              print(f"Request {i + 1}: Failed - {e}")
        ```

- **API Endpoint**:
    - Hosted at: `http://localhost:8080/api/test` (adjust port as needed).