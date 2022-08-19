#Definimos nuestra lista la cual almacenara las respuestas del formulario 
answer =''
visual= 0
auditivo= 0
cinestesico= 0

print("Bienvenido al sistema de prediccion de estilos de aprendizaje\n Para comenzar requeriremos que llenes un formularario de 40 preguntas el cual nos permitira conocerte mucho mas \n")
#Creamos el formulario del Modelo PNL y almacenamos las repuestas para ser analizadas en el arbol de decision
answer + input ('1. ¿Cuál de las siguientes actividades disfrutas más?\n a) Escuchar música\n b) Ver películas\n c) Bailar con buena música\n')
answer + input ('2. ¿Qué programa de televisión prefieres?\n a) Reportajes de descubrimientos y lugares\n b) Cómico y de entretenimiento\n c) Noticias del mundo\n')
answer + input ('3. Cuando conversas con otra persona, tú:\n a) La escuchas atentamente\n b) La observas\n c) Tiendes a tocarla\n')
answer + input ('4. Si pudieras adquirir uno de los siguientes artículos, ¿cuál elegirías?\n a) Un jacuzzi\n b) Un estéreo\n c) Un televisor\n')
answer + input ('5. ¿Qué prefieres hacer un sábado por la tarde?\n a) Quedarte en casa\n b) Ir a un concierto\n c) Ir al cine\n')
answer + input ('6. ¿Qué tipo de exámenes se te facilitan más?\n a) Examen oral\n b) Examen escrito\n c) Examen de opción múltiple\n')
answer + input ('7. ¿Cómo te orientas más fácilmente?\n a) Mediante el uso de un mapa\n b) Pidiendo indicaciones\n c) A través de la intuición\n')
answer + input ('8. ¿En qué prefieres ocupar tu tiempo en un lugar de descanso?\n a) Pensar\n b) Caminar por los alrededores\n c) Descansar\n')
answer + input ('9. ¿Qué te halaga más?\n a) Que te digan que tienes buen aspecto\n b) Que te digan que tienes un trato muy agradable\n c) Que te digan que tienes una conversación interesante\n')
answer + input ('10. ¿Cuál de estos ambientes te atrae más?\n a) Uno en el que se sienta un clima agradable\n b) Uno en el que se escuchen las olas del mar\n c) Uno con una hermosa vista al océano\n')

answer + input ('11. ¿De qué manera se te facilita aprender algo?\n a) Repitiendo en voz alta\n b) Escribiéndolo varias veces\n c) Relacionándolo con algo divertido\n')
answer + input ('12. ¿A qué evento preferirías asistir?\n a) A una reunión social\n b) A una exposición de arte\n c) A una conferencia\n')
answer + input ('13. ¿De qué manera te formas una opinión de otras personas?\n a) Por la sinceridad en su voz\n b) Por la forma de estrecharte la mano\n c) Por su aspecto\n')
answer + input ('14. ¿Cómo te consideras?\n a) Atlético\n b) Intelectua\n c) Sociable\n')
answer + input ('15. ¿Qué tipo de películas te gustan más?\n a) Clásicas\n b) De acción\n c) De amor\n')
answer + input ('16. ¿Cómo prefieres mantenerte en contacto con otra persona?\n a) Por correo electrónico\n b) Tomando un café juntos\n c) Por teléfono\n')
answer + input ('17. ¿Cuál de las siguientes frases se identifican más contigo?\n a) Me gusta que mi coche se sienta bien al conducirlo\n b) Percibo hasta el mas ligero ruido que hace mi coche\n c) Es importante que mi coche esté limpio por fuera y por dentro\n')
answer + input ('18. ¿Cómo prefieres pasar el tiempo con tu novia o novio?\n a) Conversando\n b) Acariciándose\n c) Mirando algo juntos\n')
answer + input ('19. Si no encuentras las llaves en una bolsa\n a) La buscas mirando\n b) Sacudes la bolsa para oír el ruido\n c) Buscas al tacto\n')
answer + input ('20. Cuando tratas de recordar algo, ¿cómo lo haces?\n a) A través de imágenes\n b) A través de emociones\n c) A través de sonidos\n')

answer + input ('21. Si tuvieras dinero, ¿qué harías?\n a) Comprar una casa\n b) Viajar y conocer el mundo\n c) Adquirir un estudio de grabación\n')
answer + input ('22. ¿Con qué frase te identificas más?\n a) Reconozco a las personas por su voz\n b) No recuerdo el aspecto de la gente\n c) Recuerdo el aspecto de alguien, pero no su nombre\n')
answer + input ('23. Si tuvieras que quedarte en una isla desierta, ¿qué preferirías llevar contigo?\n a) Algunos buenos libros\n b) Un radio portátil de alta frecuencia\n c) Golosinas y comida enlatada\n')
answer + input ('24. ¿Cuál de los siguientes entretenimientos prefieres?\n a) Tocar un instrumento musical\n b) Sacar fotografías\n c) Actividades manuales\n')
answer + input ('25. ¿Cómo es tu forma de vestir?\n a) Impecable\n b) Informal\n c) Muy informal\n')
answer + input ('26. ¿Qué es lo que más te gusta de una fogata nocturna?\n a) El calor del fuego y los bombones asados\n b) El sonido del fuego quemando la leña\n c) Mirar el fuego y las estrellas\n')
answer + input ('27. ¿Cómo se te facilita entender algo?\n a) Cuando te lo explican verbalmente\n b) Cuando utilizan medios visuales\n c) Cuando se realiza a través de alguna actividad\n')
answer + input ('28. ¿Por qué te distingues?\n a) Por tener una gran intuición\n b) Por ser un buen conversador\n c) Por ser un buen observador\n')
answer + input ('29. ¿Qué es lo que más disfrutas de un amanecer?\n a) La emoción de vivir un nuevo día\n b) Las tonalidades del cielo\n c) El canto de las aves\n')
answer + input ('30. Si pudieras elegir ¿qué preferirías ser?\n a) Un gran médico\n b) Un gran músico\n c) Un gran pintor\n')

