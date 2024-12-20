from django.shortcuts import render
from peliculas.models import Pelicula

#FUNCION PARA CARGAR LA PAGINA INDEX
def mostrarIndex(request):
    return render(request, "index.html")

#FUNCION PARA CARGAR EL FORMULARIO DE REGISTRO
def mostrarFormRegistrar(request):
    return render(request, "form_registrar.html")

#FUNCION PARA CARGAR EL LISTADO DE PELICULAS EN LA PAFINA
def mostrarListado(request):
    pel = Pelicula.objects.all().values()
    datos = {'pel' : pel}
    return render(request, "listado.html", datos)

#FUNCION PARA REGISTRAR UNA NUEVA PELICULA
def registrarPelicula(request):
    if request.method == 'POST':
        nom = request.POST['txtnom']
        try:
            fot = request.FILES['txtfot']
        except:
            fot = "imagenes_bd/noimagen.jpg"

        comprobarNombre = Pelicula.objects.filter(nombre=nom)
        if comprobarNombre:
            datos = {'r2' : 'ERROR, EL NOMBRE DE LA PELICULA YA EXISTE'}
            return render(request,"form_registrar.html", datos)
        else:
            pel = Pelicula(nombre= nom, foto=fot)
            pel.save()
            datos = {'r' : 'GENIAL, SE REGISTRO LA PELICULA CON EXITO'}
            return render(request,"form_registrar.html", datos)
    else:
        datos = {'r2' : 'ERROR, NO SE PUEDE PROCESAR LA SOLICITUD'}
        return render(request,"form_registrar.html", datos)


#FUNCION PARA ELIMINAR LA PELICULA (DESDE LA BD Y DESDE EL ARCHIVO)
def eliminarPelicula(request, id):
    try:
        #Borrar la pelicula desde la BD
        pel = Pelicula.objects.get(id=id)
        nompel = pel.nombre
        ruta_foto = "media/" + str(pel.foto)
        pel.delete()

        #AHORA DEBEMOS BORRAR EL ARCHIVO DELA IMAGEN
        import os
        if ruta_foto != "media/imagenes_bd/noimagen.jpg":
            os.remove(ruta_foto)

        #AHORA DEBEMOS DEVOLVERNOS Y MOSTRAR EL LISTADO DE PELUICULAS 
        pel = Pelicula.objects.all().values()
        datos = {'pel' : pel, 'r' : 'FELICITACINES, LA PELICULA FUE ELIMINADA CON EXITO'}
        return render(request, "listado.html", datos)
    except:
        #AHORA DEBEMOS DEVOLVERNOS Y MOSTRAR EL LISTADO DE PELUICULAS 
        pel = Pelicula.objects.all().values()
        datos = {'pel' : pel, 'r2' : 'ERROR AL ELIMINAR LA PELICULA'}
        return render(request, "listado.html", datos)

#FUNCION PARA MOSTRAR EL FORMULARIO DE ACTUALIZAR CON LOS DATOS DE LA PELICULA SELECCIONADA
def mostrarFormActualizar(request, id):
    try:
        pel = Pelicula.objects.get(id=id)
        datos = {'pel' : pel}
        return render(request, "form_actualizar.html", datos)    
    except:
        pel = Pelicula.objects.all().values()
        datos = {'pel' : pel, 'r2' : 'ERROR AL BUSCAR PARA EDITAR LA PELICULA'}
        return render(request, "listado.html", datos)

#FUNCION PARA ACTUALIZAR LA PELICULA
def actualizarPelicula(request, id):
    try:
        nom = request.POST['txtnom']        #ESTE ES EL NUEVO NOMBRE
        pel = Pelicula.objects.get(id=id)
        try:
            fot = request.FILES['txtfot']   #ESTA ES LA NUEVA FOTO
            ruta_foto = "media/" + str(pel.foto)
            import os
            if ruta_foto != "media/imagenes_bd/noimagen.jpg":
                os.remove(ruta_foto)
        except:
            fot = pel.foto   #ENTRA AL EXCEPT CUANDO NO SE QUISO REEMPLAZAR LA FOTO
        
        pel.nombre = nom  #AQUI REEMPLAZO EL NOMBRE
        pel.foto = fot    #AQUI REEMPLAZO LA FOTO
        pel.save()        #AQUI GRABO LOS CAMBIOS

        pel = Pelicula.objects.all().values()
        datos = {'pel': pel, 'r':'FELICITACIONES, SE REALIZO CON EXITO LA MODIFICACION'}
        return render(request, "listado.html", datos)
    except:
        pel = Pelicula.objects.all().values()
        datos = {'pel': pel, 'r2':'ERRROR, NO SE PUDO MODIFICAR LA PELICULA'}
        return render(request, "listado.html", datos)
