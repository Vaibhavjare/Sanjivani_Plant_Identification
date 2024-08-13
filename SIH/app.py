
# Define class_names based on your training classes
class_names = [
    "Citron lime",
    "Aloevera",
    "Amarnath Globe",
    "Amla",
    "Amruthaballi",
    "Arali",
    "Asthama weed",
    "Badipala",
    "Balloon Vine",
    "Bamboo",
    "Beans",
    "Betel",
    "Bhrami",
    "Bringaraja",
    "Caricature",
    "camphor",
    "Catharanthus",
    "Castor",
    "Chilly",
    "Chakte",
    "Curry",
    "Coffee",
    "Common rue (naagdalli)",
    "Coriander",
    "Drumstick",
    "Doddpathre",
    "Eucalyptus",
    "Ekka",
    "Ganike",
    "Ganigale",
    "Ginger",
    "Gasagase",
    "Henna",
    "Guava",
    "Honge",
    "Hibiscus",
    "Jackfruit",
    "Insulin",
    "Kambajala",
    "Jasmine",
    "kamakasturi",
    "Lantana",
    "Kasambruga",
    "Kepala",
    "Kohlrabi",
    "Malabar Spinach",
    "Lemon",
    "Lemongrass",
    "Malabar Nut",
    "Neem",
    "Mango",
    "Marigold",
    "Mint",
    "Onion",
    "Nelavembu",
    "Nerale",
    "Nooni",
    "Papaya",
    "Padri",
    "Padri Papaya Parijatha Pumpkin",
    "Palak (Spinach)",
    "Pomoegranate",
    "Parijatha",
    "Pea",
    "Pepper",
    "Sampige",
    "Pumpkin",
    "Radish",
    "Rose",
    "Spinach1",
    "Tamarind",
    "Seethaashoka",
    "Seethapala",
    "Thumbe",
    "Tomato",
    "Taro",
    "Tecoma",
    "Ashoka",
    "Tomato",
    "Tulsi",
    "Turmeric"
]



import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
from torchvision import models
import torch.nn.functional as F
# import med1 as med
def det(inp):
    # Define the transformations for preprocessing (same as training)
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    # Define class_names based on your training classes
    # Replace with your actual class names


    # Load the saved model architecture (same as used for training)
    model = models.resnet18(pretrained=False)  # Use the same architecture
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, 81)  # Same output layer as training

    # Load the saved model weights
    model.load_state_dict(torch.load('your_model.pth'))
    model.eval()  # Set the model to evaluation mode

    # Load and preprocess the input image
    global input_image_path
    input_image_path = inp
    input_image = Image.open(input_image_path)
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)  # Add batch dimension (1 image)

    # Move the input batch to the same device as the model (CPU or GPU)
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    input_batch = input_batch.to(device)

    # Perform inference
    with torch.no_grad():
        output = model(input_batch)
        probabilities = F.softmax(output, dim=1)  # Compute softmax probabilities

    # Get the predicted class index and confidence
    _, predicted_class = output.max(1)
    confidence = probabilities[0, predicted_class].item()



    # Map the class index to the class name using class_names
    predicted_class_name = class_names[predicted_class]

    print(f'Predicted Class: {predicted_class_name}, {predicted_class}, Confidence: {confidence:.4f}')

    return predicted_class_name,confidence

