import dotenv , os , requests 
from PIL import Image
from io import BytesIO
# Loading Env variabels
dotenv.load_dotenv()

class ImageGenerator() :
    def __init__(self) :
        self.API_TOKEN=os.getenv("API_TOKEN")
        self.API_URL = "https://api-inference.huggingface.co/models/playgroundai/playground-v2-1024px-aesthetic"
        self.headers = {"Authorization": f"Bearer {self.API_TOKEN}"}
    def generate(self,user_input : str , image_count = 1):
        payload = {
            "inputs" : user_input,
            "parameters" : {
                "use_cache" : False ,
            }
        }
        for x in range(0,image_count) :
            response = requests.post(self.API_URL, headers=self.headers, json=payload)
            
            try: 
                # Create a dir
                if "images" in os.listdir() : 
                    pass
                else:
                    os.mkdir("images")
                # Save the image
                image = Image.open(BytesIO(response.content))
                image.seek(0)
                image.save(f"images/image [{x}].png")
                print(f"image [{x}] has been saved succefully")
            except Exception as e :
                print(str(e))

generator = ImageGenerator()

while True : 
    user_input = str(input("Describe what you want to generate : \n  "))
    count = int(input("How much images you'd like? :\n  "))
    generator.generate(user_input , count)