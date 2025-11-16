# ALX Travel App - Database Modeling and Seeding

A Django-based travel booking platform with database models for listings, bookings, and reviews.

## Project Structure

```
alx_travel_app/
├── manage.py
├── alx_travel_app/
│   ├── settings.py
│   └── urls.py
└── listings/
    ├── models.py              # Listing, Booking, Review models
    ├── serializers.py         # DRF serializers
    ├── management/
    │   └── commands/
    │       └── seed.py        # Database seeding command
    └── migrations/
```

## Models

### Listing
Represents a property available for booking.

**Fields:**
- `listing_id` (UUID, Primary Key)
- `host` (Foreign Key to User)
- `title` (CharField)
- `description` (TextField)
- `location` (CharField)
- `price_per_night` (DecimalField)
- `created_at` (DateTimeField)
- `updated_at` (DateTimeField)

### Booking
Represents a booking made by a user.

**Fields:**
- `booking_id` (UUID, Primary Key)
- `listing` (Foreign Key to Listing)
- `user` (Foreign Key to User)
- `start_date` (DateField)
- `end_date` (DateField)
- `total_price` (DecimalField)
- `status` (CharField: pending, confirmed, canceled)
- `created_at` (DateTimeField)

### Review
Represents a user review for a listing.

**Fields:**
- `review_id` (UUID, Primary Key)
- `listing` (Foreign Key to Listing)
- `user` (Foreign Key to User)
- `rating` (IntegerField: 1-5)
- `comment` (TextField)
- `created_at` (DateTimeField)

## Setup Instructions

### 1. Install Dependencies

```bash
pip install django djangorestframework
```

### 2. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Seed the Database

```bash
python manage.py seed
```

This command will:
- Clear existing data
- Create 4 sample users (2 hosts, 2 guests)
- Create 5 sample listings
- Create 4 sample bookings
- Create 5 sample reviews

### 4. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 5. Run Development Server

```bash
python manage.py runserver
```

Access the admin panel at: `http://localhost:8000/admin/`

## Serializers

### ListingSerializer
Serializes Listing model data for API responses.

**Features:**
- Nested host information
- Read-only listing_id, timestamps
- Write-only host_id for creation

### BookingSerializer
Serializes Booking model data for API responses.

**Features:**
- Nested listing and user information
- Date validation (end_date > start_date)
- Status choices validation

### ReviewSerializer
Serializes Review model data for API responses.

**Features:**
- Nested listing and user information
- Rating validation (1-5)
- Unique constraint (one review per user per listing)

## Sample Data

After running the seed command, you'll have:

**Users:**
- host1 (John Doe) - email: host1@example.com
- host2 (Jane Smith) - email: host2@example.com
- guest1 (Alice Johnson) - email: guest1@example.com
- guest2 (Bob Williams) - email: guest2@example.com

All users have password: `password123`

**Listings:**
- Cozy Beach House (Malibu, California) - $250/night
- Mountain Cabin Retreat (Aspen, Colorado) - $180/night
- Downtown Luxury Apartment (New York, NY) - $350/night
- Countryside Villa (Napa Valley, California) - $420/night
- Lakeside Cottage (Lake Tahoe, Nevada) - $200/night

## Database Relationships

```
User (1) ──────── (Many) Listing
  │                         │
  │                         │
  └─────── (Many) Booking ──┘
            │
            │
User (1) ── (Many) Review ── (Many) Listing (1)
```

## Management Commands

### seed
Populates the database with sample data.

**Usage:**
```bash
python manage.py seed
```

**What it does:**
1. Clears existing listings, bookings, and reviews
2. Creates sample users
3. Creates sample listings with various locations
4. Creates sample bookings with different statuses
5. Creates sample reviews with ratings and comments

## Testing

### Verify Models
```bash
python manage.py shell
```

```python
from listings.models import Listing, Booking, Review
from django.contrib.auth.models import User

# Check counts
print(f"Users: {User.objects.count()}")
print(f"Listings: {Listing.objects.count()}")
print(f"Bookings: {Booking.objects.count()}")
print(f"Reviews: {Review.objects.count()}")

# Get all listings
listings = Listing.objects.all()
for listing in listings:
    print(f"{listing.title} - ${listing.price_per_night}/night")
```

### Verify Serializers
```bash
python manage.py shell
```

```python
from listings.models import Listing
from listings.serializers import ListingSerializer

listing = Listing.objects.first()
serializer = ListingSerializer(listing)
print(serializer.data)
```

## Requirements

- Python 3.8+
- Django 5.0+
- Django REST Framework 3.14+

## Author

ALX Software Engineering Program

## License

MIT License
