import nltk
from nltk.chat.util import Chat

# Define patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am doing well, thank you!', 'I\'m fine, thanks!', 'Pretty good!']),
    (r'what is your name?', ['My name is ChatBot.', 'You can call me ChatBot.', 'I\'m ChatBot.']),
    (r'(.) your name(.)', ['My name is ChatBot.', 'You can call me ChatBot.', 'I\'m ChatBot.']),
    (r'.*help.*', ['Sure, I can help you. What do you need help with?']),
    (r'(.*) (location|city) ?', ['I\'m a virtual assistant. But i live in your heart.']),
    (r'bye|goodbye', ['Goodbye!', 'Bye!', 'Take care!']),
    (r'I am feeling sad', ['I am here to listen. What\'s on your mind?', 'It\'s okay to feel this way. I\'m here for you.']),
    (r'Can you talk to me?', ['Of course! What would you like to talk about?', 'I\'m here to chat. What\'s on your mind?']),
    (r'Tell me a joke', ['Why don’t scientists trust atoms? Because they make up everything!', 'How does a penguin build its house? Igloos it together!', 'Why do not skeletons fight each other? They do not have the guts!']),
    (r'What do you like to do?', ['I like to talk to you because you are my friend and also learning new things.']),
    (r'What is your favorite color?', ['what is the color of your eyes, that is my favorite color.']),
    (r'What is the meaning of life?', ['The meaning of life is a philosophical question. In simpler terms, the meaning of life is about finding happiness, fulfillment, and purpose in whatever way makes sense to you. It could be through relationships, achievements, helping others, or simply enjoying the journey. It is about living a life that feels meaningful and satisfying to you.']),
    (r'How old are you?', ['I am a computer program, so I don\'t have an age.']),
     (r'I am feeling stressed', ['I understand. It is a common feeling. Would you like to talk about what\'s causing your stress?']),
    (r'How can I reduce stress?', ['There are many ways to reduce stress, such as deep breathing, meditation, exercise, and spending time with loved ones.']),
    (r'What are some stress management techniques?', ['Some stress management techniques include mindfulness, relaxation techniques, and seeking support from friends, family, or a therapist.']),
    (r'How do I deal with anxiety?', ['To deal with anxiety, it can be helpful to practice relaxation techniques, challenge negative thoughts, and seek support from a therapist or counselor.']),
    (r'What are the signs of burnout?', ['Signs of burnout include exhaustion, feeling detached from work or personal life, and reduced performance. It\'s important to take steps to address burnout, such as taking breaks and seeking support.']),
    (r'How can I improve my mental health?', ['To improve your mental health, it can be helpful to practice self-care, seek support from friends or a therapist, and engage in activities that bring you joy.']),
    (r'What are some self-care tips for mental health?', ['Some self-care tips for mental health include getting enough sleep, eating well, exercising regularly, and setting aside time for hobbies or relaxation.']),
    (r'How do I know if I need therapy?', ['You may consider therapy if you are experiencing persistent feelings of sadness, anxiety, or stress, or if you are having difficulty coping with daily life.']),
    (r'What can I do to feel better when I am feeling down?', ['It can be helpful to engage in activities that lift your mood, such as spending time with loved ones, exercising, or doing something you enjoy.']),
    (r'How do I practice mindfulness?', ['Mindfulness can be practiced by paying attention to the present moment without judgment. You can practice mindfulness through meditation, yoga, or simply by focusing on your breath.']),
    (r'I want to end my life', ['Why are you coward? As, i know you are a worrior. So, how you can do that.?']),
    (r'How can I cope with suicidal thoughts?', ['Coping with suicidal thoughts can be challenging. It\'s important to talk to someone you trust and seek professional help.']),
    (r'What should I do if I think someone is suicidal?', ['If you are concerned about someone who may be suicidal, it\'s important to talk to them openly and encourage them to seek help. You can also contact a mental health professional or a helpline for advice.']),
    (r'Can you help me with suicide prevention?', ['I can provide you with information and resources on suicide prevention. It\'s important to talk to a mental health professional for personalized support.']),
    (r'Is there a suicide hotline I can call?', ['Yes, there are suicide hotlines available in many countries. I can help you find a hotline in your area.']),
    (r'What are some warning signs of suicide?', ['Warning signs of suicide include talking about wanting to die, feeling hopeless or trapped, and withdrawing from friends and family.']),
    (r'How can I support someone who is suicidal?', ['You can support someone who is suicidal by listening to them without judgment, encouraging them to seek help, and staying connected with them.']), 
    
]


chatbot = Chat(patterns)

# Define a default response for when no pattern matches
default_response = 'I am a Mental Health Chatbot, please ask me some question regarding health issues.'

# Start the conversationaksjdfjkakfjkjh
print("Welcome to ChatBot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    if response is None:
        print("ChatBot:", default_response)
    else:
        print("ChatBot:", response)
    if user_input.lower() == 'bye':
        break
