from dash import dcc
from dash import html, dash_table


def get_layout(app,Application,df):

    body_layout= html.Div(
        children=[
                html.Div(
                children=[
                    #html.P(children="\U0001f600", className="header-emoji"),
                    #set image on top of site
                    html.P(children=html.Img(src=app.get_asset_url('Screenshot_1.png'), className="logo",width=80,height=80), className="header-emoji"),
                    html.H1(
                        children="KPI Metrics and Security Analyzer for Doğuş Teknoloji", className="header-title"
                    ),
                    html.P(
                        children="Doğuş Teknoloji için KPI ve Güvenlik Analizi Farklı iştirakler için skorlar üretilmesini sağlar"
                        " KPI Metrikleri ve Security Logları baz alınır.",
                        className="header-description",
                    ),
                ],
                className="header",
            ),
            dcc.Dropdown(
                #children="Uygulama Adı",
                id="filter_dropdown",
                className="menu-title",
                options=[{"label": Application, "value": Application} for Application in Application],
                placeholder="-Select a Site-",
                multi=True,
                value=df.Application.values,
            ),
            dash_table.DataTable(
                id="table-container",
                columns=[{"name": i, "id": i} for i in df.columns],
                style_table={'height': '200px', 'overflowY': 'auto','width':'50%'},
                data=df.to_dict("records"),
                style_cell={'textAlign': 'center'},
                style_cell_conditional=[
                    {
                    'if': {'column_id': 'Application'},
                    'textAlign': 'center'
                    }]
    #todo: monthly kpi values to graph
            )
        ]
    )
    return body_layout