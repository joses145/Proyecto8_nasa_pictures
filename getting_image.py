import requests


def generate_image(image_url):
    new_image_url = (image_url)
    response = requests.get(new_image_url)
    with open("image.jpg", "wb") as file:
        file.write(response.content)


