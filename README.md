# 📹 Django Video Chat LMS Integration

A real-time video chat web application built with Django and WebSockets. This app supports one-on-one and group (mesh) video calls, with chat sidebar, mic/camera toggle, and mobile responsiveness — perfect for Learning Management Systems (LMS) where students and tutors interact concurrently.

---

## 🚀 Features

- ✅ One-on-one video chat
- ✅ Group video call (Mesh-style)
- ✅ Real-time chat sidebar
- ✅ Mic/Camera toggle controls
- ✅ Mobile responsive (Tailwind CSS)
- ✅ Django Channels + WebRTC signaling
- ✅ WebSocket backend handling

---

## 🛠 Tech Stack

- **Backend**: Django 5, Channels, Redis
- **Frontend**: HTML5, Tailwind CSS, JavaScript (WebRTC)
- **Real-time**: WebSockets
- **Signaling**: Custom Django `consumers.py`
- **Database**: SQLite (default, can switch to PostgreSQL)
- **Deployment**: [Optional: Add platform like Railway, Heroku, etc.]

---

## 🖥️ Screenshots

_Add screenshots of the video chat, mobile view, chat sidebar, etc._

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/Omartinsville/VideochatUsing.git
cd django-videochat

# (Optional) Create a virtual environment
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Set environment variables (or create a .env file)
export SECRET_KEY=your-secret-key
export DEBUG=True

# Apply migrations
python manage.py migrate

# Run development server
python manage.py runserver

# 📹 Django Video Chat LMS Integration

A real-time video chat web application built with Django and WebSockets. This app supports one-on-one and group (mesh) video calls, with chat sidebar, mic/camera toggle, and mobile responsiveness — perfect for Learning Management Systems (LMS) where students and tutors interact concurrently.

---

## 🚀 Features

- ✅ One-on-one video chat
- ✅ Group video call (Mesh-style)
- ✅ Real-time chat sidebar
- ✅ Mic/Camera toggle controls
- ✅ Mobile responsive (Tailwind CSS)
- ✅ Django Channels + WebRTC signaling
- ✅ WebSocket backend handling

---

## 🛠 Tech Stack

- **Backend**: Django 5, Channels, Redis
- **Frontend**: HTML5, Tailwind CSS, JavaScript (WebRTC)
- **Real-time**: WebSockets
- **Signaling**: Custom Django `consumers.py`
- **Database**: SQLite (default, can switch to PostgreSQL)
- **Deployment**: [Optional: Add platform like Railway, Heroku, etc.]

---

## 🖥️ Screenshots

_Add screenshots of the video chat, mobile view, chat sidebar, etc._

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/django-videochat.git
cd django-videochat

# (Optional) Create a virtual environment
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Set environment variables (or create a .env file)
export SECRET_KEY=your-secret-key
export DEBUG=True

# Apply migrations
python manage.py migrate

# Run development server
python manage.py runserver


📱 Mobile Access
To test from your phone:

Make sure your PC and phone are on the same Wi-Fi.

Get your computer’s local IP: ipconfig (Windows) or ifconfig (Linux/Mac).

Visit http://<your-ip>:8000/call/room-name/ on your phone browser.

🔧 WebSocket + Group Call Logic
This app uses mesh-based group call architecture via Django Channels.

Each user joins a room and initiates peer connections with all other users.

The consumers.py handles signaling and message broadcasting.

Includes support for toggling mic/camera and chat messaging.

⚙️ Deployment
Coming soon — Guide for deploying on Railway, Heroku, or a VPS.

🙋‍♂️ Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

📄 License
MIT License

✨ Author
Martins Oluwagbemiga Akindele
📧 omartinsville106@gmail.com
🌐 GitHub | LinkedIn


---

Let me know if you want:

- A tailored `requirements.txt` file
- A `deployment.md` guide
- Screenshots or badges added
- Live link/button if hosted

Happy coding!
