# 🌱 Ecosphere – GreenFund Connect

**Crowdfunding platform for renewable energy projects** combining AI-powered investor-founder matchmaking, sentiment analysis, and an escrow-backed payment system.  

Built using **MongoDB**, **React**, **React Native**, **Node.js**, **Flask**, **FAISS**, **Llama**, and **Whisper**.

---

## 🔧 Tech Stack

- **Frontend:** React (Web), React Native (Mobile)
- **Backend:** Node.js (API), Flask (AI microservices)
- **Database:** MongoDB
- **AI & ML:**
  - **FAISS** – Investor-founder vector matching
  - **Llama** – Project feasibility scoring and sentiment analysis
  - **Whisper** – Real-time voice transcription for meeting reviews
  - **OpenCV + YOLO** – Eco-product detection for marketplace
- **Payments:** Escrow-backed system (Razorpay integration)

---

## 🚀 Features

### 🔗 Investor–Founder Connect
- AI-based matchmaking using **FAISS** on project + investor embeddings.
- Sentiment and engagement scoring using **Llama** and **Whisper** on video meetings.

### 💰 Secure Crowdfunding
- Milestone-based escrow payment architecture.
- User score & carbon footprint-based investment badges.

### 🛍️ Eco-Marketplace
- Recommends eco-friendly products based on object detection (OpenCV).
- Items scored with **environmental impact metrics**.

### 📊 Real-time Dashboard
- Track project progress, funding stages, CO₂ offsets.
- Personalized calendar (Google Calendar sync) and community updates.

---

## 🧠 AI Modules Breakdown

| Module               | Purpose                                      | Tech Used                 |
|----------------------|----------------------------------------------|---------------------------|
| Feasibility Scoring  | Assess project success likelihood            | Llama (custom fine-tuned) |
| Meeting Sentiment    | Analyze tone in investor-founder calls       | Whisper + Llama           |
| Marketplace Engine   | Suggest eco-products from images             | OpenCV + YOLO             |
| Matchmaking          | Recommend matches via embeddings             | FAISS + MongoDB vectors   |

---

### 🧑‍💼 Investor App 
![Investor App UI](https://github.com/user-attachments/assets/94ae3cf7-5620-4303-953c-a1ec17e9cded)
![Investor App UI](https://github.com/user-attachments/assets/e17cd95b-f5a6-452b-bdb9-d4f7176c9d5e)
![image](https://github.com/user-attachments/assets/89e1a5e1-7c0e-4e7a-a938-8c955cdc7a78)
![Investor App UI](https://github.com/user-attachments/assets/1d7d7c19-d87d-4f32-8e88-cc41b92c1c54)

### 🖥️ Founder Web Dashboard 
(![Screenshot 2025-05-08 205724](https://github.com/user-attachments/assets/f54fb819-c01f-41fd-a9cc-24e16ece2ccb))
![Screenshot 2025-05-08 205733](https://github.com/user-attachments/assets/b9b56672-64f4-4aaa-b7e6-0a2e4fdeaeff)
![Web Dashboard UI](https://github.com/user-attachments/assets/d32ea454-0888-47fb-84c5-37aeb1a74f77)
---

## 📦 How to Run

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/ecosphere-greenfund.git
cd ecosphere-greenfund
```
2. Start Backend
```bash
cd backend
npm install
npm run dev
```
3. Start Flask AI Services
```bash
Copy
Edit
cd backend-pyhton
pip install -r requirements.txt
python app.py
```
4. Start Frontend (Web)
```bash
cd frontend
npm install
npm start
```
5. Run React Native App
```bash
cd mobile-app
npx expo start
```
📌 Future Scope
Decentralized green tokens integration.
ESG-based project scoring.
Community-led local solar/wind initiatives with real-time tracking.
Enterprise dashboard for government/NGO involvement.

🙌 Contributing
We welcome PRs and feedback. Please see CONTRIBUTING.md for more details.

