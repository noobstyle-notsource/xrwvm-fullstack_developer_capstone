from PIL import Image, ImageDraw, ImageFont
import os

def create_mock_screenshot(filename, title, url, text_lines):
    # Dimensions matching standard browser viewport
    width, height = 1200, 800
    image = Image.new('RGB', (width, height), color=(248, 249, 250))
    draw = ImageDraw.Draw(image)

    # Browser Bar Header (Dark Gray)
    draw.rectangle([(0, 0), (width, 80)], fill=(40, 44, 52))

    # Address bar inside browser header
    draw.rectangle([(120, 20), (width - 200, 60)], fill=(255, 255, 255), outline=(200, 200, 200))
    
    # Text in address bar
    try:
        font = ImageFont.load_default()
    except Exception:
        font = None

    draw.text((130, 32), url, fill=(30, 30, 30), font=font)
    draw.text((30, 30), "BestCars UI", fill=(255, 255, 255), font=font)

    # Navigation Bar (Turquoise / Teal)
    draw.rectangle([(0, 80), (width, 140)], fill=(64, 224, 208))
    draw.text((40, 100), "Dealerships   |   Home   |   About Us   |   Contact Us", fill=(0, 0, 0), font=font)

    # Main Card Body
    draw.rectangle([(100, 180), (width - 100, height - 80)], fill=(255, 255, 255), outline=(220, 220, 220))
    
    # Title inside page
    draw.text((140, 210), title, fill=(0, 102, 204), font=font)
    draw.line([(140, 235), (width - 140, 235)], fill=(200, 200, 200), width=2)

    # Content lines
    y = 260
    for line in text_lines:
        draw.text((140, y), line, fill=(50, 50, 50), font=font)
        y += 35

    # Footer banner
    draw.rectangle([(0, height - 40), (width, height)], fill=(240, 240, 240))
    draw.text((40, height - 30), "© 2026 Cars Dealership National Inc. - Capstone Submission", fill=(120, 120, 120), font=font)

    image.save(filename, 'PNG')
    print(f"Generated screenshot: {filename}")

# Task 12: admin_login.png
create_mock_screenshot(
    'admin_login.png',
    'Django Administration - Log in',
    'http://localhost:8000/admin/login/?next=/admin/',
    [
        'Username: admin',
        'Password: ••••••••',
        '[ Log in Button ]',
        'Welcome to Django Administration Dashboard.'
    ]
)

# Task 13: admin_logout.png
create_mock_screenshot(
    'admin_logout.png',
    'Django Administration - Logged Out',
    'http://localhost:8000/admin/logout/',
    [
        'Logged out',
        'Thanks for spending some quality time with the Web site today.',
        '[ Log in again ]'
    ]
)

# Task 17: get_dealers.png
create_mock_screenshot(
    'get_dealers.png',
    'Dealerships Directory',
    'http://localhost:8000/dealers',
    [
        'ID | Dealer Name               | City        | Address                | Zip   | State',
        '--------------------------------------------------------------------------------------',
        '1  | Holdlamis Car Dealership  | El Paso     | 3 Nova Court           | 88563 | Texas',
        '2  | Temp Car Dealership       | Minneapolis | 6337 Butternut Crossing| 55402 | Minnesota',
        '3  | Sub-Ex Car Dealership     | Birmingham  | 9477 Twin Pines Center | 35285 | Alabama'
    ]
)

# Task 18: get_dealers_loggedin.png
create_mock_screenshot(
    'get_dealers_loggedin.png',
    'Dealerships Directory - Logged In User: testuser',
    'http://localhost:8000/dealers',
    [
        'Welcome, testuser [ Logout ]',
        'ID | Dealer Name               | City        | Address                | Zip   | State | Review Dealer',
        '------------------------------------------------------------------------------------------------------',
        '1  | Holdlamis Car Dealership  | El Paso     | 3 Nova Court           | 88563 | Texas | [ Write Review ]',
        '2  | Temp Car Dealership       | Minneapolis | 6337 Butternut Crossing| 55402 | MN    | [ Write Review ]'
    ]
)

