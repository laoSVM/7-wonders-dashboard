import pandas as pd
import streamlit as st
from data import GameManager
from data_transformation import (
    get_players_base_stats,
    get_player_wonder_stats,
    get_champion_player,
    get_master_player,
    join_best_performing_wonder_with_players
)

st.set_page_config(page_title="7 Wonders!", page_icon="🎬")

file_id = st.secrets["FILE_ID"]
gm = GameManager(file_id)
load_success = gm.download_data()

def main():
    if load_success:
        st.success('数据读取成功✅')
        df = gm.get_table_data()
        players_base_stats = get_players_base_stats(df)
        player_wonder_stats = get_player_wonder_stats(df)

    st.title("7 Wonders 启动!")

    kpi_1, kpi_2, kpi_3 = st.columns(3)
    champion_player = get_champion_player(players_base_stats)
    kpi_1.metric("Champion Player", champion_player['PLAYER'], f"{champion_player['WINNING RATE']: .0%}")
    master_player = get_master_player(players_base_stats)
    kpi_2.metric("Master Player", master_player['PLAYER'], f"{master_player['WIN']}")

    players_df = join_best_performing_wonder_with_players(players_base_stats, player_wonder_stats)

    st.dataframe(
        players_df,
        column_config={
            "PLAYER": "Player",
            "GAMES PLAYED": "场次",
            "AVG POINTS": st.column_config.NumberColumn(
                "Avg Points",
                help="Avg Points",
                format="%d",
            ),
            "WINNING RATE": st.column_config.NumberColumn(
                "Winning Rate",
                help="Winning Rate",
                format="%.2f",
            ),
            "BEST WONDER WIN RATE": st.column_config.NumberColumn(
                "Winning Rate",
                help="Winning Rate",
                format="%.2f",
            ),
        },
        hide_index=True,
    )

if __name__ == "__main__":
    main()