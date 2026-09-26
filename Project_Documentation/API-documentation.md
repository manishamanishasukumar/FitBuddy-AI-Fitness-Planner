POST /generate-workout
Body: {"user_id":"test1", "age":20, "weight":70, "height":175, "goal":"Weight Loss", "health_info":"knee pain"}
Response: 200 OK with plan JSON

POST /update-workout
Body: {"user_id":"test1", "feedback":"Make it easier"}
Response: 200 OK with updated plan

GET /docs - Swagger UI for testing