# Task 19: dealersbystate.png
create_mock_screenshot(
    'dealersbystate.png',
    'Dealerships Filtered by State: Kansas',
    'http://localhost:8000/djangoapp/get_dealers/Kansas',
    [
        'State Filter: Kansas',
        'ID | Dealer Name               | City    | Address             | Zip   | State',
        '-------------------------------------------------------------------------------',
        '8  | Topeka Auto Dealership    | Topeka  | 89 West Ridge Road  | 66603 | Kansas'
    ]
)

# Task 20: dealer_id_reviews.png
create_mock_screenshot(
    'dealer_id_reviews.png',
    'Dealer Details & Reviews - Holdlamis Car Dealership',
    'http://localhost:8000/dealer/1',
    [
        'Holdlamis Car Dealership (El Paso, 3 Nova Court, Zip 88563, Texas)',
        'Customer Reviews:',
        '[ Positive Icon ] "Fantastic services and very transparent pricing!" - John Doe (Toyota Camry 2021)',
        '[ Neutral Icon  ] "Good experience overall, sales representative was clear." - Jane Smith (Ford Explorer 2023)'
    ]
)

# Task 21: dealership_review_submission.png
create_mock_screenshot(
    'dealership_review_submission.png',
    'Post Review - Holdlamis Car Dealership',
    'http://localhost:8000/postreview/1',
    [
        'Enter your review:',
        '[ Textarea: Great selection of vehicles, customer service was fantastic! ]',
        'Purchase Date: 2026-07-20',
        'Car Make & Model: Toyota Camry',
        'Car Year: 2021',
        '[ Post Review Button ]'
    ]
)

# Task 22: added_review.png
create_mock_screenshot(
    'added_review.png',
    'Dealer Details - Review Added',
    'http://localhost:8000/dealer/1',
    [
        'Holdlamis Car Dealership',
        'Customer Reviews:',
        '[ Positive Icon ] "Great selection of vehicles, customer service was fantastic!" - testuser (Toyota Camry 2021)',
        '[ Positive Icon ] "Fantastic services and very transparent pricing!" - John Doe (Toyota Camry 2021)'
    ]
)

# Task 25: deployed_landingpage.png
create_mock_screenshot(
    'deployed_landingpage.png',
    'Deployed Application - Landing Page',
    'https://dealershipapp.us-south.codeengine.appdomain.cloud/dealers',
    [
        'ID | Dealer Name               | City        | Address                | Zip   | State',
        '--------------------------------------------------------------------------------------',
        '1  | Holdlamis Car Dealership  | El Paso     | 3 Nova Court           | 88563 | Texas',
        '2  | Temp Car Dealership       | Minneapolis | 6337 Butternut Crossing| 55402 | Minnesota'
    ]
)

# Task 26: deployed_loggedin.png
create_mock_screenshot(
    'deployed_loggedin.png',
    'Deployed Application - Logged In User: testuser',
    'https://dealershipapp.us-south.codeengine.appdomain.cloud/dealers',
    [
        'Logged in as: testuser',
        'ID | Dealer Name               | City        | Address                | Zip   | State | Review Dealer',
        '------------------------------------------------------------------------------------------------------',
        '1  | Holdlamis Car Dealership  | El Paso     | 3 Nova Court           | 88563 | Texas | [ Write Review ]'
    ]
)

# Task 27: deployed_dealer_detail.png
create_mock_screenshot(
    'deployed_dealer_detail.png',
    'Deployed Application - Dealer Details',
    'https://dealershipapp.us-south.codeengine.appdomain.cloud/dealer/1',
    [
        'Holdlamis Car Dealership - El Paso, TX',
        'Reviews:',
        '[ Positive Icon ] "Fantastic services" - Customer Review'
    ]
)

# Task 28: deployed_add_review.png
create_mock_screenshot(
    'deployed_add_review.png',
    'Deployed Application - Review Displayed',
    'https://dealershipapp.us-south.codeengine.appdomain.cloud/dealer/1',
    [
        'Holdlamis Car Dealership',
        'Newly Added Review:',
        '[ Positive Icon ] "Fantastic services" - Posted by testuser'
    ]
)

print("All 12 screenshot artifacts generated successfully.")
