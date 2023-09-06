from django.shortcuts import render
from django.http import JsonResponse
import openai
import PyPDF2

API_KEY = ""
openai.api_key = API_KEY



def chatbot_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message', '').strip()
        
        if user_message.lower() == "quit":
            return JsonResponse({'assistant_response': 'Goodbye!'})
        else:
            # Get the chat log from session or create if not present
            chat_log = request.session.get('chat_log', [])
           
            # Add the user message to the chat log
            chat_log.append({"role": "user", "content": user_message})
            
            # Trim chat history if it exceeds the maximum
            max_history = 5  # Set the maximum number of previous messages to keep
            if len(chat_log) > max_history:
                chat_log = chat_log[-max_history:]
            
            # Extract text from the PDF knowledge base
            
            
            # Append the PDF text to the user's message
            
            
            # Send the messages to the model
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": """ you are an assistant
                                                        """},
                    {"role": "user", "content": user_message}
                ]
            )
            
            assistant_response = response['choices'][0]['message']['content']
            
            # Add the assistant response to the chat log
            chat_log.append({"role": "assistant", "content": assistant_response})
            
            # Save the updated chat log to session
            request.session['chat_log'] = chat_log
            
            return JsonResponse({'assistant_response': assistant_response})
    
    return render(request, 'message_app/chatbot.html')
