from app import app, db, bcrypt
from models.style import Style
from models.find import Find


with app.app_context():
    db.drop_all()
    db.create_all()

#Finds
colletta_printed_dress = Find(
image_url='https://media.frenchconnection.com/ms/fcuk/71lik-womens-cr-brightflamemulti-coletta-printed-dress.jpg?404=fcuk/71lik.jpg&width=425&height=637',
shop_logo_img_url='http://www.stickpng.com/assets/images/5a1aca8bf65d84088faf1392.png',
price='£85.00',
description='A bold red hue offers a striking backdrop to vibrant flowers on the Coletta Crepe Floral Dress. The short sleeved dress has a flattering, flowing shape with a wrap front and tie waistband. Covered in a colourful floral pattern, the dress is perfect for special occasions this summer, paired with heels or with trainers for a casual off-duty style.'
)
db.session.add(colletta_printed_dress)

cadencia_crepe_dress = Find(
image_url='https://media.frenchconnection.com/ms/fcuk/71lfa-womens-fu-lightsweetpeamulti-cadencia-crepe-short-floral-dress.jpg?404=fcuk/71lfa.jpg&width=425&height=637',
shop_logo_img_url='http://www.stickpng.com/assets/images/5a1aca8bf65d84088faf1392.png',
price='£95.00',
description='From work to the weekend, the Cadencia Floral Dress is a pretty summer favourite. The light, short dress has a flattering look with a V neckline and short, fluted sleeves. Covered in a fast floral print and finished with ruffle trims, the dress is perfect for pairing with heels or trainers for a more casual look.'
)
db.session.add(cadencia_crepe_dress)

#Styles
ruffle_shoulder_dress = Style(
image_url='https://uk.louisvuitton.com/images/is/image/lv/1/PP_VP_AS/louis-vuitton--FGDS94JHP508_PM2_Front%20view.jpg?wid=382&hei=382',
shop_logo_img_url='https://ballzbeatz.com/wp-content/uploads/2018/01/Louis-Vuitton-Logo-V-Vinyl-Decal-Sticker.jpg',
price='£2960.00',
description='Combining several of this season\'s geometric prints into one design, the Print Patchwork Dress made from silk crepe de Chine is a true statement piece. It features long, rounded neckties, while ruffles at the shoulders and waist, as well as shoulder wings, add volume. The adjustable Monogram belt with canvas tips provides a personalised fit.',
finds=[colletta_printed_dress, cadencia_crepe_dress]
)
db.session.add(ruffle_shoulder_dress)


db.session.commit()
