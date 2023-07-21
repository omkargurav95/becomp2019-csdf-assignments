import random
from captcha.image import ImageCaptcha


def generate_captcha(text_length=6):
    captcha_text = ''.join(
        random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=text_length))
    captcha_image = ImageCaptcha()
    image_data = captcha_image.generate_image(captcha_text)
    return captcha_text, image_data


def verify_captcha(user_input, captcha_text):
    return user_input.lower() == captcha_text.lower()


captcha_text, image_data = generate_captcha()
captcha_image_file = 'captcha_image.png'
image_data.save(captcha_image_file)
print(f'Captcha text: {captcha_text}')
user_input = input('Enter the captcha text: ')
if verify_captcha(user_input, captcha_text):
    print('Captcha verified successfully!')
else:
    print('Captcha verification failed.')
