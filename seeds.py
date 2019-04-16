from app import app, db, bcrypt
from models.style import Style


with app.app_context():
    db.drop_all()
    db.create_all()

#Styles
ruffle_shoulder_dress = Style(
image_url='https://uk.louisvuitton.com/images/is/image/lv/1/PP_VP_AS/louis-vuitton--FGDS94JHP508_PM2_Front%20view.jpg?wid=382&hei=382',
shop_logo_img_url='https://ballzbeatz.com/wp-content/uploads/2018/01/Louis-Vuitton-Logo-V-Vinyl-Decal-Sticker.jpg',
price='£2960.00',
description='Combining several of this season\'s geometric prints into one design, the Print Patchwork Dress made from silk crepe de Chine is a true statement piece. It features long, rounded neckties, while ruffles at the shoulders and waist, as well as shoulder wings, add volume. The adjustable Monogram belt with canvas tips provides a personalised fit.')
db.session.add(ruffle_shoulder_dress)

db.session.commit()
