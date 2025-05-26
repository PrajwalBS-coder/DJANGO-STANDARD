# django-image-upload

This project provides an API for uploading images to a Django application. It includes functionality for validating and storing images, as well as unit tests to ensure the API behaves as expected.

## Project Structure

```
django-image-upload
├── api
│   ├── __init__.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── models
│   ├── __init__.py
│   └── image_model.py
├── tests
│   ├── __init__.py
│   └── test_upload.py
├── utils
│   ├── __init__.py
│   └── validators.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd django-image-upload
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

## Usage

- The API endpoint for uploading images is defined in `api/urls.py`. You can send a POST request to this endpoint with the image file included in the form data.

## Testing

- Unit tests for the image upload functionality can be found in `tests/test_upload.py`. To run the tests, use the following command:
  ```bash
  python manage.py test
  ```

## License

This project is licensed under the MIT License.