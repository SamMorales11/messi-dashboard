import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# ====================== PAGE CONFIG ======================
st.set_page_config(
    page_title="Lionel Messi | Career Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== CUSTOM CSS (PURE BLUE THEME) ======================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    :root {
        --primary-color: #38BDF8 !important;
    }

    ::selection {
        background-color: #0284C7 !important;
        color: #FFFFFF !important;
    }
    
    /* SIDEBAR */
    [data-testid="stSidebar"] {
        background-color: #081028 !important;
        border-right: 1px solid rgba(56, 189, 248, 0.15) !important;
    }

    [data-testid="stSidebar"] h3 {
        color: #F8FAFC !important;
        font-weight: 700 !important;
        letter-spacing: -0.3px !important;
    }

    [data-testid="stSidebar"] hr {
        border-color: rgba(56, 189, 248, 0.2) !important;
        margin-top: 12px !important;
        margin-bottom: 20px !important;
    }

    [data-testid="stSidebar"] label {
        color: #94A3B8 !important;
        font-size: 13px !important;
        font-weight: 500 !important;
    }

    [data-testid="stSidebar"] div[data-baseweb="select"] > div {
        background-color: #0F172A !important;
        border: 1px solid rgba(56, 189, 248, 0.25) !important;
        border-radius: 8px !important;
        color: #F8FAFC !important;
    }

    [data-testid="stSidebar"] div[data-baseweb="select"]:hover > div {
        border-color: #38BDF8 !important;
        box-shadow: 0 0 8px rgba(56, 189, 248, 0.25) !important;
    }

    /* SLIDER OVERRIDES */
    [data-testid="stSidebar"] [data-testid="stSlider"] * {
        color: #38BDF8 !important;
    }

    [data-testid="stSidebar"] div[data-testid="stSliderThumbValue"],
    [data-testid="stSidebar"] div[data-testid="stThumbValue"],
    [data-testid="stSidebar"] [data-testid="stSlider"] [data-baseweb="tooltip"] {
        color: #38BDF8 !important;
        font-weight: 600 !important;
    }

    [data-testid="stSidebar"] [data-testid="stSlider"] div[data-baseweb="slider"] > div {
        background: rgba(56, 189, 248, 0.2) !important;
    }

    [data-testid="stSidebar"] [data-testid="stSlider"] div[data-baseweb="slider"] > div > div {
        background: #38BDF8 !important;
    }

    [data-testid="stSidebar"] [data-testid="stSlider"] div[role="slider"],
    [data-testid="stSidebar"] [data-testid="stSlider"] div[data-baseweb="thumb"] {
        background-color: #38BDF8 !important;
        border: 2px solid #081028 !important;
        box-shadow: 0 0 10px rgba(56, 189, 248, 0.6) !important;
    }

    [data-testid="stSidebar"] div[data-testid="stTickBarMin"],
    [data-testid="stSidebar"] div[data-testid="stTickBarMax"] {
        color: #38BDF8 !important;
        font-weight: 600 !important;
    }

    /* HEADER */
    .header-container {
        background: linear-gradient(135deg, #0A192F 0%, #0F2B48 50%, #1E3A8A 100%);
        padding: 24px 28px;
        border-radius: 14px;
        border: 1px solid rgba(100, 181, 246, 0.25);
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
        margin-bottom: 24px;
    }
    
    .header-title {
        color: #FFFFFF;
        font-size: 28px;
        font-weight: 700;
        letter-spacing: -0.5px;
        margin: 0 0 6px 0;
    }
    
    .header-subtitle {
        color: #94A3B8;
        font-size: 14px;
        font-weight: 400;
        margin: 0;
    }
    
    .badge-period {
        background-color: rgba(56, 189, 248, 0.15);
        color: #38BDF8;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        border: 1px solid rgba(56, 189, 248, 0.3);
        display: inline-block;
        margin-top: 10px;
    }

    /* KPI CARDS */
    .kpi-card {
        background: linear-gradient(145deg, #0F172A, #1E293B);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 12px;
        padding: 18px 20px;
        text-align: left;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        position: relative;
        overflow: hidden;
    }
    
    .kpi-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 3px;
        background: linear-gradient(90deg, #38BDF8, #1D4ED8);
    }
    
    .kpi-label {
        font-size: 12px;
        font-weight: 600;
        color: #94A3B8;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 8px;
    }
    
    .kpi-value {
        font-size: 32px;
        font-weight: 700;
        color: #F8FAFC;
        letter-spacing: -1px;
    }

    /* TABS */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        border-bottom: 1px solid #1E293B;
        padding-bottom: 4px;
    }

    .stTabs [data-baseweb="tab"] {
        height: 42px;
        background-color: transparent !important;
        border-radius: 8px;
        color: #94A3B8 !important;
        font-weight: 500;
        font-size: 14px;
        padding: 0px 18px;
        border: none !important;
        transition: all 0.2s ease;
    }

    .stTabs [data-baseweb="tab"]:hover {
        color: #38BDF8 !important;
        background-color: rgba(56, 189, 248, 0.08) !important;
    }

    .stTabs [aria-selected="true"] {
        background-color: rgba(56, 189, 248, 0.12) !important;
        color: #38BDF8 !important;
        font-weight: 600 !important;
        border: 1px solid rgba(56, 189, 248, 0.3) !important;
    }

    .stTabs [data-baseweb="tab-highlight-title"],
    .stTabs [data-baseweb="tab-border"],
    div[data-baseweb="tab-highlight"] {
        background-color: #38BDF8 !important;
    }
    
    [data-testid="stDataFrame"] {
        border: 1px solid #1E293B;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)


# ====================== LOAD DATA ======================
@st.cache_data
def load_data():
    df = pd.read_csv("data/messi dataset/messi_goals_assists_2008_2026.csv")
    
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['year_month'] = df['date'].dt.to_period('M').astype(str)
    
    def standardize_club(club):
        if club == 'FC Barcelona':
            return 'Barcelona'
        elif club in ['Paris Saint-Germain', 'PSG']:
            return 'PSG'
        elif 'Inter Miami' in str(club):
            return 'Inter Miami'
        elif club == 'Argentina':
            return 'Argentina'
        return club
    
    df['club'] = df['club_or_country'].apply(standardize_club)
    df['is_international'] = df['club'] == 'Argentina'
    df['venue_type'] = df['venue'].str.strip().str.title()
    df['goal_contribution'] = df['goals'] + df['assists']
    
    def categorize_stage(stage):
        stage = str(stage).lower()
        if 'final' in stage:
            return 'Final'
        elif any(x in stage for x in ['semi', 'sf', 'quarter', 'qf', 'r16', 'round of 16', 'r32']):
            return 'Knockout'
        elif 'group' in stage:
            return 'Group Stage'
        elif 'league' in stage or 'matchday' in stage:
            return 'League'
        return 'Other'
    
    df['stage_category'] = df['stage'].apply(categorize_stage)
    df = df.sort_values('date').reset_index(drop=True)
    
    return df

df = load_data()

# ====================== SIDEBAR FILTERS ======================
st.sidebar.markdown("### Control Panel")
st.sidebar.markdown("---")

# Club filter
clubs = ['All Clubs & Country'] + sorted(df['club'].unique().tolist())
selected_club = st.sidebar.selectbox("Filter by Club / National Team", clubs)

# Venue filter
venues = ['All Venues'] + sorted(df['venue_type'].unique().tolist())
selected_venue = st.sidebar.selectbox("Filter by Venue", venues)

# Competition filter
competitions = ['All Competitions'] + sorted(df['competition'].unique().tolist())
selected_competition = st.sidebar.selectbox("Filter by Competition", competitions)

# Stage filter
stages = ['All Stages'] + sorted(df['stage_category'].unique().tolist())
selected_stage = st.sidebar.selectbox("Filter by Stage", stages)

# Year range
min_year = int(df['year'].min())
max_year = int(df['year'].max())
year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (min_year, max_year))

# Apply filters
filtered_df = df.copy()

if selected_club != 'All Clubs & Country':
    filtered_df = filtered_df[filtered_df['club'] == selected_club]

if selected_venue != 'All Venues':
    filtered_df = filtered_df[filtered_df['venue_type'] == selected_venue]

if selected_competition != 'All Competitions':
    filtered_df = filtered_df[filtered_df['competition'] == selected_competition]

if selected_stage != 'All Stages':
    filtered_df = filtered_df[filtered_df['stage_category'] == selected_stage]

filtered_df = filtered_df[
    (filtered_df['year'] >= year_range[0]) & 
    (filtered_df['year'] <= year_range[1])
].copy()

# Recalculate cumulative on filtered data
filtered_df['career_goals'] = filtered_df['goals'].cumsum()
filtered_df['career_assists'] = filtered_df['assists'].cumsum()
filtered_df['career_goal_contributions'] = filtered_df['goal_contribution'].cumsum()


# ====================== HEADER ======================
min_date_str = df['date'].min().strftime('%d %b %Y')
max_date_str = df['date'].max().strftime('%d %b %Y')

st.markdown(f"""
<div class="header-container">
    <div class="header-title">
        Lionel Messi — Career Analytics Dashboard
    </div>
    <div class="header-subtitle">
        Comprehensive performance metrics and historical goal contribution analysis
    </div>
    <div class="badge-period">
        Data Period: {min_date_str} — {max_date_str}
    </div>
</div>
""", unsafe_allow_html=True)


# ====================== KPI CARDS ======================
total_goals = int(filtered_df['goals'].sum()) if not filtered_df.empty else 0
total_assists = int(filtered_df['assists'].sum()) if not filtered_df.empty else 0
total_contrib = int(filtered_df['goal_contribution'].sum()) if not filtered_df.empty else 0
total_matches = len(filtered_df)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Total Goals</div>
        <div class="kpi-value">{total_goals:,}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Total Assists</div>
        <div class="kpi-value">{total_assists:,}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Goal Contributions</div>
        <div class="kpi-value">{total_contrib:,}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Matches with G/A</div>
        <div class="kpi-value">{total_matches:,}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ====================== PLOTLY LAYOUT DEFAULTS ======================
plotly_layout_defaults = dict(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(family="Inter, sans-serif", color="#E2E8F0"),
    xaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.06)', zeroline=False),
    yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.06)', zeroline=False),
    margin=dict(l=20, r=20, t=40, b=20)
)

