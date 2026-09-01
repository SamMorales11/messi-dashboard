<img width="735" height="245" alt="download (17)" src="https://github.com/user-attachments/assets/f472f623-8f4d-4cb7-aff0-fb8ce821898c" />

# 🐐 Lionel Messi Career Analytics Dashboard

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

Interactive dashboard that analyzes Lionel Messi’s entire career goal contributions (goals + assists) from 2005 to 2026 across clubs and the Argentina national team.

**Live Demo:** [Click here to open the dashboard](https://your-app-name.streamlit.app)

## 📊 Project Overview

This project explores Messi’s career through data, focusing on matches where he recorded a goal or an assist. The dashboard provides interactive visualizations and filters to uncover performance patterns across different clubs, competitions, venues, and career stages.

### Key Features

- **Interactive Filters**: Club, Venue, Competition, Stage, and Year Range
- **KPI Cards** with comparison against previous period
- **Career Timeline**: Cumulative goals, assists, and goal contributions
- **Performance by Team**: Barcelona vs PSG vs Inter Miami vs Argentina
- **Venue Analysis**: Home vs Away vs Neutral
- **Competition Breakdown**
- **Stage Performance**: League, Group Stage, Knockout, Final
- **Club Era Comparison**: Early / Peak / Late Barcelona + PSG + Inter Miami
- **Milestone Tracker**: When Messi reached 100, 200, 300... goals
- **Monthly Heatmap**: Goal contribution intensity over the years
- **Top 10 Matches**: Best individual performances by goal contributions

---

## 🛠️ Tech Stack

| Tool            | Purpose                          |
|-----------------|----------------------------------|
| Python          | Core programming language        |
| Pandas          | Data cleaning & transformation   |
| Plotly          | Interactive visualizations       |
| Streamlit       | Web dashboard framework          |
| Jupyter Notebook| Exploratory Data Analysis        |

---

## 📁 Project Structure
```bash
messi-dashboard/
├── app/
│   └── streamlit_app.py          # Main Streamlit application
├── data/
│   └── messi dataset/
│       └── messi_goals_assists_2008_2026.csv
├── notebooks/
│   └── 01_eda_and_preparation.ipynb
├── requirements.txt
└── README.md
   ```
--
## 🚀 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/SamMorales11/messi-dashboard.git
   cd messi-dashboard
   ```
2. **Create virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```
3. **Install dependenciesBash**
```bash
pip install -r requirements.txt
```
4. **Run the dashboardBash**
```bash
streamlit run app/streamlit_app.py
```

## 📈 Dataset
The dataset contains 531 matches in which Lionel Messi recorded at least one goal or assist, covering:

675 Goals
304 Assists
979 Goal Contributions

spanning his career at FC Barcelona, Paris Saint-Germain, Inter Miami, and the Argentina National Team.

## 📸 Dashboard Preview

<img width="992" height="364" alt="Screenshot 2026-08-24 073410" src="https://github.com/user-attachments/assets/963769f6-cbeb-423e-bd51-5a9f8f5c0195" />
<img width="1004" height="590" alt="Screenshot 2026-08-24 073423" src="https://github.com/user-attachments/assets/4ade98e2-41da-453a-bc79-86f36405350d" />
<img width="968" height="421" alt="Screenshot 2026-08-24 073442" src="https://github.com/user-attachments/assets/72b8bfb8-7f30-4d28-a30b-a2a27c4deef4" />
<img width="989" height="195" alt="Screenshot 2026-08-24 073447" src="https://github.com/user-attachments/assets/75d0011f-60f5-46b7-8c8c-5b6badbed2c7" />
<img width="1008" height="421" alt="Screenshot 2026-08-24 073456" src="https://github.com/user-attachments/assets/ee6d0cf9-52ce-4aa1-aa77-01f0da050789" />

## ✨ Future Improvements ##
Add player comparison (Messi vs other players)
Include expected goals (xG) metrics
Deploy advanced filtering with more granular stages
Mobile responsive optimization

## 📄 License
This project is open source and available under the MIT License.

