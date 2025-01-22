from dotenv import load_dotenv
import os
import requests, json

 # import namespaces
from azure.ai.translation.text import *
from azure.ai.translation.text.models import InputTextItem

def main():
    global translator_endpoint
    global cog_key
    global cog_region
    
    try:
        # Get Configuration Settings
        load_dotenv()
        cog_key = os.getenv('COG_SERVICE_KEY')
        cog_region = os.getenv('COG_SERVICE_REGION')
        translator_endpoint = 'https://api.cognitive.microsofttranslator.com'

        # Create client using endpoint and key
        credential = TranslatorCredential(cog_key, cog_region)
        client = TextTranslationClient(credential)

        # Analyze each text file in the reviews folder
        reviews_folder = 'reviews'
        for file_name in os.listdir(reviews_folder):
            # Read the file contents
            print('\n-------------\n' + file_name)
            text = open(os.path.join(reviews_folder, file_name), encoding='utf8').read()
            print('\n' + text)

            # Detect the language
            language = GetLanguage(client, text)
            print('Language:',language)

            # Translate if not already English
            if language != 'en':
                translation = Translate(client, text, language)
                print("\nTranslation:\n{}".format(translation))
                
    except Exception as ex:
        print(ex)

def GetLanguage(client, text):
    # Default language is English
    language = 'en'

    # Use the Azure AI Translator detect function


    # Return the language
    return language

def Translate(client, text, source_language):
    translation = ''

     # Choose target language
    languagesResponse = client.get_languages(scope="translation")
    print("{} languages supported.".format(len(languagesResponse.translation)))
    print("(See https://learn.microsoft.com/azure/ai-services/translator/language-support#translation)")
    print("Enter a target language code for translation (for example, 'en'):")
    targetLanguage = "xx"
    supportedLanguage = False
    while supportedLanguage == False:
        targetLanguage = input()
        if  targetLanguage in languagesResponse.translation.keys():
            supportedLanguage = True
        else:
            print("{} is not a supported language.".format(targetLanguage))

    # Return the translation
    return translation

if __name__ == "__main__":
    main()