"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}


    user1 = {"genre": "pop", "mood": "happy", "energy": 0.8}
    user2 = {"genre": "lofi", "mood": "chill", "energy": 0.4}
    recommendations_user1 = recommend_songs(user1, songs, k=5)
    recommendations_user2 = recommend_songs(user2, songs, k=5)

    # Print recommendations for User 1
    print("\nTop recommendations for User 1 (pop/happy):\n")
    for song, score, explanation in recommendations_user1:
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}\n")

    # Print recommendations for User 2
    print("\nTop recommendations for User 2 (lofi/chill):\n")
    for song, score, explanation in recommendations_user2:
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}\n")

    print("\nTop recommendations:\n")
    # for rec in recommendations:
    #     # You decide the structure of each returned item.
    #     # A common pattern is: (song, score, explanation)
    #     song, score, explanation = rec
    #     print(f"{song['title']} - Score: {score:.2f}")
    #     print(f"Because: {explanation}")
    #     print()


if __name__ == "__main__":
    main()
