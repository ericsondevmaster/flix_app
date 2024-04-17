import streamlit as st
import plotly.express as px
from movies.service import MovieService


def show_home():
    movie_service = MovieService()
    movie_stats = movie_service.get_movie_stats()

    st.title('Estatísticas de Filmes:')

    if len(movie_stats['movies_by_genre']) > 0:
        st.subheader('Filmes Por Gênero:')
        fig = px.pie(
            movie_stats['movies_by_genre'],
            values='count',
            names='genre__name',
            title='Filmes Por Gênero'
        )
        st.plotly_chart(fig)

    st.subheader('Total de Filmes Cadastrados:')
    st.write(movie_stats['total_movies'])

    st.subheader('Total de Filmes Por Gênero:')
    for genre in movie_stats['movies_by_genre']:
        st.write(f"{genre['genre__name']}: {genre['count']}")

    st.subheader('Total de Avaliações Cadastradas:')
    st.write(movie_stats['total_reviews'])

    st.subheader('Média Geral de Estrelas Nas Avaliações:')
    st.write(movie_stats['average_stars'])
