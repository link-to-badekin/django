from django.db import models

# Create your models here.
class NavBar(models.model):
	"""Навигация в хэдере и не только
	Класс самого меню, элементы меню class NavItem 
	"""
	name = models.CharField(verbose_name = "Название меню", max_length = 50, 
		help_text = "Введите название для меню")
	def __str__(self):
		return self.name
	def getNavItem(self):
		return NavItem.objects.filter(menu = self.id)
	class Meta:
        verbose_name = 'Меню навигации'



class NavItem(models.model):
	"""docstring for NavItem
	Элементы меню
	menu - родительское меню, где будет отображаться кнопка
	link - ссылка элемента 
	icon - потенциальная иконка для меню 
	position - позиция в меню
	"""
	name = models.CharField(verbose_name = "Название ссылки", max_length = 50, 
		help_text = "Введите название для кнопки")
	menu = models.ForeignKey(to = NavBar, on_delete = models.CASCADE, 
		verbose_name = "Родительское меню" ) 
	link = models.URLField(verbose_name = "Ссылка для перехода")
	icon = models.ImageField(verbose_name="Иконка",upload_to='navbar/item', blank=True)
	position = models.PositiveSmallIntegerField(verbose_name = "Позиция",
		default = getNumElemnts)
	#submenu = 
	def __str__(self):
		return  "Элемент меню {}: {} ,ссылается на {}".format(
			str(NavBar.objects.get(self.menu)),self.name, self.link)
	def getName(self):
	 	return self.name
	def getLink(self):
		return self.link
	def getNumElemnts(self)
		return NavItem.objects.filter(menu = self.menu).count()
	class Meta:
        ordering = ('position',)
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
