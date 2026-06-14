🧠 Why This Is Important

In small systems:
User Service
http://localhost:5001

But in real systems:
User Service
IP changes constantly

Instead of hardcoding addresses:
service-name → address lookup

This is called Service Discovery.

👉 Used by:
	•	Kubernetes
	•	Netflix Eureka
	•	Consul
	•	AWS ECS

⸻

🛠 Tech Stack
	•	Python
	•	Flask
	•	Dictionary Registry

⸻

📂 Project Structure
service-discovery/
├── registry.py
├── service.py
└── README.md
