#Libraries
from mimetypes import guess_type
import base64
from IPython.display import display, Image

# Function to display an image inside Juptyer Notebook
def display_image(image_path, width=None, height=None):
    # Load and display the image
    image = Image(filename=image_path, width=width, height=height)
    display(image)


# Beautify/format print response
def word_wrap(string, n_chars=100):
    # Wrap a string at the next space after n_chars
    if len(string) < n_chars:
        return string
    else:
        return string[:n_chars].rsplit(' ', 1)[0] + '\n' + word_wrap(string[len(string[:n_chars].rsplit(' ', 1)[0])+1:], n_chars)
    
# Function to encode a local image into data URL 
def local_image_to_data_url(image_path):
    # Guess the MIME type of the image based on the file extension
    mime_type, _ = guess_type(image_path)
    if mime_type is None:
        mime_type = 'application/octet-stream'  # Default MIME type if none is found

    # Read and encode the image file
    with open(image_path, "rb") as image_file:
        base64_encoded_data = base64.b64encode(image_file.read()).decode('utf-8')

    # Construct the data URL
    return f"data:{mime_type};base64,{base64_encoded_data}"

# Function to encode a local image into base64 
def local_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        base64_encoded_data = base64.b64encode(image_file.read()).decode('utf-8')

    return base64_encoded_data