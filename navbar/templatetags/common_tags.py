from django import template
from navbar.models import NavBar 
register = template.Library()

@register.inclusion_tag('NavBar.html', takes_context=True)
#inclusion_tag(путь к шаблону, takes_context=True)

def show_top_menu(context):
	"""
	тег для обображения хэдера 
	По имени управляющей модели получаем набор его элементов
	"""
    menu = NavBar.objects.get(name = context)
    if menu:
    	menu_items = menu.getNavItem()
    	if menu_items :
	    	return {
    	    	"menu_items": menu_items,
    		}
 	else:
 		return 0 # сделать пустой класс для ошибок