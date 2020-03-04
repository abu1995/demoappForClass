from tethys_sdk.base import TethysAppBase, url_map_maker


class Demo(TethysAppBase):
    """
    Tethys app class for Demo.
    """

    name = 'Demo'
    index = 'demo:home'
    icon = 'demo/images/icon.gif'
    package = 'demo'
    root_url = 'demo'
    color = '#000000'
    background_color = '#FFFF00'
    description = 'About me app'
    tags = 'Aboutme Intro'
    enable_feedback = False
    feedback_emails = []

       def url_maps(self):
           """
           Add controllers
           """
           UrlMap = url_map_maker(self.root_url)

           url_maps = (
               UrlMap(
                   name='home',
                   url='demo',
                   controller='demo.controllers.home'
               ),
               UrlMap(
                   name='map',
                   url='demo/map',
                   controller='demo.controllers.map'
               ),
               UrlMap(
                   name='design',
                   url='demo/design',
                   controller='demo.controllers.design_pages'
               ),
               UrlMap(
                   name='proposal',
                   url='demo/proposal',
                   controller='demo.controllers.proposal'
               ))

           return url_maps

