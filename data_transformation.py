from data import GameManager

gm = GameManager()
df = gm.get_table_data()

def get_players_base_stats(df):
    players_df = df.groupby('PLAYER').agg({
        'GAME_ID': 'count',
        'WIN': 'sum',
        'TOTAL_POINTS': 'mean'
    }).reset_index()

    players_df = players_df.rename(columns={
        'GAME_ID': 'GAMES PLAYED',
        'TOTAL_POINTS': 'AVG POINTS'
    })

    players_df['WINNING RATE'] = players_df.apply(lambda x: x['WIN'] / x['GAMES PLAYED'],  axis=1)
    players_df = players_df.sort_values('WINNING RATE', ascending=False)

    return players_df

def get_player_wonder_stats(df):
    player_wonder_stats = df.groupby(['PLAYER', 'WONDERS']).agg({
        'GAME_ID': 'count',
        'RANK': 'mean',
        'WIN': 'sum'
    }).reset_index()

    player_wonder_stats = player_wonder_stats.rename(columns={
        'GAME_ID': 'GAMES PLAYED',
        'RANK': 'AVG RANK',
    })

    player_wonder_stats['WINNING RATE'] = player_wonder_stats.apply(lambda x: x['WIN'] / x['GAMES PLAYED'], axis=1)

    return player_wonder_stats

def get_player_best_performing_wonder(player_wonder_stats, columns_to_keep=[]):
    best_performing = player_wonder_stats.loc[player_wonder_stats.groupby('PLAYER')['WINNING RATE'].idxmax()]
    best_performing = best_performing.rename(columns={
        'WONDERS': 'BEST WONDER',
        'GAMES PLAYED': 'BEST WONDER GAMES',
        'AVG RANK': 'BEST WONDER AVG RANK',
        'WINNING RATE': 'BEST WONDER WIN RATE'
    })

    if not columns_to_keep:
        columns_to_keep = best_performing.columns
    
    return best_performing[columns_to_keep]

def join_best_performing_wonder_with_players():
    players_df = get_players_base_stats(df)

    player_wonder_stats = get_player_wonder_stats(df)
    best_performing = get_player_best_performing_wonder(player_wonder_stats, ['PLAYER', 'BEST WONDER', 'BEST WONDER WIN RATE'])

    players_df = pd.merge(players_df, best_performing, on='PLAYER')

    return players_df

