def validate_image_file(image):
    allowed_types = ['image/jpeg', 'image/png', 'image/jpg']
    if image.content_type not in allowed_types:
        raise ValueError('Invalid file type. Only JPG, JPEG, and PNG are allowed.')

def validate_image_size(image, max_size=5 * 1024 * 1024):
    if image.size > max_size:
        raise ValueError(f'File size too large. Maximum size is {max_size / (1024 * 1024)}MB.')