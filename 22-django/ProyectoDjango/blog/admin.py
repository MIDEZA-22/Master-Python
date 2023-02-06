from django.contrib import admin
from . models import Category, Article #an 1h-IMPORTAR LA "class Category y class Article" DE "models.py" CORRESPONDIENTE A LA APP CREADA "blog"
 
#an CONFIGURACIONES EXTRAS PARA EL PANEL DE ADMINISTRACION CON RESPECTO A LA APP "blog" PARA LUEGO AGREGAR EL "CategoryAdmin" y el "ArticleAdmin" AL 2h CORRESPONDIENTEMENTE
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',) #az Se pone una coma al final de 'created_at' para que el programa lo interprete como una tupla.SINO NO FUNCIONA
    list_display = ('name', 'created_at') #az Se muestra una tabla con las columnas correspondientes
    search_fields = ('name', 'description') #az Mostrar un buscador

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'created_at', 'update_at') #az se pone el 'user' por ahora se convirtio en un campo de solo lectura
    search_fields = ('title', 'content', 'user__username', 'categories__name') #az Mostrar un buscador
    list_display = ('title', 'user','public', 'created_at') #az Se muestra una tabla con las columnas correspondientes
    list_filter = ('public', 'user__username', 'categories__name') #az Filtrar con respecto al campo 'visible'

    #an MANIPULAR EL COMPORTAMIENTO CUANDO SE GRABE UN ARTICULO EN EL PANEL DE ADMINISTRACION SIN SELECCIONAR EL "Usuario". DEBIDO A QUE EL CAMPO "Usuario" YA NO ESTA VISIBLE EN EL PANEL, PORQUE EN "models.py", ESPECIFICAMENTE EN EL CAMPO "user" SE COLOCOLO EL "editable=False"
    def save_model(self, request, obj, form, change): #az Todos los parametros son necesarios para crear el hook
        if not obj.user_id:
            obj.user_id = request.user.id
            
        obj.save()

#an 2h-REGISTRAR EL MODELO CREADO EN "models.py" CON EL NOMBRE DE "class Category" y "class Article" PARA VISUALIZARLO EN EL PANEL DE ADMINISTRACION
admin.site.register(Category, CategoryAdmin) #az Se le pasa como parametro las clase 'CategoryAdmin' para mostrar los campos de solo lectura
admin.site.register(Article, ArticleAdmin) #az Se le pasa como parametro las clase 'ArticleAdmin' para mostrar los campos de solo lectura