answer + input ('31. Cuando eliges tu ropa, ¿qué es lo más importante para ti?\n a) Que sea adecuada\n b) Que luzca bien\n c) Que sea cómoda\n')
answer + input ('32. ¿Qué es lo que más disfrutas de una habitación?\n a) Que sea silenciosa\n b) Que sea confortable\n c) Que esté limpia y ordenada\n')
answer + input ('33. ¿Qué es más sexy para ti?\n a) Una iluminación tenue\n b) El perfume\n c) Cierto tipo de música\n')
answer + input ('34. ¿A qué tipo de espectáculo preferirías asistir?\n a) A un concierto de música\n b) A un espectáculo de magia\n c) A una muestra gastronómica\n')
answer + input ('35. ¿Qué te atrae más de una persona?\n a) Su trato y forma de ser\n b) Su aspecto físico\n c) Su conversación\n')
answer + input ('36. Cuando vas de compras, ¿en dónde pasas mucho tiempo?\n a) En una librería\n b) En una perfumería\n c) En una tienda de discos\n')
answer + input ('37. ¿Cuáles tu idea de una noche romántica?\n a) A la luz de las velas\n b) Con música romántica\n c) Bailando tranquilamente\n')
answer + input ('38. ¿Qué es lo que más disfrutas de viajar?\n a) Conocer personas y hacer nuevos amigos\n b) Conocer lugares nuevos\n c) Aprender sobre otras costumbres\n')
answer + input ('39. Cuando estás en la ciudad, ¿qué es lo que más hechas de menos del campo?\n a) El aire limpio y refrescante\n b) Los paisajes\n c) La tranquilidad\n')
answer + input ('40. Si te ofrecieran uno de los siguientes empleos, ¿cuál elegirías?\n a) Director de una estación de radio\n b) Director de un club deportivo\n c) Director de una revista\n')

#Creamos el arbol de desicion el cual nos va a definir el camino asia el estilo de aprendizaje 


if answer[0] == 'B':
    visual=+1
if answer[0] == 'A':
    auditivo=+1
if answer[0] == 'C':
    cinestecito=+1

if answer[1] == 'A':
    visual=+1
if answer[1] == 'C':
    auditivo=+1
if answer[1] == 'B':
    cinestecito=+1

if answer[2] == 'B':
    visual=+1
if answer[2] == 'A':
    auditivo=+1
if answer[2] == 'C':
    cinestecito=+1

if answer[3] == 'C':
    visual=+1
if answer[3] == 'B':
    auditivo=+1
if answer[3] == 'A':
    cinestecito=+1

if answer[4] == 'C':
    visual=+1
if answer[4] == 'B':
    auditivo=+1
if answer[4] == 'A':
    cinestecito=+1

if answer[5] == 'B':
    visual=+1
if answer[5] == 'A':
    auditivo=+1
if answer[5] == 'C':
    cinestecito=+1

if answer[6] == 'A':
    visual=+1
if answer[6] == 'B':
    auditivo=+1
if answer[6] == 'C':
    cinestecito=+1

if answer[7] == 'B':
    visual=+1
if answer[7] == 'A':
    auditivo=+1
if answer[7] == 'C':
    cinestecito=+1

if answer[8] == 'A':
    visual=+1
if answer[8] == 'C':
    auditivo=+1
if answer[8] == 'B':
    cinestecito=+1

if answer[9] == 'C':
    visual=+1
if answer[9] == 'B':
    auditivo=+1
if answer[9] == 'A':
    cinestecito=+1

if answer[10] == 'B':
    visual=+1
if answer[10] == 'A':
    auditivo=+1
if answer[10] == 'C':
    cinestecito=+1

if answer[11] == 'B':
    visual=+1
if answer[11] == 'C':
    auditivo=+1
if answer[11] == 'A':
    cinestecito=+1

if answer[12] == 'C':
    visual=+1
if answer[12] == 'A':
    auditivo=+1
if answer[12] == 'B':
    cinestecito=+1

if answer[13] == 'A':
    visual=+1
if answer[13] == 'B':
    auditivo=+1
if answer[13] == 'C':
    cinestecito=+1

if answer[14] == 'B':
    visual=+1
