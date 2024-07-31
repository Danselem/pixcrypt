#usr/bin/env python
import streamlit as st
import os
from dotenv import load_dotenv
from pathlib import Path
import base64
import google.generativeai as genai
import comet_llm
import time

dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)

# set up comet
COMET_API_KEY = os.environ["COMET_API_KEY"]
COMET_WORKSPACE = os.environ["COMET_WORKSPACE"]
COMET_PROJECT = os.environ["COMET_PROJECT"]
os.environ['GOOGLE_API_KEY'] = os.environ['GOOGLE_API_KEY']
os.environ['GRPC_VERBOSITY'] = 'ERROR'

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones

def get_gemini_response(input,image,prompt):
    safety_settings=[
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    }]
    
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    # model = model.start_chat(history=[])
    response = model.generate_content([input,image[0],prompt,], stream=True, safety_settings=safety_settings)
    return response

def input_image_setup(uploaded_image):
    # Check if a file has been uploaded
    if uploaded_image is not None:
        # Read the file into bytes
        bytes_data = uploaded_image.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_image.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        # raise FileNotFoundError("No file uploaded")
        st.error("Can't read uploaded image.")

##initialize our streamlit app

st.set_page_config(page_title="PixCrypt App",
                    page_icon=":art:",
                    layout="centered",
                    initial_sidebar_state="auto")



