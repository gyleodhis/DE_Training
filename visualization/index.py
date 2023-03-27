import dash
from dash import Dash, html, dcc

from dash.dependencies import Input, Output
# from controller.climate_data import fig_top_emitter_by_year, emission_by_continent

app = Dash(__name__,use_pages=True)
server = app.server
app.title = 'SADIQ_OIL'

app.layout = html.Div(
    className='hold-transition sidebar-mini layout-fixed layout-footer-fixed layout-navbar-fixed',
    children=[
        html.Div(className='wrapper', children=[
            # dcc.Location(id='url', refresh=False),
            html.Nav(className="main-header navbar navbar-expand",
                     # Left navbar links
                     children=[
                         html.Ul(className="navbar-nav", children=[
                             html.Li(className='nav-item', children=[
                                 html.A(className='nav-link', href='#', **{'data-widget': 'pushmenu'}, role='button',
                                        children=[html.I(className='fas fa-bars')])]),
                             html.Li(className='nav-item d-sm-inline-block', children=[
                                 html.A('Home', className='nav-link', href=dash.page_registry['pages.home']['path'])])
                         ]),
                         html.Ul(className='navbar-nav ml-auto', children=[
                             html.Form(className='form-inline ml-3', children=[
                                 html.Div(className='input-group input-group-sm', children=[
                                     dcc.Input(className='form-control form-control-navbar', type='search',
                                               placeholder='Search'),
                                     html.Div(className='input-group-append',
                                              children=[
                                                  html.Button(className='btn btn-navbar', type='submit',
                                                              children=html.I(className='fas fa-search'))
                                              ])])])])
                     ]),
            # Main Sidebar Container
            html.Aside(className='main-sidebar sidebar-dark-primary elevation-4',
                       # Logo container
                       children=[
                           html.A(className='brand-link',
                                  href='#',
                                  target='_blank', children=[
                                   html.Img(className='brand-image img-circle elevation-3', src='assets/img/logo.png',
                                            alt='Saqig',
                                            style={'opacity': .8}),
                                   html.Span('SADIQ OIL', className='brand-text font-weight-light')
                               ]),
                           html.Div(className='sidebar', children=[
                               html.Div(className='mt-2', children=[
                                   html.Ul(className='nav nav-pills nav-sidebar flex-column',**{'data-widget': 'treeview', 'data-accordion': 'false'},
                                           role='menu',children=[
                                           html.Li(className='nav-item active', children=[
                                               html.A(className='nav-link', href=dash.page_registry['pages.home']['path'], children=[
                                                   html.I(className='nav-icon fas fa-globe-africa text-success'),
                                                   html.P(children=['Home'])])
                                           ])
                                       ])
                               ])
                           ])
                       ]),
            # Content Wrapper. Contains page content
            html.Div(className='content-wrapper',
                     # Content Header (Page header)
                     children=[
                         dash.page_container
                         # html.Div(id='page-content')
                     ]),
            html.Footer(className='main-footer', children=[
                html.Strong('Sadiq Oil© | All Rights Reserved | 2023')
            ])])
    ])


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=3000, debug=True)
