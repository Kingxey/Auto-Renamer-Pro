

class Scripts():
    
    PROGRESS_BAR = """\n
<b>» ᴛᴀɪʟʟᴇ</b> : {1} | {2}  
<b>» ꜰᴀɪᴛ</b> : {0}%  
<b>» ᴠɪᴛᴇssᴇ</b> : {3}/s  
<b>» ᴇᴛᴀ</b> : {4}"""

    START_TXT = """
<b><blockquote> Salut! {}  </blockquote>

Je suis Yor Forger, connue sous le nom de princesse Hibara 👸,|| et aussi l'épouse de Kingcey 🌀.||

Tout comme je protège ceux qui me sont chers 💖, je vais m'assurer que vos fichiers soient renommés avec précision et style 🎨.  
Ajoutez une légende personnalisée 📝, une miniature élégante ✨ et laissez-moi séquencer vos fichiers à la perfection 📁. 
</b>
"""
    FILE_NAME_TXT = """<b>» <u>Configurer le format de renommage automatique</u></b>

<b>Variables :</b>
➲ `episode` - Pour remplacer le numéro de l'épisode 
➲ `saison` - Pour remplacer le numéro de la saison
➲ `quality` - Pour remplacer la qualité    

<b>‣ Voici un exemple :- </b> <code> /autorename Spy X family [Ssaison - EPepisode - [Quality] [Dual] @KGCAnime </code>

<b>‣ /autorename : Renommez vos fichiers multimédia en incluant les variables 'épisode' et 'qualité' dans votre texte, pour extraire l'épisode et la qualité présents dans le nom de fichier original.</b>"""


    ABOUT_TXT = f"""<b>❍ JE suis : <a href="https://t.me/Auto_Renamer_Zbot">Princesse Hibara</a>  
❍ Développeur : <a href="https://t.me/Kingcey"> ◡̈⃝ㅤ🇰ιηg¢єу</a>   
❍ Language : <a href="https://www.python.org/">Python</a>  
❍ DATA-BASE : <a href="https://www.mongodb.com/">MONGO-DB</a>  
❍ Serveur : <a href="https://t.me/hyoshassistantbot">Octeko</a>  
❍ Canal D'anime : <a href="https://t.me/KGCAnime">KGCAnime</a>  

➻ Cliquez sur les boutons ci-dessous pour obtenir de l'aide et des informations basiques sur moi.</b>"""


    THUMBNAIL_TXT = """<b><u>» Pour définir une miniature personnalisée.</u></b>
    
➲ /start : Envoyez n'importe quelle photo pour la définir automatiquement comme miniature.
➲ /del_thumb : Utilisez cette commande pour supprimer votre ancienne miniature.
➲ /view_thumb : Utilisez cette commande pour voir votre miniature actuelle.

Note : Si aucune miniature n'est enregistrée dans le bot, la miniature du fichier original sera utilisée pour le fichier renommé."""

    CAPTION_TXT = """<b><u>» Pour définir une légende personnalisée et le type de média.</u></b>
    
<b>Variables :</b>         
TAILLES: <code>{filesize}</code>  
DUREE: <code>{duration}</code>  
NOM: <code>{filename}</code>

➲ /set_caption : Pour définir une légende personnalisée.  
➲ /see_caption : Pour voir votre légende personnalisée.  
➲ /del_caption : Pour supprimer votre légende personnalisée.

» Par exemple : - /set_caption nom de fichier: {filename}"""


    PROGRESS_BAR = """\n
<b>» TAILLE</b> : {1} | {2}  
<b>» Pourcentage</b> : {0}%  
<b>» Vitesse</b> : {3}/s  
<b>» Temps</b> : {4}"""


    DONATE_TXT = """Nous croyons en un monde meilleur, et avec votre aide, nous pouvons y parvenir. 🌍💖 Chaque contribution, quel que soit son montant, compte énormément pour nous ! Que vous puissiez donner 1€, 10€, ou même plus, chaque geste compte et nous rapproche un peu plus de notre objectif. 🙏✨

💻📱 C'est tellement simple de faire un don ! Que vous soyez confortablement installé chez vous avec votre ordinateur ou en déplacement avec votre téléphone, le processus de don est rapide et sécurisé. En quelques clics, vous pouvez faire partie de quelque chose de grand. 💫

💙 Pourquoi donner ? Votre soutien nous permet de financer des projets essentiels, d'aider ceux qui en ont besoin et de promouvoir des initiatives qui ont un véritable impact dans notre communauté. Grâce à des donations comme la vôtre, nous pouvons offrir des ressources, des formations et un soutien aux personnes qui en ont le plus besoin. 🎁✨

🤝 Rejoignez notre communauté ! En faisant un don, vous ne vous contentez pas de soutenir une cause : vous rejoignez une communauté de personnes passionnées et engagées, prêtes à faire la différence ensemble. Plus nous sommes nombreux, plus notre impact est puissant ! 💪🌈

📣 Ne sous-estimez jamais le pouvoir de votre don ! Chaque euro compte et peut façonner des vies ! Faites un don aujourd'hui et devenez un acteur du changement ! 🙌🌷 

Merci infiniment pour votre générosité et votre soutien. Vous êtes essentiel à notre mission !
Le pouvoir de votre don Nous aidera à maintenir tous nos bots actifs  ❤️
Merci infinement"""


    PREMIUM_TXT = """<b>Améliorez notre service premium et profitez de fonctionnalités exclusives :  
○ Renommage illimité : renommez autant de fichiers que vous le souhaitez sans aucune restriction.  
○ Accès anticipé : soyez le premier à tester et utiliser nos dernières fonctionnalités avancées avant tout le monde.

• Utilisez /plan pour voir tous nos plans en une fonction échelle.

➲ Première étape : payer le montant correspondant à votre plan préféré.  

➲ Deuxième étape : prenez une capture d'écran de votre paiement et partagez-la directement ici : @Kingcey  

➲ Alternative : ou téléchargez la capture d'écran ici et répondez avec la commande /bought.

Votre plan premium sera activé après vérification.</b>"""


    PREPLANS_TXT = """<b>👋 Sᴀʟᴜᴛ,

🎖️ <u>ᴘʟᴀɴs ᴅɪsᴘᴏɴɪʙʟᴇs</u> :

Tarification :  
➜ Premium mensuel : 3.99$ / mois  
➜ Premium quotidien : 0.99 / jour  
➜ Pour l'hébergement de bot : contactez @Kingcey  

➲ Payer ici - <code> @Kingcey </code>

‼️Tᴇ́ʟᴇᴄʜargᴇʀ ʟᴀ cᴀᴘᴛᴜʀᴇ ᴅᴇ ʟ'ecrᴀn ᴅᴜ ᴘᴀʏᴇᴍᴇɴᴛ ɪᴄɪ ᴇᴛ ʀᴇᴘᴏɴᴅᴇᴢ ᴀᴠᴇᴄ lᴀ cᴏᴍᴍᴀɴᴅᴇ /bought.</b>"""


    HELP_TXT = """<b>Voici le menu d'aide avec les commandes importantes :

Fonctionnalités impressionnantes🫧

Le bot de renommage est un outil pratique qui vous aide à renommer et gérer vos fichiers facilement.

➲ /autorename : renommer automatiquement vos fichiers.  
➲ /metadata : commandes pour activer/désactiver les métadatas.  
➲ /help : obtenir de l'aide rapide.  
➲ /set_dump : pour définir le canal à dumper (où vos fichiers seront envoyés une fois renommés).

Nb : Assurez-vous d'activer le mode séquentiel pour que le bot puisse trier et envoyer les fichiers dans le bon ordre."""


    SEND_METADATA = """
<b>-- Paramètres des métadatas.--</b>

➜ /metadata : Activer ou supprimer les métadatas.

**Description** : Les métadatas vont modifier les fichiers vidéo MKV, y compris tous les titres audio, streams et sous-titres.""" 


    SOURCE_TXT = """
<b>Salut,
  Jᴇ sᴜɪs ᴜɴ bᴏᴛ ᴅᴇ ʀᴇɴᴏᴍᴍᴀɢᴇ ᴀᴜᴛᴏᴍᴀᴛɪǫᴜᴇ,
ᴜɴ bᴏᴛ ᴛᴇʟᴇɢʀᴀᴍ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ ᴅᴇ ʀᴇɴᴏᴍᴍᴀɢᴇ ᴀᴜᴛᴏᴍᴀᴛɪǫᴜᴇ.</b>

ᴇᴄʀɪᴛ ᴇɴ ᴘʏᴛʜᴏɴ ᴀᴠᴇᴄ ʟ'ᴀɪᴅᴇ ᴅᴇ :
[Pyrogram](https://github.com/pyrogram/pyrogram)
[Python-Telegram-Bot](https://github.com/python-telegram-bot/python-telegram-bot)
ᴇᴛ ᴜᴛɪʟɪsᴀɴᴛ [Mongo](https://cloud.mongodb.com) cᴏᴍᴇ ʙᴀsᴇ ᴅᴇ ᴅᴏɴᴎᴇᴇᴇᴏᴠᴇᴇ

<b>Voici mon cᴏᴅᴇ sᴏᴜʀᴄᴇ :</b> [GitHub](https://github.com/kalebavincent/autorenamebot)

ʟᴇ bᴏᴛ ᴅᴇ ʀᴇɴᴏᴍᴍᴀɢᴇ ᴀᴜᴛᴏᴍᴀᴛɪǫᴜᴇ ᴇsᴛ sᴏᴜʀ ʟɪᴄᴇɴᴄᴇ [MIT](https://github.com/kalebavincent/autorenamebot/blob/main/LICENSE).
© 2025 | [Support Chat](https://t.me/tout_manga_confondu), ᴛᴏᴜs ᴅʀᴏɪᴛs ʀéserᴠéᴇᴇᴇ
""" 





Txt = Scripts()
