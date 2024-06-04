import customtkinter as ctk
from PIL import Image
from pyswip import Prolog

class QuestionnaireApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Questionário")
        self.geometry("770x500")
        self.resizable(False, False)  # Evita que o usuário redimensione a janela

        self.image_paths = [r"C:\Users\Psyder\Documents\teste\1.png", r"C:\Users\Psyder\Documents\teste\2.png", r"C:\Users\Psyder\Documents\teste\3.png"]
        self.image_index = 0

        self.frame = None
        self.show_intro_page()

    def show_intro_page(self):
        if self.frame:
            self.frame.destroy()

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(fill="both", expand=True)

        self.left_frame = ctk.CTkFrame(self.frame, width=400)
        self.left_frame.pack(side="left", fill="both", expand=True)

        right_frame = ctk.CTkFrame(self.frame, width=400, fg_color="white")
        right_frame.pack(side="right", fill="both", expand=True)

        self.update_image()

        right_inner_frame = ctk.CTkFrame(right_frame, fg_color="white")
        right_inner_frame.pack(expand=True)

        title_label = ctk.CTkLabel(right_inner_frame, text="Recommender", font=("Arial", 24, "bold"), text_color="black")
        title_label.pack(pady=(20, 10))

        intro_text = (
            "Bem-vindo ao Nosso Questionário de Perfil em Programação!\n\n"
            "Neste questionário, vamos fazer algumas perguntas para entender melhor suas preferências, "
            "habilidades e interesses no campo da programação. Nosso objetivo é identificar em qual área "
            "você pode se destacar mais: Back-End, Front-End ou Banco de Dados.\n\n"
            "Suas respostas nos ajudarão a sugerir qual área de programação pode ser a mais adequada para você. "
            "Seja sincero e aproveite para refletir sobre suas preferências e habilidades. Isso não só vai nos ajudar "
            "a traçar um perfil mais preciso, mas também pode ser uma oportunidade para você se conhecer melhor como "
            "profissional.\n\n"
            "Vamos começar?\n\n"
            "Clique em Começar Questionário para prosseguir com o questionário.\n\n"
        )

        intro_textbox = ctk.CTkTextbox(right_inner_frame, width=350, height=300, fg_color="white", text_color="black", wrap="word")
        intro_textbox.pack(pady=10, padx=20)
        intro_textbox.insert("1.0", intro_text)
        intro_textbox.configure(state="disabled")

        start_button = ctk.CTkButton(right_inner_frame, text="Começar Questionário", command=self.show_question_page_1)
        start_button.pack(pady=20)

    def update_image(self):
        image_path = self.image_paths[self.image_index]
        img = Image.open(image_path)
        img = img.resize((400, 500), Image.LANCZOS)
        self.photo = ctk.CTkImage(img, size=(400, 500))

        if hasattr(self, 'image_label'):
            self.image_label.configure(image=self.photo)
        else:
            self.image_label = ctk.CTkLabel(self.left_frame, image=self.photo, text="")
            self.image_label.pack()

        self.image_index = (self.image_index + 1) % len(self.image_paths)
        self.after(3000, self.update_image)

    def show_question_page_1(self):
        if self.frame:
            self.frame.destroy()

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(fill="both", expand=True)

        questions = [
            ("1. Qual é a sua linguagem de programação favorita?", ["Python", "JavaScript", "Java", "C#", "Outra"]),
            ("2. Você prefere criar interfaces visuais ou trabalhar com lógica de negócios?", ["Interfaces Visuais", "Lógica de Negócios"]),
            ("3. Você gosta de trabalhar com manipulação e análise de dados?", ["Sim", "Não"]),
        ]

        self.answers_1 = []

        for question, options in questions:
            question_label = ctk.CTkLabel(self.frame, text=question, font=("Arial", 16))
            question_label.pack(pady=(20, 5))
            answer_combobox = ctk.CTkComboBox(self.frame, values=options, width=500)
            answer_combobox.pack(pady=(0, 20))
            self.answers_1.append(answer_combobox)

        next_button = ctk.CTkButton(self.frame, text="Próximo", command=self.show_question_page_2)
        next_button.pack(pady=20)

    def show_question_page_2(self):
        self.answers_1_values = self.collect_answers(self.answers_1)
        if self.frame:
            self.frame.destroy()

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(fill="both", expand=True)

        questions = [
            ("4. Você tem interesse em aprender sobre servidores e banco de dados?", ["Sim", "Não"]),
            ("5. Você gosta de ver resultados visuais imediatos do seu trabalho?", ["Sim", "Não"]),
            ("6. Você prefere trabalhar em projetos individuais ou em equipe?", ["Individuais", "Equipe"]),
        ]

        self.answers_2 = []

        for question, options in questions:
            question_label = ctk.CTkLabel(self.frame, text=question, font=("Arial", 16))
            question_label.pack(pady=(20, 5))
            answer_combobox = ctk.CTkComboBox(self.frame, values=options, width=500)
            answer_combobox.pack(pady=(0, 20))
            self.answers_2.append(answer_combobox)

        next_button = ctk.CTkButton(self.frame, text="Próximo", command=self.show_question_page_3)
        next_button.pack(pady=20)

    def show_question_page_3(self):
        self.answers_2_values = self.collect_answers(self.answers_2)
        if self.frame:
            self.frame.destroy()

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(fill="both", expand=True)

        questions = [
            ("7. Você se sente confortável com o conceito de APIs e integração de sistemas?", ["Sim", "Não"]),
            ("8. Você gosta de otimizar o desempenho e a escalabilidade de sistemas?", ["Sim", "Não"]),
            ("9. Você tem interesse em segurança da informação e proteção de dados?", ["Sim", "Não"]),
        ]

        self.answers_3 = []

        for question, options in questions:
            question_label = ctk.CTkLabel(self.frame, text=question, font=("Arial", 16))
            question_label.pack(pady=(20, 5))
            answer_combobox = ctk.CTkComboBox(self.frame, values=options, width=500)
            answer_combobox.pack(pady=(0, 20))
            self.answers_3.append(answer_combobox)

        submit_button = ctk.CTkButton(self.frame, text="Enviar", command=self.submit_answers)
        submit_button.pack(pady=20)

    def collect_answers(self, answers):
        return [combo.get() for combo in answers]

    def submit_answers(self):
        answers_3_values = self.collect_answers(self.answers_3)
        answers = self.answers_1_values + self.answers_2_values + answers_3_values
        print("Respostas:", answers)
        self.show_recommendation_page(answers)

    def show_recommendation_page(self, answers):
        if self.frame:
            self.frame.destroy()

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(fill="both", expand=True)

        recommendation = self.determine_recommendation(answers)

        recommendation_label = ctk.CTkLabel(self.frame, text=recommendation, font=("Arial", 18))
        recommendation_label.pack(pady=20)

        tech_label = ctk.CTkLabel(self.frame, text="Tecnologias Recomendadas:", font=("Arial", 16))
        tech_label.pack(pady=10)

        technologies = self.get_technologies_for_recommendation(recommendation)
        for tech in technologies:
            tech_item = ctk.CTkLabel(self.frame, text=f"• {tech}", font=("Arial", 14))
            tech_item.pack(anchor="w", padx=20)

    def determine_recommendation(self, answers):
        prolog = Prolog()
        prolog.consult("recommender.pl")

        answers_str = "[" + ",".join([f'"{ans}"' for ans in answers]) + "]"
        query = f"recommendation({answers_str}, Recommendation)"
        result = list(prolog.query(query))[0]
        return result["Recommendation"]

    def get_technologies_for_recommendation(self, recommendation):
        prolog = Prolog()
        prolog.consult("recommender.pl")

        query = f"recommended_technologies({recommendation}, Technologies)"
        result = list(prolog.query(query))[0]
        technologies_bytes = result["Technologies"]
        # Convert bytes to string
        technologies = [tech.decode('utf-8') if isinstance(tech, bytes) else tech for tech in technologies_bytes]
        return technologies

if __name__ == "__main__":
    app = QuestionnaireApp()
    app.mainloop()
