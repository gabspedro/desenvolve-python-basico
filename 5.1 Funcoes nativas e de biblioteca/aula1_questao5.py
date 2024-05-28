import emoji

print("Emojis Disponíveis:")
print("\n")

print("❤️  - :red_heart:")
print("😈 - :smiling_face_with_horns:")
print("🫥  - :dotted_line_face:")
print("🥺 - :pleading_face:")
print("😱 - :face_screaming_in_fear:")
print("\n")

emoji = str(emoji.emojize(input("Escolha o ': :' do Emoji para Emojificar Ele: ")))

if emoji == ":red_heart:":
    print(emoji.emojize('Olá Mundo!!!! :red_heart::red_heart::red_heart::red_heart:'))
elif emoji == ":smiling_face_with_horns:":
    print(emoji.emojize('Oii Mundo RsRs! :smiling_face_with_horns::smiling_face_with_horns:'))
elif emoji == ":dotted_line_face:":
    print(emoji.emojize('Oi Mundo :dotted_line_face:'))
elif emoji == ":pleading_face:":
    print(emoji.emojize('Oii Mundo... Então né kkkk :pleading_face:'))
elif emoji == ":face_screaming_in_fear:":
    print(emoji.emojize('Mundo??? OLÀÁÁ! :face_screaming_in_fear:'))
else:
    print("O ': ;' Informado está Incorreto!")