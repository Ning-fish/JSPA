#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !pip install jupyter_dash
# !pip install dash_dangerously_set_inner_html


# In[6]:


from jupyter_dash import JupyterDash
from dash import Dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_dangerously_set_inner_html
import requests
import json
import visdcc

external_scripts = [
    'https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',
    'https://code.jquery.com/ui/1.12.1/jquery-ui.min.js']

app = JupyterDash(__name__, suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.MINTY],
                external_scripts=external_scripts)
#app = Dash(__name__)

app.layout = html.Div([html.Div([
#      html.Span(dbc.Badge("JSP", color="primary", className="mr-1",
#                             style={'display': 'inline-block'})),
     html.Img(src=app.get_asset_url('logo2.png'),
                       style={'height':'10%', 'width':'10%',
                              'textAlign': 'center',
                              'padding': '5px',
                              'display': 'inline-block',
                              'margin': '0 0.2em'}),
     html.Div('TKU Japanese Sentence Pattern Analyzer 日文句型分析儀, V1.0',
                 style={'color': '#454d26',
                       'fontSize': '18px',
                       'textAlign': 'left',
                       'font-weight' :'bold',
                       'display': 'inline-block'}),
     html.Br(),
     html.Div('Based on Mecab POS Tagger and Regular Expressions',
             style={'color': '#6a7051',
                   'fontSize': '15px',
                   'textAlign': 'left',
                   'font-weight' :'bold',
                   'display': 'inline-block',
                   'margin': '0 1em'}),

                        ], id= 'header'),

     html.Div(dbc.Container([
     html.Br(),
        dcc.Textarea(
            id='textarea-example',
            value='政府は10月から11月に、ワクチンを受けたい全部の人の注射が終わると考えています。そのころには、ワクチンが終わった証明を持っている人がレストランやイベント、旅行などに行きやすくすることを考えています。',
            placeholder='解析したいテキストを入力！',
            style={'width': '100%', 'height': '300px','text-align': 'left','font-family': 'UD デジタル 教科書体 NK-R'}
        )],id='main')),
    

    html.Div( 
        dbc.FormGroup([
#             html.Span(dbc.Badge("文法分類", className="mr-2")),
            
        dbc.RadioItems(id='dict_dropdown',
                     value='unidic',
                     inline=True),
                        ]) ),
    html.Hr(),
                       
    html.Div( 
        dbc.FormGroup([
            html.Span(dbc.Badge("句型分類", className="mr-2")), 
         
html.Div(
    [
        dbc.Button(
            "初級I", id="open", n_clicks=0, color="primary"
        ),
        dbc.Button(
            "初級II", id="open2", n_clicks=0, color="info"
        ),
        dbc.Button("Basic Forms", id="open3", n_clicks=0, color="warning"
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Collapse(
                        
                        
        html.Div([
                        dbc.Checklist(
                        id="all-or-none",
                        options=[{"label": "Select All", "value": "All"}],
                        value=[],
                    ),
                    dbc.Button("L6-L8", id="open_6_8", n_clicks=0, color="primary"),
            dbc.Collapse(
                    dbc.Checklist(id='pattern_6_8',
                        options=[{'label': d, 'value': c} 
                                 for d,c in zip(['より','が','對象が＋い形容詞／な形容詞','から','ほう','いる／ある','いる／ある','かかる'],
                                                ['L6-1','L6-2','L7-1','L7-2','L7-3','L8-1','L8-2','L8-3']) ],
                     inline=True,
                     value=[]), id="colla6_8"),
            
                    dbc.Button("L9-L11", id="open_9_11", n_clicks=0, color="primary"),
            dbc.Collapse(
                    dbc.Checklist(id='pattern_9_11',
                         options=[{'label': d, 'value': c}
                                  for d,c in zip(['ほしい','方向へ／目的に／移動動詞','たい','やすい／にくい','ている','て形','てください','てから','ながら'],
                                                 ['L9-1','L9-2','L9-3','L9-4','L10-1','L11-1','L11-2','L11-3','L11-4']) ],
                     inline=True,
                     value=[]), id="colla9_11"),
            
                    dbc.Button("L12-L15", id="open_12_15", n_clicks=0, color="primary"),
            dbc.Collapse(
                    dbc.Checklist(id='pattern_12_15',
                         options=[{'label': d, 'value': c}
                                  for d,c in zip(['ないで','なければならない','にする','にする','てはいけない','なる','できる'],
                                                 ['L12-1','L12-2','L12-3','L13-1','L13-2','L15-1','L15-2']) ],
                     inline=True,
                     value=[]), id="colla12_15"),
            
                    dbc.Button("L16-L20", id="open_16_20", n_clicks=0, color="primary"),
            dbc.Collapse(
                    dbc.Checklist(id='pattern_16_20',
                         options=[{'label': d, 'value': c}
                                  for d,c in zip(['た形','たり','まま','あとで','と思う','だろう／でしょう','まえに','ほうがいい','とき','たら','し','形容詞の副詞的用法'],
                                                 ['L16-1','L16-2','L16-3','L16-4','L17-1','L17-2','L18-1','L18-2','L18-3','L19-1','L19-2','L20-1']) ],
                     inline=True,
                     value=[]), id="colla16_20")
                ]),
            
            
            id="collapse",
            is_open=False,
                    )
                ),
                dbc.Col(
                    dbc.Collapse(        
            html.Div([
                        dbc.Checklist(
                        id="all-or-none2",
                        options=[{"label": "Select All", "value": "All"}],
                        value=[],
                    ),
                    dbc.Button("L21-L23", id="open_21_23", n_clicks=0, color="info"),
            dbc.Collapse(
                    dbc.Checklist(id='pattern_21_23',
                         options=[{'label': d, 'value': c}
                                  for d,c in zip(['ので','のに','なら','しか～ない','意向形（う／よう）','意向形と思う','つもり','予定'],
                                                 ['L21-1','L21-2','L21-3','L22-1','L23-1','L23-2','L23-3','L23-4']) ],
                     inline=True,
                     value=[]), id="colla21_23"),
                
                    dbc.Button("L24-L26", id="open_24_26", n_clicks=0, color="info"),
            dbc.Collapse(
                    dbc.Checklist(id='pattern_24_26',
                         options=[{'label': d, 'value': c}
                                  for d,c in zip(['ようだ','ようにする','ようになる','命令形','な','なさい','てくる','ていく'],
                                                 ['L24-1','L24-2','L24-3','L25-1','L25-2','L25-3','L26-1','L26-2']) ],
                     inline=True,
                     value=[]), id="colla24_26"),
            
                    dbc.Button("L27-L28", id="open_27_28", n_clicks=0, color="info"),
            dbc.Collapse(
                    dbc.Checklist(id='pattern_27_28',
                         options=[{'label': d, 'value': c}
                                  for d,c in zip(['てみる','てしまう','ておく','ば','なら（ば）','〜ば〜ほど'],
                                                 ['L27-1','L27-2','L27-3','L28-1','L28-2','L28-3']) ],
                     inline=True,
                     value=[]), id="colla27_28"),
            
                    dbc.Button("L29-L31", id="open_29_31", n_clicks=0, color="info"),
            dbc.Collapse(
                    dbc.Checklist(id='pattern_29_31',
                         options=[{'label': d, 'value': c}
                                  for d,c in zip(['そうだ','そうな','ために','すぎる','なさすぎる','れる／られる'],
                                                 ['L29-1','L29-2','L29-3','L29-4','L29-5','L30L31']) ],
                     inline=True,
                     value=[]), id="colla29_31"),
            
                    dbc.Button("L32-L34", id="open_32_34", n_clicks=0, color="info"),
            dbc.Collapse(
                    dbc.Checklist(id='pattern_32_34',
                         options=[{'label': d, 'value': c}
                                  for d,c in zip(['そうだ','かどうか','か','らしい','かもしれない','はずだ','はずがない','ことが／もある','ことにする','ことになる'],
                                                 ['L32-1','L32-2','L32-3','L33-1','L33-2','L33-3','L33-4','L34-1','L34-2','L34-3']) ],
                     inline=True,
                     value=[]), id="colla32_34")
                ]),
            id="collapse2",
            is_open=False,
                    )
                ),
        dbc.Col(
                    dbc.Collapse(
        html.Div([
                        dbc.Checklist(
                        id="all-or-none3",
                        options=[{"label": "Select All", "value": "All"}],
                        value=[],
                    ),
                    dbc.Button("V_naAdj", id="open_V_naAdj", n_clicks=0, color="warning"),
            dbc.Collapse(
                    dbc.Checklist(id='pattern_V_naAdj',
                         options=[{'label': d, 'value': d}
                                  for d in ['V-Plain-Present','V-Plain-Past','Adj-Plain','naAdj-Plain-DA','naAdj-Plain-NA']],
                     inline=True,
                     value=[]), id="collaV_naAdj"),
            
                    dbc.Button("N_N", id="open_N_N", n_clicks=0, color="warning"),
            dbc.Collapse(
                    dbc.Checklist(id='pattern_N_N',
                         options=[{'label': d, 'value': d}
                                  for d in ['N-Plain-DA','N-Plain-NA','N-Plain-NO','V-Polite-Present/Past','Adj-Polite','naAdj-Polite','N-Polite']],
                     inline=True,
                     value=[]), id="collaN_N"),
            
                    dbc.Button("P23", id="open_P23", n_clicks=0, color="warning"),
            dbc.Collapse(
                    dbc.Checklist(id='pattern_P23',
                         options=[{'label': d, 'value': d}
                                  for d in ['P23-1','P23-2','P23-3','P23-4','P23-5','P23-6']],
                     inline=True,
                     value=[]), id="collaP23"),
            
                    dbc.Button("V", id="open_V", n_clicks=0, color="warning"),
            dbc.Collapse(
                    dbc.Checklist(id='pattern_V',
                         options=[{'label': d, 'value': d}
                                  for d in ['V1','V2','V3','V4','V5','V6','V7','V8','V9','V10']],
                     inline=True,
                     value=[]), id="collaV"),

                    dbc.Button("ADJ", id="open_ADJ", n_clicks=0, color="warning"),
            dbc.Collapse(
                    dbc.Checklist(id='pattern_ADJ',
                         options=[{'label': d, 'value': d}
                                  for d in ['ADJ1','ADJ2','ADJ3','ADJ4','ADJ5','ADJV1','ADJV2','ADJV3','ADJV4','ADJV5']],
                     inline=True,
                     value=[]), id="collaADJ")
                ]),
            id="collapse3",
            is_open=False,
                    )
                ),
            ],
            className="mr-3",
        ),
    ]
), 

                        ]) ),

    #html.Div(id='textarea-example-output', style={'whiteSpace': 'pre-line'}),
    #html.Div(dcc.Input(id='input-on-submit', type='text')),

                       
    html.Div([
        
    html.Button('解析してみる', id='submit-val', n_clicks=0),

               
    html.Br(),  
    html.Br(), 
        

        
#         dbc.CardHeader(
#         dbc.Tabs(
#              [
#             dbc.Tab(label='分析結果', id='table_header_body'),
# #             dbc.Tab(label='自印除錯', id='debug'),
            
# #             dbc.Tab(label='api輸出', id='api_output'),
# #             dbc.Tab(label='api輸入', id='api_input'),
# #             dbc.Tab(label='print區', id='print_out')
#              ],
#         id="tabs",
#         active_tab="分析結果") )
        
    dbc.Card(
        [dbc.CardHeader("分析結果",
                       id='cardheader'),
         dbc.CardBody([html.P("", id='table_header_body')]),
        ],id="cards",
    ),
    
    ],id='main2'),

                       
     html.Div('TKU Japanese Sentence Pattern Analyzer (JSPA)', id='footer'),                  
                       
], id='container')


