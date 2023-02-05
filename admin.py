from flask import Blueprint
from . import db
from .models import ProductCategory, Product, Order
import datetime

bp = Blueprint('admin', __name__, url_prefix='/admin/')

# function to put some seed data in the database


@bp.route('/dbseed/')
def dbseed():
    category1 = ProductCategory(
        name='Kids Travel Accessories', description='Explore our exclusive accessories brand from headphones to keychains', image='Accessories/Banner.jpg')
    category2 = ProductCategory(
        name='Apparel/Costume', description='Go adventuous with our aviation-themed apparel ranging from astronaut to crew costume.', image='Apparel/Banner.jpg')
    category3 = ProductCategory(
        name='Back-To-School', description='School season is coming! Grab a soarair bag tag and note book as your school companions!', image='BackToSchool/Banner.jpg')
    category4 = ProductCategory(
        name='Flight Comforts', description='Enjoy a comfy flight with Soarair kids pajamas, sleeping eye masks and other sleep essentials.', image='FlightComforts/Banner.jpg')
    category5 = ProductCategory(
        name='Kids Bags/Luggage', description='From zip backpacks to ride-on suitcases, your kid can enjoy a travel experience of their own.', image='Luggage/Banner.jpg')
    category6 = ProductCategory(
        name='Models & Toys', description='Kids lovable Soarair toy models. Treat your kids to a cuddly companion for this travel session.', image='ToyPlanes/Banner.jpg')

    try:
        db.session.add(category1)
        db.session.add(category2)
        db.session.add(category3)
        db.session.add(category4)
        db.session.add(category5)
        db.session.add(category6)
        db.session.commit()
    except:
        return 'There was an issue adding the categories in dbseed function'

    p1 = Product(category_id=category1.id, name='Soarair Kids Bluetooth Matte Touch Bass Stereo Wireless Headset Black',
                 description='Soarair Kids Bluetooth Headphones give kids the freedom to listen to their favorite tunes or watch movies completely cable free. With full Bluetooth control directly from the ear cup, these headphones allow you to play, pause, skip, rewind or adjust volume without touching the phone or play device.', price=59, points=10260, ageIntended=8, rating=2, date=datetime.datetime(2020, 5, 17), image1='Accessories/BlackHeadset1.jpg', image2='Accessories/BlackHeadset2.jpg')
    p2 = Product(category_id=category1.id, name='Travel Passport RFID Holder Accessories Kids Blue',
                 description='With The Pattern Of Australia Embossing Rfid Blocking, Prevent Personal Account Information Disclosure, get a passport holder for your kids!', price=33, points=7850, ageIntended=8, rating=5, date=datetime.datetime(2020, 5, 28), image1='Accessories/PassportHolder1.jpg', image2='Accessories/PassportHolder2.jpg')
    p3 = Product(category_id=category1.id, name='Lightweight Headphone with Microphone - Headset for Kids with Mic, Black',
                 description='Get the best for your childs travel with Soarair Headphones for Kids. With full Bluetooth control directly from the ear cup, these headphones allow you to play / pause / skip / rewind or adjust volume without touching the phone or play device.', price=96, points=15700, ageIntended=5, rating=3, date=datetime.datetime(2020, 4, 28), image1='Accessories/HeadphoneMic1.jpg', image2='Accessories/HeadphoneMic2.jpg')
    p4 = Product(category_id=category2.id, name='Kids Little Adventurer Rocket Jet Costume',
                 description='Complete your kids aviation costume with this fun-looking Rocket Costume. Pair it with your own pants and accessories for an out-of-this-world costume!', price=26, points=1400, ageIntended=5, rating=5, date=datetime.datetime(2021, 4, 28), image1='Apparel/Babyjet1.jpg', image2='Apparel/Babyjet2.jpg')
    p5 = Product(category_id=category2.id, name='Kids/Baby Soarair Logo Red Bamboo T-Shirts Small Size 6',
                 description='Super soft, eco friendly bamboo tshirts for baby, kids & teens with raw natural wave texture on tshirt featuring Soarair logo.', price=25, points=1205, ageIntended=4, rating=1, date=datetime.datetime(2022, 4, 28), image1='Apparel/RedT1.jpg', image2='Apparel/RedT2.jpg')
    p6 = Product(category_id=category2.id, name='Kids/Baby Soarair Logo White Bamboo T-Shirts Medium Size 8',
                 description='Super soft, eco friendly bamboo tshirts for baby, kids & teens with raw natural wave texture on tshirt featuring Soarair logo.', price=25, points=1205, ageIntended=4, rating=3, date=datetime.datetime(2018, 4, 22), image1='Apparel/WhiteT1.jpg', image2='Apparel/WhiteT2.jpg')
    p7 = Product(category_id=category3.id, name='Hardcover Spiral Bound A5 Notebook Blue for Kids',
                 description='Use this notebook journal to write down everything that pops into your head, may be travel ideas and notes. 150 sheets line paper, easy to peel off any pages.', price=48, points=1717, ageIntended=7, rating=2, date=datetime.datetime(2022, 1, 12), image1='BackToSchool/Notebook1.jpg', image2='BackToSchool/Notebook2.jpg')
    p8 = Product(category_id=category3.id, name='School Backpack Bag Arctic  Blue for Kids',
                 description='The backpack focuses on softness, design and the little fine details to make it stand out, perfect for carrying back to school.', price=29, points=1335, ageIntended=4, rating=3, date=datetime.datetime(2022, 3, 13), image1='BackToSchool/SchoolBag1.jpg', image2='BackToSchool/SchoolBag2.jpg')
    p9 = Product(category_id=category4.id, name='Black and Red Check Flight Blanket',
                 description='Snuggle up in this cosy, aesthetic and fluffy blanket,  perfect for car trips, camping, sleepovers or flights! The pattern is woven into the soft cotton fabric, and will look great on a bed or a couch.', price=52, points=2800, ageIntended=6, rating=5, date=datetime.datetime(2022, 3, 1), image1='FlightComforts/Blanket1.jpg', image2='FlightComforts/Blanket2.jpg')
    p10 = Product(category_id=category4.id, name='Face Mask Reusable Cotton Cloth Fabric W/ 2 Pm2.5 Perfect Fit Adjustable White Small for Kids',
                  description=' With 3 Layers texture provides effective antibacterial, antidust, prevent droplet and invasive bacteria, perfect for flight. One Size perfect fits most kids over 8.', price=19.78, points=1275, ageIntended=10, rating=3, date=datetime.datetime(2022, 3, 19), image1='FlightComforts/FaceMask1.jpg', image2='FlightComforts/FaceMask2.jpg')
    p11 = Product(category_id=category4.id, name='Pajama & Eye Mask Travel Set',
                  description='This Pajama and Eye Mask is a wonderful gift for those some classic contemporary styling on their pajama fit and want a cosy flight journey!', price=25.46, points=2855, ageIntended=2, rating=4, date=datetime.datetime(2021, 2, 13), image1='FlightComforts/PJSet1.jpg', image2='FlightComforts/PJSet2.jpg')
    p12 = Product(category_id=category4.id, name='Black and Red Check Slippers Size 3-4',
                  description='This gorgeous duo comes beautifully presented in a box decorated with further Me to You illustrations and the words - Take some time just for you, perfect wearables for a long-haul flight!', price=42.46, points=8300, ageIntended=8, rating=1, date=datetime.datetime(2021, 8, 18), image1='FlightComforts/Slippers1.jpg', image2='FlightComforts/Slippers2.jpg')
    p13 = Product(category_id=category5.id, name='16" Giraffe Hard Shell Suitcase',
                  description='With cute pattern and attractive appearance, the kids carry-on suitcase is popular with children. The durable ABS shell and premium frosted film promise long service time. Whats more, a luggage and a backpack add extra storage space and help you organize various items. Kids can move the suitcase anywhere due to the smooth casters. The retractable handle meets the needs of children with different heights. Start your exciting adventure with our luggage!', price=150, points=13350, ageIntended=6, rating=5, date=datetime.datetime(2022, 9, 23), image1='Luggage/AnimalLuggage1.jpg', image2='Luggage/AnimalLuggage2.jpg')
    p14 = Product(category_id=category5.id, name='Carry On 30L Kids Suitcase Boys Travel Trolley Luggage 4 Wheels Arctic',
                  description='A must-have suitcase for kids. Made of high-quality polycarbonate and ABS, these kids suitcases are extremely lightweight but durable. Waterproof and mirrored finish molded shell is hard enough to protect your kids stuff. With lovely cartoon design, your kids will love it at first sign, motivating them to pack their stuff independently. Featuring telescopic handle and 4 spinner wheels, it is convenient for kids to travel.', price=31.33, points=2835, ageIntended=5, rating=5, date=datetime.datetime(2022, 12, 13), image1='Luggage/BabySmallCarryon1.jpg', image2='Luggage/BabySmallCarryon2.jpg')
    p15 = Product(category_id=category5.id, name='19in Small 4 Wheel Hard Suitcase - White',
                  description='Made of durable and non-toxic materials, our luggage set ensures long-term use. The newly upgraded frosted protective film can effectively prevent scratches. The multi-level adjustable telescopic handle can meet the needs of children of different heights. Widened shoulder straps on the backpack can relieve the pressure on childrens shoulders.', price=140, points=1400, ageIntended=5, rating=4, date=datetime.datetime(2021, 12, 14), image1='Luggage/BlackSmallLuggage1.jpg', image2='Luggage/BlackSmallLuggage2.jpg')
    p16 = Product(category_id=category5.id, name='Kids LadyBird Ride On Suitcase Children Travel Luggage Carry Bag Trolley Wheel',
                  description='Travel through the airport with your kid on their very own ride on suitcase. Pull them along or let them use their feet to push along beside you. Travelling has never been so fun or cute. Fill your luggage bag up. Attach the strap. Place child on suitcase. Flip out feet stands. You are now ready for the first inaugural rideable suitcase championships. Compete with all other dads.', price=51.99, points=5299, ageIntended=6, rating=5, date=datetime.datetime(2020, 2, 13), image1='Luggage/LadyBirdRideOn1.jpg', image2='Luggage/LadyBirdRideOn2.jpg')
    p17 = Product(category_id=category6.id, name='Blue 48CM Foam Plane Glider',
                  description='The wind glider is an excellent party gift for family gatherings, birthday parties, childrens day parties, school parties, etc. Give children the best flying toy gifts, such as aviation and airplane themed parties, Christmas, Thanksgiving, Halloween, and gliders are also used as rewards for good behavior at home. The best gift for boys and girls.', price=21.99, points=4020, ageIntended=4, rating=4, date=datetime.datetime(2022, 7, 15), image1='ToyPlanes/FoamPlaneBlue1.jpg', image2='ToyPlanes/FoamPlaneBlue2.jpg')
    p18 = Product(category_id=category6.id, name='Purple 48CM Foam Plane Glider',
                  description='The wind glider is an excellent party gift for family gatherings, birthday parties, childrens day parties, school parties, etc. Give children the best flying toy gifts, such as aviation and airplane themed parties, Christmas, Thanksgiving, Halloween, and gliders are also used as rewards for good behavior at home. The best gift for boys and girls.', price=21.99, points=4020, ageIntended=4, rating=3, date=datetime.datetime(2022, 7, 15), image1='ToyPlanes/FoamPlanePurple1.jpg', image2='ToyPlanes/FoamPlanePurple2.jpg')
    p19 = Product(category_id=category6.id, name='Red 48CM Foam Plane Glider',
                  description='The wind glider is an excellent party gift for family gatherings, birthday parties, childrens day parties, school parties, etc. Give children the best flying toy gifts, such as aviation and airplane themed parties, Christmas, Thanksgiving, Halloween, and gliders are also used as rewards for good behavior at home. The best gift for boys and girls.', price=21.99, points=4020, ageIntended=4, rating=5, date=datetime.datetime(2022, 7, 15), image1='ToyPlanes/FoamPlaneRed1.jpg', image2='ToyPlanes/FoamPlaneRed2.jpg')
    p20 = Product(category_id=category6.id, name='Yellow 48CM Foam Plane Glider',
                  description='The wind glider is an excellent party gift for family gatherings, birthday parties, childrens day parties, school parties, etc. Give children the best flying toy gifts, such as aviation and airplane themed parties, Christmas, Thanksgiving, Halloween, and gliders are also used as rewards for good behavior at home. The best gift for boys and girls.', price=21.99, points=4020, ageIntended=4, rating=2, date=datetime.datetime(2022, 7, 15), image1='ToyPlanes/FoamPlaneYellow1.jpg', image2='ToyPlanes/FoamPlaneYellow2.jpg')
    p21 = Product(category_id=category6.id, name='Airplane Ride On/ Rocker with Wheels for Kids Red',
                  description='This versatile ride on Aeroplane can be turned into a rocking plane by simply attaching rocking base which is included. This ride on plane can be initially used with rocker base for children aged closer to 12 months and as your little one grows the rocker base can be removed and plane can be used as a ride-on strengthening little legs and help promote physical activity', price=570, points=40201, ageIntended=8, rating=1, date=datetime.datetime(2012, 7, 15), image1='ToyPlanes/LargePlaneRed1.jpg', image2='ToyPlanes/LargePlaneRed2.jpg')
    p22 = Product(category_id=category6.id, name='Retro LGS Biplane Red',
                  description='Large, natural timber and red, retro styled, bi-plane with stunt pilot driver and rubberised wheels. Beautiful, yet sturdy enough to play with.', price=1.99, points=100, ageIntended=1, rating=5, date=datetime.datetime(2022, 10, 3), image1='ToyPlanes/PlasticPlane1.jpg', image2='ToyPlanes/PlasticPlane2.jpg')
    p23 = Product(category_id=category6.id, name='Toy Plane Costume, Cardboard Easy Assembly, Pretend Play',
                  description='UNIQUE DESIGN: a nod to vintage plane design and unlike anything else in the neighborhood. Great for pilot costume or pretend play any day of the year!', price=180, points=57181, ageIntended=1, rating=1, date=datetime.datetime(2022, 1, 1), image1='ToyPlanes/WhiteCardboardPlane1.jpg', image2='ToyPlanes/WhiteCardboardPlane2.jpg')

    try:
        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.add(p4)
        db.session.add(p5)
        db.session.add(p6)
        db.session.add(p7)
        db.session.add(p8)
        db.session.add(p9)
        db.session.add(p10)
        db.session.add(p11)
        db.session.add(p12)
        db.session.add(p13)
        db.session.add(p14)
        db.session.add(p15)
        db.session.add(p16)
        db.session.add(p17)
        db.session.add(p18)
        db.session.add(p19)
        db.session.add(p20)
        db.session.add(p21)
        db.session.add(p22)
        db.session.add(p23)
        db.session.commit()
    except:
        return 'There was an issue adding a product in dbseed function'

    # i1 = Image(product_id=p1.id, name='Accessories/BlackHeadset1.jpg')
    # i2 = Image(product_id=p1.id, name='Accessories/BlackHeadset2.jpg')
    # i3 = Image(product_id=p1.id, name='Accessories/BlackHeadset3.jpg')
    # i4 = Image(product_id=p2.id, name='Accessories/PassportHolder1.jpg')
    # i5 = Image(product_id=p2.id, name='Accessories/PassportHolder2.jpg')
    # i6 = Image(product_id=p3.id, name='Accessories/HeadphoneMic1.jpg')
    # i7 = Image(product_id=p3.id, name='Accessories/HeadphoneMic2.jpg')
    # i8 = Image(product_id=p4.id, name='Apparel/Babyjet1.jpg')
    # i9 = Image(product_id=p4.id, name='Apparel/Babyjet2.jpg')
    # i10 = Image(product_id=p4.id, name='Apparel/Babyjet3.jpg')
    # i11 = Image(product_id=p5.id, name='Apparel/RedT1.jpg')
    # i12 = Image(product_id=p5.id, name='Apparel/RedT2.jpg')
    # i13 = Image(product_id=p5.id, name='Apparel/RedT3.jpg')
    # i14 = Image(product_id=p5.id, name='Apparel/RedT4.jpg')
    # i15 = Image(product_id=p5.id, name='Apparel/RedT5.jpg')
    # i16 = Image(product_id=p6.id, name='Apparel/WhiteT1.jpg')
    # i17 = Image(product_id=p6.id, name='Apparel/WhiteT2.jpg')
    # i18 = Image(product_id=p6.id, name='Apparel/WhiteT3.jpg')
    # i19 = Image(product_id=p7.id, name='BackToSchool/Notebook1.jpg')
    # i20 = Image(product_id=p7.id, name='BackToSchool/Notebook2.jpg')
    # i21 = Image(product_id=p7.id, name='BackToSchool/Notebook3.jpg')
    # i22 = Image(product_id=p8.id, name='BackToSchool/SchoolBag1.jpg')
    # i23 = Image(product_id=p8.id, name='BackToSchool/SchoolBag2.jpg')
    # i24 = Image(product_id=p8.id, name='BackToSchool/SchoolBag3.jpg')
    # i25 = Image(product_id=p9.id, name='FlightComforts/Blanket1.jpg')
    # i26 = Image(product_id=p9.id, name='FlightComforts/Blanket2.jpg')
    # i27 = Image(product_id=p9.id, name='FlightComforts/Blanket3.jpg')
    # i28 = Image(product_id=p10.id, name='FlightComforts/FaceMask1.jpg')
    # i29 = Image(product_id=p10.id, name='FlightComforts/FaceMask2.jpg')
    # i30 = Image(product_id=p11.id, name='FlightComforts/PJSet1.jpg')
    # i31 = Image(product_id=p11.id, name='FlightComforts/PJSet2.jpg')
    # i32 = Image(product_id=p11.id, name='FlightComforts/PJSet3.jpg')
    # i33 = Image(product_id=p12.id, name='FlightComforts/Slippers1.jpg')
    # i34 = Image(product_id=p12.id, name='FlightComforts/Slippers2.jpg')
    # i35 = Image(product_id=p13.id, name='Luggage/AnimalLuggage1.jpg')
    # i36 = Image(product_id=p13.id, name='Luggage/AnimalLuggage2.jpg')
    # i37 = Image(product_id=p13.id, name='Luggage/AnimalLuggage3.jpg')
    # i38 = Image(product_id=p14.id, name='Luggage/BabySmallCarryon1.jpg')
    # i39 = Image(product_id=p14.id, name='Luggage/BabySmallCarryon2.jpg')
    # i40 = Image(product_id=p14.id, name='Luggage/BabySmallCarryon3.jpg')
    # i41 = Image(product_id=p15.id, name='Luggage/BlackSmallLuggage1.jpg')
    # i42 = Image(product_id=p15.id, name='Luggage/BlackSmallLuggage2.jpg')
    # i43 = Image(product_id=p15.id, name='Luggage/BlackSmallLuggage3.jpg')
    # i44 = Image(product_id=p15.id, name='Luggage/BlackSmallLuggage4.jpg')
    # i45 = Image(product_id=p16.id, name='Luggage/LadyBirdRideOn1.jpg')
    # i46 = Image(product_id=p16.id, name='Luggage/LadyBirdRideOn2.jpg')
    # i47 = Image(product_id=p16.id, name='Luggage/LadyBirdRideOn2.jpg')
    # i48 = Image(product_id=p17.id, name='ToyPlanes/FoamPlaneBlue1.jpg')
    # i49 = Image(product_id=p17.id, name='ToyPlanes/FoamPlaneBlue2.jpg')
    # i50 = Image(product_id=p18.id, name='ToyPlanes/FoamPlanePurple1.jpg')
    # i51 = Image(product_id=p18.id, name='ToyPlanes/FoamPlanePurple2.jpg')
    # i52 = Image(product_id=p18.id, name='ToyPlanes/FoamPlanePurple3.jpg')
    # i53 = Image(product_id=p19.id, name='ToyPlanes/FoamPlaneRed1.jpg')
    # i54 = Image(product_id=p19.id, name='ToyPlanes/FoamPlaneRed2.jpg')
    # i55 = Image(product_id=p19.id, name='ToyPlanes/FoamPlaneRed3.jpg')
    # i56 = Image(product_id=p20.id, name='ToyPlanes/FoamPlaneYellow1.jpg')
    # i57 = Image(product_id=p20.id, name='ToyPlanes/FoamPlaneYellow2.jpg')
    # i58 = Image(product_id=p20.id, name='ToyPlanes/FoamPlaneYellow3.jpg')
    # i59 = Image(product_id=p21.id, name='ToyPlanes/LargePlaneRed1.jpg')
    # i60 = Image(product_id=p21.id, name='ToyPlanes/LargePlaneRed2.jpg')
    # i61 = Image(product_id=p21.id, name='ToyPlanes/LargePlaneRed3.jpg')
    # i62 = Image(product_id=p22.id, name='ToyPlanes/PlasticPlane1.jpg')
    # i63 = Image(product_id=p22.id, name='ToyPlanes/PlasticPlane2.jpg')
    # i64 = Image(product_id=p22.id, name='ToyPlanes/PlasticPlane3.jpg')
    # i65 = Image(product_id=p22.id, name='ToyPlanes/PlasticPlane4.jpg')
    # i66 = Image(product_id=p23.id, name='ToyPlanes/WhiteCardboardPlane1.jpg')
    # i67 = Image(product_id=p23.id, name='ToyPlanes/WhiteCardboardPlane2.jpg')
    # i68 = Image(product_id=p23.id, name='ToyPlanes/WhiteCardboardPlane3.jpg')

    # try:
    #     db.session.add(i1)
    #     db.session.add(i2)
    #     db.session.add(i3)
    #     db.session.add(i4)
    #     db.session.add(i5)
    #     db.session.add(i6)
    #     db.session.add(i7)
    #     db.session.add(i8)
    #     db.session.add(i9)
    #     db.session.add(i10)
    #     db.session.add(i11)
    #     db.session.add(i12)
    #     db.session.add(i13)
    #     db.session.add(i14)
    #     db.session.add(i15)
    #     db.session.add(i16)
    #     db.session.add(i17)
    #     db.session.add(i18)
    #     db.session.add(i19)
    #     db.session.add(i20)
    #     db.session.add(i21)
    #     db.session.add(i22)
    #     db.session.add(i23)
    #     db.session.add(i24)
    #     db.session.add(i25)
    #     db.session.add(i26)
    #     db.session.add(i27)
    #     db.session.add(i28)
    #     db.session.add(i29)
    #     db.session.add(i30)
    #     db.session.add(i31)
    #     db.session.add(i32)
    #     db.session.add(i33)
    #     db.session.add(i34)
    #     db.session.add(i35)
    #     db.session.add(i36)
    #     db.session.add(i37)
    #     db.session.add(i38)
    #     db.session.add(i39)
    #     db.session.add(i40)
    #     db.session.add(i41)
    #     db.session.add(i42)
    #     db.session.add(i43)
    #     db.session.add(i44)
    #     db.session.add(i45)
    #     db.session.add(i46)
    #     db.session.add(i47)
    #     db.session.add(i48)
    #     db.session.add(i49)
    #     db.session.add(i50)
    #     db.session.add(i51)
    #     db.session.add(i52)
    #     db.session.add(i53)
    #     db.session.add(i54)
    #     db.session.add(i55)
    #     db.session.add(i56)
    #     db.session.add(i57)
    #     db.session.add(i58)
    #     db.session.add(i59)
    #     db.session.add(i60)
    #     db.session.add(i61)
    #     db.session.add(i62)
    #     db.session.add(i63)
    #     db.session.add(i64)
    #     db.session.add(i65)
    #     db.session.add(i66)
    #     db.session.add(i67)
    #     db.session.add(i68)
    #     db.session.commit()
    # except:
    #     return 'There was an issue adding an image in dbseed function'
    return 'DATA LOADED'
