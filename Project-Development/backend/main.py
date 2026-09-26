from fastapi import FastAPI, HTTPException
# POST /generate-workout - generates 7-day plan
# If user_id exists -> raise 409 Conflict (This is your screenshot error - expected behavior)
# POST /update-workout - takes feedback like "knee pain" and regenerates plan