# ====================== TABS ======================
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Career Timeline", 
    "Performance by Team", 
    "Venue Analysis", 
    "Competitions",
    "Milestones",
    "Monthly Heatmap"
])

# ----- TAB 1: Career Timeline -----
with tab1:
    st.markdown("#### Cumulative Goal Contributions Timeline")
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=filtered_df['date'], y=filtered_df['career_goals'],
        mode='lines', name='Goals',
        line=dict(color='#38BDF8', width=2.5)
    ))
    fig.add_trace(go.Scatter(
        x=filtered_df['date'], y=filtered_df['career_assists'],
        mode='lines', name='Assists',
        line=dict(color='#2563EB', width=2.5)
    ))
    fig.add_trace(go.Scatter(
        x=filtered_df['date'], y=filtered_df['career_goal_contributions'],
        mode='lines', name='Total G+A',
        line=dict(color='#93C5FD', width=2.5)
    ))
    
    fig.update_layout(
        **plotly_layout_defaults,
        hovermode='x unified',
        height=480,
        legend=dict(orientation='h', y=1.12, x=1, xanchor='right', font=dict(size=12))
    )
    st.plotly_chart(fig, use_container_width=True)

# ----- TAB 2: By Club -----
with tab2:
    st.markdown("#### Goals & Assists Breakdown by Club / Country")
    
    club_stats = filtered_df.groupby('club').agg({
        'goals': 'sum',
        'assists': 'sum',
        'goal_contribution': 'sum',
        'date': 'count'
    }).rename(columns={'date': 'matches'}).reset_index()
    
    fig = px.bar(
        club_stats,
        x='club',
        y=['goals', 'assists'],
        barmode='group',
        text_auto=True,
        color_discrete_map={'goals': '#38BDF8', 'assists': '#1D4ED8'},
        labels={'value': 'Count', 'variable': 'Category', 'club': 'Team'}
    )
    fig.update_layout(
        **plotly_layout_defaults,
        height=420,
        legend=dict(orientation='h', y=1.1, x=1, xanchor='right')
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.dataframe(
        club_stats.sort_values('goal_contribution', ascending=False),
        column_config={
            "club": "Team",
            "goals": "Goals",
            "assists": "Assists",
            "goal_contribution": "Total G+A",
            "matches": "Matches"
        },
        use_container_width=True,
        hide_index=True
    )

# ----- TAB 3: Home vs Away -----
with tab3:
    st.markdown("#### Performance Metrics Across Venues")
    
    venue_stats = filtered_df.groupby('venue_type').agg({
        'goals': 'sum',
        'assists': 'sum',
        'goal_contribution': 'sum',
        'date': 'count'
    }).rename(columns={'date': 'matches'}).reset_index()
    
    if not venue_stats.empty:
        venue_stats['G+A per Match'] = (venue_stats['goal_contribution'] / venue_stats['matches']).round(2)
    else:
        venue_stats['G+A per Match'] = 0.0
    
    col_v1, col_v2 = st.columns([1.2, 1])
    
    with col_v1:
        fig = px.bar(
            venue_stats,
            x='venue_type',
            y='goal_contribution',
            color='venue_type',
            text='goal_contribution',
            color_discrete_sequence=['#38BDF8', '#2563EB', '#0284C7'],
            labels={'venue_type': 'Venue', 'goal_contribution': 'Goal Contributions'}
        )
        fig.update_layout(
            **plotly_layout_defaults,
            showlegend=False,
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col_v2:
        st.dataframe(
            venue_stats,
            column_config={
                "venue_type": "Venue",
                "goals": "Goals",
                "assists": "Assists",
                "goal_contribution": "Total G+A",
                "matches": "Matches",
                "G+A per Match": "G+A / Match"
            },
            use_container_width=True,
            hide_index=True
        )

# ----- TAB 4: Competitions -----
with tab4:
    st.markdown("#### Top Competitions by Total Goal Contributions")
    
    comp_stats = filtered_df.groupby('competition').agg({
        'goals': 'sum',
        'assists': 'sum',
        'goal_contribution': 'sum'
    }).sort_values('goal_contribution', ascending=False).head(12).reset_index()
    
    fig = px.bar(
        comp_stats,
        x='goal_contribution',
        y='competition',
        orientation='h',
        text='goal_contribution',
        color='goal_contribution',
        color_continuous_scale=['#0C4A6E', '#0284C7', '#38BDF8', '#7DD3FC'],
        labels={'goal_contribution': 'Goal Contributions', 'competition': 'Competition'}
    )
    fig.update_layout(
        **plotly_layout_defaults,
        height=480,
        coloraxis_showscale=False
    )
    fig.update_yaxes(categoryorder='total ascending')
    
    st.plotly_chart(fig, use_container_width=True)

# ----- TAB 5: Milestones -----
with tab5:
    st.markdown("#### Career Goals Milestones")
    
    milestones = [100, 200, 300, 400, 500, 600, 650, 675]
    milestone_data = []
    
    for m in milestones:
        subset = filtered_df[filtered_df['career_goals'] >= m]
        if len(subset) > 0:
            row = subset.iloc[0]
            
            opponent = row.get('opponent', 'Opponent') if 'opponent' in row else 'N/A'
            team_name = row.get('team', row.get('club', 'Team'))
            
            milestone_data.append({
                'Milestone': f"{m} Goals",
                'Date': row['date'].strftime('%Y-%m-%d'),
                'Match': f"{team_name} vs {opponent}",
                'Competition': row.get('competition', 'N/A'),
                'Club': row.get('club', 'N/A'),
                'Goals in Match': int(row['goals']),
                'Career Goals': int(row['career_goals'])
            })
    
    if milestone_data:
        milestone_df = pd.DataFrame(milestone_data)
        
        fig = go.Figure()
        color_map = {
            'Barcelona': '#38BDF8',
            'PSG': '#1D4ED8',
            'Inter Miami': '#60A5FA',
            'Argentina': '#7DD3FC'
        }
        
        for _, row in milestone_df.iterrows():
            fig.add_trace(go.Scatter(
                x=[row['Date']],
                y=[row['Milestone']],
                mode='markers+text',
                marker=dict(size=14, color=color_map.get(row['Club'], '#38BDF8')),
                text=row['Date'],
                textposition='middle right',
                name=row['Club'],
                hovertemplate=(
                    f"<b>{row['Milestone']}</b><br>" +
                    f"Date: {row['Date']}<br>" +
                    f"Match: {row['Match']}<br>" +
                    f"Competition: {row['Competition']}<br>" +
                    f"Club: {row['Club']}<extra></extra>"
                ),
                showlegend=False
            ))
        
        fig.update_layout(
            **plotly_layout_defaults,
            height=480
        )
        fig.update_yaxes(categoryorder='array', categoryarray=milestone_df['Milestone'].tolist()[::-1])
        fig.update_xaxes(type='date')
        
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(milestone_df, use_container_width=True, hide_index=True)
    else:
        st.info("No milestones reached with the current filters.")

# ----- TAB 6: Monthly Heatmap -----
with tab6:
    st.markdown("#### Monthly Goal Contributions Heatmap")
    
    if not filtered_df.empty:
        heatmap_data = filtered_df.groupby(['year', 'month'])['goal_contribution'].sum().reset_index()
        heatmap_pivot = heatmap_data.pivot(index='month', columns='year', values='goal_contribution').fillna(0)
        
        month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        fig = px.imshow(
            heatmap_pivot,
            labels=dict(x="Year", y="Month", color="G+A"),
            x=heatmap_pivot.columns,
            y=[month_labels[i-1] for i in heatmap_pivot.index],
            color_continuous_scale=['#0C4A6E', '#0284C7', '#38BDF8', '#7DD3FC', '#E0F2FE'],
            aspect="auto"
        )
        
        fig.update_layout(
            **plotly_layout_defaults,
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Warna lebih terang = semakin banyak goal contributions di bulan tersebut.")
    else:
        st.info("No data available for the selected filters.")

# ====================== FOOTER ======================
st.markdown("---")
st.caption("Lionel Messi Career Analytics | Built with Streamlit & Plotly")