@app.callback(
#     Output('debug', 'children'),
#     Output('api_output', 'children'),
#     Output('api_input', 'children'),
    Output('table_header_body','children'),
#     Output('print_out','children'),
    Input('submit-val', 'n_clicks'),
    State('textarea-example', 'value'),
    State('dict_dropdown', 'value'),
    State('pattern_6_8', 'value'),
    State('pattern_9_11', 'value'),
    State('pattern_12_15', 'value'),
    State('pattern_16_20', 'value'),
    State('pattern_21_23', 'value'),
    State('pattern_24_26', 'value'),
    State('pattern_27_28', 'value'),
    State('pattern_29_31', 'value'),
    State('pattern_32_34', 'value'),
    State('pattern_V_naAdj', 'value'),
    State('pattern_N_N', 'value'),
    State('pattern_P23', 'value'),
    State('pattern_V', 'value'),
    State('pattern_ADJ', 'value')
    
)


def update_output(n_clicks, article, dict_type, pattern_id_list_6_8, pattern_id_list_9_11, pattern_id_list_12_15, pattern_id_list_16_20, pattern_id_list_21_23, pattern_id_list_24_26, pattern_id_list_27_28, pattern_id_list_29_31, pattern_id_list_32_34, pattern_id_list_V_naAdj, pattern_id_list_N_N, pattern_id_list_P23, pattern_id_list_V, pattern_id_list_ADJ):
    pattern_id_list = []
    pattern_id_list.extend(pattern_id_list_6_8)
    pattern_id_list.extend(pattern_id_list_9_11)
    pattern_id_list.extend(pattern_id_list_12_15)
    pattern_id_list.extend(pattern_id_list_16_20)
    pattern_id_list.extend(pattern_id_list_21_23)
    pattern_id_list.extend(pattern_id_list_24_26)
    pattern_id_list.extend(pattern_id_list_27_28)
    pattern_id_list.extend(pattern_id_list_29_31)
    pattern_id_list.extend(pattern_id_list_32_34)
    pattern_id_list.extend(pattern_id_list_V_naAdj)
    pattern_id_list.extend(pattern_id_list_N_N)
    pattern_id_list.extend(pattern_id_list_P23)
    pattern_id_list.extend(pattern_id_list_V)
    pattern_id_list.extend(pattern_id_list_ADJ)
    
    data = {"article": article, "dict_type": dict_type, "pattern_id_list": pattern_id_list}
    headers = {'Content-Type': 'application/json'}
    
    # 用res回傳
    res = requests.post(url='http://lingpu.im.tku.edu.tw:35140/api/filter', headers=headers, data=json.dumps(data))
    res_json = res.json()
    result_dic = res_json.get('filter')
    debug = f'<pre>clicks: {n_clicks}, article:{article}, dict_type:{dict_type}, pattern_id_list:{pattern_id_list}</pre>'
    row_list = []
        

    for pattern_id in result_dic:
        pattern_result_list = result_dic[pattern_id]
        title_id = pattern_id
        name_id = pattern_result_list[0]
        degree_id = name_id.split('<br/>')[0]
        element_id = name_id.split('<br/>')[1:-1]
        element_id2 = '<br/>'.join(element_id)
        briefly_id = name_id.split('<br/>')[-1]
        desc_id = pattern_result_list[1]
        desc_id2 = ''
        if pattern_id != 'z?':
            desc_id2 = '<br/>'.join(desc_id)
        sent_list = pattern_result_list[2:]
        len_sent_list = len(sent_list)
        row_list.extend([html.Tr([html.Td(dash_dangerously_set_inner_html.DangerouslySetInnerHTML(f'{degree_id}'), rowSpan = len_sent_list + 2, style={'font-weight':'bold'}),
                                 html.Td(dash_dangerously_set_inner_html.DangerouslySetInnerHTML(f'{element_id2}'),rowSpan = len_sent_list + 2, style={'font-weight':'bold'}),
                                 html.Td([title_id + '句型 : ' + desc_id2], style={'color':'#235486','font-weight':'bold','border-bottom':'2px #7896B5 double'})
                                 ]),
                         html.Tr(html.Td(dash_dangerously_set_inner_html.DangerouslySetInnerHTML('文法簡説 : '+f'{briefly_id}'),
                                                   style={'font-weight':'bold','color':'#408080','border-bottom':'2px #89AEAE double'}) ) ,
                         html.Tr(html.Td(dash_dangerously_set_inner_html.DangerouslySetInnerHTML(f'{sent_list[0]}')) )
                        ])
        
        for sent in sent_list[1:]:
            row_list.append(html.Tr([html.Td(dash_dangerously_set_inner_html.DangerouslySetInnerHTML(f'{sent}'))],style={'border-bottom':'3px #C1C5AF double'}))
        
            
    if pattern_id_list == []:
        pass
    else:
        table_header = [html.Thead(html.Tr([html.Th('難易程度'), html.Th("文法要素"), html.Th("例句sentence")],style={'border-top':'1px #f9f4d4 double','border-bottom':'3px #E0D7AE double','color':'#A49A70'}))]
        table_body = [html.Tbody(row_list, style={'color':'#888059'})]
    return dbc.Table(table_header + table_body),#             str(result_dic),\
