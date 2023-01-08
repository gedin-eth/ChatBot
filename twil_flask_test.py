from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import os
import openai
import random
import requests
from bs4 import BeautifulSoup



openai.api_key = "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"

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    
    

    topic = body.split(":",1)
    if len(topic)> 1:
        tweet = topic[1]

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == 'Yee':
        resp.message("The fool doth think he is wise, but the wise man knows himself to be a fool.")
    elif topic[0] == 'Tweet':


        text = "Generate 3 tweets about " + tweet + ", they should have all the components of a viral tweet";
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=text,
            temperature=0,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
        

        response_text = response.get('choices')[0]['text']
        resp.message(response_text)
    elif topic[0] == 'Date':
        question = "Can you send a flirty response to a person I want to date? They messaged the quote below '" + tweet + "'";

        response = openai.Completion.create(
          model="text-davinci-002",
          prompt=question,
          temperature=0.7,
          max_tokens=256,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
        )
        
        response_text = response.get('choices')[0]['text']
        resp.message(response_text)
    elif topic[0] == 'Text':
        question = tweet + '?';

        response = openai.Completion.create(
          model="text-davinci-002",
          prompt=question,
          temperature=0.7,
          max_tokens=256,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
        )
        response_text = response.get('choices')[0]['text']
        resp.message(response_text)
    elif topic[0] == 'Date':
        question = tweet + '?';

        response = openai.Completion.create(
          model="text-davinci-002",
          prompt=question,
          temperature=0.7,
          max_tokens=256,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
        )
        
        response_text = response.get('choices')[0]['text']
        resp.message(response_text)
    elif (body == 'Titz' or body == 'titz' or body == 'Titties' or body == 'titties' or body == 'Tits' or body == 'tits') :
        random_number = random.randint(1, 10)
        print(random_number)
        switch = {
            1: "Ask, and it shall be given, https://i.pinimg.com/originals/8d/fd/3a/8dfd3ab45f437005b6b65b9ee157a444.jpg",
            2: "Ask, and it shall be given, https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSG2ru3CiiN0yGonSuOMm5jVBRs_-dV2kO9aQ&usqp=CAU",
            3: "Ask, and it shall be given, https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkhTUZE7lkaaGnYvrmZuNVxYoCGQVzB3-rFA&usqp=CAU",
            4: "Ask, and it shall be given, https://i2-prod.mirror.co.uk/incoming/article24594237.ece/ALTERNATES/n310p/1_PAY-My-massive-boobs-ruined-my-life-but-now-I-love-them-Model-reveals-how-her-34K-chest-almost-got-h.jpg",
            5: "Ask, and it shall be given, https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1426235762l/25132912.jpg",
            6: "Ask, and it shall be given, https://pbs.twimg.com/media/FW8_dSPUUAESgJv?format=jpg&name=900x900",
            7: "Ask, and it shall be given, https://www.the-sun.com/wp-content/uploads/sites/6/2022/06/b6bd65ec-30d3-4d38-9b82-c1433bfcf74b.jpg",
            8: "Ask, and it shall be given, https://www.washingtonpost.com/wp-apps/imrs.php?src=https://arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/XVCQMIHEXYI6XCGFJ7LDQLCHZM.jpg&w=1440",
            9: "Ask, and it shall be given, https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSpPoFVVpG82zAwmTDd-M7PTOAA5hhHrcZf_A&usqp=CAU",
            10:"Ask, and it shall be given, https://media-exp1.licdn.com/dms/image/C4E03AQGEg0tVxRKzRA/profile-displayphoto-shrink_800_800/0/1607103632694?e=2147483647&v=beta&t=RiYnNezjmKGFoW60wKOV-ccyFelP38qQ61OLQI0VFC8"
            }
        
        resp.message(switch[random_number])
        
      
    elif body == 'BIP':
        # get the web page
        page = requests.get('https://realitysteve.com/category/bachelor-in-paradise-8-spoilers/')

        # create a BeautifulSoup object
        soup = BeautifulSoup(page.content, 'html.parser')

        # find the latest Bachelor ABC series news
        news_items = soup.find_all('div', class_='blog-widget-text left relative')

        # print news
        lnews = []
        for news in news_items:
            lnews.append('article: ' + news.find('h1').get_text())
            print(news.find('h1').get_text())

        loot = lnews.append('all articles can be found at: https://realitysteve.com/category/bachelor-in-paradise-8-spoilers')
        print(lnews)
        resp.message(str(lnews))
        
    elif body == 'Yup':
        resp.message("Whenever you find yourself on the side of the majority, it is time to reform (or pause and reflect).")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