if answer[14] == 'A':
    auditivo=+1
if answer[14] == 'C':
    cinestecito=+1

if answer[15] == 'A':
    visual=+1
if answer[15] == 'C':
    auditivo=+1
if answer[15] == 'B':
    cinestecito=+1

if answer[16] == 'C':
    visual=+1
if answer[16] == 'B':
    auditivo=+1
if answer[16] == 'A':
    cinestecito=+1

if answer[17] == 'C':
    visual=+1
if answer[17] == 'A':
    auditivo=+1
if answer[17] == 'B':
    cinestecito=+1

if answer[18] == 'A':
    visual=+1
if answer[18] == 'B':
    auditivo=+1
if answer[18] == 'C':
    cinestecito=+1

if answer[19] == 'A':
    visual=+1
if answer[19] == 'C':
    auditivo=+1
if answer[19] == 'B':
    cinestecito=+1

if answer[20] == 'B':
    visual=+1
if answer[20] == 'C':
    auditivo=+1
if answer[20] == 'A':
    cinestecito=+1

if answer[21] == 'C':
    visual=+1
if answer[21] == 'A':
    auditivo=+1
if answer[21] == 'B':
    cinestecito=+1

if answer[22] == 'A':
    visual=+1
if answer[22] == 'B':
    auditivo=+1
if answer[22] == 'C':
    cinestecito=+1

if answer[23] == 'B':
    visual=+1
if answer[23] == 'A':
    auditivo=+1
if answer[23] == 'C':
    cinestecito=+1

if answer[24] == 'A':
    visual=+1
if answer[24] == 'B':
    auditivo=+1
if answer[24] == 'C':
    cinestecito=+1

if answer[25] == 'C':
    visual=+1
if answer[25] == 'B':
    auditivo=+1
if answer[25] == 'A':
    cinestecito=+1

if answer[26] == 'B':
    visual=+1
if answer[26] == 'A':
    auditivo=+1
if answer[26] == 'C':
    cinestecito=+1

if answer[27] == 'C':
    visual=+1
if answer[27] == 'B':
    auditivo=+1
if answer[27] == 'A':
    cinestecito=+1

if answer[28] == 'B':
    visual=+1
if answer[28] == 'A':
    auditivo=+1
if answer[28] == 'A':
    cinestecito=+1

if answer[29] == 'C':
    visual=+1
if answer[29] == 'B':
    auditivo=+1
if answer[29] == 'A':
    cinestecito=+1

if answer[30] == 'B':
    visual=+1
if answer[30] == 'A':
    auditivo=+1
if answer[30] == 'C':
    cinestecito=+1

if answer[31] == 'C':
    visual=+1
if answer[31] == 'A':
    auditivo=+1
if answer[31] == 'B':
    cinestecito=+1

if answer[32] == 'A':
    visual=+1
if answer[32] == 'C':
    auditivo=+1
if answer[32] == 'B':
    cinestecito=+1
    
if answer[33] == 'B':
    visual=+1
if answer[33] == 'A':
    auditivo=+1
if answer[33] == 'C':
    cinestecito=+1
    
if answer[34] == 'B':
    visual=+1
if answer[34] == 'C':
    auditivo=+1
if answer[34] == 'A':
    cinestecito=+1
    
if answer[35] == 'A':
    visual=+1
if answer[35] == 'C':
    auditivo=+1
if answer[35] == 'B':
    cinestecito=+1
    
if answer[36] == 'A':
    visual=+1
if answer[36] == 'B':
    auditivo=+1
if answer[36] == 'C':
    cinestecito=+1
    
if answer[37] == 'B':
    visual=+1
if answer[37] == 'C':
    auditivo=+1
if answer[37] == 'A':
    cinestecito=+1
    
if answer[38] == 'B':
    visual=+1
if answer[38] == 'C':
    auditivo=+1
if answer[38] == 'A':
    cinestecito=+1
    
if answer[39] == 'C':
    visual=+1
if answer[39] == 'A':
    auditivo=+1
if answer[39] == 'B':
    cinestecito=+1
    
#Presentamos por salida de texto el estilo de aprendizaje mas a fin al usuario predecido por el arbol de desicion 

if visual > auditivo and visual > cinestesico:
  print("Luego de a ver analizado la informacion hemos concluido que su estilo de aprendizaje predilecto es el VISUAL")

if auditivo > visual and auditivo > cinestesico:
  print("Luego de a ver analizado la informacion hemos concluido que su estilo de aprendizaje predilecto es el AUDITIVO")

if cinestesico > auditivo and cinestesico > visual:
  print("Luego de a ver analizado la informacion hemos concluido que su estilo de aprendizaje predilecto es el CINESTESICO")

#importamos la libreria necesaria para presentar la grafica 
import matplotlib.pyplot as plt

#Creacion de la grafica segun los porcentajes obtenidos 

estilosAprendizaje = [visual,auditivo,cinestesico]
nombres = ["Visual","Auditivo","Cinestesico"]
plt.pie(estilosAprendizaje, labels=nombres, autopct="%0.1f %%")
plt.axis("equal")
plt.show()