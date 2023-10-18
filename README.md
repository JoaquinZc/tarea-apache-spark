### PASOS PARA DUPLICAR

 - Primero abre Docker Desktop.
 - Segundo abre la carpeta donde está el proyecto y luego abre la carpeta que dice spark y dale doble clic al archivo "build", este construirá la imagen el docker, o más bien descarga todo lo que necesitas, espera hasta que termine y después ve al docker desktop y ve si en la pestaña de imágenes está la carpeta imagen llamada mi-spark
 - Tercero ve a la carpeta raiz y da doble clic en "execute" y ahora, vuelves a la carpeta raíz y das doble clic en "console"
 - Cuarto, una vez en la consola se ejecuta el comando "cd bin" y luego "./spark-submit --master spark://0.0.0.0:7077 /opt/spark-apps/app1.py"