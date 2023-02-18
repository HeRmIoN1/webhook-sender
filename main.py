from discordwebhook import Discord
#you'r webhook
discord = Discord(url="")
discord.post(
    embeds=[
        {
            "author": {
              #Your Embad name
                "name": "Hermione",
              #your name url
                "url": "",
              #your icon url
                "icon_url": "https://cdn.discordapp.com/attachments/1062044473368006666/1076195135521566841/53e1d2474c53a814f1dc8460962e33791c3ad6e04e50744074267bd29e45c4_640.jpg",
            },
          #your title name
            "title": "Hermione",
          #your Embad description , Field name
            "description": "Embed description",
            "fields": [
                {"name": "Field Name 1", "value": "Value 1", "inline": True},
                {"name": "Field Name 2", "value": "Value 2", "inline": True},
                {"name": "Field Name 3", "value": "Field Value 3"},
            ],
          #your tumbnail , image url , footer name and icon url
            "thumbnail": {"url": "https://cdn.discordapp.com/attachments/1062044473368006666/1076195135521566841/53e1d2474c53a814f1dc8460962e33791c3ad6e04e50744074267bd29e45c4_640.jpg"},
            "image": {"url": "https://cdn.discordapp.com/attachments/1062044473368006666/1076195135521566841/53e1d2474c53a814f1dc8460962e33791c3ad6e04e50744074267bd29e45c4_640.jpg"},
            "footer": {
                "text": "Embed Footer",
                "icon_url": "https://cdn.discordapp.com/attachments/1062044473368006666/1076195135521566841/53e1d2474c53a814f1dc8460962e33791c3ad6e04e50744074267bd29e45c4_640.jpg",
            },
        }
    ],
)
#by hermione
