from django.conf import settings

from edc_navbar import NavbarItem, site_navbars, Navbar

eventcalendar = Navbar(name='eventcalendar')
no_url_namespace = True if settings.APP_NAME == 'eventcalendar' else False

eventcalendar.append_item(
    NavbarItem(name='dashboard',
               label='dashboard',
               fa_icon='fa-cogs',
               url_name='eventcalendar:dashboard'))

site_navbars.register(eventcalendar)
