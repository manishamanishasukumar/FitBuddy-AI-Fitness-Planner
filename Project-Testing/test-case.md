TC01 - New User: Input: user_id=mani123, age=20, goal=Muscle Gain -> Expected: 200 OK with 7-day plan -> Status: PASS

TC02 - Duplicate User: Input: Same user_id=mani123 again -> Expected: 409 Conflict "User ID already exists" -> Status: PASS (This is your screenshot, this is correct design to prevent overwrite)

TC03 - Feedback Update: Input: user_id=mani123, feedback="Make Day 5 easier, knee pain" -> Expected: Day 5 with low-impact exercises -> Status: PASS

TC04 - Invalid Input: age=200 -> Expected: Validation Error -> Status: PASS
