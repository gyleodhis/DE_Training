import dash
from dash import html, dcc
from controller.data_load import *
import controller.my_functions as mf

dash.register_page(__name__,path='/parafin',name='Parafin',title='Sadiq',image_url='assets/img/site_meta.jpeg',
                   description='Leading Oil Producer in Nigeria')
layout = html.Div([
    html.Section(className='content-header', children=[
        html.Div(className='container-fluid', children=[
            html.Div(className='row mb-2', children=[
                html.Div(className='col-sm-6', children=[
                    html.H1('Oil Fields Data')
                ]),
                html.Div(className='col-sm-6', children=[
                    html.Ol(className='breadcrumb float-sm-right', children=[
                        html.Li(className='breadcrumb-item', children=[
                            html.A('Home', href='/')
                        ]),
                        html.Li('Oil', className='breadcrumb-item active')
                    ])
                ])
            ])
        ])
    ]),
    html.Section(className='content', children=[
        html.Div(className='container-fluid', children=[
            html.Div(className='row', children=[
                html.Div(className='col-md-12', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col-md-3', children=[
                            html.Div(className='small-box bg-danger', children=[
                                html.Div(className='inner', children=[
                                    html.H4(df_oil['Field'].iloc[0]),
                                    html.P('%s Barels'%mf.round_up(df_oil['Oil_production'].sum(),2))
                                ]),
                                html.A('Total Barels',className='small-box-footer', href='#')
                            ])
                        ]),
                        html.Div(className='col-md-3', children=[
                            html.Div(className='small-box bg-danger', children=[
                                html.Div(className='inner', children=[
                                    html.H4(oil_by_field().tail()['Field'].iloc[0]),
                                    html.P('%s Barels'%oil_by_field().tail()['Oil_production'].iloc[1])
                                ]),
                                html.A('Highest Field Producer',className='small-box-footer', href='#')
                            ])
                        ]),
                        html.Div(className='col-md-3', children=[
                            html.Div(className='small-box bg-danger', children=[
                                html.Div(className='inner', children=[
                                    html.H4(oil_by_field()['Field'].iloc[0]),
                                    html.P('%s Barels'%oil_by_field()['Oil_production'].iloc[0])
                                ]),
                                html.A('Least Producer',className='small-box-footer', href='#')
                            ])
                        ]),
                        html.Div(className='col-md-3', children=[
                            html.Div(className='small-box bg-danger', children=[
                                html.Div(className='inner', children=[
                                    html.H4(oil_by_field()['Field'].iloc[1]),
                                    html.P('%s Barels'%oil_by_field()['Oil_production'].iloc[1])
                                ]),
                                html.A('2nd Least Producer',className='small-box-footer', href='#')
                            ])
                        ])
                    ])
                ])
            ]),
            # The row for graphs
            html.Div(className='row', children=[
                html.Div(className='col-md-12', children=[
                    html.Div(className='card', children=[
                        html.Div(className='card-header border-0', children=[
                            html.Div(className='d-flex justify-content-between', children=[
                                html.H3('To Fields', className='card-title'),
                                html.Div(className='card-tools', children=[
                                    html.Ul(className='nav nav-pills ml-auto', children=[
                                        html.Li(className='nav-item',
                                                children=html.A('Top Producers', className='nav-link active',
                                                                href='#africa', **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item',
                                                children=html.A('Least Producers', className='nav-link',
                                                                href='#namerica',
                                                                **{'data-toggle': 'tab'}))
                                    ])
                                ])
                            ])
                        ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='tab-content p-0', children=[
                                html.Div(className='active tab-pane', id='africa', children=[
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(children=[dcc.Graph(figure=fig_bar())],
                                                    type='circle',color='#006400')
                                    ])]),
                                html.Div(className='tab-pane', id='namerica', children=[
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(children=[dcc.Graph(figure=fig_funnel())],
                                                    type='circle',color='#006400',)
                                    ])])
                            ])
                        ])
                    ])
                ])
            ])
        ])
    ])

])