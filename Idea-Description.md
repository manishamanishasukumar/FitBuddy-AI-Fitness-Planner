FitBuddy is a Web Application that uses Google Gemini 1.5 Flash model to generate personalized fitness plans.

Input: user_id, age, gender, weight, height, fitness_goal (Weight Loss / Muscle Gain / Stay Fit), available_time, health_conditions (e.g., knee pain), diet_preference.

Process: We create a smart prompt and send to Gemini API. Gemini returns a strict JSON with 7-day plan.

Output: For each day - Exercise Name, Sets, Reps, Duration, Diet Tip.

Innovation: Feedback Loop System. If user says "Day 3 is too hard", we call /update-workout API and AI regenerates only that day with low-impact exercises instantly.
