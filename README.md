# 🐐 Lionel Messi — Career Analytics Dashboard

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

Interactive dashboard that analyzes Lionel Messi’s entire career goal contributions (goals + assists) from 2005 to 2026 across clubs and the Argentina national team.

**Live Demo:** [Click here to open the dashboard](https://your-app-name.streamlit.app)

---

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