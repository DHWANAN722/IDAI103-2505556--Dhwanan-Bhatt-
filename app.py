from flask import Flask, render_template, jsonify, request
import requests
from datetime import datetime, timedelta
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Sample data for demonstration (in production, you'd use real API)
SPORTS_DATA = {
    'football': {
        'matches': [
            {
                'id': 1,
                'home_team': 'Manchester United',
                'away_team': 'Liverpool',
                'home_score': 2,
                'away_score': 1,
                'status': 'Live',
                'time': '67\'',
                'league': 'Premier League',
                'date': datetime.now().strftime('%Y-%m-%d')
            },
            {
                'id': 2,
                'home_team': 'Barcelona',
                'away_team': 'Real Madrid',
                'home_score': 3,
                'away_score': 3,
                'status': 'Finished',
                'time': 'FT',
                'league': 'La Liga',
                'date': datetime.now().strftime('%Y-%m-%d')
            },
            {
                'id': 3,
                'home_team': 'Chelsea',
                'away_team': 'Arsenal',
                'home_score': 0,
                'away_score': 0,
                'status': 'Upcoming',
                'time': '15:00',
                'league': 'Premier League',
                'date': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
            }
        ],
        'standings': [
            {'position': 1, 'team': 'Manchester City', 'played': 25, 'won': 18, 'drawn': 4, 'lost': 3, 'points': 58},
            {'position': 2, 'team': 'Arsenal', 'played': 25, 'won': 17, 'drawn': 5, 'lost': 3, 'points': 56},
            {'position': 3, 'team': 'Liverpool', 'played': 25, 'won': 16, 'drawn': 6, 'lost': 3, 'points': 54},
            {'position': 4, 'team': 'Aston Villa', 'played': 25, 'won': 15, 'drawn': 4, 'lost': 6, 'points': 49},
            {'position': 5, 'team': 'Tottenham', 'played': 25, 'won': 14, 'drawn': 5, 'lost': 6, 'points': 47}
        ]
    },
    'basketball': {
        'matches': [
            {
                'id': 4,
                'home_team': 'LA Lakers',
                'away_team': 'Boston Celtics',
                'home_score': 108,
                'away_score': 102,
                'status': 'Live',
                'time': 'Q3 5:23',
                'league': 'NBA',
                'date': datetime.now().strftime('%Y-%m-%d')
            },
            {
                'id': 5,
                'home_team': 'Golden State Warriors',
                'away_team': 'Miami Heat',
                'home_score': 115,
                'away_score': 110,
                'status': 'Finished',
                'time': 'Final',
                'league': 'NBA',
                'date': datetime.now().strftime('%Y-%m-%d')
            }
        ],
        'standings': [
            {'position': 1, 'team': 'Boston Celtics', 'played': 55, 'won': 42, 'lost': 13, 'win_pct': '.764'},
            {'position': 2, 'team': 'Milwaukee Bucks', 'played': 55, 'won': 38, 'lost': 17, 'win_pct': '.691'},
            {'position': 3, 'team': 'Philadelphia 76ers', 'played': 55, 'won': 35, 'lost': 20, 'win_pct': '.636'},
            {'position': 4, 'team': 'Cleveland Cavaliers', 'played': 55, 'won': 34, 'lost': 21, 'win_pct': '.618'},
            {'position': 5, 'team': 'New York Knicks', 'played': 55, 'won': 33, 'lost': 22, 'win_pct': '.600'}
        ]
    },
    'cricket': {
        'matches': [
            {
                'id': 6,
                'home_team': 'India',
                'away_team': 'Australia',
                'home_score': '285/7',
                'away_score': '156/4',
                'status': 'Live',
                'time': 'Innings 2: Over 35',
                'league': 'Test Series',
                'date': datetime.now().strftime('%Y-%m-%d')
            },
            {
                'id': 7,
                'home_team': 'England',
                'away_team': 'Pakistan',
                'home_score': '320/8',
                'away_score': '295/10',
                'status': 'Finished',
                'time': 'ENG Won',
                'league': 'ODI Series',
                'date': datetime.now().strftime('%Y-%m-%d')
            }
        ],
        'standings': [
            {'position': 1, 'team': 'India', 'played': 12, 'won': 9, 'lost': 2, 'tied': 1, 'points': 108},
            {'position': 2, 'team': 'Australia', 'played': 12, 'won': 8, 'lost': 3, 'tied': 1, 'points': 98},
            {'position': 3, 'team': 'England', 'played': 12, 'won': 7, 'lost': 4, 'tied': 1, 'points': 86},
            {'position': 4, 'team': 'South Africa', 'played': 12, 'won': 6, 'lost': 5, 'tied': 1, 'points': 74},
            {'position': 5, 'team': 'New Zealand', 'played': 12, 'won': 5, 'lost': 6, 'tied': 1, 'points': 62}
        ]
    }
}

NEWS_DATA = [
    {
        'title': 'Historic Victory: Underdog Team Claims Championship',
        'summary': 'In a stunning turn of events, the underdogs secured their first championship title in franchise history.',
        'category': 'football',
        'date': datetime.now().strftime('%Y-%m-%d'),
        'image': 'trophy.jpg'
    },
    {
        'title': 'Record-Breaking Performance Sets New Standard',
        'summary': 'Star player achieves unprecedented statistics, breaking records that stood for decades.',
        'category': 'basketball',
        'date': datetime.now().strftime('%Y-%m-%d'),
        'image': 'record.jpg'
    },
    {
        'title': 'International Tournament Announces New Format',
        'summary': 'Major changes to tournament structure promise more excitement for fans worldwide.',
        'category': 'cricket',
        'date': datetime.now().strftime('%Y-%m-%d'),
        'image': 'tournament.jpg'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/sports/<sport>')
def get_sport_data(sport):
    if sport in SPORTS_DATA:
        return jsonify(SPORTS_DATA[sport])
    return jsonify({'error': 'Sport not found'}), 404

@app.route('/api/matches/live')
def get_live_matches():
    live_matches = []
    for sport, data in SPORTS_DATA.items():
        for match in data['matches']:
            if match['status'] == 'Live':
                match_copy = match.copy()
                match_copy['sport'] = sport
                live_matches.append(match_copy)
    return jsonify(live_matches)

@app.route('/api/news')
def get_news():
    category = request.args.get('category', 'all')
    if category == 'all':
        return jsonify(NEWS_DATA)
    filtered_news = [news for news in NEWS_DATA if news['category'] == category]
    return jsonify(filtered_news)

@app.route('/api/match/<int:match_id>')
def get_match_details(match_id):
    for sport, data in SPORTS_DATA.items():
        for match in data['matches']:
            if match['id'] == match_id:
                match_copy = match.copy()
                match_copy['sport'] = sport
                # Add additional details
                match_copy['stats'] = {
                    'possession': {'home': 55, 'away': 45},
                    'shots': {'home': 12, 'away': 8},
                    'corners': {'home': 6, 'away': 4}
                } if sport == 'football' else {}
                return jsonify(match_copy)
    return jsonify({'error': 'Match not found'}), 404

@app.route('/football')
def football():
    return render_template('sport.html', sport='football', sport_name='Football')

@app.route('/basketball')
def basketball():
    return render_template('sport.html', sport='basketball', sport_name='Basketball')

@app.route('/cricket')
def cricket():
    return render_template('sport.html', sport='cricket', sport_name='Cricket')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