#            str(data),\
#            dash_dangerously_set_inner_html.DangerouslySetInnerHTML(f'{debug}'),\
#            sent_list                      


@app.callback(
    Output("colla6_8", "is_open"),
    [Input("open_6_8", "n_clicks")],
    [State("colla6_8", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("colla9_11", "is_open"),
    [Input("open_9_11", "n_clicks")],
    [State("colla9_11", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("colla12_15", "is_open"),
    [Input("open_12_15", "n_clicks")],
    [State("colla12_15", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("colla16_20", "is_open"),
    [Input("open_16_20", "n_clicks")],
    [State("colla16_20", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("colla21_23", "is_open"),
    [Input("open_21_23", "n_clicks")],
    [State("colla21_23", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("colla24_26", "is_open"),
    [Input("open_24_26", "n_clicks")],
    [State("colla24_26", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("colla27_28", "is_open"),
    [Input("open_27_28", "n_clicks")],
    [State("colla27_28", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("colla29_31", "is_open"),
    [Input("open_29_31", "n_clicks")],
    [State("colla29_31", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("colla32_34", "is_open"),
    [Input("open_32_34", "n_clicks")],
    [State("colla32_34", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collaV_naAdj", "is_open"),
    [Input("open_V_naAdj", "n_clicks")],
    [State("collaV_naAdj", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collaN_N", "is_open"),
    [Input("open_N_N", "n_clicks")],
    [State("collaN_N", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collaP23", "is_open"),
    [Input("open_P23", "n_clicks")],
    [State("collaP23", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collaV", "is_open"),
    [Input("open_V", "n_clicks")],
    [State("collaV", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collaADJ", "is_open"),
    [Input("open_ADJ", "n_clicks")],
    [State("collaADJ", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("pattern_6_8", "value"),
    Output("pattern_9_11", "value"),
    Output("pattern_12_15", "value"),
    Output("pattern_16_20", "value"),
    [Input("all-or-none", "value")],
    [State("pattern_6_8", "options")],
    [State("pattern_9_11", "options")],
    [State("pattern_12_15", "options")],
    [State("pattern_16_20", "options")],

)
def select_all_none(all_selected, options_6_8, options_9_11, options_12_15, options_16_20):
    all_or_none_6_8 = []
    all_or_none_6_8 = [option["value"] for option in options_6_8 if 'All' in all_selected]
    all_or_none_9_11 = []
    all_or_none_9_11 = [option["value"] for option in options_9_11 if 'All' in all_selected]
    all_or_none_12_15 = []
    all_or_none_12_15 = [option["value"] for option in options_12_15 if 'All' in all_selected]
    all_or_none_16_20 = []
    all_or_none_16_20 = [option["value"] for option in options_16_20 if 'All' in all_selected]
#     print(all_selected)
    return all_or_none_6_8, all_or_none_9_11, all_or_none_12_15, all_or_none_16_20

@app.callback(
    Output("pattern_21_23", "value"),
    Output("pattern_24_26", "value"),
    Output("pattern_27_28", "value"),
    Output("pattern_29_31", "value"),
    Output("pattern_32_34", "value"),
    [Input("all-or-none2", "value")],
    [State("pattern_21_23", "options")],
    [State("pattern_24_26", "options")],
    [State("pattern_27_28", "options")],
    [State("pattern_29_31", "options")],
    [State("pattern_32_34", "options")],

)
def select_all_none(all_selected, options_21_23, options_24_26, options_27_28, options_29_31, options_32_34):
    all_or_none_21_23 = []
    all_or_none_21_23 = [option["value"] for option in options_21_23 if 'All' in all_selected]
    all_or_none_24_26 = []
    all_or_none_24_26 = [option["value"] for option in options_24_26 if 'All' in all_selected]
    all_or_none_27_28 = []
    all_or_none_27_28 = [option["value"] for option in options_27_28 if 'All' in all_selected]
    all_or_none_29_31 = []
    all_or_none_29_31 = [option["value"] for option in options_29_31 if 'All' in all_selected]
    all_or_none_32_34 = []
    all_or_none_32_34 = [option["value"] for option in options_32_34 if 'All' in all_selected]
#     print(all_selected)
    return all_or_none_21_23, all_or_none_24_26, all_or_none_27_28, all_or_none_29_31, all_or_none_32_34

@app.callback(
    Output("pattern_V_naAdj", "value"),
    Output("pattern_N_N", "value"),
    Output("pattern_P23", "value"),
    Output("pattern_V", "value"),
    Output("pattern_ADJ", "value"),
    [Input("all-or-none3", "value")],
    [State("pattern_V_naAdj", "options")],
    [State("pattern_N_N", "options")],
    [State("pattern_P23", "options")],
    [State("pattern_V", "options")],
    [State("pattern_ADJ", "options")],

)
def select_all_none(all_selected, options_V_naAdj, options_N_N, options_P23, options_V, options_ADJ):
    all_or_none_V_naAdj = []
    all_or_none_V_naAdj = [option["value"] for option in options_V_naAdj if 'All' in all_selected]
    all_or_none_N_N = []
    all_or_none_N_N = [option["value"] for option in options_N_N if 'All' in all_selected]
    all_or_none_P23 = []
    all_or_none_P23 = [option["value"] for option in options_P23 if 'All' in all_selected]
    all_or_none_V = []
    all_or_none_V = [option["value"] for option in options_V if 'All' in all_selected]
    all_or_none_ADJ = []
    all_or_none_ADJ = [option["value"] for option in options_ADJ if 'All' in all_selected]
#     print(all_selected)
    return all_or_none_V_naAdj, all_or_none_N_N, all_or_none_P23, all_or_none_V, all_or_none_ADJ

@app.callback(
    Output("collapse", "is_open"),
    [Input("open", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse2", "is_open"),
    [Input("open2", "n_clicks")],
    [State("collapse2", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse3", "is_open"),
    [Input("open3", "n_clicks")],
    [State("collapse3", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open



if __name__ == '__main__':
    #app.run_server(debug=True)
    #app.run_server(port=1236)
#     app.run_server(mode='inline', debug=True, port=3388)
#    app.run_server(debug=True, use_reloader=False)
     app.run_server(debug=False, use_reloader=False, host='0.0.0.0', port=8050)


# In[ ]:




