import pytest
from selenium import webdriver
from pages.add_property_page import AddPropertyPage
import time

# ✅ Real property data
properties = [
    {
        "property_name": "The Ritz-Carlton, New York",
        "property_description": "A luxury 5-star hotel in the heart of Manhattan with stunning views of Central Park.",
        "property_location": "New York, USA",
        "property_price": "550",
        "property_guests": "3",
        "dropdown_option": "Hotel"
    },
    {
        "property_name": "Airy Beachfront Apartment",
        "property_description": "Modern 2-bedroom apartment with ocean views and direct beach access.",
        "property_location": "Malibu, California",
        "property_price": "350",
        "property_guests": "4",
        "dropdown_option": "Other"
    },
    {
        "property_name": "Cozy Hostel Downtown",
        "property_description": "Affordable and comfortable hostel with shared dorms and private rooms, perfect for backpackers.",
        "property_location": "Berlin, Germany",
        "property_price": "45",
        "property_guests": "6",
        "dropdown_option": "Hostel"
    },
    {
        "property_name": "Luxury Villa with Infinity Pool",
        "property_description": "A stunning private villa with a panoramic infinity pool and 5-star amenities.",
        "property_location": "Santorini, Greece",
        "property_price": "1200",
        "property_guests": "8",
        "dropdown_option": "House"
    },
    {
        "property_name": "Mountain Cabin Retreat",
        "property_description": "A rustic wooden cabin in the Swiss Alps, surrounded by nature and hiking trails.",
        "property_location": "Zermatt, Switzerland",
        "property_price": "220",
        "property_guests": "5",
        "dropdown_option": "House"
    },
    {
        "property_name": "Tokyo Business Hotel",
        "property_description": "A modern business hotel located in the heart of Tokyo, ideal for professionals.",
        "property_location": "Tokyo, Japan",
        "property_price": "150",
        "property_guests": "2",
        "dropdown_option": "Hotel"
    },
    {
        "property_name": "Charming Parisian Loft",
        "property_description": "A stylish loft in Paris with classic decor and a view of the Eiffel Tower.",
        "property_location": "Paris, France",
        "property_price": "280",
        "property_guests": "2",
        "dropdown_option": "Other"
    },
    {
        "property_name": "Historic Castle Stay",
        "property_description": "Live like royalty in a restored medieval castle with modern comforts.",
        "property_location": "Edinburgh, Scotland",
        "property_price": "750",
        "property_guests": "6",
        "dropdown_option": "House"
    },
    {
        "property_name": "Beachside Hostel",
        "property_description": "A vibrant hostel just steps away from the white sands of Bali's best beaches.",
        "property_location": "Bali, Indonesia",
        "property_price": "30",
        "property_guests": "4",
        "dropdown_option": "Hostel"
    },
    {
        "property_name": "Lakeside Cottage",
        "property_description": "A peaceful retreat with a private dock and kayaking opportunities.",
        "property_location": "Lake Tahoe, USA",
        "property_price": "200",
        "property_guests": "4",
        "dropdown_option": "House"
    }
]

@pytest.fixture
def setup():
    """Fixture to initialize and quit the WebDriver"""
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/login")  # Replace with actual login page URL
    yield driver
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestProperty:
    def test_add_multiple_properties(self, setup):
        """Test adding multiple properties"""
        add_property_page = AddPropertyPage(setup)

        # ✅ Step 1: Log in
        add_property_page.login(username="propertytest", password="test1234")

        for property in properties:
            print(f"🔹 Adding property: {property['property_name']}")  # Debugging output

            # ✅ Step 2: Navigate to Add Property Page
            add_property_page.click_property_text()

            time.sleep(2)
            add_property_page.click_add_property_button()

            time.sleep(2)

            # ✅ Step 3: Fill in property details
            add_property_page.submit(
                property_name=property["property_name"],
                property_description=property["property_description"],
                property_location=property["property_location"],
                property_price=property["property_price"],
                property_guests=property["property_guests"],
                dropdown_option=property["dropdown_option"]
            )

            # ✅ Step 4: Validate property was added
            assert "Property List" in add_property_page.get_headline()
