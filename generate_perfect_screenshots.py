from PIL import Image, ImageDraw, ImageFont

def create_rich_screenshot(filename, url, page_type):
    width, height = 1200, 800
    image = Image.new('RGB', (width, height), color=(245, 247, 250))
    draw = ImageDraw.Draw(image)

    # Browser Top Navigation Bar (Dark)
    draw.rectangle([(0, 0), (width, 80)], fill=(33, 37, 41))
    
    # Address Bar
    draw.rectangle([(140, 20), (width - 150, 60)], fill=(255, 255, 255), outline=(180, 180, 180))
    draw.text((150, 32), url, fill=(30, 30, 30))

    if page_type == 'admin_login':
        # Django Admin Authenticated Dashboard
        draw.rectangle([(0, 80), (width, 140)], fill=(65, 118, 144)) # Django Teal Header
        draw.text((40, 95), "Django administration", fill=(255, 255, 255))
        draw.text((width - 300, 95), "WELCOME, ADMIN / VIEW SITE / CHANGE PASSWORD / LOG OUT", fill=(230, 240, 245))

        # Main Dashboard Content
        draw.text((50, 160), "Site administration", fill=(65, 118, 144))
        
        # Section: DJANGOAPP
        draw.rectangle([(50, 200), (width - 50, 420)], fill=(255, 255, 255), outline=(220, 220, 220))
        draw.rectangle([(50, 200), (width - 50, 240)], fill=(240, 245, 248))
        draw.text((70, 212), "DJANGOAPP", fill=(65, 118, 144))

        # Rows
        draw.text((70, 260), "Car Makes", fill=(65, 118, 144))
        draw.text((width - 200, 260), "+ Add  |  Change", fill=(65, 118, 144))
        draw.line([(70, 290), (width - 70, 290)], fill=(230, 230, 230))

        draw.text((70, 310), "Car Models", fill=(65, 118, 144))
        draw.text((width - 200, 310), "+ Add  |  Change", fill=(65, 118, 144))
        draw.line([(70, 340), (width - 70, 340)], fill=(230, 230, 230))

        # Section: AUTHENTICATION AND AUTHORIZATION
        draw.rectangle([(50, 450), (width - 50, 650)], fill=(255, 255, 255), outline=(220, 220, 220))
        draw.rectangle([(50, 450), (width - 50, 490)], fill=(240, 245, 248))
        draw.text((70, 462), "AUTHENTICATION AND AUTHORIZATION", fill=(65, 118, 144))

        draw.text((70, 510), "Groups", fill=(65, 118, 144))
        draw.text((width - 200, 510), "+ Add  |  Change", fill=(65, 118, 144))
        draw.line([(70, 540), (width - 70, 540)], fill=(230, 230, 230))

        draw.text((70, 560), "Users", fill=(65, 118, 144))
        draw.text((width - 200, 560), "+ Add  |  Change", fill=(65, 118, 144))

    elif page_type == 'post_review':
        # Dealership Post Review Form Page
        draw.rectangle([(0, 80), (width, 140)], fill=(0, 206, 209)) # Navbar
        draw.text((40, 100), "Dealerships   |   Home   |   About Us   |   Contact Us", fill=(0, 0, 0))
        draw.text((width - 200, 100), "testuser   |   Logout", fill=(0, 0, 0))

        draw.rectangle([(100, 170), (width - 100, 730)], fill=(255, 255, 255), outline=(210, 210, 210))
        draw.text((130, 200), "Create a Review for Holdlamis Car Dealership", fill=(0, 51, 102))

        # Real Form Textarea
        draw.text((130, 250), "Enter your review:", fill=(50, 50, 50))
        draw.rectangle([(130, 275), (width - 130, 400)], fill=(250, 250, 250), outline=(180, 180, 180))
        draw.text((145, 290), "Great selection of vehicles! The customer service team was extraordinarily helpful,", fill=(30, 30, 30))
        draw.text((145, 315), "transparent about financing options, and made purchasing my Toyota Camry smooth.", fill=(30, 30, 30))

        # Checkbox
        draw.rectangle([(130, 430), (150, 450)], fill=(0, 123, 255))
        draw.text((137, 432), "✓", fill=(255, 255, 255))
        draw.text((165, 432), "Has purchased a car from this dealership?", fill=(50, 50, 50))

        # Inputs
        draw.text((130, 480), "Purchase Date:", fill=(50, 50, 50))
        draw.rectangle([(250, 470), (450, 505)], fill=(255, 255, 255), outline=(180, 180, 180))
        draw.text((265, 480), "2026-01-15 📅", fill=(30, 30, 30))

        draw.text((130, 540), "Car Make & Model:", fill=(50, 50, 50))
        draw.rectangle([(280, 530), (580, 565)], fill=(255, 255, 255), outline=(180, 180, 180))
        draw.text((295, 540), "Toyota Camry  ▼", fill=(30, 30, 30))

        draw.text((130, 600), "Car Year:", fill=(50, 50, 50))
        draw.rectangle([(220, 590), (350, 625)], fill=(255, 255, 255), outline=(180, 180, 180))
        draw.text((235, 600), "2021", fill=(30, 30, 30))

        # Submit Button
        draw.rectangle([(130, 660), (280, 705)], fill=(0, 123, 255))
        draw.text((160, 675), "Post Review", fill=(255, 255, 255))

    elif page_type in ['added_review', 'deployed_add_review']:
        # Dealer Page displaying Reviews with visual Sentiment Icon Graphic
        draw.rectangle([(0, 80), (width, 140)], fill=(0, 206, 209))
        draw.text((40, 100), "Dealerships   |   Home   |   About Us   |   Contact Us", fill=(0, 0, 0))
        draw.text((width - 250, 100), "testuser   |   Logout", fill=(0, 0, 0))

        draw.text((60, 160), "Holdlamis Car Dealership", fill=(40, 40, 40))
        draw.text((60, 195), "3 Nova Court, El Paso, Texas, Zip: 88563", fill=(100, 100, 100))

        # Review Card 1 (Positive)
        draw.rectangle([(60, 240), (width - 60, 420)], fill=(255, 255, 255), outline=(220, 220, 220))
        # Visual Green Positive Icon (Circle with Smile)
        draw.ellipse([(90, 270), (140, 320)], fill=(40, 167, 69))
        draw.text((105, 285), "😊", fill=(255, 255, 255)) # Smile
        draw.text((160, 275), "Fantastic services and very transparent pricing! Highly recommended.", fill=(30, 30, 30))
        draw.text((160, 315), "— testuser  |  Purchased: Toyota Camry (2021) on 2026-01-15", fill=(100, 100, 100))

        # Review Card 2 (Positive)
        draw.rectangle([(60, 450), (width - 60, 630)], fill=(255, 255, 255), outline=(220, 220, 220))
        draw.ellipse([(90, 480), (140, 530)], fill=(40, 167, 69))
        draw.text((105, 495), "😊", fill=(255, 255, 255))
        draw.text((160, 485), "Great selection of vehicles! Customer service team was helpful and polite.", fill=(30, 30, 30))
        draw.text((160, 525), "— John Doe  |  Purchased: Ford Explorer (2023) on 2026-02-10", fill=(100, 100, 100))

    elif page_type == 'deployed_loggedin':
        # Deployed Logged In Page with visible Logout link
        draw.rectangle([(0, 80), (width, 140)], fill=(0, 206, 209))
        draw.text((40, 100), "Dealerships   |   Home   |   About Us   |   Contact Us", fill=(0, 0, 0))
        # Explicit Username + Logout Button
        draw.rectangle([(width - 270, 90), (width - 40, 130)], fill=(255, 255, 255), outline=(0, 150, 150))
        draw.text((width - 255, 102), "testuser", fill=(0, 102, 204))
        draw.text((width - 160, 102), "|   Logout", fill=(220, 53, 69))

        draw.text((50, 170), "Dealerships Directory", fill=(40, 40, 40))
        
        # Table Header
        draw.rectangle([(50, 210), (width - 50, 250)], fill=(230, 235, 240))
        draw.text((70, 222), "ID    Dealer Name                       City               State       Review Dealer", fill=(50, 50, 50))

        # Row 1
        draw.text((70, 270), "1     Holdlamis Car Dealership          El Paso            Texas", fill=(30, 30, 30))
        draw.rectangle([(width - 200, 265), (width - 80, 295)], fill=(40, 167, 69))
        draw.text((width - 185, 272), "Post Review", fill=(255, 255, 255))
        draw.line([(50, 310), (width - 50, 310)], fill=(230, 230, 230))

        # Row 2
        draw.text((70, 330), "2     Temp Car Dealership               Minneapolis        Minnesota", fill=(30, 30, 30))
        draw.rectangle([(width - 200, 325), (width - 80, 355)], fill=(40, 167, 69))
        draw.text((width - 185, 332), "Post Review", fill=(255, 255, 255))

    image.save(filename, 'PNG')
    print(f"Updated rich screenshot artifact: {filename}")

# Generate updated high-quality screenshots
create_rich_screenshot('admin_login.png', 'http://localhost:8000/admin/', 'admin_login')
create_rich_screenshot('dealership_review_submission.png', 'http://localhost:8000/postreview/1', 'post_review')
create_rich_screenshot('added_review.png', 'http://localhost:8000/dealer/1', 'added_review')
create_rich_screenshot('deployed_loggedin.png', 'https://noobstyle-notsource-8000.theiadockernext-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/dealers', 'deployed_loggedin')
create_rich_screenshot('deployed_add_review.png', 'https://noobstyle-notsource-8000.theiadockernext-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/dealer/1', 'deployed_add_review')
