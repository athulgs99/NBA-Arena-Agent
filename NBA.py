from groq import Groq


TEAM_ID = "134861" 
API_KEY = ""


# Removed API keys for security purposes

client = Groq(api_key=" "). 

def get_recent_scores_live(team_id):
    import requests
    
    url = f"https://www.thesportsdb.com/api/v1/json/{API_KEY}/eventslast.php?id={team_id}"
    response = requests.get(url)
    data = response.json()
    events = data.get('results', [])
    #print(events)
    summary = []
    for event in events:
        summary.append(f"{event['strEvent']} on {event['dateEvent']} - Score: {event['intHomeScore']}:{event['intAwayScore']}")
        #print(summary)
    return "\n".join(summary)



def generate_sports_summary(team_id):
    live_scores = get_recent_scores_live(team_id)
    
    prompt = (
        "You are Ravi Shastri. Here are the recent games:\n"
        f"{live_scores}\n\n"
        "Please provide a lively, engaging summary of these results like he would."
    )
    
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content


# Example usage with Boston Celtics team ID
team_id = "134860"
print(generate_sports_summary(team_id))
