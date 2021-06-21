from django.db import models

# Create your models here.
class Post(models.Model):
	"""
			Это записи для блога
		докрутить изменение через админку, если не будет из коробки,
		картинки и прочее медиа искать в media/blog/Post
	"""
	date = models.DateField(verbose_name = "Дата публикации", auto_now = True)
	title = models.CharField(verbose_name = "Заголовок", max_length = 50, 
		help_text = "Введите Заголовок")
	preview = models.ImageField(verbose_name="Обложка поста" ,upload_to='blog/Post', blank=True)
	ncomments = models.PositiveSmallIntegerField(verbose_name="Количество комментариев", default = 0)
	likes = models.PositiveSmallIntegerField(verbose_name="Количество лайков", default = 0)
	post_text = models.TextField(verbose_name = "Текст поста",default = "Добавьте текст")
	post_link = models.URLField(verbose_name = "Ссылка на пост", )

	def __str__(self):
		return  "Запись:"+self.title+"опубликована:"+str(self.date)
	
	def getDate(self):
		return self.date

	def getTitle(self):
		return self.title

	def getDescription(self):
		size = len(self.post_text) 
		if size > 200:
			return self.post_text[:200]
		else:
			return self.post_text

	def getText(self):
		return self.post_text
	
	def getPostStat(self):
		return [self.likes,self.ncomments]

	def getLink(self):
		return self.post_link

	def getPreview(self):
		if self.preview:
			return self.preview
		else:
			return False