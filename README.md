🚨 Ultrasonic Security Alarm

This project uses an ultrasonic sensor and a buzzer to detect any object or person that enters a defined area. When something comes closer than 200 cm, the alarm sounds.

Tested on: ESP32

🔧 Components
ESP32 DevKit
HC-SR04 ultrasonic sensor
Buzzer
🔌 Wiring
Part	Pin
TRIG	GPIO 16
ECHO	GPIO 4
Buzzer	GPIO 13
⚙️ How it works
The sensor measures the distance every 0.1 seconds.
If the distance is 200 cm or less, the buzzer sounds.
If not, the buzzer stays off.
▶️ Run

Copy main.py to the board and reset it. You can also test it in the Wokwi simulator using diagram.json.

📟 Sample output
152.4
151.9
87.3
🚀 Possible improvements
Add a door sensor (for example, a magnetic reed switch) to trigger the alarm when the door opens
Add a timeout to the echo loop
Add an LED or a notification module
Add more security modules
📄 License

MIT

