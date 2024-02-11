from gtts import gTTS
import os
import time

class LearningBot:
    def __init__(self):
        self.output_file = "output.mp3"

    def answer_question(self, question):
        if "course" in question.lower():
            response = "Our platform offers a variety of courses on programming, data science, machine learning, and more."
        elif "certificate" in question.lower():
            response = "Yes, we offer certificates upon completion of our courses."
        elif "price" in question.lower():
            response = "Our course prices vary depending on the content and duration. You can check our website for more details."
        elif "enroll" in question.lower() or "register" in question.lower():
            response = "To enroll in a course, simply visit our website and follow the enrollment process."
        else:
            response = "I'm sorry, I don't understand. Please ask another question."

        self.text_to_speech(response)

    def text_to_speech(self, text, intro=True, outro=False):
        if intro:
            intro_text = "Hello! I'm the PacketprepBot. How can I help you today?"
            tts = gTTS(text=intro_text, lang='en', slow=False)
            tts.save(self.output_file)
            self.play_audio()

        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(self.output_file)
        self.play_audio()

        if outro:
            outro_text = "Thank you for using PacketprepBot. Have a great day!"
            tts = gTTS(text=outro_text, lang='en', slow=False)
            tts.save(self.output_file)
            self.play_audio()

    def play_audio(self):
        # Determine the appropriate command based on the operating system
        if os.name == 'nt':  # Windows
            os.system("start " + self.output_file)
        else:
            os.system("mpg123 " + self.output_file)  # Linux (requires mpg123 to be installed)

    def delete_audio_file(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
            print("Audio file deleted.")
        else:
            print("No audio file to delete.")

def main():
    bot = LearningBot()
    print("Welcome to the PacketprepBot!")
    print("Ask me anything about our learning platform.")

    intro_text = "Hello! I'm the PacketprepBot. How can I help you today?"
    bot.text_to_speech(intro_text, intro=True)

    while True:
        question = input("You: ")
        if question.lower() == "exit":
            bot.text_to_speech("Goodbye!", outro=True)
            break
        bot.answer_question(question)
        time.sleep(5)  # Wait for the audio to finish playing before deleting the file
        bot.delete_audio_file()

if __name__ == "__main__":
    main()
