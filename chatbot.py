import os
import openai
import time
openai.api_key  = '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'

# def get_completion(prompt, model="gpt-3.5-turbo"):
#     messages = [{"role": "user", "content": prompt}]
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=0, # this is the degree of randomness of the model's output
#     )
#     return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]

context = [ {'role':'system','content':"""You are TravelBotX, designed to enhance the user experience on your tourism website. \
                Whether the user is planning a dream vacation, seeking local insights, managing bookings, or requiring top-notch customer service, you are here to elevate user\'s travel experience. With your friendly and knowledgeable persona' \ 
                'you serve as a one-stop solution for all your customer travel needs. You will serve the customers with: '\
                'Booking Assistance: Your are equipped with an extensive database of flights and hotels from around the world.User will tell it\'s travel dates, preferred destinations, and any specific requirements, and you will swiftly provide with a curated list of the best options available, ensuring a hassle-free booking process.'\
                'Local Insights:Help user Discover hidden gems and popular attractions with your local insights. From must-visit landmarks to off-the-beaten-path treasures, you can suggest exciting places, restaurants with delectable cuisines, and upcoming events tailored to your user\'s preferences.'\
                'Refunds and Cancellations: You will efficiently handle refunds and cancellations for your customer bookings. User will let you know their situation, and you will guide you through the process with clear and concise instructions.""" }, ]


greet_prompt = "Create a greeting message to welcome the customer at the beginning of the conversation. The goal is to establish a friendly and helpful tone\
Warm Welcome: Start the message with a friendly greeting, such as "'Hello'" or "'Hi there.'"\
Express excitement about assisting the user in their travel endeavors and creating a positive experience.\
Availability: Mention that the chatbot is available 24/7 to assist the user.\
Call-to-Action: Encourage the user to ask questions or provide commands related to travel.\
Keep the message very concise "

context.append({'role':'system','content': f"{greet_prompt}"})
response = get_completion_from_messages(context)

print(f"TravelBotX: {response}",end="\n\n")

while True:
    try:
        user = input("You: ")
        context.append({'role':'user','content':f"{user}"})
        print("\n")
        if user in ['exit','bye']:
            break
        response = get_completion_from_messages(context)
        print(f"TravelBotX: {response}",end="\n\n")
        context.append({'role':'system','content':f"{response}"})
    except openai.error.ServiceUnavailableError as e:
        print("I want rest now!!")
        time.sleep(30)
    except openai.error.RateLimitError as e:
        print(f"due to {e} we are shutting down the system !!")
        time.sleep(120)

bye_prompt = "Write a goodbye message to a customer at the end of a chat session."\
"Ensure that the message is friendly, polite, and leaves a positive impression. You can use phrases like "'thank you,'" "'have a great day,'" and "'see you soon'" to make the farewell warm and welcoming.Feel free to personalize the message based on the context of the conversation."
context.append({'role':'system','content': f"{bye_prompt}"})
response = get_completion_from_messages(context)
print(f"TravelBotX: {response}",end="\n")