# Custom CSS for gradient background and centering content
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #ff7e5f, #feb47b); /* Gradient from pink to orange */
        font-family: Arial, sans-serif;
    }
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    .content {
        width: 50%;
        max-width: 800px; /* Limit maximum width to 800px */
        text-align: center;
    }
    .title {
        color: #fff; /* White color */
        font-size: 48px;
        font-weight: bold;
        margin-bottom: 20px;
        text-align: center; /* Center the text */
    }
    .subtitle {
        color: #fff; /* White color */
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
        text-align: center; /* Center the text */
    }
    </style>
    """, unsafe_allow_html=True)


# Initialize the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Content centered within half of the page width
with st.container() as container:
    with st.container() as content:
        # Your Streamlit app content here
        
        st.markdown('<h1 class="title"><span style="color: #ff7e5f;">Pix</span><span \
            style="color: #feb47b;">Crypt</span> <span style="color: #000000;"> GPT</span> \
                <i class="fas fa-lock"></i></h1>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle"><span style="color: #EE9A4D;">Your product description App</span> <i class="fas fa-lock"></i></p>', unsafe_allow_html=True)
        # Display the chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])



# Add "About" section to the sidebar
st.sidebar.header("About PixCrypt GPT")

with st.sidebar:
    st.markdown(
        "Welcome to PixCrypt GPT, an AI-powered app designed to help \
            small and medium-sized enterprises (SMEs) create compelling \
                descriptions for their product photos."
    )
    st.markdown(
        "Small business owners often struggle to craft effective descriptions\
            for their product images. PixCrypt GPT aims to help teams \
                and small business owners overcome this challenge. With \
                    a single prompt, our AI can assist you in producing \
                        high-quality descriptions for your products."
    )
    st.markdown("Created by [Daniel Egbo](https://www.linkedin.com/in/egbodaniel/).")
    # Add "Star on GitHub" link to the sidebar
    st.sidebar.markdown(
        "⭐ Star on GitHub: [![Star on GitHub](\
            https://img.shields.io/github/stars/Danselem/pixcrypt?style=social)](\
                https://github.com/Danselem/pixcrypt)"
    )
    
    st.markdown("""---""")
    
   
# Add "FAQs" section to the sidebar
st.sidebar.header("FAQs")

with st.sidebar:
    
    with st.expander("What is PixCrypt GPT?", expanded=False):
        
        st.markdown("""PixCrypt GPT is a product description app.""")
    
    with st.expander("How does PixCrypt GPT work?", expanded=False):
        st.markdown(
            """
            PixCrypt GPT enables you to upload an image \
                and provide a text prompt, which our AI then \
                    uses to generate a product description for you.
            """
            )
    
    with st.expander("How to use PixCrypt GPT?", expanded=False):
        
        st.markdown(
            """
            To use PixCrypt GPT, simply upload your \
                product image and also input a text prompt. \
                    This will enable PixCrypt to generate your \
                        descriptions within a few seconds.
                    """)
    
            
    with st.expander("Are the model descriptions 100% accurate?", expanded=False):
        
        st.markdown(
            """
            No, the model descriptions are not 100% accurate. \
            PixCrypt GPT relies on Large Language Models (LLMs) \
            to generate its output. While these models are highly \
            advanced, they are not infallible and may occasionally \
            produce mistakes or "hallucinations" (i.e., generating \
            irrelevant or inaccurate content)..
            """
            )

st.markdown("""---""")



uploaded_image = st.file_uploader("Select an image...", 
                                 type=["jpg", "jpeg", "png"], help=r"Click the `Browse files` to upload an image of your choice.")
image=""   


if uploaded_image is not None:
        # Display the image with custom CSS
        
        image_data = base64.b64encode(uploaded_image.read()).decode()
        
        st.markdown(
            f'<div style="display: flex; justify-content: center;"><img src="data:image/png;base64,{image_data}" alt="Uploaded Image" style="width: 50%; height: auto; max-width: 500px; border-radius: 15%; border: 10px solid #ff7f0e;"></div>', 
            unsafe_allow_html=True
        )
        
# st.header("PixCrypt App")
# input_text = st.text_area(
#         label="Provide key terms you want the app to consider \
#             while curating beautiful description for your product.",
#         placeholder="Enter your prompt details...",
#         height=150,
#         key="app_input",
#         help="Please provide a detailed description of the image, including any \
#             relevant information you want the app to include in the result.",
#     )

input_text = st.chat_input(placeholder="Enter your prompt details...",
                           key="app_input",
                           ) # on_submit=False

# submit_button=st.button("Describe the Product")

               
input_prompt = """
            Welcome to the Expert Product Image Description task. 
            \n Your expertise is crucial in understanding product images and crafting compelling descriptions. 
            \n You will receive input product images, and your role is to 
            generate captivating product descriptions based on the visual information.

            \n Example: Analyze the provided image of a [Product Type] and generate a detailed description. 
            \n Highlight key features, materials used, and any unique design elements. 
            \n Consider potential customer inquiries and proactively address them in your description.

            \n Your goal is to create vivid, informative, and engaging product descriptions that resonate with our target audience. 
            Maintain a professional tone and ensure that your responses are tailored to the specific details present in the image.
            """


comet_llm.init(COMET_API_KEY, COMET_WORKSPACE, project=COMET_PROJECT)

## If ask button is clicked


if input_text:
    # Show a spinner while generating the threat model
    with st.spinner("Reading your product and generating description..."):
        start = time.time()
        
        inputs = [input_text]
        
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": input_text})
        
        # Display user message in chat message container
        with st.container():
            with st.chat_message("user"):
                st.markdown(input_text)
        
        image_data = input_image_setup(uploaded_image)
        
        inputs.append(image_data)
        
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
        
            for response in get_gemini_response(input_prompt, 
                                            image_data, input_text):
                full_response += response.text
                
                message_placeholder.markdown(full_response + "▌")
        
            message_placeholder.markdown(full_response)
        # st.subheader("Hey Buddy \n Here is your product description:")
        st.session_state.messages.append({"role": "assistant", "content": full_response})
        
        end = time.time()
        
        comet_llm.log_prompt(
            timestamp = time.time(),
            prompt=input_text,
            prompt_template=input_prompt,
            output=full_response,
            tags = ["Gemini", "multi-modal"],
            duration = round(end - start, 3)
            )

    # except Exception as e:
    #     st.error(f"Error generating threat model: {e}")

elif uploaded_image and not input_text:
    st.error("Please enter your prompt details in the chat box to describe the product.")
# elif input_text and not uploaded_image:
#     st.error("Please upload your product image before describing the product.")
# else:
#     st.error("Please upload your product image and prompt details before describing the product.")


