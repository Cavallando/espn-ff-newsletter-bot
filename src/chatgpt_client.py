import openai
import os
import json
from chatgpt_input import CHATGPT_API_KEY

# Set up your OpenAI API client
client = openai.OpenAI(api_key=CHATGPT_API_KEY)

def generate_fantasy_recap(team_summary, boxscore_summary):
    """
    Generates a funny recap of the latest fantasy football league results.
    """
    prompt = f"""
    Please provide a funny and engaging recap of the latest week's fantasy football league results.

    League Overview:
    - 10-team PPR league
    - Starting lineup: 1 QB, 2 RB, 2 WR, 1 TE, 2 FLEX, 1 K
    - Teams ranked by wins, with total points as a tiebreaker
    - 14-week regular season, 3-week playoffs
    - Top 6 teams make playoffs; top 2 get a bye
    - The winner gets a trophy and bragging rights; last place gets punished

    League Team Data:
    {json.dumps(team_summary, indent=2)}

    Weekly Matchup Data:
    {json.dumps(boxscore_summary, indent=2)}

    Guidelines:
    - Highlight key matchups, surprise performances, and notable storylines.
    - Use sarcasm, humor, and be rude, edgy, and creative when mocking underperforming teams.
    - Use player data from the boxscores to comment on over- or under-performance, and missed starts.
    - Recap each of the 5 matchups in roughly 6 sentences.
    - List team names (e.g., "Team A vs. Team B") at the start of each recap.
    - Always refer to owners by first name.
    - End each matchup with owner names and final scores (e.g., "Jake beat Brian 24-17").

    Standings:
    - Rank teams by **wins** first, and if two or more teams have the same number of wins, use **total points (points_for)** as a tiebreaker.
    - For the standings, list the rank, record (W-L), team name, owner, and total points.
    - The team with the most wins should be ranked at the top, and teams with fewer wins should follow. If wins are tied, rank by total points (higher points comes first).

    End the entire recap with:
    - Listing the team that had the highest weekly score out of all the matchups.
    - Notes on how teams are trending towards becoming the league winner, the worst team, and the team with the highest overall points.
    - A listing of the standings including the rank, record (W-L), team name, owner, and total points.
"""


    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a humorous fantasy football recap writer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=5000,
        n=1,
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()