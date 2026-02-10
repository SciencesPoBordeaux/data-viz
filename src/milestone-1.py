import pandas as pd
import altair as alt
alt.data_transformers.enable("vegafusion")
alt.renderers.enable("browser")

data_url = 'https://raw.githubusercontent.com/datamisc/ts-2024/main/data.csv'
df = pd.read_csv(data_url, compression='gzip')
df.head()

selected_variable = 'V241501x'

horizontal_bar = alt.Chart(df[df[selected_variable] > 0]).mark_bar().encode(
    y=alt.Y(selected_variable,
            type='nominal',
            title='Il faut renommer cet axe...',
            sort='-x'),
    x=alt.X('count()', title='Nombre de Répondants'),
    color=alt.Color(selected_variable,
                    type='nominal',
                    legend=None),
    tooltip=[selected_variable, 'count()']
).properties(
    title=alt.TitleParams(
        text='Ajouter un titre pertinent en fonction de la variable',
        subtitle='Source: Ajouter la source appropriée.',
        fontSize=16,
        subtitleFontSize=12,
        subtitleColor='gray',
        anchor='start'
    ),
    width=600,
    height=400
)

horizontal_bar
