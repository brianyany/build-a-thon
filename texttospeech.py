import pyttsx3

engine = pyttsx3.init(driverName='sapi5')
engine.say("The temperature is seventy degree")
engine.runAndWait()



# import talkey
# tts = talkey.Talkey(
#     preferred_languages=['en', 'af', 'el', 'fr'],

#     preferred_factor=80.0,


#     engine_preference=['espeak'],


#     espeak={
 
#         'options': {
#             'enabled': True,
#         },


#         'defaults': {
#                 'words_per_minute': 150,
#                 'variant': 'f4',
#         },


#         'languages': {
#             'en': {
#                 'voice': 'english-mb-en1',
#                 'words_per_minute': 130
#             },
#         }
#     }
# )
# tts.say('Steven, its all over for you')