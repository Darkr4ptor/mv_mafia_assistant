import streamlit as st

### --- Header section --- ###
st.header('Asistente de mafia para GM')


### --- Sidebar section --- ###

st.sidebar.header('Opciones')

check_preview_table   = st.sidebar.checkbox('Previsualizar Obituario')
check_add_player_url  = st.sidebar.checkbox('Añadir enlace a ISO del jugador')

### --- Main section --- ###

### Prepare markdown table headers ###

table_header =  '| # | Jugador      | Estado | Rol | Momento de la muerte |\n'
table_format = '|---|:--------------:|:--------:|:-----:|--------|:-----:|\n'
table        = table_header + table_format

# Empty thread URL 
thread_url   =  ''


input_players = st.text_area(label='Introduce tu lista de jugadores, un jugador por línea.',
                             value='',
                             max_chars=500)


if check_add_player_url:
    thread_url = st.text_input(label='URL del hilo', value='', max_chars=150)


player_list = input_players.split('\n')

if input_players:

    if thread_url or not check_add_player_url:

        for player in player_list:

            if thread_url:
                player_name = f'[{player}]({thread_url}?u={player})'
            else:
                player_name = player

            player_id  = player_list.index(player) + 1

            player_row = f'|{player_id}|{player_name}|Vivo|-|-|\n'

            table = table + player_row


        if check_preview_table:
            st.subheader('Obituario')
            st.markdown(table)
    
        st.subheader('')
        st.text_area(label='Código para Mediavida',
                     value=table)
    else:
        st.error('Introduce la URL del hilo de tu partida.')
    


else:
    st.error('Introduce al menos 1 jugador.')